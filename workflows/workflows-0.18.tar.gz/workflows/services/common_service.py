from __future__ import absolute_import, division
import logging
import Queue
import workflows
import workflows.logging
from workflows.transport.queue_transport import QueueTransport

class CommonService(object):
  '''
  Base class for workflow services. A service is a piece of software that runs
  in an isolated environment, communicating only via queues with the outside
  world. Units of work are injected via a queue. Results, status and log
  messages, etc. are written out via a queue. Any task can be encapsulated
  as a service, for example a service that counts spots on an image passed
  as a filename, and returns the number of counts.

  To instantiate a service two Queue-like objects should be passed to the
  constructors, one to communicate from the service to the frontend, one to
  communicate from the frontend to the service.
  '''

  # Human readable service name -----------------------------------------------

  _service_name = 'unnamed service'

  # Logger name ---------------------------------------------------------------

  _logger_name = 'workflows.service'  # The logger can be accessed via self.log

  # Overrideable functions ----------------------------------------------------

  def initializing(self):
    '''Service initialization. This function is run before any commands are
       received from the frontend. This is the place to request channel
       subscriptions with the messaging layer, and register callbacks.
       This function can be overridden by specific service implementations.'''
    pass

  def in_shutdown(self):
    '''Service shutdown. This function is run before the service is terminated.
       No more commands are received, but communications can still be sent.
       This function can be overridden by specific service implementations.'''
    pass

  # Internal service status codes ---------------------------------------------
  # These codes will be sent to the frontend to indicate the current state of
  # the main loop regardless of the status text, which can be set freely by
  # the specific service.

  # The state transitions are: (see definition of start() below)
  #  constructor() -> NEW
  #            NEW -> start() being called -> STARTING
  #       STARTING -> self.initializing() -> IDLE
  #           IDLE -> wait for messages on command queue -> PROCESSING
  #              \--> optionally: idle timer elapsed -> TIMER
  #     PROCESSING -> process command -> IDLE
  #              \--> shutdown command received -> SHUTDOWN
  #          TIMER -> process event -> IDLE
  #       SHUTDOWN -> self.in_shutdown() -> END
  #  unhandled exception -> ERROR

  SERVICE_STATUS_NEW, SERVICE_STATUS_STARTING, SERVICE_STATUS_IDLE, \
    SERVICE_STATUS_TIMER, SERVICE_STATUS_PROCESSING, SERVICE_STATUS_SHUTDOWN, \
    SERVICE_STATUS_END, SERVICE_STATUS_ERROR = range(8)

  # Extra states that are not used by services themselves but may be used
  # externally:

  SERVICE_STATUS_NONE = -1     # Node has no service instance loaded
  SERVICE_STATUS_TEARDOWN = -2 # Node is shutting down

  # Number to short string conversion

  human_readable_state = {
    SERVICE_STATUS_NEW: 'constructing',
    SERVICE_STATUS_STARTING: 'starting',
    SERVICE_STATUS_IDLE: 'idle',
    SERVICE_STATUS_TIMER: 'timer event',
    SERVICE_STATUS_PROCESSING: 'processing',
    SERVICE_STATUS_SHUTDOWN: 'shutting down',
    SERVICE_STATUS_END: 'shutdown',
    SERVICE_STATUS_ERROR: 'error',
    SERVICE_STATUS_NONE: 'no service loaded',
    SERVICE_STATUS_TEARDOWN: 'shutdown',
  }

  # Not so overrideable functions ---------------------------------------------

  def __init__(self, *args, **kwargs):
    '''Service constructor. Parameters include optional references to two
       pipes: frontend= for messages from the service to the frontend,
       and commands= for messages from the frontend to the service.'''
    self.__pipe_frontend = kwargs.get('frontend')
    self.__pipe_commands = kwargs.get('commands')
    self._transport = workflows.transport.queue_transport.QueueTransport()
    self._transport.set_send_function(self.__send_to_frontend)
    self._transport.connect()
    self.__shutdown = False
    self.__callback_register = {}
    self.__update_service_status(self.SERVICE_STATUS_NEW)
    self._idle_callback = None
    self._idle_time = None

    # Logger will be overwritten in start() function
    self.log = logging.getLogger(self._logger_name)

  def __send_to_frontend(self, data_structure):
    '''Put a message in the pipe for the frontend.'''
    if self.__pipe_frontend:
      self.__pipe_frontend.send(data_structure)

  def _log_send(self, logrecord):
    '''Forward log records to the frontend.'''
    self.__send_to_frontend({
      'band': 'log',
      'payload': logrecord
    })

  def _register(self, message_band, callback):
    '''Register a callback function for a specific message band.'''
    self.__callback_register[message_band] = callback

  def _register_idle(self, idle_time, callback):
    '''Register a callback function that is run when idling for a given
       time span (in seconds).'''
    self._idle_callback = callback
    self._idle_time = idle_time

  def __update_service_status(self, statuscode):
    '''Set the internal status of the service object, and notify frontend.'''
    self.__service_status = statuscode
    self.__send_to_frontend({
      'band': 'status_update',
      'statuscode': self.__service_status
    })

  def get_name(self):
    '''Return a name for this service.
       Change the name by overwriting self._service_name.'''
    return self._service_name

  def initialize_logging(self):
    '''Reset the logging for the service process. All logged messages are
       forwarded to the frontend. If any filtering is desired, then this must
       take place on the service side.'''
    # Reset logging to pass logrecords into the queue to the frontend only.
    # Existing handlers may be broken as they were copied into a new process,
    # so should be discarded.
    for loggername in [None] + list(logging.Logger.manager.loggerDict.keys()):
      logger = logging.getLogger(loggername)
      while logger.handlers:
        logger.removeHandler(logger.handlers[0])

    # Re-enable logging to console
    root_logger = logging.getLogger()

    # By default pass all warning (and higher) level messages to the frontend
    root_logger.setLevel(logging.WARN)
    root_logger.addHandler(workflows.logging.CallbackHandler(self._log_send))

    # Set up the service logger and pass all info (and higher) level messages
    self.log = logging.getLogger(self._logger_name)
    self.log.setLevel(logging.INFO)

    # Additionally, write all critical messages directly to console
    console = logging.StreamHandler()
    console.setLevel(logging.CRITICAL)
    root_logger.addHandler(console)

  def start(self):
    '''Start listening to command queue, process commands in main loop,
       set status, etc...
       This function is most likely called by the frontend in a separate
       process.'''
    self.initialize_logging()

    self.__update_service_status(self.SERVICE_STATUS_STARTING)

    self.initializing()
    self._register('command', self.__process_command)
    self._register('transport_message', self.__process_transport)

    if self.__pipe_commands is None:
      # can only listen to commands if command queue is defined
      self.__shutdown = True

    while not self.__shutdown: # main loop
      self.__update_service_status(self.SERVICE_STATUS_IDLE)

      if self._idle_time is None:
        message = self.__pipe_commands.recv()
      else:
        if self.__pipe_commands.poll(self._idle_time):
          message = self.__pipe_commands.recv()
        else:
          self.__update_service_status(self.SERVICE_STATUS_TIMER)
          if self._idle_callback is not None:
            self._idle_callback()
          continue

      self.__update_service_status(self.SERVICE_STATUS_PROCESSING)

      if message and 'band' in message:
        processor = self.__callback_register.get(message['band'])
        if processor is None:
          self.log.warn('received message on unregistered band\n%s', message)
        else:
          processor(message.get('payload'))
      else:
        self.log.warn('received message without band information\n%s', message)

    self.__update_service_status(self.SERVICE_STATUS_SHUTDOWN)

    self.in_shutdown()

    self.__update_service_status(self.SERVICE_STATUS_END)

  def __process_command(self, command):
    '''Process an incoming command message from the frontend.'''
    if command == Commands.SHUTDOWN:
      self.__shutdown = True

  def __process_transport(self, message):
    '''Process an incoming transport message from the frontend.'''
    if self._transport.subscription_requires_ack(message['subscription_id']):
      self._transport.register_message(message['subscription_id'],
                                       message['header']['message-id'])
    self._transport.subscription_callback(message['subscription_id']) \
      ( message['header'], message['message'] )

  #
  # -- Plugin-related function -----------------------------------------------
  #

  class __metaclass__(type):
    '''Define metaclass function to keep a list of all subclasses. This enables
       looking up service mechanisms by name.'''
    def __init__(cls, name, base, attrs):
      '''Add new subclass of CommonService to list of all known subclasses.'''
      if not hasattr(cls, 'service_register'):
        cls.service_register = {}
      else:
        cls.service_register[name] = cls

class Commands():
  '''A list of command strings used for communicating with the frontend.'''
  SHUTDOWN = 'shutdown'
