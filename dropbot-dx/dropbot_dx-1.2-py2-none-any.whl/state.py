# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='state.proto',
  package='dropbot_dx',
  serialized_pb=_b('\n\x0bstate.proto\x12\ndropbot_dx\"\xb7\x01\n\x05State\x12\x14\n\x07voltage\x18\x01 \x01(\x02:\x03\x31\x30\x30\x12\x18\n\tfrequency\x18\x02 \x01(\x02:\x05\x31\x30\x30\x30\x30\x12 \n\x11hv_output_enabled\x18\x03 \x01(\x08:\x05\x66\x61lse\x12 \n\x12hv_output_selected\x18\x04 \x01(\x08:\x04true\x12\x1b\n\rlight_enabled\x18\x05 \x01(\x08:\x04true\x12\x1d\n\x0emagnet_engaged\x18\x06 \x01(\x08:\x05\x66\x61lse')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STATE = _descriptor.Descriptor(
  name='State',
  full_name='dropbot_dx.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voltage', full_name='dropbot_dx.State.voltage', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='dropbot_dx.State.frequency', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=10000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hv_output_enabled', full_name='dropbot_dx.State.hv_output_enabled', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hv_output_selected', full_name='dropbot_dx.State.hv_output_selected', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='light_enabled', full_name='dropbot_dx.State.light_enabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magnet_engaged', full_name='dropbot_dx.State.magnet_engaged', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=211,
)

DESCRIPTOR.message_types_by_name['State'] = _STATE

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(
  DESCRIPTOR = _STATE,
  __module__ = 'state_pb2'
  # @@protoc_insertion_point(class_scope:dropbot_dx.State)
  ))
_sym_db.RegisterMessage(State)


# @@protoc_insertion_point(module_scope)
