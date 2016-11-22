from __future__ import absolute_import, division

import workflows.services
from workflows.services.common_service import Commands, CommonService
import mock
from multiprocessing import Pipe
import pytest

def test_instantiate_basic_service():
  '''Create a basic service object'''
  service = CommonService()

  assert service.get_name() is not None

def test_logging_to_frontend():
  '''Log messages should be passed to frontend'''
  fe_pipe = mock.Mock()
  service = CommonService(frontend=fe_pipe)

  # Start service to initialize logging
  service.start()

  # Note that by default only warning and higher are passed to frontend
  service.log.warn(mock.sentinel.logmessage)

  fe_pipe.send.assert_called()
  assert fe_pipe.send.call_args == (({'band': 'log', 'payload': mock.ANY},), {})
  logrec = fe_pipe.send.call_args[0][0]['payload']
  assert logrec.levelname == 'WARNING'
  assert str(mock.sentinel.logmessage) in logrec.message

def test_receive_and_follow_shutdown_command():
  '''Receive a shutdown message via the command pipe and act on it.
     Check that status codes are updated properly.'''
  cmd_pipe = mock.Mock()
  cmd_pipe.poll.return_value = True
  cmd_pipe.recv.side_effect = [
    { 'band': 'command',
      'payload': Commands.SHUTDOWN },
    AssertionError('Not observing commands') ]
  fe_pipe, fe_pipe_out = Pipe()

  # Create service
  service = CommonService(
      commands=cmd_pipe, frontend=fe_pipe)
  # override class API to ensure overidden functions are called
  service.initializing = mock.Mock()
  service.in_shutdown = mock.Mock()

  # Check new status
  messages = []
  while fe_pipe_out.poll():
    message = fe_pipe_out.recv()
    if 'statuscode' in message:
      messages.append(message['statuscode'])
  assert messages == [ service.SERVICE_STATUS_NEW ]

  # Start service
  service.start()

  # Check startup/shutdown sequence
  service.initializing.assert_called_once()
  service.in_shutdown.assert_called_once()
  cmd_pipe.recv.assert_called_once_with()
  messages = []
  while fe_pipe_out.poll():
    message = fe_pipe_out.recv()
    if 'statuscode' in message:
      messages.append(message['statuscode'])
  assert messages == [
    service.SERVICE_STATUS_STARTING,
    service.SERVICE_STATUS_IDLE,
    service.SERVICE_STATUS_PROCESSING,
    service.SERVICE_STATUS_SHUTDOWN,
    service.SERVICE_STATUS_END,
    ]

def test_idle_timer_is_triggered():
  '''Check that the idle timer callback is run if set.'''
  cmd_pipe = mock.Mock()
  cmd_pipe.poll.side_effect = [ False, True ]
  cmd_pipe.recv.side_effect = [
    { 'band': 'command',
      'payload': Commands.SHUTDOWN },
    AssertionError('Not observing commands') ]
  fe_pipe, fe_pipe_out = Pipe()
  idle_trigger = mock.Mock()

  # Create service
  service = CommonService(commands=cmd_pipe, frontend=fe_pipe)
  service._register_idle(10, idle_trigger)

  # Start service
  service.start()

  # Check trigger has been called
  idle_trigger.assert_called_once_with()

  # Check startup/shutdown sequence
  cmd_pipe.recv.assert_called_once_with()
  assert cmd_pipe.poll.call_count == 2
  assert cmd_pipe.poll.call_args == ((10,),)
  messages = []
  while fe_pipe_out.poll():
    message = fe_pipe_out.recv()
    if 'statuscode' in message:
      messages.append(message['statuscode'])
  assert messages == [
    service.SERVICE_STATUS_NEW,
    service.SERVICE_STATUS_STARTING,
    service.SERVICE_STATUS_IDLE,
    service.SERVICE_STATUS_TIMER,
    service.SERVICE_STATUS_IDLE,
    service.SERVICE_STATUS_PROCESSING,
    service.SERVICE_STATUS_SHUTDOWN,
    service.SERVICE_STATUS_END,
    ]

def test_callbacks_are_routed_correctly():
  '''Incoming messages are routed to the correct callback functions'''
  cmd_pipe = mock.Mock()
  cmd_pipe.poll.return_value = True
  cmd_pipe.recv.side_effect = [
    { 'band': mock.sentinel.band,
      'payload': mock.sentinel.payload },
    { 'band': 'command',
      'payload': Commands.SHUTDOWN },
    AssertionError('Not observing commands') ]
  fe_pipe, _ = Pipe()
  callback = mock.Mock()

  # Create service
  service = CommonService(commands=cmd_pipe, frontend=fe_pipe)
  service._register(mock.sentinel.band, callback)

  # Start service
  service.start()

  # Check callback occured
  callback.assert_called_with(mock.sentinel.payload)

def test_log_unknown_band_data():
  '''All unidentified messages should be logged to the frondend.'''
  cmd_pipe = mock.Mock()
  cmd_pipe.poll.return_value = True
  cmd_pipe.recv.side_effect = [
    { 'band': mock.sentinel.band, 'payload': mock.sentinel.failure1 },
    { 'payload': mock.sentinel.failure2 },
    { 'band': 'command',
      'payload': Commands.SHUTDOWN },
    AssertionError('Not observing commands') ]
  fe_pipe, fe_pipe_out = Pipe()

  # Create service
  service = CommonService(commands=cmd_pipe, frontend=fe_pipe)

  # Start service
  service.start()

  # Check startup/shutdown sequence
  messages = []
  while fe_pipe_out.poll():
    message = fe_pipe_out.recv()
    if message.get('band') == 'log':
      messages.append(message.get('payload'))
  assert len(messages) == 2
  assert messages[0].name == 'workflows.service'
  assert 'unregistered band' in messages[0].message
  assert str(mock.sentinel.band) in messages[0].message
  assert messages[1].name == 'workflows.service'
  assert 'without band' in messages[1].message
