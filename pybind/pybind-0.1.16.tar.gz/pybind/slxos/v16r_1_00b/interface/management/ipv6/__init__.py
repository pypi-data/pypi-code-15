
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import icmpv6
import ipv6_address_cont
import access_group
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/management/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IPv6 configurations for this management 
interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__icmpv6','__ipv6_address_cont','__ipv6_address','__ipv6_gateways','__access_group',)

  _yang_name = 'ipv6'
  _rest_name = 'ipv6'

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
    self.__ipv6_address_cont = YANGDynClass(base=ipv6_address_cont.ipv6_address_cont, is_container='container', yang_name="ipv6-address-cont", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv6 address configuration for this \nmanagement interface.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__icmpv6 = YANGDynClass(base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMPv6 control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__ipv6_address = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-address", rest_name="ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 addresses assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    self.__ipv6_gateways = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-gateways", rest_name="ipv6-gateways", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 gateways assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    self.__access_group = YANGDynClass(base=access_group.access_group, is_container='container', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip6_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)

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
      return [u'interface', u'management', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Management', u'ipv6']

  def _get_icmpv6(self):
    """
    Getter method for icmpv6, mapped from YANG variable /interface/management/ipv6/icmpv6 (container)

    YANG Description: The ICMPv6 control for this management interface.
    """
    return self.__icmpv6
      
  def _set_icmpv6(self, v, load=False):
    """
    Setter method for icmpv6, mapped from YANG variable /interface/management/ipv6/icmpv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmpv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmpv6() directly.

    YANG Description: The ICMPv6 control for this management interface.
    """
    try:
      t = YANGDynClass(v,base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMPv6 control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmpv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMPv6 control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__icmpv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmpv6(self):
    self.__icmpv6 = YANGDynClass(base=icmpv6.icmpv6, is_container='container', yang_name="icmpv6", rest_name="icmpv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMPv6 control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_ipv6_address_cont(self):
    """
    Getter method for ipv6_address_cont, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont (container)

    YANG Description: The IPv6 address configuration for this 
management interface.
    """
    return self.__ipv6_address_cont
      
  def _set_ipv6_address_cont(self, v, load=False):
    """
    Setter method for ipv6_address_cont, mapped from YANG variable /interface/management/ipv6/ipv6_address_cont (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_address_cont is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_address_cont() directly.

    YANG Description: The IPv6 address configuration for this 
management interface.
    """
    try:
      t = YANGDynClass(v,base=ipv6_address_cont.ipv6_address_cont, is_container='container', yang_name="ipv6-address-cont", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv6 address configuration for this \nmanagement interface.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_address_cont must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_address_cont.ipv6_address_cont, is_container='container', yang_name="ipv6-address-cont", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv6 address configuration for this \nmanagement interface.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__ipv6_address_cont = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_address_cont(self):
    self.__ipv6_address_cont = YANGDynClass(base=ipv6_address_cont.ipv6_address_cont, is_container='container', yang_name="ipv6-address-cont", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv6 address configuration for this \nmanagement interface.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_ipv6_address(self):
    """
    Getter method for ipv6_address, mapped from YANG variable /interface/management/ipv6/ipv6_address (string)

    YANG Description: The list of IPv6 addresses assigned for this 
management interface.
    """
    return self.__ipv6_address
      
  def _set_ipv6_address(self, v, load=False):
    """
    Setter method for ipv6_address, mapped from YANG variable /interface/management/ipv6/ipv6_address (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_address() directly.

    YANG Description: The list of IPv6 addresses assigned for this 
management interface.
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-address", rest_name="ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 addresses assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_address must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-address", rest_name="ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 addresses assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)""",
        })

    self.__ipv6_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_address(self):
    self.__ipv6_address = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-address", rest_name="ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 addresses assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)


  def _get_ipv6_gateways(self):
    """
    Getter method for ipv6_gateways, mapped from YANG variable /interface/management/ipv6/ipv6_gateways (string)

    YANG Description: The list of IPv6 gateways assigned for this 
management interface.
    """
    return self.__ipv6_gateways
      
  def _set_ipv6_gateways(self, v, load=False):
    """
    Setter method for ipv6_gateways, mapped from YANG variable /interface/management/ipv6/ipv6_gateways (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_gateways is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_gateways() directly.

    YANG Description: The list of IPv6 gateways assigned for this 
management interface.
    """
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-gateways", rest_name="ipv6-gateways", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 gateways assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_gateways must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-gateways", rest_name="ipv6-gateways", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 gateways assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)""",
        })

    self.__ipv6_gateways = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_gateways(self):
    self.__ipv6_gateways = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="ipv6-gateways", rest_name="ipv6-gateways", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of IPv6 gateways assigned for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)


  def _get_access_group(self):
    """
    Getter method for access_group, mapped from YANG variable /interface/management/ipv6/access_group (container)
    """
    return self.__access_group
      
  def _set_access_group(self, v, load=False):
    """
    Setter method for access_group, mapped from YANG variable /interface/management/ipv6/access_group (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_group() directly.
    """
    try:
      t = YANGDynClass(v,base=access_group.access_group, is_container='container', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip6_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_group must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_group.access_group, is_container='container', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip6_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)""",
        })

    self.__access_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_group(self):
    self.__access_group = YANGDynClass(base=access_group.access_group, is_container='container', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_ACL_CONFIG', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip6_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-access-list', defining_module='brocade-ipv6-access-list', yang_type='container', is_config=True)

  icmpv6 = __builtin__.property(_get_icmpv6, _set_icmpv6)
  ipv6_address_cont = __builtin__.property(_get_ipv6_address_cont, _set_ipv6_address_cont)
  ipv6_address = __builtin__.property(_get_ipv6_address)
  ipv6_gateways = __builtin__.property(_get_ipv6_gateways)
  access_group = __builtin__.property(_get_access_group, _set_access_group)


  _pyangbind_elements = {'icmpv6': icmpv6, 'ipv6_address_cont': ipv6_address_cont, 'ipv6_address': ipv6_address, 'ipv6_gateways': ipv6_gateways, 'access_group': access_group, }


