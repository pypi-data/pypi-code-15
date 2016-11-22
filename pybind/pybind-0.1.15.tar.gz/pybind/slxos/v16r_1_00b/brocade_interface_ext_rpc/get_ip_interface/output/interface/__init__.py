
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ip_address
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface-ext - based on the path /brocade_interface_ext_rpc/get-ip-interface/output/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: A list of interface entries. Each row represents
management information applicable to a particular
interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_type','__interface_name','__if_name','__ip_address','__if_state','__line_protocol_state','__proxy_arp','__vrf',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__proxy_arp = YANGDynClass(base=unicode, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__if_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'testing': {'value': 4}, u'up': {'value': 2}},), is_leaf=True, yang_name="if-state", rest_name="if-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    self.__if_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="if-name", rest_name="if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__line_protocol_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'up': {'value': 2}},), is_leaf=True, yang_name="line-protocol-state", rest_name="line-protocol-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='union', is_config=True)
    self.__ip_address = YANGDynClass(base=YANGListType("ipv4",ip_address.ip_address, yang_name="ip-address", rest_name="ip-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4', extensions=None), is_container='list', yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)

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
      return [u'brocade_interface_ext_rpc', u'get-ip-interface', u'output', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-ip-interface', u'output', u'interface']

  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/interface_type (enumeration)

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'loopback': {'value': 7}, u'unknown': {'value': 1}, u'port-channel': {'value': 5}, u'fibrechannel': {'value': 8}, u'ethernet': {'value': 10}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/interface_name (union)

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
ethernet               slot/port
port-channel           Port channel ID
l2vlan                 Vlan ID
unknown                Zero-length string.

The value of an 'interface-name' must always be 
consistent with the value of the associated 
'interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'interface-type' must fail with an error.
    """
    return self.__interface_name
      
  def _set_interface_name(self, v, load=False):
    """
    Setter method for interface_name, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/interface_name (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
ethernet               slot/port
port-channel           Port channel ID
l2vlan                 Vlan ID
unknown                Zero-length string.

The value of an 'interface-name' must always be 
consistent with the value of the associated 
'interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'interface-type' must fail with an error.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with union""",
          'defined-type': "brocade-interface-ext:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='union', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='union', is_config=True)


  def _get_if_name(self):
    """
    Getter method for if_name, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/if_name (string)

    YANG Description: This indicates the interface display name as 
in MIB-II's ifTable. However interface-name and
interface-type values of this instance forms 
fully qualified name for this interface.
    """
    return self.__if_name
      
  def _set_if_name(self, v, load=False):
    """
    Setter method for if_name, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/if_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_if_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_if_name() directly.

    YANG Description: This indicates the interface display name as 
in MIB-II's ifTable. However interface-name and
interface-type values of this instance forms 
fully qualified name for this interface.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="if-name", rest_name="if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """if_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="if-name", rest_name="if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__if_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_if_name(self):
    self.__if_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="if-name", rest_name="if-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_ip_address(self):
    """
    Getter method for ip_address, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address (list)

    YANG Description: This indicates whether IP address is primary/secondary
and corresponding Broadcast IP
    """
    return self.__ip_address
      
  def _set_ip_address(self, v, load=False):
    """
    Setter method for ip_address, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/ip_address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_address() directly.

    YANG Description: This indicates whether IP address is primary/secondary
and corresponding Broadcast IP
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ipv4",ip_address.ip_address, yang_name="ip-address", rest_name="ip-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4', extensions=None), is_container='list', yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv4",ip_address.ip_address, yang_name="ip-address", rest_name="ip-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4', extensions=None), is_container='list', yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)""",
        })

    self.__ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_address(self):
    self.__ip_address = YANGDynClass(base=YANGListType("ipv4",ip_address.ip_address, yang_name="ip-address", rest_name="ip-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4', extensions=None), is_container='list', yang_name="ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)


  def _get_if_state(self):
    """
    Getter method for if_state, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/if_state (enumeration)

    YANG Description: This indicates the current operational state
of this interface. The 'testing' state 
indicates that no operational packets can be
passed. If 'shutdown' leaf of corresponding 
interface instance of brocade-interface module
is set, then 'if-state' should be 'down'. 
If 'shutdown' is changed deleted, then 
'if-state' should change to 'up' if the 
interface is ready to transmit and receive 
network traffic; it should remain in the 'down'
state if and only if there is a fault that 
prevents it from going to the 'up' state.
    """
    return self.__if_state
      
  def _set_if_state(self, v, load=False):
    """
    Setter method for if_state, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/if_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_if_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_if_state() directly.

    YANG Description: This indicates the current operational state
of this interface. The 'testing' state 
indicates that no operational packets can be
passed. If 'shutdown' leaf of corresponding 
interface instance of brocade-interface module
is set, then 'if-state' should be 'down'. 
If 'shutdown' is changed deleted, then 
'if-state' should change to 'up' if the 
interface is ready to transmit and receive 
network traffic; it should remain in the 'down'
state if and only if there is a fault that 
prevents it from going to the 'up' state.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'testing': {'value': 4}, u'up': {'value': 2}},), is_leaf=True, yang_name="if-state", rest_name="if-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """if_state must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'testing': {'value': 4}, u'up': {'value': 2}},), is_leaf=True, yang_name="if-state", rest_name="if-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__if_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_if_state(self):
    self.__if_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'testing': {'value': 4}, u'up': {'value': 2}},), is_leaf=True, yang_name="if-state", rest_name="if-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)


  def _get_line_protocol_state(self):
    """
    Getter method for line_protocol_state, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/line_protocol_state (enumeration)

    YANG Description: This indicates the 'Line protocol' state of
this interface.
    """
    return self.__line_protocol_state
      
  def _set_line_protocol_state(self, v, load=False):
    """
    Setter method for line_protocol_state, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/line_protocol_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_line_protocol_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_line_protocol_state() directly.

    YANG Description: This indicates the 'Line protocol' state of
this interface.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'up': {'value': 2}},), is_leaf=True, yang_name="line-protocol-state", rest_name="line-protocol-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """line_protocol_state must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'up': {'value': 2}},), is_leaf=True, yang_name="line-protocol-state", rest_name="line-protocol-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__line_protocol_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_line_protocol_state(self):
    self.__line_protocol_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'down': {'value': 3}, u'unknown': {'value': 1}, u'up': {'value': 2}},), is_leaf=True, yang_name="line-protocol-state", rest_name="line-protocol-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)


  def _get_proxy_arp(self):
    """
    Getter method for proxy_arp, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/proxy_arp (string)

    YANG Description: This indicates the 'proxy-arp' state of the
interface.
    """
    return self.__proxy_arp
      
  def _set_proxy_arp(self, v, load=False):
    """
    Setter method for proxy_arp, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/proxy_arp (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_proxy_arp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_proxy_arp() directly.

    YANG Description: This indicates the 'proxy-arp' state of the
interface.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """proxy_arp must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__proxy_arp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_proxy_arp(self):
    self.__proxy_arp = YANGDynClass(base=unicode, is_leaf=True, yang_name="proxy-arp", rest_name="proxy-arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/vrf (string)

    YANG Description: This indicates the 'vrf' of the interface.
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /brocade_interface_ext_rpc/get_ip_interface/output/interface/vrf (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.

    YANG Description: This indicates the 'vrf' of the interface.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)

  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)
  if_name = __builtin__.property(_get_if_name, _set_if_name)
  ip_address = __builtin__.property(_get_ip_address, _set_ip_address)
  if_state = __builtin__.property(_get_if_state, _set_if_state)
  line_protocol_state = __builtin__.property(_get_line_protocol_state, _set_line_protocol_state)
  proxy_arp = __builtin__.property(_get_proxy_arp, _set_proxy_arp)
  vrf = __builtin__.property(_get_vrf, _set_vrf)


  _pyangbind_elements = {'interface_type': interface_type, 'interface_name': interface_name, 'if_name': if_name, 'ip_address': ip_address, 'if_state': if_state, 'line_protocol_state': line_protocol_state, 'proxy_arp': proxy_arp, 'vrf': vrf, }


