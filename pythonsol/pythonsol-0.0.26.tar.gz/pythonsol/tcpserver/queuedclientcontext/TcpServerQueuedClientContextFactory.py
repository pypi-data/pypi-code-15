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

# Logger
import logging

from pythonsol.SolBase import SolBase
from pythonsol.tcpserver.basefactory.TcpServerClientContextAbstractFactory import TcpServerClientContextAbstractFactory
from pythonsol.tcpserver.queuedclientcontext.TcpServerQueuedClientContext import TcpServerQueuedClientContext


SolBase.logging_init()
logger = logging.getLogger("TcpServerQueuedClientContextFactory")


class TcpServerQueuedClientContextFactory(TcpServerClientContextAbstractFactory):
    """
    Default factory.
    """

    # noinspection PyMethodMayBeStatic
    def get_new_clientcontext(self, tcp_server, client_id, client_socket, client_addr):
        """
        Return a new client context instance.
        :param tcp_server: The tcpserver instance.
        :param  client_id: an integer, which is the unique id of this client.
        :param  client_socket: The server socket.
        :param  client_addr: The remote addr information.
        :return Returned object MUST be a subclass of TcpServerClientContext.
        """
        return TcpServerQueuedClientContext(tcp_server, client_id, client_socket, client_addr)
