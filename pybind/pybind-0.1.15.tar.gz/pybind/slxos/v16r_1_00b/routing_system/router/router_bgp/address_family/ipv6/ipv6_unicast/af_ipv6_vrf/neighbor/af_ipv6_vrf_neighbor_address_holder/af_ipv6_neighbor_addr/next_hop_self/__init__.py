
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class next_hop_self(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/neighbor/af-ipv6-vrf-neighbor-address-holder/af-ipv6-neighbor-addr/next-hop-self. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__next_hop_self_always','__next_hop_self_status',)

  _yang_name = 'next-hop-self'
  _rest_name = 'next-hop-self'

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
    self.__next_hop_self_always = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-self-always", rest_name="always", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-always'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow nexthopself for RR routes', u'alt-name': u'always'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__next_hop_self_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-self-status", rest_name="", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-status'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'neighbor', u'af-ipv6-vrf-neighbor-address-holder', u'af-ipv6-neighbor-addr', u'next-hop-self']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'neighbor', u'next-hop-self']

  def _get_next_hop_self_always(self):
    """
    Getter method for next_hop_self_always, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/next_hop_self/next_hop_self_always (empty)
    """
    return self.__next_hop_self_always
      
  def _set_next_hop_self_always(self, v, load=False):
    """
    Setter method for next_hop_self_always, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/next_hop_self/next_hop_self_always (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop_self_always is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop_self_always() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="next-hop-self-always", rest_name="always", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-always'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow nexthopself for RR routes', u'alt-name': u'always'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop_self_always must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-self-always", rest_name="always", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-always'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow nexthopself for RR routes', u'alt-name': u'always'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__next_hop_self_always = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop_self_always(self):
    self.__next_hop_self_always = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-self-always", rest_name="always", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-always'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow nexthopself for RR routes', u'alt-name': u'always'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_next_hop_self_status(self):
    """
    Getter method for next_hop_self_status, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/next_hop_self/next_hop_self_status (empty)
    """
    return self.__next_hop_self_status
      
  def _set_next_hop_self_status(self, v, load=False):
    """
    Setter method for next_hop_self_status, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/next_hop_self/next_hop_self_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop_self_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop_self_status() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="next-hop-self-status", rest_name="", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-status'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop_self_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-self-status", rest_name="", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-status'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__next_hop_self_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop_self_status(self):
    self.__next_hop_self_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-self-status", rest_name="", parent=self, choice=(u'ch-next-hop-self-type', u'ca-next-hop-self-status'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  next_hop_self_always = __builtin__.property(_get_next_hop_self_always, _set_next_hop_self_always)
  next_hop_self_status = __builtin__.property(_get_next_hop_self_status, _set_next_hop_self_status)

  __choices__ = {u'ch-next-hop-self-type': {u'ca-next-hop-self-always': [u'next_hop_self_always'], u'ca-next-hop-self-status': [u'next_hop_self_status']}}
  _pyangbind_elements = {'next_hop_self_always': next_hop_self_always, 'next_hop_self_status': next_hop_self_status, }


