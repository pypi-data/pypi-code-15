"""
# -*- coding: utf-8 -*-
# ===============================================================================
#
# Copyright (C) 2013/2014/2015 Laurent Champagnac
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
# ===============================================================================
"""

from pythonsol.SolBase import SolBase
SolBase.voodoo_init()

# Logger
from Queue import Empty
from socket import error
from errno import EWOULDBLOCK
import logging
from threading import Lock

from gevent import GreenletExit
import gevent
from gevent._socketcommon import wait_read, wait_write
from gevent.queue import Queue

from pythonsol.meter.MeterManager import MeterManager
from pythonsol.SolBase import SolBase
from pythonsol.tcpbase.SignaledBuffer import SignaledBuffer
from pythonsol.tcpserver.TcpServerStat import TcpServerStat

logger = logging.getLogger("TcpSocketManager")


class TcpSocketManager(object):
    """
    Tcp socket manager.
    """

    # Send queue : Wait in ms per loop.
    # Upon queue fill, called is unlocked immediately.
    # We use a call go get(Block=True, QUEUE_WAIT_MS_PER_LOOP) to avoid eating cpu while waiting.
    # Value in second OR None for unlimited wait.
    QUEUE_WAIT_SEC_PER_LOOP = None

    # =====================================================
    # HELPER FOR SOCKET CLOSING
    # =====================================================

    @classmethod
    def safe_close_socket(cls, soc_to_close):
        """
        Safe close a socket
        :param cls: cls
        :param soc_to_close: socket
        :return: Nothing
        """

        if soc_to_close is None:
            return

        try:
            soc_to_close.shutdown(2)
        except Exception as e:
            logger.debug("Socket shutdown ex=%s", SolBase.extostr(e))

        try:
            soc_to_close.close()
        except Exception as e:
            logger.debug("Socket close ex=%s", SolBase.extostr(e))

        try:
            del soc_to_close
        except Exception as e:
            logger.debug("Socket del ex=%s", SolBase.extostr(e))

    def __init__(self, callback_disconnect, callback_receive, on_receive_profile_self=False):
        """
        Constructor.
        :param callback_disconnect: Callback to call upon socket disconnection.
        :param callback_receive:  Callback to call upon socket receive.
        :param on_receive_profile_self: If True, self will be provided as onReceive param
        :type on_receive_profile_self: bool
        :return: Nothing.
        """

        # Connected flag (backed by is_connected property)
        self.is_connected = False

        # Socket instance
        self._socket = None

        # Send queue
        self.__send_queue = Queue()

        # Callback : called when something is received from the socket
        self._callback_receive = callback_receive
        self._on_receive_profile_self = on_receive_profile_self

        # Callback : called upon socket disconnection
        self._callback_disconnect = callback_disconnect

        # Timestamps
        self._dt_created = SolBase.datecurrent()
        self._dt_last_recv = self._dt_created
        self._dt_last_send = self._dt_created

        # SSL Handshake asynch
        self.__ssl_handshake_asynch = False
        self.__ssl_handshake_pending = False
        self.__ssl_handshake_timeout_ms = None
        self.__ssl_wait_debug_ms = None
        self.__ssl_timeout_greenlet = None
        self.__ssl_locker = Lock()

        # SSL handshake time
        self.__ssl_handshake_ms = None

        # Fatal error
        self.__internal_fatal_error = False

        # Check the TcpServerStats
        if MeterManager.get(TcpServerStat) is None:
            logger.info("TcpServerStat not registered in MeterManager, adding it now")
            MeterManager.put(TcpServerStat())

    # ================================
    # TO STRING OVERWRITE
    # ================================

    def __str__(self):
        """
        To string override
        :return: A string
        :rtype string
        """

        to = None
        if self.current_socket:
            to = self.current_socket.timeout
        return "s.to={0}*dt.creat={1}*dt.recv={2}*dt.send={3}*q.send.size={4}*is.co={5}/{6}*cl={7}*id={8}".format(
            to,
            int(SolBase.datediff(self._dt_created) * 0.001),
            int(SolBase.datediff(self._dt_last_recv) * 0.001),
            int(SolBase.datediff(self._dt_last_send) * 0.001),
            self.__send_queue.qsize(),
            self.is_connected,
            self.__is_running(),
            self.__class__.__name__,
            id(self)
        )

    def set_callback_receive(self, callback_receive, provide_self):
        """
        Set the receive callback
        :param callback_receive: Callback
        :param provide_self: If false, callback_receive(localBuffer) otherwise callback_receive(localBuffer, self)
        :type provide_self: bool
        :return: Nothing
        """

        self._callback_receive = callback_receive
        self._on_receive_profile_self = provide_self

    # ================================
    # SSL HANDSHAKE TIMEOUT
    # ================================

    def __shedule_ssl_handshake_timeout(self):
        """
        Shedule a ssl handshake timeout
        :return: Nothing
        """

        with self.__ssl_locker:
            logger.debug("__shedule_ssl_handshake_timeout : ms=%s, self=%s", self.__ssl_handshake_timeout_ms, self)
            self.__ssl_timeout_greenlet = gevent.spawn_later(self.__ssl_handshake_timeout_ms * 0.001,
                                                             self.__on_ssl_timeout)

    def _unschedule_ssl_handshake_timeout(self):
        """
        Unschedule the ssl timeout
        :return: Nothing
        """
        with self.__ssl_locker:
            logger.debug("_unschedule_ssl_handshake_timeout, self=%s", self)

            if self.__ssl_timeout_greenlet:
                self.__ssl_timeout_greenlet.kill()
                self.__ssl_timeout_greenlet = None

    def __on_ssl_timeout(self):
        """
        Called when SSL timeout.
        :return: Nothing
        """
        # Reset first (in LOCK)
        with self.__ssl_locker:
            self.__ssl_timeout_greenlet = None

        # Process (outside of LOCK, high level may call _unschedule_ssl_handshake_timeout in lock)
        logger.debug("__on_ssl_timeout, self=%s", self)

        # Check
        if not self.__ssl_handshake_pending:
            # Done, exit
            return
        elif not self.__is_running():
            # Not connected, exit
            return

        # Not done, FATAL
        logger.warn("handshake timeout, fatal, ms=%s, self=%s", self.__ssl_handshake_timeout_ms, self)

        # Stat
        MeterManager.get(TcpServerStat).ssl_handshake_timeout_count.increment()

        # Timeout, Fatal, exit now
        self._disconnect_helper("__on_ssl_timeout")

    # ================================
    # GETTER/SETTER
    # ================================

    def set_ssl_handshake_asynch(self, ssl_handshake_asynch_enable, ssl_handshake_timeout_ms, ssl_wait_debug_ms=None):
        """
        Enable or disable ssl asynch handshake.
        :param ssl_handshake_asynch_enable: Boolean. If True, will enable it.
        :param ssl_handshake_timeout_ms: Apply if asynch handshake is enable. Timeout in ms for handshake itself.
        :param ssl_wait_debug_ms: Debug only.
        :return: Nothing.
        """

        self.__ssl_handshake_asynch = ssl_handshake_asynch_enable
        self.__ssl_handshake_timeout_ms = ssl_handshake_timeout_ms
        self.__ssl_wait_debug_ms = ssl_wait_debug_ms

        # If enable, switch to pending true
        if self.__ssl_handshake_asynch:
            # Now pending
            self.__ssl_handshake_pending = True

            # Schedule a greenlet, waiting for ssl to complete
            self.__shedule_ssl_handshake_timeout()

    def _set_ssl_handshake_ms(self, ms):
        """
        Set the time taken to perform the ssl handshake.
        :param ms: Millis.
        :return: Nothing
        """
        self.__ssl_handshake_ms = ms

    def _set_socket(self, my_soc):
        """
        Setter
        :param my_soc: The socket.
        """
        self._socket = my_soc

    def _set_is_connected(self, b):
        """
        Setter
        :param b: New value.
        :return Nothing.
        """
        self.__isConnected = b

    def _get_ssl_handshake_ms(self):
        """
        Return the ssl handshake elapsed ms.
        :return: Integer or None if not set.
        """
        return self.__ssl_handshake_ms

    def _get_socket(self):
        """
        Getter.
        :return: The current socket.
        """
        return self._socket

    def _get_is_connected(self):
        """
        Getter.
        :return: A boolean.
        :rtype bool
        """
        return self.__isConnected

    def _get_send_queue(self):
        """
        Getter.
        :return: The gevent send queue.
        """
        return self.__send_queue

    def _get_dt_created(self):
        """
        Getter.
        :return: A datetime.
        """
        return self._dt_created

    def _get_dt_last_send(self):
        """
        Getter.
        :return: A datetime.
        """
        return self._dt_last_send

    def _get_dt_last_recv(self):
        """
        Getter.
        :return: A datetime.
        """
        return self._dt_last_recv

    # ================================
    # PROPERTIES
    # ================================

    # Properties
    is_connected = property(_get_is_connected, _set_is_connected)
    current_socket = property(_get_socket, _set_socket)
    send_queue = property(_get_send_queue)

    # Properties : timestamp
    date_created = property(_get_dt_created)
    date_last_send = property(_get_dt_last_send)
    date_last_recv = property(_get_dt_last_recv)

    # ================================
    # SEND TO SOCKET
    # ================================

    def send_binary_to_socket(self, buffer_to_send):
        """
        Send to socket, asynch.
        :param buffer_to_send: The localBuffer to send (a str or bytes)
        :return: True is send has been scheduled, false otherwise.
        """

        # Check
        if not isinstance(buffer_to_send, str):
            logger.error("buffer_to_send not a binary, class=%s, self=%s",
                         SolBase.get_classname(buffer_to_send), self)
            return False

        # Check
        if not self.__is_running():
            logger.debug("not connected, returning false, self=%s", self)
            return False

        # Enqueue
        self.__send_queue.put(buffer_to_send)

        # Stats
        MeterManager.get(TcpServerStat).server_bytes_send_pending.increment(len(buffer_to_send))

        return True

    def send_binary_to_socket_with_signal(self, signaled_buffer):
        """
        Send to socket, asynch.
        Upon completion, signaled_buffer.send_event is set.
        Caution : Caller MUST check the boolean returned. If False, the event will NOT be set.
        :param signaled_buffer: A signaled_buffer instance.
        :type signaled_buffer: SignaledBuffer
        :return: True is send has been scheduled, false otherwise.
        """

        # Check
        if not isinstance(signaled_buffer, SignaledBuffer):
            logger.error(
                "signaled_buffer not a SignaledBuffer, class=%s, self=%s",
                SolBase.get_classname(signaled_buffer), self)
            return False

            # Check
        if not isinstance(signaled_buffer.binary_buffer, str):
            logger.error(
                "binary_buffer not a binary, class=%s, self=%s",
                SolBase.get_classname(signaled_buffer.binary_buffer), self)
            return False

        # Check
        if not self.__is_running():
            logger.debug(
                "not connected, returning false, self=%s",
                self)
            return False

        # Enqueue
        self.__send_queue.put(signaled_buffer)

        # Stats
        MeterManager.get(TcpServerStat).server_bytes_send_pending.increment(len(signaled_buffer.binary_buffer))

        return True

    def send_text_to_socket(self, text_to_send, append_lf=True):
        """
        Send text to socket, asynch.
        :param text_to_send: The text to send (str)
        :param append_lf: If true, append an \n
        :return: True is send has been scheduled, false otherwise.
        """

        # Check
        if not isinstance(text_to_send, str):
            logger.error("text_to_send not an str, class=%s, buf=%s, self=%s",
                         SolBase.get_classname(text_to_send), repr(text_to_send), self)
            return False

        # Enqueue
        if append_lf:
            return self.send_binary_to_socket(text_to_send + "\n")
        else:
            return self.send_binary_to_socket(text_to_send)

    def send_unicode_to_socket(self, unicode_to_send, encoding="utf-8", append_lf=True):
        """
        Send text to socket, asynch.
        :param unicode_to_send: The text to send (unicode)
        :param encoding: The encoding to use.
        :param append_lf: If true, append an \n
        :return: True is send has been scheduled, false otherwise.
        """

        # Check
        if not isinstance(unicode_to_send, unicode):
            logger.error(
                "unicode_to_send not an unicode, class=%s, unicode=%s, self=%s",
                SolBase.get_classname(unicode_to_send), repr(unicode_to_send), self)
            return False

        # Go
        unicode_temp = unicode_to_send

        # LF if required
        if append_lf:
            unicode_temp += u"\n"

        # Convert to binary localBuffer
        bin_buf = SolBase.unicode_to_binary(unicode_temp, encoding)

        # Send binary
        return self.send_binary_to_socket(bin_buf)

    def get_send_queue_len(self):
        """
        Return the send queue len.
        :return The queue length (integer)
        """
        return self.__send_queue.qsize()

    # ================================
    # DISCONNECT HELPER
    # ================================

    def unset_internal_fatal_error_for_reconnect(self):
        """"
        This must be called before firing a reconnect AFTER a disconnection
        """

        self.__internal_fatal_error = False

    def _disconnect_helper(self, reason):
        """
        Fire a disconnect on our end and notify upper level is possible
        :param reason: Reason
        :type reason: str
        """

        logger.debug("Disconnect from inside, reason=%s", reason)

        # Disengage r/w loops now
        # CAUTION : NEVER (NEVER) internally flag "is_connected=False" here, you will BLAST upper level implementations
        self.__internal_fatal_error = True

        # Close the socket
        TcpSocketManager.safe_close_socket(self.current_socket)
        self.current_socket = None

        # Callback now
        if self._callback_disconnect:
            self._callback_disconnect()
        else:
            logger.error(
                "_disconnect_helper is None, check your implementation, self=%s", self)

    def __is_running(self):
        """
        Return true if we are connected and we do not have a fatal error
        :return: bool
        """

        return self.is_connected and not self.__internal_fatal_error

    # ================================
    # SOCKET WAIT
    # ================================

    def _wait_for_socket_recv(self):
        """
        Wait for socket available for read (recv).
        :return Return True if available, False otherwise.
        """

        # Check
        if not self.__is_running():
            logger.debug("not connected, returning false, self=%s", self)
            return False

        # Go
        try:
            # Wait
            wait_read(self._socket.fileno())

            # Ready
            return True
        except Exception as e:
            logger.warn("Exception, ex=%s, self=%s", SolBase.extostr(e),
                        self)
            return False

    def _wait_for_socket_send(self):
        """
        Wait for socket available for write (send).
        :return Return True if available, False otherwise.
        """

        # Check
        if not self.__is_running():
            logger.debug("not connected, returning false, self=%s", self)
            return False

        # Go
        try:
            # Wait
            wait_write(self.current_socket.fileno())

            # Ready
            return True
        except Exception as e:
            logger.warn("Exception, ex=%s, self=%s", SolBase.extostr(e),
                        self)
            return False

    # ================================
    # SOCKET LOOP : READ
    # ================================

    def _read_loop(self):
        """
        High level read loop on socket
        """
        logger.debug("entering now, self=%s", self)
        try:
            self._read_loop_internal()
        except GreenletExit:
            logger.debug("exiting due to GreenletExit, self=%s", self)
            return
        except Exception as e:
            logger.error("Exception raised, ex=%s, self=%s", SolBase.extostr(e), self)
        finally:
            logger.debug("exiting now, self=%s", self)
            SolBase.sleep(0)

    def _read_loop_internal(self):
        """
        Low level read loop on socket
        """
        logger.debug("entering now, self=%s", self)
        try:
            while self.__is_running():
                try:
                    if self.__ssl_handshake_pending:
                        # Pending SSL handshake + received something
                        # Handle SSL handshake now

                        # Stats
                        MeterManager.get(TcpServerStat).delay_server_accept_to_sslhandshakestart.put(
                            SolBase.datediff(self._dt_created))

                        # Timestamps
                        self._dt_last_recv = SolBase.datecurrent()

                        # Debug ONLY
                        if self.__ssl_wait_debug_ms:
                            logger.error("Debug : waiting for SSL handshake, ms=%s, self=%s", self.__ssl_wait_debug_ms,
                                         self)
                            SolBase.sleep(self.__ssl_wait_debug_ms)
                            logger.error("Debug : waiting for SSL handshake : done, self=%s", self)

                        # Do the handshake
                        self.current_socket.do_handshake()

                        # Done, cancel timeout
                        self._unschedule_ssl_handshake_timeout()

                        # Ms
                        ms = SolBase.datediff(self._dt_last_recv)

                        # SSL Stats (for client)
                        self._set_ssl_handshake_ms(ms)

                        # Server stats
                        MeterManager.get(TcpServerStat).delay_server_sslhandshake.put(ms)

                        # Done
                        self.__ssl_handshake_pending = False

                        # Non blocking mode now
                        self.current_socket.setblocking(0)
                        self.current_socket.settimeout(None)

                        # Reloop in normal mode
                        continue

                    # Wait for socket to be available for read
                    ok = self._wait_for_socket_recv()
                    if not ok:
                        # This is not really normal
                        logger.warn(
                            "_wait_for_socket_recv returned False, self=%s",
                            self)
                    elif not self.__is_running():
                        logger.debug(
                            "_wait_for_socket_recv returned True, __is_running()==False, exiting, self=%s",
                            self)
                        return
                    else:
                        # Something to read...
                        local_buf = self._read_from_socket()
                        if not self.__is_running():
                            logger.debug(
                                "_read_from_socket returned, __is_running()==False, exiting, self=%s",
                                self)
                        elif local_buf is None:
                            # This is not really normal
                            logger.debug(
                                "_read_from_socket returned None, self=%s",
                                self)
                        elif len(local_buf) == 0:
                            # This is not really normal
                            logger.debug(
                                "_read_from_socket returned empty string, self=%s",
                                self)
                            # Gevent 1.0.2 : call disconnect
                            self._disconnect_helper("_read_from_socket returned empty string")
                        else:
                            # Timestamps
                            self._dt_last_recv = SolBase.datecurrent()

                            # Notify
                            if self._callback_receive:
                                # Self provide ?
                                if self._on_receive_profile_self:
                                    self._callback_receive(local_buf, self)
                                else:
                                    self._callback_receive(local_buf)

                            else:
                                logger.error(
                                    "_callback_receive is None, check you implementation, self=%s",
                                    self)

                    # Next read
                    SolBase.sleep(0)
                except Exception as e:
                    logger.warn("IN_LOOP Exception raised, ex=%s, self=%s",
                                SolBase.extostr(e), self)
        except Exception as e:
            logger.error("METHOD Exception raised, ex=%s, self=%s",
                         SolBase.extostr(e), self)
        finally:
            logger.debug("exiting now, self=%s", self)
            SolBase.sleep(0)

    def _read_from_socket(self):
        """
        Read from the socket. Return a local_buf or None.
        """

        # Check
        if not self.__is_running():
            logger.debug("not connected, doing nothing, self=%s", self)
            return None

        try:
            # TODO : Socket local_buf size
            # TODO : Socket, upon server closure, will BLOCK on recv. Upon time, auto disconnect the client.

            # Try to read
            local_buf = self.current_socket.recv(1024)

            # If local_buf is empty string, socket is disconnected.
            if local_buf and len(local_buf) == 0:
                # Disconnect
                logger.debug(
                    "empty string received, disconnecting ourselves, self=%s",
                    self)
                self._disconnect_helper("_read_from_socket : Empty string")
                return None

            # Stats
            MeterManager.get(TcpServerStat).server_bytes_received.increment(len(local_buf))
            # Ok
            return local_buf
        except error as e:
            # [Errno 11] Resource temporarily unavailable
            # Means that nothing is available to read.
            # If not this, we raise.
            if e.args[0] != EWOULDBLOCK:
                # Raise :)
                logger.debug("_tryReadWrite : _read_from_socket : error, ex=%s, self=%s", SolBase.extostr(e), self)
                self._disconnect_helper("_read_from_socket : error / No EWOULDBLOCK")
                return None
            else:
                # Normal
                logger.debug("_tryReadWrite : _read_from_socket : normal exception/EWOULDBLOCK, ex=%s, self=%s", e,
                             self)
                return None
        except Exception as e:
            logger.debug("_tryReadWrite : _read_from_socket : Exception, ex=%s, self=%s", SolBase.extostr(e), self)
            self._disconnect_helper("_read_from_socket : Exception / No EWOULDBLOCK")
            return None

    # ================================
    # SOCKET LOOP : WRITE
    # ================================

    def _write_loop(self):
        """
        High level read loop on socket
        """
        logger.debug("entering now, self=%s", self)
        try:
            self._write_loop_internal()
        except GreenletExit:
            logger.debug("exiting due to GreenletExit, self=%s", self)
            return
        except Exception as e:
            logger.error("Exception raised, ex=%s, self=%s", SolBase.extostr(e), self)
        finally:
            logger.debug("exiting now, , self=%s", self)
            SolBase.sleep(0)

    def _write_loop_internal(self):
        """
        Low level read/write loop on socket
        """
        logger.debug("entering now, self=%s", self)
        try:
            while self.__is_running():
                try:
                    # Wait for the queue
                    try:
                        # Call, with blocking.
                        item = self.send_queue.get(True, TcpSocketManager.QUEUE_WAIT_SEC_PER_LOOP)

                    except Empty:
                        # Next read
                        SolBase.sleep(0)
                        continue

                    # Go some
                    if isinstance(item, str):
                        # Length
                        length = len(item)
                        # Buffer to send
                        buf_to_send = item
                        # Event to signal
                        event_to_signal = None
                    elif isinstance(item, SignaledBuffer):
                        # Stats
                        length = len(item.binary_buffer)
                        # Buffer to send
                        buf_to_send = item.binary_buffer
                        # Event to signal
                        event_to_signal = item.send_event
                    else:
                        logger.warn(
                            "not managed class in queue, class=%s, item=%s",
                            SolBase.get_classname(item), item)
                        continue

                    # Stat now (mantis 687)
                    MeterManager.get(TcpServerStat).server_bytes_send_pending.increment(-length)

                    # Wait for socket to be available for write
                    logger.debug("waiting for socket to send=%s, self=%s",
                                 repr(item), self)
                    ok = self._wait_for_socket_send()
                    if not ok:
                        # This is not really normal
                        logger.warn(
                            "_wait_for_socket_send returned False, self=%s",
                            self)
                    elif not self.__is_running():
                        logger.debug(
                            "Ready for send, but __is_running==False, exiting, send=%s, self=%s",
                            self)
                        return
                    else:
                        try:
                            # Ready to write, fire
                            logger.debug(
                                "writing to socket to send=%s, self=%s",
                                repr(item), self)
                            ok = self._write_to_socket(buf_to_send)
                            if not ok:
                                # This is not really normal
                                logger.warn(
                                    "_write_to_socket returned False, self=%s",
                                    self)

                            # Signal if applicable
                            if event_to_signal:
                                event_to_signal.set()
                        finally:
                            # Timestamps
                            self._dt_last_send = SolBase.datecurrent()

                            # Stats
                            MeterManager.get(TcpServerStat).server_bytes_send_done.increment(length)

                    # Next read
                    SolBase.sleep(0)
                except Exception as e:
                    logger.warn("IN_LOOP Exception raised, ex=%s, self=%s",
                                SolBase.extostr(e), self)
        except Exception as e:
            logger.error("METHOD Exception raised, ex=%s, self=%s",
                         SolBase.extostr(e), self)
        finally:
            logger.debug("exiting now, , self=%s", self)
            SolBase.sleep(0)

    def _write_to_socket(self, local_buffer):
        """
        Write to the socket.
        """

        # Check
        if not self.__is_running():
            logger.debug("not connected, doing nothing, self=%s", self)
            return False

        try:
            #
            self.current_socket.sendall(local_buffer)
            return True
        except error as e:
            # [Errno 11] Resource temporarily unavailable
            # Means that nothing is available to read.
            # If not this, we raise.
            if e.args[0] != EWOULDBLOCK:
                # Raise :)
                logger.debug("Exception, ex=%s, self=%s", SolBase.extostr(e),
                             self)
                self._disconnect_helper("_write_to_socket : error / No EWOULDBLOCK")
                return False
            else:
                # Normal
                logger.debug("normal exception/EWOULDBLOCK, ex=%s, self=%s", e,
                             self)
                return False
        except Exception as e:
            logger.info("Exception, ex=%s, self=%s", SolBase.extostr(e), self)
            self._disconnect_helper("_write_to_socket : Exception")
            return False
