
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/interface/vlan/ipv6/mldVlan/snooping/mrouter/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__if_type','__value',)

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
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..11']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='string-type', is_config=True)
    self.__if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {'value': 2}, u'Port-channel': {'value': 3}, u'GigabitEthernet': {'value': 0}, u'TenGigabitEthernet': {'value': 1}, u'HundredGigabitEthernet': {'value': 4}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='enumeration', is_config=True)

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
      return [u'interface-vlan', u'interface', u'vlan', u'ipv6', u'mldVlan', u'snooping', u'mrouter', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Vlan', u'ipv6', u'mld', u'snooping', u'mrouter', u'interface']

  def _get_if_type(self):
    """
    Getter method for if_type, mapped from YANG variable /interface_vlan/interface/vlan/ipv6/mldVlan/snooping/mrouter/interface/if_type (enumeration)
    """
    return self.__if_type
      
  def _set_if_type(self, v, load=False):
    """
    Setter method for if_type, mapped from YANG variable /interface_vlan/interface/vlan/ipv6/mldVlan/snooping/mrouter/interface/if_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_if_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_if_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {'value': 2}, u'Port-channel': {'value': 3}, u'GigabitEthernet': {'value': 0}, u'TenGigabitEthernet': {'value': 1}, u'HundredGigabitEthernet': {'value': 4}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """if_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-mld-snooping:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {'value': 2}, u'Port-channel': {'value': 3}, u'GigabitEthernet': {'value': 0}, u'TenGigabitEthernet': {'value': 1}, u'HundredGigabitEthernet': {'value': 4}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='enumeration', is_config=True)""",
        })

    self.__if_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_if_type(self):
    self.__if_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'FortyGigabitEthernet': {'value': 2}, u'Port-channel': {'value': 3}, u'GigabitEthernet': {'value': 0}, u'TenGigabitEthernet': {'value': 1}, u'HundredGigabitEthernet': {'value': 4}},), is_leaf=True, yang_name="if-type", rest_name="if-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='enumeration', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /interface_vlan/interface/vlan/ipv6/mldVlan/snooping/mrouter/interface/value (string-type)
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /interface_vlan/interface/vlan/ipv6/mldVlan/snooping/mrouter/interface/value (string-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..11']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='string-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with string-type""",
          'defined-type': "brocade-mld-snooping:string-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..11']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='string-type', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..11']}), is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='string-type', is_config=True)

  if_type = __builtin__.property(_get_if_type, _set_if_type)
  value = __builtin__.property(_get_value, _set_value)


  _pyangbind_elements = {'if_type': if_type, 'value': value, }


