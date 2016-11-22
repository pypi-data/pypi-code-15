
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import port_secutiry_mac_address
class sticky(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/switchport/port-security/sticky. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Sticky MAC
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sticky_flag','__port_secutiry_mac_address',)

  _yang_name = 'sticky'
  _rest_name = 'sticky'

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
    self.__sticky_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sticky-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky Flag', u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__port_secutiry_mac_address = YANGDynClass(base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)

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
      return [u'interface', u'ethernet', u'switchport', u'port-security', u'sticky']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'switchport', u'port-security', u'sticky']

  def _get_sticky_flag(self):
    """
    Getter method for sticky_flag, mapped from YANG variable /interface/ethernet/switchport/port_security/sticky/sticky_flag (empty)

    YANG Description: Sticky Flag
    """
    return self.__sticky_flag
      
  def _set_sticky_flag(self, v, load=False):
    """
    Setter method for sticky_flag, mapped from YANG variable /interface/ethernet/switchport/port_security/sticky/sticky_flag (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sticky_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sticky_flag() directly.

    YANG Description: Sticky Flag
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="sticky-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky Flag', u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sticky_flag must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sticky-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky Flag', u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__sticky_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sticky_flag(self):
    self.__sticky_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sticky-flag", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sticky Flag', u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_port_secutiry_mac_address(self):
    """
    Getter method for port_secutiry_mac_address, mapped from YANG variable /interface/ethernet/switchport/port_security/sticky/port_secutiry_mac_address (list)

    YANG Description: Mac Address commands
    """
    return self.__port_secutiry_mac_address
      
  def _set_port_secutiry_mac_address(self, v, load=False):
    """
    Setter method for port_secutiry_mac_address, mapped from YANG variable /interface/ethernet/switchport/port_security/sticky/port_secutiry_mac_address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_secutiry_mac_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_secutiry_mac_address() directly.

    YANG Description: Mac Address commands
    """
    try:
      t = YANGDynClass(v,base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_secutiry_mac_address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__port_secutiry_mac_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_secutiry_mac_address(self):
    self.__port_secutiry_mac_address = YANGDynClass(base=YANGListType("mac_address port_sec_vlan",port_secutiry_mac_address.port_secutiry_mac_address, yang_name="port-secutiry-mac-address", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-address port-sec-vlan', extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}), is_container='list', yang_name="port-secutiry-mac-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Mac Address commands', u'cli-drop-node-name': None, u'cli-suppress-mode': None, u'callpoint': u'interface_portsecurity_sticky_mac', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)

  sticky_flag = __builtin__.property(_get_sticky_flag, _set_sticky_flag)
  port_secutiry_mac_address = __builtin__.property(_get_port_secutiry_mac_address, _set_port_secutiry_mac_address)


  _pyangbind_elements = {'sticky_flag': sticky_flag, 'port_secutiry_mac_address': port_secutiry_mac_address, }


