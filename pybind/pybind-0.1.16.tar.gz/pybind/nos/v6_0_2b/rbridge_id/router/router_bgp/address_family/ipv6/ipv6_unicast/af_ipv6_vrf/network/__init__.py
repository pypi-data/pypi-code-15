
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class network(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/network. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__network_ipv6_address','__network_weight','__backdoor','__network_route_map',)

  _yang_name = 'network'
  _rest_name = 'network'

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
    self.__backdoor = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="backdoor", rest_name="backdoor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a BGP backdoor route', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__network_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="network-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to modify the attributes', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    self.__network_weight = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="network-weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set BGP weight for network', u'cli-full-command': None, u'alt-name': u'weight'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='absolute-decimal-number', is_config=True)
    self.__network_ipv6_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-ipv6-address", rest_name="network-ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/M IPV6 address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'network']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'network']

  def _get_network_ipv6_address(self):
    """
    Getter method for network_ipv6_address, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/network_ipv6_address (inet:ipv6-prefix)
    """
    return self.__network_ipv6_address
      
  def _set_network_ipv6_address(self, v, load=False):
    """
    Setter method for network_ipv6_address, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/network_ipv6_address (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_ipv6_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_ipv6_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-ipv6-address", rest_name="network-ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/M IPV6 address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_ipv6_address must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-ipv6-address", rest_name="network-ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/M IPV6 address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__network_ipv6_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_ipv6_address(self):
    self.__network_ipv6_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="network-ipv6-address", rest_name="network-ipv6-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/M IPV6 address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)


  def _get_network_weight(self):
    """
    Getter method for network_weight, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/network_weight (absolute-decimal-number)
    """
    return self.__network_weight
      
  def _set_network_weight(self, v, load=False):
    """
    Setter method for network_weight, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/network_weight (absolute-decimal-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_weight() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="network-weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set BGP weight for network', u'cli-full-command': None, u'alt-name': u'weight'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='absolute-decimal-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_weight must be of a type compatible with absolute-decimal-number""",
          'defined-type': "brocade-bgp:absolute-decimal-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="network-weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set BGP weight for network', u'cli-full-command': None, u'alt-name': u'weight'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='absolute-decimal-number', is_config=True)""",
        })

    self.__network_weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_weight(self):
    self.__network_weight = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="network-weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set BGP weight for network', u'cli-full-command': None, u'alt-name': u'weight'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='absolute-decimal-number', is_config=True)


  def _get_backdoor(self):
    """
    Getter method for backdoor, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/backdoor (empty)
    """
    return self.__backdoor
      
  def _set_backdoor(self, v, load=False):
    """
    Setter method for backdoor, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/backdoor (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_backdoor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_backdoor() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="backdoor", rest_name="backdoor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a BGP backdoor route', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """backdoor must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="backdoor", rest_name="backdoor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a BGP backdoor route', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__backdoor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_backdoor(self):
    self.__backdoor = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="backdoor", rest_name="backdoor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a BGP backdoor route', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_network_route_map(self):
    """
    Getter method for network_route_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/network_route_map (rmap-type)
    """
    return self.__network_route_map
      
  def _set_network_route_map(self, v, load=False):
    """
    Setter method for network_route_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/network/network_route_map (rmap-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_network_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_network_route_map() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="network-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to modify the attributes', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """network_route_map must be of a type compatible with rmap-type""",
          'defined-type': "brocade-bgp:rmap-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="network-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to modify the attributes', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)""",
        })

    self.__network_route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_network_route_map(self):
    self.__network_route_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="network-route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-map to modify the attributes', u'cli-full-command': None, u'alt-name': u'route-map'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='rmap-type', is_config=True)

  network_ipv6_address = __builtin__.property(_get_network_ipv6_address, _set_network_ipv6_address)
  network_weight = __builtin__.property(_get_network_weight, _set_network_weight)
  backdoor = __builtin__.property(_get_backdoor, _set_backdoor)
  network_route_map = __builtin__.property(_get_network_route_map, _set_network_route_map)


  _pyangbind_elements = {'network_ipv6_address': network_ipv6_address, 'network_weight': network_weight, 'backdoor': backdoor, 'network_route_map': network_route_map, }


