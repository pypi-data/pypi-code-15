
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vnetwork_hosts(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vswitch - based on the path /brocade_vswitch_rpc/get-vnetwork-hosts/output/vnetwork-hosts. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__vmnic','__datacenter','__mac','__vswitch','__interface_type','__interface_name',)

  _yang_name = 'vnetwork-hosts'
  _rest_name = 'vnetwork-hosts'

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
    self.__datacenter = YANGDynClass(base=unicode, is_leaf=True, yang_name="datacenter", rest_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__vmnic = YANGDynClass(base=unicode, is_leaf=True, yang_name="vmnic", rest_name="vmnic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)
    self.__mac = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)
    self.__vswitch = YANGDynClass(base=unicode, is_leaf=True, yang_name="vswitch", rest_name="vswitch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='union', is_config=True)

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
      return [u'brocade_vswitch_rpc', u'get-vnetwork-hosts', u'output', u'vnetwork-hosts']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-vnetwork-hosts', u'output', u'vnetwork-hosts']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/name (string)

    YANG Description: host name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: host name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_vmnic(self):
    """
    Getter method for vmnic, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/vmnic (string)

    YANG Description: host NIC
    """
    return self.__vmnic
      
  def _set_vmnic(self, v, load=False):
    """
    Setter method for vmnic, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/vmnic (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vmnic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vmnic() directly.

    YANG Description: host NIC
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vmnic", rest_name="vmnic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vmnic must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vmnic", rest_name="vmnic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__vmnic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vmnic(self):
    self.__vmnic = YANGDynClass(base=unicode, is_leaf=True, yang_name="vmnic", rest_name="vmnic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_datacenter(self):
    """
    Getter method for datacenter, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/datacenter (string)

    YANG Description: host datacenter
    """
    return self.__datacenter
      
  def _set_datacenter(self, v, load=False):
    """
    Setter method for datacenter, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/datacenter (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_datacenter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_datacenter() directly.

    YANG Description: host datacenter
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="datacenter", rest_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """datacenter must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="datacenter", rest_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__datacenter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_datacenter(self):
    self.__datacenter = YANGDynClass(base=unicode, is_leaf=True, yang_name="datacenter", rest_name="datacenter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/mac (yang:mac-address)

    YANG Description: vmnic Mac address in HH:HH:HH:HH:HH:HH format
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/mac (yang:mac-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.

    YANG Description: vmnic Mac address in HH:HH:HH:HH:HH:HH format
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with yang:mac-address""",
          'defined-type': "yang:mac-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'}), is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='yang:mac-address', is_config=True)


  def _get_vswitch(self):
    """
    Getter method for vswitch, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/vswitch (string)

    YANG Description: regular or distributed virtual switch
    """
    return self.__vswitch
      
  def _set_vswitch(self, v, load=False):
    """
    Setter method for vswitch, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/vswitch (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vswitch is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vswitch() directly.

    YANG Description: regular or distributed virtual switch
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vswitch", rest_name="vswitch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vswitch must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vswitch", rest_name="vswitch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__vswitch = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vswitch(self):
    self.__vswitch = YANGDynClass(base=unicode, is_leaf=True, yang_name="vswitch", rest_name="vswitch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_interface_type(self):
    """
    Getter method for interface_type, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/interface_type (enumeration)

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    return self.__interface_type
      
  def _set_interface_type(self, v, load=False):
    """
    Setter method for interface_type, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_type() directly.

    YANG Description: The type of the interface. An 'unknown' type 
represents error scenario and should not be used.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-vswitch:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)""",
        })

    self.__interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_type(self):
    self.__interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 5}, u'loopback': {'value': 7}, u'fortygigabitethernet': {'value': 4}, u'unknown': {'value': 1}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 3}, u'tunnel': {'value': 10}, u'hundredgigabitethernet': {'value': 9}, u'fibrechannel': {'value': 8}, u'l2vlan': {'value': 6}},), is_leaf=True, yang_name="interface-type", rest_name="interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u"The type of the interface. An 'unknown' type \nrepresents error scenario and should not be used."}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='enumeration', is_config=True)


  def _get_interface_name(self):
    """
    Getter method for interface_name, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/interface_name (union)

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
gigabitethernet        [rbridge-id]/slot/port
tengigabitethernet     [rbridge-id]/slot/port
fortygigabitethernet   [rbridge-id]/slot/port
hundredgigabitethernet [rbridge-id]/slot/port
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
    Setter method for interface_name, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts/interface_name (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_name() directly.

    YANG Description: The Interface value. The interface value is always 
interpreted within the context of the value of 
'interface-type' leaf:

interface-type         interface-name
-----------------      --------------------
gigabitethernet        [rbridge-id]/slot/port
tengigabitethernet     [rbridge-id]/slot/port
fortygigabitethernet   [rbridge-id]/slot/port
hundredgigabitethernet [rbridge-id]/slot/port
port-channel           Port channel ID
l2vlan                 Vlan ID
unknown                Zero-length string.

The value of an 'interface-name' must always be 
consistent with the value of the associated 
'interface-type'.  Attempts to set an interface-name
to a value inconsistent with the associated 
'interface-type' must fail with an error.
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_name must be of a type compatible with union""",
          'defined-type': "brocade-vswitch:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='union', is_config=True)""",
        })

    self.__interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_name(self):
    self.__interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..6144']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),], is_leaf=True, yang_name="interface-name", rest_name="interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The Interface value.'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='union', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  vmnic = __builtin__.property(_get_vmnic, _set_vmnic)
  datacenter = __builtin__.property(_get_datacenter, _set_datacenter)
  mac = __builtin__.property(_get_mac, _set_mac)
  vswitch = __builtin__.property(_get_vswitch, _set_vswitch)
  interface_type = __builtin__.property(_get_interface_type, _set_interface_type)
  interface_name = __builtin__.property(_get_interface_name, _set_interface_name)


  _pyangbind_elements = {'name': name, 'vmnic': vmnic, 'datacenter': datacenter, 'mac': mac, 'vswitch': vswitch, 'interface_type': interface_type, 'interface_name': interface_name, }


