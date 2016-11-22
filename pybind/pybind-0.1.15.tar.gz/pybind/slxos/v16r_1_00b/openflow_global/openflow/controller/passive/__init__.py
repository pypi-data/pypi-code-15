
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class passive(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow - based on the path /openflow-global/openflow/controller/passive. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: OpenFlow passive controller configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__passive_connection_method','__passive_controller_address','__passive_connection_port','__passive_controller_vrf',)

  _yang_name = 'passive'
  _rest_name = 'passive'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__passive_controller_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="passive-controller-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name of VRF (Default = mgmt-vrf)', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='common-def:vrf-name', is_config=True)
    self.__passive_controller_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv4 listening address', u'cli-full-no': None, u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)
    self.__passive_connection_method = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'no-ssl': {'value': 1}},), is_leaf=True, yang_name="passive-connection-method", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)
    self.__passive_connection_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-connection-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'listening Port', u'alt-name': u'port', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'openflow-global', u'openflow', u'controller', u'passive']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow', u'controller', u'passive']

  def _get_passive_connection_method(self):
    """
    Getter method for passive_connection_method, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_connection_method (enumeration)

    YANG Description: This parameter defines the connection method to be
used to connect to OpenFlow controller. By default no-ssl is
used
    """
    return self.__passive_connection_method
      
  def _set_passive_connection_method(self, v, load=False):
    """
    Setter method for passive_connection_method, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_connection_method (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_connection_method is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_connection_method() directly.

    YANG Description: This parameter defines the connection method to be
used to connect to OpenFlow controller. By default no-ssl is
used
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'no-ssl': {'value': 1}},), is_leaf=True, yang_name="passive-connection-method", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_connection_method must be of a type compatible with enumeration""",
          'defined-type': "brocade-openflow:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'no-ssl': {'value': 1}},), is_leaf=True, yang_name="passive-connection-method", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)""",
        })

    self.__passive_connection_method = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_connection_method(self):
    self.__passive_connection_method = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'no-ssl': {'value': 1}},), is_leaf=True, yang_name="passive-connection-method", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Connection method', u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='enumeration', is_config=True)


  def _get_passive_controller_address(self):
    """
    Getter method for passive_controller_address, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_controller_address (inet:ip-address)

    YANG Description: IP address passive of the OpenFlow controller. Only IPv4 address
is supported.
    """
    return self.__passive_controller_address
      
  def _set_passive_controller_address(self, v, load=False):
    """
    Setter method for passive_controller_address, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_controller_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_controller_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_controller_address() directly.

    YANG Description: IP address passive of the OpenFlow controller. Only IPv4 address
is supported.
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv4 listening address', u'cli-full-no': None, u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_controller_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv4 listening address', u'cli-full-no': None, u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__passive_controller_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_controller_address(self):
    self.__passive_controller_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv4 listening address', u'cli-full-no': None, u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)


  def _get_passive_connection_port(self):
    """
    Getter method for passive_connection_port, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_connection_port (uint32)

    YANG Description: TCP port number for the OpenFlow controller.
    """
    return self.__passive_connection_port
      
  def _set_passive_connection_port(self, v, load=False):
    """
    Setter method for passive_connection_port, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_connection_port (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_connection_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_connection_port() directly.

    YANG Description: TCP port number for the OpenFlow controller.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-connection-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'listening Port', u'alt-name': u'port', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_connection_port must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-connection-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'listening Port', u'alt-name': u'port', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)""",
        })

    self.__passive_connection_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_connection_port(self):
    self.__passive_connection_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-connection-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'listening Port', u'alt-name': u'port', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)


  def _get_passive_controller_vrf(self):
    """
    Getter method for passive_controller_vrf, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_controller_vrf (common-def:vrf-name)
    """
    return self.__passive_controller_vrf
      
  def _set_passive_controller_vrf(self, v, load=False):
    """
    Setter method for passive_controller_vrf, mapped from YANG variable /openflow_global/openflow/controller/passive/passive_controller_vrf (common-def:vrf-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_controller_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_controller_vrf() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="passive-controller-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name of VRF (Default = mgmt-vrf)', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='common-def:vrf-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_controller_vrf must be of a type compatible with common-def:vrf-name""",
          'defined-type': "common-def:vrf-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="passive-controller-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name of VRF (Default = mgmt-vrf)', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='common-def:vrf-name', is_config=True)""",
        })

    self.__passive_controller_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_controller_vrf(self):
    self.__passive_controller_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="passive-controller-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Name of VRF (Default = mgmt-vrf)', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='common-def:vrf-name', is_config=True)

  passive_connection_method = __builtin__.property(_get_passive_connection_method, _set_passive_connection_method)
  passive_controller_address = __builtin__.property(_get_passive_controller_address, _set_passive_controller_address)
  passive_connection_port = __builtin__.property(_get_passive_connection_port, _set_passive_connection_port)
  passive_controller_vrf = __builtin__.property(_get_passive_controller_vrf, _set_passive_controller_vrf)


  _pyangbind_elements = {'passive_connection_method': passive_connection_method, 'passive_controller_address': passive_controller_address, 'passive_connection_port': passive_connection_port, 'passive_controller_vrf': passive_controller_vrf, }


