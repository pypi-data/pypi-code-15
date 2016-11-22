
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class link_local_static_route_nh_vrf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vrf - based on the path /vrf/address-family/ipv6/unicast/ipv6/route/link-local-static-route-nh-vrf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__static_route_next_vrf_dest','__next_hop_vrf','__link_local_next_hop','__link_local_route_oif_type','__link_local_route_oif_name',)

  _yang_name = 'link-local-static-route-nh-vrf'
  _rest_name = ''

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
    self.__static_route_next_vrf_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-next-vrf-dest", rest_name="static-route-next-vrf-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)
    self.__next_hop_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="next-hop-vrf", rest_name="next-hop-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next Hop Vrf Name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='common-def:vrf-name', is_config=True)
    self.__link_local_next_hop = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="link-local-next-hop", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Next hop IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    self.__link_local_route_oif_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="link-local-route-oif-name", rest_name="link-local-route-oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)
    self.__link_local_route_oif_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 3}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="link-local-route-oif-type", rest_name="link-local-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)

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
      return [u'vrf', u'address-family', u'ipv6', u'unicast', u'ipv6', u'route', u'link-local-static-route-nh-vrf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vrf', u'address-family', u'ipv6', u'unicast', u'ipv6', u'route']

  def _get_static_route_next_vrf_dest(self):
    """
    Getter method for static_route_next_vrf_dest, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/static_route_next_vrf_dest (inet:ipv6-prefix)
    """
    return self.__static_route_next_vrf_dest
      
  def _set_static_route_next_vrf_dest(self, v, load=False):
    """
    Setter method for static_route_next_vrf_dest, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/static_route_next_vrf_dest (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_next_vrf_dest is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_next_vrf_dest() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-next-vrf-dest", rest_name="static-route-next-vrf-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_next_vrf_dest must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-next-vrf-dest", rest_name="static-route-next-vrf-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__static_route_next_vrf_dest = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_next_vrf_dest(self):
    self.__static_route_next_vrf_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-next-vrf-dest", rest_name="static-route-next-vrf-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)


  def _get_next_hop_vrf(self):
    """
    Getter method for next_hop_vrf, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/next_hop_vrf (common-def:vrf-name)
    """
    return self.__next_hop_vrf
      
  def _set_next_hop_vrf(self, v, load=False):
    """
    Setter method for next_hop_vrf, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/next_hop_vrf (common-def:vrf-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop_vrf() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="next-hop-vrf", rest_name="next-hop-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next Hop Vrf Name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='common-def:vrf-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop_vrf must be of a type compatible with common-def:vrf-name""",
          'defined-type': "common-def:vrf-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="next-hop-vrf", rest_name="next-hop-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next Hop Vrf Name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='common-def:vrf-name', is_config=True)""",
        })

    self.__next_hop_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop_vrf(self):
    self.__next_hop_vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="next-hop-vrf", rest_name="next-hop-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next Hop Vrf Name', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='common-def:vrf-name', is_config=True)


  def _get_link_local_next_hop(self):
    """
    Getter method for link_local_next_hop, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/link_local_next_hop (inet:ipv6-address)
    """
    return self.__link_local_next_hop
      
  def _set_link_local_next_hop(self, v, load=False):
    """
    Setter method for link_local_next_hop, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/link_local_next_hop (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_local_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_local_next_hop() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="link-local-next-hop", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Next hop IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_local_next_hop must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="link-local-next-hop", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Next hop IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__link_local_next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_local_next_hop(self):
    self.__link_local_next_hop = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="link-local-next-hop", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Next hop IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)


  def _get_link_local_route_oif_type(self):
    """
    Getter method for link_local_route_oif_type, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/link_local_route_oif_type (enumeration)
    """
    return self.__link_local_route_oif_type
      
  def _set_link_local_route_oif_type(self, v, load=False):
    """
    Setter method for link_local_route_oif_type, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/link_local_route_oif_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_local_route_oif_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_local_route_oif_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 3}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="link-local-route-oif-type", rest_name="link-local-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_local_route_oif_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-ipv6-rtm:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 3}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="link-local-route-oif-type", rest_name="link-local-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)""",
        })

    self.__link_local_route_oif_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_local_route_oif_type(self):
    self.__link_local_route_oif_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'management': {'value': 3}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="link-local-route-oif-type", rest_name="link-local-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)


  def _get_link_local_route_oif_name(self):
    """
    Getter method for link_local_route_oif_name, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/link_local_route_oif_name (string)
    """
    return self.__link_local_route_oif_name
      
  def _set_link_local_route_oif_name(self, v, load=False):
    """
    Setter method for link_local_route_oif_name, mapped from YANG variable /vrf/address_family/ipv6/unicast/ipv6/route/link_local_static_route_nh_vrf/link_local_route_oif_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_local_route_oif_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_local_route_oif_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="link-local-route-oif-name", rest_name="link-local-route-oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_local_route_oif_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="link-local-route-oif-name", rest_name="link-local-route-oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)""",
        })

    self.__link_local_route_oif_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_local_route_oif_name(self):
    self.__link_local_route_oif_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="link-local-route-oif-name", rest_name="link-local-route-oif-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)

  static_route_next_vrf_dest = __builtin__.property(_get_static_route_next_vrf_dest, _set_static_route_next_vrf_dest)
  next_hop_vrf = __builtin__.property(_get_next_hop_vrf, _set_next_hop_vrf)
  link_local_next_hop = __builtin__.property(_get_link_local_next_hop, _set_link_local_next_hop)
  link_local_route_oif_type = __builtin__.property(_get_link_local_route_oif_type, _set_link_local_route_oif_type)
  link_local_route_oif_name = __builtin__.property(_get_link_local_route_oif_name, _set_link_local_route_oif_name)


  _pyangbind_elements = {'static_route_next_vrf_dest': static_route_next_vrf_dest, 'next_hop_vrf': next_hop_vrf, 'link_local_next_hop': link_local_next_hop, 'link_local_route_oif_type': link_local_route_oif_type, 'link_local_route_oif_name': link_local_route_oif_name, }


