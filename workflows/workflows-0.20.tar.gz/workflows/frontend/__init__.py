from __future__ import absolute_import, division
import logging
import multiprocessing
import Queue
import threading
import time
import workflows.services
from workflows.services.common_service import CommonService
import workflows.status
import workflows.transport

class Frontend():
  '''The frontend class encapsulates the actual service. It controls the
     service process and keeps the connection to the transport layer. It
     can process control messages directly, or pass messages on to the
     service. On initialization a status advertising thread is started,
     which keeps running in the background.'''

  def __init__(self, transport=None, service=None,
      transport_command_prefix=None):
    '''Create a frontend instance. Connect to the transport layer, start any
       requested service, begin broadcasting status information and listen
       for control commands.
       :param transport: Either the name of a transport class, a transport
                         class, or a transport class object.
       :param service: A class or name of the class to be instantiated in a
                       subprocess as service.
       :param transport_command_prefix: An optional prefix of a transport
                                        subscription to be listened to for
                                        commands.
    '''
    self.__lock = threading.RLock()
    self.__hostid = self._generate_unique_host_id()
    self._service = None
    self._service_name = None
    self._service_transportid = None
    self._pipe_commands = None # frontend -> service
    self._pipe_service = None  # frontend <- service
    self._service_status = CommonService.SERVICE_STATUS_NONE

    self.restart_service = True
    self.shutdown = False

    # Set up logging
    class logadapter():
      '''A helper class that acts like a dictionary, but actually reads its
         values from the get_status() function.'''
      status_fn = self.get_status
      status = status_fn()

      def __iter__(self):
        '''Update cached status values, renaming the keys for logging.
           Return a dictionary key iterator.'''
        self.status = { 'workflows_' + k: v
                        for k, v in self.status_fn().iteritems() }
        return self.status.__iter__()

      def __getitem__(self, key):
        '''Return a value from the status dictionary.'''
        return self.status.__getitem__(key)
    self.log = logging.LoggerAdapter(
                   logging.getLogger('workflows.frontend'),
                   logadapter())

    # Connect to the network transport layer
    if transport is None or isinstance(transport, basestring):
      self._transport = workflows.transport.lookup(transport)()
    elif hasattr(transport, '__call__'):
      self._transport = transport()
    else:
      self._transport = transport
    assert self._transport.connect(), "Could not connect to transport layer"
    self._service_transportid = self._transport.register_client()

    if transport_command_prefix:
      self._transport.subscribe(transport_command_prefix + self.__hostid,
                                self.process_transport_command)
      self.log.debug('Listening for commands on transport layer')

    # Start initial service if one has been requested
    self._service_factory = service
    if service is not None:
      self._service_status = CommonService.SERVICE_STATUS_NEW
      self.switch_service(service)

    # Start broadcasting node information
    self._status_advertiser = workflows.status.StatusAdvertise(
        interval=6,
        status_callback=self.get_status,
        transport=self._transport)
    self._status_advertiser.start()

  def run(self):
    '''The main loop of the frontend. Here incoming messages from the service
       are processed and forwarded to the corresponding callback methods.'''
    self.log.info("Current service: " + str(self._service))
    n = 3600
    while n > 0 and not self.shutdown:
      if self._pipe_service and self._pipe_service.poll(1):
        try:
          message = self._pipe_service.recv()
          if isinstance(message, dict) and 'band' in message:
            # only dictionaries with 'band' entry are valid messages
            try:
              handler = getattr(self, 'parse_band_' + message['band'])
            except AttributeError:
              handler = None
              self.log.warn("Unknown band " + str(message['band']))
            if handler:
#              try:
                handler(message)
#              except Exception:
#                print 'Uh oh. What to do.'
          else:
            self.log.warn("Invalid message received " + str(message))
        except Queue.Empty:
          pass
      n = n - 1
      if self._service_status == CommonService.SERVICE_STATUS_ERROR:
        self._transport.disconnect()
        print "Disced"
        import sys
        sys.exit(1)

    self._service_status = CommonService.SERVICE_STATUS_TEARDOWN
    self._status_advertiser.trigger()
    self._terminate_service()
    self._status_advertiser.stop_and_wait()
    self.log.info("Fin. Terminating.")

  def send_command(self, command):
    '''Send command to service via the command queue.'''
#   print "To command queue: ", command
    if self._pipe_commands:
      self._pipe_commands.send(command)

  def process_transport_command(self, header, message):
    '''Parse a command coming in through the transport command subscription'''
    if message and message.get('command'):
      self.log.info('Received command \'%s\' via transport layer', message['command'])
      if message['command'] == 'shutdown':
        self.shutdown = True
    else:
      self.log.warn('Received invalid transport command message')

  def parse_band_log(self, message):
    '''Process incoming logging messages from the service.'''
    if 'payload' in message and hasattr(message['payload'], 'name'):
      record = message['payload']
      for k, v in self.get_status().iteritems():
        setattr(record, 'workflows_' + k, v)
      logging.getLogger(record.name).handle(record)
    else:
      self.log.warn("Received broken record on log band\nMessage: %s\nRecord: %s",
                    str(message),
                    str(hasattr(message.get('payload'), '__dict__') and message['payload'].__dict__))

  def parse_band_status_update(self, message):
    '''Process incoming status updates from the service.'''
    self.log.debug("Status update: " + str(message))
    self._service_status = message['statuscode']
    self._status_advertiser.trigger()

  def get_host_id(self):
    '''Get a cached copy of the host id.'''
    return self.__hostid

  @staticmethod
  def _generate_unique_host_id():
    '''Generate a unique ID, that is somewhat guaranteed to be unique among all
       instances running at the same time.'''
    import socket
    host = '.'.join(reversed(socket.gethostname().split('.')))
    import os
    pid = os.getpid()
    return "%s.%d" % (host, pid)

  def get_status(self):
    '''Returns a dictionary containing all relevant status information to be
       broadcast across the network.'''
    return { 'host': self.__hostid,
             'status': self._service_status,
             'statustext': CommonService.human_readable_state.get(self._service_status),
             'service': self._service_name }

  def switch_service(self, new_service):
    '''Start a new service in a subprocess.
       :param new_service: Either a service name or a service class.
       :return: True on success, False on failure.
    '''
    with self.__lock:
      # Terminate existing service if necessary
      if self._service is not None:
        self._terminate_service()

      # Find service class if necessary
      if isinstance(new_service, basestring):
        service_class = workflows.services.lookup(new_service)
      else:
        service_class = new_service

      if not service_class:
        return False

      # Set up pipes and connect new service object
      self._pipe_commands, svc_commands = multiprocessing.Pipe()
      svc_tofrontend, self._pipe_service = multiprocessing.Pipe()
      service_instance = service_class(
        commands=svc_commands,
        frontend=svc_tofrontend)

      # Clean out transport layer for new service
      if self._service_transportid:
        self._transport.drop_client(self._service_transportid)
      self._service_transportid = self._transport.register_client()

      # Start new service in a separate process
      self._service = multiprocessing.Process(
        target=service_instance.start, args=())
      self._service_name = service_instance.get_name()
      self._service.daemon = True
      self._service.start()
    return True

  def _terminate_service(self):
    '''Force termination of running service.
       Disconnect queues, end queue feeder threads.
       Wait for service process to clear, drop all references.'''
    with self.__lock:
      self._service.terminate()
      self._pipe_commands.close()
      self._pipe_service.close()
      self._pipe_commands = None
      self._pipe_service = None
      self._service_name = None
      self._service_status = CommonService.SERVICE_STATUS_END
      if self._service_transportid:
        self._transport.drop_client(self._service_transportid)
      self._service_transportid = None
      self._service.join() # must wait for process to be actually destroyed
      self._service = None

# ---- Transport calls -----------------------------------------------------

  _transaction_mapping = {}

  def parse_band_transport(self, message):
    '''Treat messages sent from service via queue. These were encoded by
       transport.queue_transport on the other end. Forward the messages to
       individual functions parse_band_transport_${call}() depending on the
       'call' field.
       param: message: The full queue message data structure.
    '''
    try:
      handler = getattr(self, 'parse_band_transport_' + message['call'])
    except AttributeError:
      # TODO: This should go to a log
      print 'Unknown transport handler for message', message
      return
    if 'transaction' in message['payload'][1]:
#     print "Mapping transaction %s to %s for %s" % (
#         str( message['payload'][1]['transaction'] ),
#         str( self._transaction_mapping[message['payload'][1]['transaction']] ),
#         message['call'])
      message['payload'][1]['transaction'] = \
        self._transaction_mapping[message['payload'][1]['transaction']]
    handler(message)

  def parse_band_transport_send(self, message):
    '''Counterpart to the transport.send call from the service.
       Forward the call to the real transport layer.'''
    args, kwargs = message['payload']
    self._transport.send(*args, **kwargs)

  def parse_band_transport_broadcast(self, message):
    '''Counterpart to the transport.broadcast call from the service.
       Forward the call to the real transport layer.'''
    args, kwargs = message['payload']
    self._transport.broadcast(*args, **kwargs)

  def parse_band_transport_ack(self, message):
    '''Counterpart to the transport.ack call from the service.
       Forward the call to the real transport layer.'''
    args, kwargs = message['payload']
    self._transport.ack(*args, **kwargs)

  def parse_band_transport_nack(self, message):
    '''Counterpart to the transport.nack call from the service.
       Forward the call to the real transport layer.'''
    args, kwargs = message['payload']
    self._transport.nack(*args, **kwargs)

  def parse_band_transport_transaction_begin(self, message):
    '''Counterpart to the transport.transaction_begin call from the service.
       Forward the call to the real transport layer.'''
    args, kwargs = message['payload']
    service_txn_id = args[0]
    self._transaction_mapping[service_txn_id] = \
      self._transport.transaction_begin(clientid=self._service_transportid)

  def parse_band_transport_transaction_commit(self, message):
    '''Counterpart to the transport.transaction_begin call from the service.
       Forward the call to the real transport layer.'''
    args, kwargs = message['payload']
    service_txn_id = args[0]
    assert service_txn_id in self._transaction_mapping
    self._transport.transaction_commit(self._transaction_mapping[service_txn_id])
    del(self._transaction_mapping[service_txn_id])

  def parse_band_transport_transaction_abort(self, message):
    '''Counterpart to the transport.transaction_abort call from the service.
       Forward the call to the real transport layer.'''
    args, kwargs = message['payload']
    service_txn_id = args[0]
    assert service_txn_id in self._transaction_mapping
    self._transport.transaction_abort(self._transaction_mapping[service_txn_id])
    del(self._transaction_mapping[service_txn_id])

  def parse_band_transport_subscribe(self, message):
    '''Counterpart to the transport.subscribe call from the service.
       Forward the call to the real transport layer.'''
    subscription_id, channel = message['payload'][0][:2]
    self._transport.subscribe(channel,
      lambda cb_header, cb_message:
      self.send_command( {
          'band': 'transport_message',
          'payload': {
            'subscription_id': subscription_id,
            'header': cb_header,
            'message': cb_message,
          },
        } ),
       *message['payload'][0][2:],
       **message['payload'][1]
    )

  def parse_band_transport_subscribe_broadcast(self, message):
    '''Counterpart to the transport.subscribe_broadcast call from the service.
       Forward the call to the real transport layer.'''
    subscription_id, channel = message['payload'][0][:2]
    self._transport.subscribe_broadcast(channel,
      lambda cb_header, cb_message:
      self.send_command( {
          'band': 'transport_message',
          'payload': {
            'subscription_id': subscription_id,
            'header': cb_header,
            'message': cb_message,
          },
        } ),
       *message['payload'][0][2:],
       **message['payload'][1]
    )
