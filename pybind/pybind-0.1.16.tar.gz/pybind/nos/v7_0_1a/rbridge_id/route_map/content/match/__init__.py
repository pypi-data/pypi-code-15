
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface
import ipv6
import ip
import extcommunity
import metric
import route_type
import tag
import as_path
import community
import next_hop
import protocol
class match(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/route-map/content/match. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Matches conditions.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrf','__interface','__ipv6','__ip','__extcommunity','__metric','__route_type','__tag','__as_path','__community','__next_hop','__protocol',)

  _yang_name = 'match'
  _rest_name = 'match'

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
    self.__extcommunity = YANGDynClass(base=extcommunity.extcommunity, is_container='container', yang_name="extcommunity", rest_name="extcommunity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match BGP/VPN extended community list', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__next_hop = YANGDynClass(base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address filter', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__protocol = YANGDynClass(base=protocol.protocol, is_container='container', yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match route on protocol type and sub-type.', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__route_type = YANGDynClass(base=route_type.route_type, is_container='container', yang_name="route-type", rest_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route type.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IP).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__metric = YANGDynClass(base=metric.metric, is_container='container', yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route metric', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__as_path = YANGDynClass(base=as_path.as_path, is_container='container', yang_name="as-path", rest_name="as-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP AS Path Access Lists.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__community = YANGDynClass(base=community.community, is_container='container', yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Community Access List Name.', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__tag = YANGDynClass(base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route tag.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='common-def:vrf-name', is_config=True)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IPv6).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name, maximum 3 interfaces supported', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'route-map', u'content', u'match']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'route-map', u'match']

  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /rbridge_id/route_map/content/match/vrf (common-def:vrf-name)

    YANG Description: VRF name
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /rbridge_id/route_map/content/match/vrf (common-def:vrf-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.

    YANG Description: VRF name
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='common-def:vrf-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with common-def:vrf-name""",
          'defined-type': "common-def:vrf-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='common-def:vrf-name', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='common-def:vrf-name', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /rbridge_id/route_map/content/match/interface (container)

    YANG Description: Interface name, maxinum 3 values in '[]'
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /rbridge_id/route_map/content/match/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Interface name, maxinum 3 values in '[]'
    """
    try:
      t = YANGDynClass(v,base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name, maximum 3 interfaces supported', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name, maximum 3 interfaces supported', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface name, maximum 3 interfaces supported', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /rbridge_id/route_map/content/match/ipv6 (container)

    YANG Description: Internet Protocol (IPv6).
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /rbridge_id/route_map/content/match/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.

    YANG Description: Internet Protocol (IPv6).
    """
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IPv6).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IPv6).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IPv6).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /rbridge_id/route_map/content/match/ip (container)

    YANG Description: Internet Protocol (IP).
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /rbridge_id/route_map/content/match/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: Internet Protocol (IP).
    """
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IP).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IP).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Protocol (IP).', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_extcommunity(self):
    """
    Getter method for extcommunity, mapped from YANG variable /rbridge_id/route_map/content/match/extcommunity (container)

    YANG Description: Match BGP/VPN extended community list
    """
    return self.__extcommunity
      
  def _set_extcommunity(self, v, load=False):
    """
    Setter method for extcommunity, mapped from YANG variable /rbridge_id/route_map/content/match/extcommunity (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extcommunity is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extcommunity() directly.

    YANG Description: Match BGP/VPN extended community list
    """
    try:
      t = YANGDynClass(v,base=extcommunity.extcommunity, is_container='container', yang_name="extcommunity", rest_name="extcommunity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match BGP/VPN extended community list', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extcommunity must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=extcommunity.extcommunity, is_container='container', yang_name="extcommunity", rest_name="extcommunity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match BGP/VPN extended community list', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__extcommunity = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extcommunity(self):
    self.__extcommunity = YANGDynClass(base=extcommunity.extcommunity, is_container='container', yang_name="extcommunity", rest_name="extcommunity", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match BGP/VPN extended community list', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_metric(self):
    """
    Getter method for metric, mapped from YANG variable /rbridge_id/route_map/content/match/metric (container)

    YANG Description: metric values in the range 0 - 4294967295
    """
    return self.__metric
      
  def _set_metric(self, v, load=False):
    """
    Setter method for metric, mapped from YANG variable /rbridge_id/route_map/content/match/metric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_metric() directly.

    YANG Description: metric values in the range 0 - 4294967295
    """
    try:
      t = YANGDynClass(v,base=metric.metric, is_container='container', yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route metric', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """metric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=metric.metric, is_container='container', yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route metric', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_metric(self):
    self.__metric = YANGDynClass(base=metric.metric, is_container='container', yang_name="metric", rest_name="metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route metric', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_route_type(self):
    """
    Getter method for route_type, mapped from YANG variable /rbridge_id/route_map/content/match/route_type (container)

    YANG Description: Route type.
    """
    return self.__route_type
      
  def _set_route_type(self, v, load=False):
    """
    Setter method for route_type, mapped from YANG variable /rbridge_id/route_map/content/match/route_type (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_type() directly.

    YANG Description: Route type.
    """
    try:
      t = YANGDynClass(v,base=route_type.route_type, is_container='container', yang_name="route-type", rest_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route type.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_type must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_type.route_type, is_container='container', yang_name="route-type", rest_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route type.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__route_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_type(self):
    self.__route_type = YANGDynClass(base=route_type.route_type, is_container='container', yang_name="route-type", rest_name="route-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route type.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_tag(self):
    """
    Getter method for tag, mapped from YANG variable /rbridge_id/route_map/content/match/tag (container)

    YANG Description: Route tag.
    """
    return self.__tag
      
  def _set_tag(self, v, load=False):
    """
    Setter method for tag, mapped from YANG variable /rbridge_id/route_map/content/match/tag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tag() directly.

    YANG Description: Route tag.
    """
    try:
      t = YANGDynClass(v,base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route tag.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route tag.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tag(self):
    self.__tag = YANGDynClass(base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route tag.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_as_path(self):
    """
    Getter method for as_path, mapped from YANG variable /rbridge_id/route_map/content/match/as_path (container)

    YANG Description: IP AS Path Access Lists.
    """
    return self.__as_path
      
  def _set_as_path(self, v, load=False):
    """
    Setter method for as_path, mapped from YANG variable /rbridge_id/route_map/content/match/as_path (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_path is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_path() directly.

    YANG Description: IP AS Path Access Lists.
    """
    try:
      t = YANGDynClass(v,base=as_path.as_path, is_container='container', yang_name="as-path", rest_name="as-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP AS Path Access Lists.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_path must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=as_path.as_path, is_container='container', yang_name="as-path", rest_name="as-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP AS Path Access Lists.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__as_path = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_path(self):
    self.__as_path = YANGDynClass(base=as_path.as_path, is_container='container', yang_name="as-path", rest_name="as-path", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP AS Path Access Lists.', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_community(self):
    """
    Getter method for community, mapped from YANG variable /rbridge_id/route_map/content/match/community (container)

    YANG Description: Community Access List Name.
    """
    return self.__community
      
  def _set_community(self, v, load=False):
    """
    Setter method for community, mapped from YANG variable /rbridge_id/route_map/content/match/community (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_community() directly.

    YANG Description: Community Access List Name.
    """
    try:
      t = YANGDynClass(v,base=community.community, is_container='container', yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Community Access List Name.', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """community must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=community.community, is_container='container', yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Community Access List Name.', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_community(self):
    self.__community = YANGDynClass(base=community.community, is_container='container', yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Community Access List Name.', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-full-no': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_next_hop(self):
    """
    Getter method for next_hop, mapped from YANG variable /rbridge_id/route_map/content/match/next_hop (container)

    YANG Description: Next hop address filter
    """
    return self.__next_hop
      
  def _set_next_hop(self, v, load=False):
    """
    Setter method for next_hop, mapped from YANG variable /rbridge_id/route_map/content/match/next_hop (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop() directly.

    YANG Description: Next hop address filter
    """
    try:
      t = YANGDynClass(v,base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address filter', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address filter', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__next_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop(self):
    self.__next_hop = YANGDynClass(base=next_hop.next_hop, is_container='container', yang_name="next-hop", rest_name="next-hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop address filter', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /rbridge_id/route_map/content/match/protocol (container)

    YANG Description: Match route on protocol type and sub-type.
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /rbridge_id/route_map/content/match/protocol (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.

    YANG Description: Match route on protocol type and sub-type.
    """
    try:
      t = YANGDynClass(v,base=protocol.protocol, is_container='container', yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match route on protocol type and sub-type.', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=protocol.protocol, is_container='container', yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match route on protocol type and sub-type.', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=protocol.protocol, is_container='container', yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Match route on protocol type and sub-type.', u'cli-compact-syntax': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)

  vrf = __builtin__.property(_get_vrf, _set_vrf)
  interface = __builtin__.property(_get_interface, _set_interface)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)
  ip = __builtin__.property(_get_ip, _set_ip)
  extcommunity = __builtin__.property(_get_extcommunity, _set_extcommunity)
  metric = __builtin__.property(_get_metric, _set_metric)
  route_type = __builtin__.property(_get_route_type, _set_route_type)
  tag = __builtin__.property(_get_tag, _set_tag)
  as_path = __builtin__.property(_get_as_path, _set_as_path)
  community = __builtin__.property(_get_community, _set_community)
  next_hop = __builtin__.property(_get_next_hop, _set_next_hop)
  protocol = __builtin__.property(_get_protocol, _set_protocol)


  _pyangbind_elements = {'vrf': vrf, 'interface': interface, 'ipv6': ipv6, 'ip': ip, 'extcommunity': extcommunity, 'metric': metric, 'route_type': route_type, 'tag': tag, 'as_path': as_path, 'community': community, 'next_hop': next_hop, 'protocol': protocol, }


