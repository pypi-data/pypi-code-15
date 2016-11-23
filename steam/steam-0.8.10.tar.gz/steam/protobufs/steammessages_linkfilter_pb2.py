# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: steammessages_linkfilter.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import steam.protobufs.steammessages_unified_base_pb2 as steammessages__unified__base__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='steammessages_linkfilter.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x1esteammessages_linkfilter.proto\x1a steammessages_unified_base.proto\"\x9d\x02\n,CCommunity_GetLinkFilterHashPrefixes_Request\x12G\n\x08hit_type\x18\x01 \x01(\rB5\x82\xb5\x18\x31The retrieved hits will be filtered to this type.\x12\\\n\x05\x63ount\x18\x02 \x01(\rBM\x82\xb5\x18IThe number of hits to retrieve in a single batch. Specify 0 for no limit.\x12\x46\n\x05start\x18\x03 \x01(\x04\x42\x37\x82\xb5\x18\x33The starting count when retrieving hits in batches.\"\x87\x01\n-CCommunity_GetLinkFilterHashPrefixes_Response\x12V\n\rhash_prefixes\x18\x01 \x03(\rB?\x82\xb5\x18;The first 32 bits of the SHA1 hashes of each hit requested.\"\x97\x02\n&CCommunity_GetLinkFilterHashes_Request\x12G\n\x08hit_type\x18\x01 \x01(\rB5\x82\xb5\x18\x31The retrieved hits will be filtered to this type.\x12\\\n\x05\x63ount\x18\x02 \x01(\rBM\x82\xb5\x18IThe number of hits to retrieve in a single batch. Specify 0 for no limit.\x12\x46\n\x05start\x18\x03 \x01(\x04\x42\x37\x82\xb5\x18\x33The starting count when retrieving hits in batches.\"j\n\'CCommunity_GetLinkFilterHashes_Response\x12?\n\x06hashes\x18\x01 \x03(\x0c\x42/\x82\xb5\x18+A list of hashes returned from our request.\"\x80\x01\n+CCommunity_GetLinkFilterListVersion_Request\x12Q\n\x08hit_type\x18\x01 \x01(\rB?\x82\xb5\x18;The version hashes for this type\'s chunks will be returned.\"\xaa\x01\n,CCommunity_GetLinkFilterListVersion_Response\x12\x46\n\x07version\x18\x01 \x01(\tB5\x82\xb5\x18\x31\x41 hash built using the IDs of the contained hits.\x12\x32\n\x05\x63ount\x18\x02 \x01(\x04\x42#\x82\xb5\x18\x1fThe number of hits of this type2\xc6\x05\n\x13\x43ommunityLinkFilter\x12\xd2\x01\n\x19GetLinkFilterHashPrefixes\x12-.CCommunity_GetLinkFilterHashPrefixes_Request\x1a..CCommunity_GetLinkFilterHashPrefixes_Response\"V\x82\xb5\x18RGet a list of hash prefixes for the specified hit type, to use for client caching.\x12\xb9\x01\n\x13GetLinkFilterHashes\x12\'.CCommunity_GetLinkFilterHashes_Request\x1a(.CCommunity_GetLinkFilterHashes_Response\"O\x82\xb5\x18KGet a list of hashes for the specified hit type, to use for client caching.\x12\xcd\x01\n\x18GetLinkFilterListVersion\x12,.CCommunity_GetLinkFilterListVersion_Request\x1a-.CCommunity_GetLinkFilterListVersion_Response\"T\x82\xb5\x18PGet a list of hashes describing the version of each chunk of the requested size.\x1aN\x82\xb5\x18JA service for recording data about Steam Community phishing link filteringB\x03\x90\x01\x01')
  ,
  dependencies=[steammessages__unified__base__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST = _descriptor.Descriptor(
  name='CCommunity_GetLinkFilterHashPrefixes_Request',
  full_name='CCommunity_GetLinkFilterHashPrefixes_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hit_type', full_name='CCommunity_GetLinkFilterHashPrefixes_Request.hit_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0301The retrieved hits will be filtered to this type.'))),
    _descriptor.FieldDescriptor(
      name='count', full_name='CCommunity_GetLinkFilterHashPrefixes_Request.count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030IThe number of hits to retrieve in a single batch. Specify 0 for no limit.'))),
    _descriptor.FieldDescriptor(
      name='start', full_name='CCommunity_GetLinkFilterHashPrefixes_Request.start', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0303The starting count when retrieving hits in batches.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=354,
)


_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE = _descriptor.Descriptor(
  name='CCommunity_GetLinkFilterHashPrefixes_Response',
  full_name='CCommunity_GetLinkFilterHashPrefixes_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash_prefixes', full_name='CCommunity_GetLinkFilterHashPrefixes_Response.hash_prefixes', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030;The first 32 bits of the SHA1 hashes of each hit requested.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=357,
  serialized_end=492,
)


_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST = _descriptor.Descriptor(
  name='CCommunity_GetLinkFilterHashes_Request',
  full_name='CCommunity_GetLinkFilterHashes_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hit_type', full_name='CCommunity_GetLinkFilterHashes_Request.hit_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0301The retrieved hits will be filtered to this type.'))),
    _descriptor.FieldDescriptor(
      name='count', full_name='CCommunity_GetLinkFilterHashes_Request.count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030IThe number of hits to retrieve in a single batch. Specify 0 for no limit.'))),
    _descriptor.FieldDescriptor(
      name='start', full_name='CCommunity_GetLinkFilterHashes_Request.start', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0303The starting count when retrieving hits in batches.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=774,
)


_CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE = _descriptor.Descriptor(
  name='CCommunity_GetLinkFilterHashes_Response',
  full_name='CCommunity_GetLinkFilterHashes_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashes', full_name='CCommunity_GetLinkFilterHashes_Response.hashes', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030+A list of hashes returned from our request.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=776,
  serialized_end=882,
)


_CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST = _descriptor.Descriptor(
  name='CCommunity_GetLinkFilterListVersion_Request',
  full_name='CCommunity_GetLinkFilterListVersion_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hit_type', full_name='CCommunity_GetLinkFilterListVersion_Request.hit_type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030;The version hashes for this type\'s chunks will be returned.'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=1013,
)


_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE = _descriptor.Descriptor(
  name='CCommunity_GetLinkFilterListVersion_Response',
  full_name='CCommunity_GetLinkFilterListVersion_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='CCommunity_GetLinkFilterListVersion_Response.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0301A hash built using the IDs of the contained hits.'))),
    _descriptor.FieldDescriptor(
      name='count', full_name='CCommunity_GetLinkFilterListVersion_Response.count', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\037The number of hits of this type'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1016,
  serialized_end=1186,
)

DESCRIPTOR.message_types_by_name['CCommunity_GetLinkFilterHashPrefixes_Request'] = _CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST
DESCRIPTOR.message_types_by_name['CCommunity_GetLinkFilterHashPrefixes_Response'] = _CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE
DESCRIPTOR.message_types_by_name['CCommunity_GetLinkFilterHashes_Request'] = _CCOMMUNITY_GETLINKFILTERHASHES_REQUEST
DESCRIPTOR.message_types_by_name['CCommunity_GetLinkFilterHashes_Response'] = _CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE
DESCRIPTOR.message_types_by_name['CCommunity_GetLinkFilterListVersion_Request'] = _CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST
DESCRIPTOR.message_types_by_name['CCommunity_GetLinkFilterListVersion_Response'] = _CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE

CCommunity_GetLinkFilterHashPrefixes_Request = _reflection.GeneratedProtocolMessageType('CCommunity_GetLinkFilterHashPrefixes_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST,
  __module__ = 'steammessages_linkfilter_pb2'
  # @@protoc_insertion_point(class_scope:CCommunity_GetLinkFilterHashPrefixes_Request)
  ))
_sym_db.RegisterMessage(CCommunity_GetLinkFilterHashPrefixes_Request)

CCommunity_GetLinkFilterHashPrefixes_Response = _reflection.GeneratedProtocolMessageType('CCommunity_GetLinkFilterHashPrefixes_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE,
  __module__ = 'steammessages_linkfilter_pb2'
  # @@protoc_insertion_point(class_scope:CCommunity_GetLinkFilterHashPrefixes_Response)
  ))
_sym_db.RegisterMessage(CCommunity_GetLinkFilterHashPrefixes_Response)

CCommunity_GetLinkFilterHashes_Request = _reflection.GeneratedProtocolMessageType('CCommunity_GetLinkFilterHashes_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCOMMUNITY_GETLINKFILTERHASHES_REQUEST,
  __module__ = 'steammessages_linkfilter_pb2'
  # @@protoc_insertion_point(class_scope:CCommunity_GetLinkFilterHashes_Request)
  ))
_sym_db.RegisterMessage(CCommunity_GetLinkFilterHashes_Request)

CCommunity_GetLinkFilterHashes_Response = _reflection.GeneratedProtocolMessageType('CCommunity_GetLinkFilterHashes_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE,
  __module__ = 'steammessages_linkfilter_pb2'
  # @@protoc_insertion_point(class_scope:CCommunity_GetLinkFilterHashes_Response)
  ))
_sym_db.RegisterMessage(CCommunity_GetLinkFilterHashes_Response)

CCommunity_GetLinkFilterListVersion_Request = _reflection.GeneratedProtocolMessageType('CCommunity_GetLinkFilterListVersion_Request', (_message.Message,), dict(
  DESCRIPTOR = _CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST,
  __module__ = 'steammessages_linkfilter_pb2'
  # @@protoc_insertion_point(class_scope:CCommunity_GetLinkFilterListVersion_Request)
  ))
_sym_db.RegisterMessage(CCommunity_GetLinkFilterListVersion_Request)

CCommunity_GetLinkFilterListVersion_Response = _reflection.GeneratedProtocolMessageType('CCommunity_GetLinkFilterListVersion_Response', (_message.Message,), dict(
  DESCRIPTOR = _CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE,
  __module__ = 'steammessages_linkfilter_pb2'
  # @@protoc_insertion_point(class_scope:CCommunity_GetLinkFilterListVersion_Response)
  ))
_sym_db.RegisterMessage(CCommunity_GetLinkFilterListVersion_Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\220\001\001'))
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST.fields_by_name['hit_type'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST.fields_by_name['hit_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0301The retrieved hits will be filtered to this type.'))
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST.fields_by_name['count'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST.fields_by_name['count']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030IThe number of hits to retrieve in a single batch. Specify 0 for no limit.'))
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST.fields_by_name['start'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST.fields_by_name['start']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0303The starting count when retrieving hits in batches.'))
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE.fields_by_name['hash_prefixes'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE.fields_by_name['hash_prefixes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030;The first 32 bits of the SHA1 hashes of each hit requested.'))
_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST.fields_by_name['hit_type'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST.fields_by_name['hit_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0301The retrieved hits will be filtered to this type.'))
_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST.fields_by_name['count'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST.fields_by_name['count']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030IThe number of hits to retrieve in a single batch. Specify 0 for no limit.'))
_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST.fields_by_name['start'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST.fields_by_name['start']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0303The starting count when retrieving hits in batches.'))
_CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE.fields_by_name['hashes'].has_options = True
_CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE.fields_by_name['hashes']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030+A list of hashes returned from our request.'))
_CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST.fields_by_name['hit_type'].has_options = True
_CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST.fields_by_name['hit_type']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030;The version hashes for this type\'s chunks will be returned.'))
_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE.fields_by_name['version'].has_options = True
_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\0301A hash built using the IDs of the contained hits.'))
_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE.fields_by_name['count'].has_options = True
_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE.fields_by_name['count']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\202\265\030\037The number of hits of this type'))

_COMMUNITYLINKFILTER = _descriptor.ServiceDescriptor(
  name='CommunityLinkFilter',
  full_name='CommunityLinkFilter',
  file=DESCRIPTOR,
  index=0,
  options=_descriptor._ParseOptions(descriptor_pb2.ServiceOptions(), _b('\202\265\030JA service for recording data about Steam Community phishing link filtering')),
  serialized_start=1189,
  serialized_end=1899,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLinkFilterHashPrefixes',
    full_name='CommunityLinkFilter.GetLinkFilterHashPrefixes',
    index=0,
    containing_service=None,
    input_type=_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_REQUEST,
    output_type=_CCOMMUNITY_GETLINKFILTERHASHPREFIXES_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030RGet a list of hash prefixes for the specified hit type, to use for client caching.')),
  ),
  _descriptor.MethodDescriptor(
    name='GetLinkFilterHashes',
    full_name='CommunityLinkFilter.GetLinkFilterHashes',
    index=1,
    containing_service=None,
    input_type=_CCOMMUNITY_GETLINKFILTERHASHES_REQUEST,
    output_type=_CCOMMUNITY_GETLINKFILTERHASHES_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030KGet a list of hashes for the specified hit type, to use for client caching.')),
  ),
  _descriptor.MethodDescriptor(
    name='GetLinkFilterListVersion',
    full_name='CommunityLinkFilter.GetLinkFilterListVersion',
    index=2,
    containing_service=None,
    input_type=_CCOMMUNITY_GETLINKFILTERLISTVERSION_REQUEST,
    output_type=_CCOMMUNITY_GETLINKFILTERLISTVERSION_RESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\265\030PGet a list of hashes describing the version of each chunk of the requested size.')),
  ),
])

CommunityLinkFilter = service_reflection.GeneratedServiceType('CommunityLinkFilter', (_service.Service,), dict(
  DESCRIPTOR = _COMMUNITYLINKFILTER,
  __module__ = 'steammessages_linkfilter_pb2'
  ))

CommunityLinkFilter_Stub = service_reflection.GeneratedServiceStubType('CommunityLinkFilter_Stub', (CommunityLinkFilter,), dict(
  DESCRIPTOR = _COMMUNITYLINKFILTER,
  __module__ = 'steammessages_linkfilter_pb2'
  ))


# @@protoc_insertion_point(module_scope)
