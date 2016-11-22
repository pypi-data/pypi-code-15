
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import router_bgp
import isis
import ospf
import hide_pim_holder
class router(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The routing system.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__router_bgp','__isis','__ospf','__hide_pim_holder',)

  _yang_name = 'router'
  _rest_name = 'router'

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
    self.__ospf = YANGDynClass(base=YANGListType("vrf",ospf.ospf, yang_name="ospf", rest_name="ospf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf', extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}), is_container='list', yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)
    self.__router_bgp = YANGDynClass(base=router_bgp.router_bgp, is_container='container', yang_name="router-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Border Gateway Protocol (BGP)', u'alt-name': u'bgp', u'sort-priority': u'74', u'callpoint': u'BgpBasic', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-router'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__isis = YANGDynClass(base=isis.isis, is_container='container', yang_name="isis", rest_name="isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS Protocol (ISIS)', u'callpoint': u'IsisBasic', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'config-isis-router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__hide_pim_holder = YANGDynClass(base=hide_pim_holder.hide_pim_holder, is_container='container', yang_name="hide-pim-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router']

  def _get_router_bgp(self):
    """
    Getter method for router_bgp, mapped from YANG variable /routing_system/router/router_bgp (container)
    """
    return self.__router_bgp
      
  def _set_router_bgp(self, v, load=False):
    """
    Setter method for router_bgp, mapped from YANG variable /routing_system/router/router_bgp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_bgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_bgp() directly.
    """
    try:
      t = YANGDynClass(v,base=router_bgp.router_bgp, is_container='container', yang_name="router-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Border Gateway Protocol (BGP)', u'alt-name': u'bgp', u'sort-priority': u'74', u'callpoint': u'BgpBasic', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-router'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_bgp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=router_bgp.router_bgp, is_container='container', yang_name="router-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Border Gateway Protocol (BGP)', u'alt-name': u'bgp', u'sort-priority': u'74', u'callpoint': u'BgpBasic', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-router'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__router_bgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_bgp(self):
    self.__router_bgp = YANGDynClass(base=router_bgp.router_bgp, is_container='container', yang_name="router-bgp", rest_name="bgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Border Gateway Protocol (BGP)', u'alt-name': u'bgp', u'sort-priority': u'74', u'callpoint': u'BgpBasic', u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-bgp-router'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_isis(self):
    """
    Getter method for isis, mapped from YANG variable /routing_system/router/isis (container)
    """
    return self.__isis
      
  def _set_isis(self, v, load=False):
    """
    Setter method for isis, mapped from YANG variable /routing_system/router/isis (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis() directly.
    """
    try:
      t = YANGDynClass(v,base=isis.isis, is_container='container', yang_name="isis", rest_name="isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS Protocol (ISIS)', u'callpoint': u'IsisBasic', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'config-isis-router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=isis.isis, is_container='container', yang_name="isis", rest_name="isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS Protocol (ISIS)', u'callpoint': u'IsisBasic', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'config-isis-router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__isis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis(self):
    self.__isis = YANGDynClass(base=isis.isis, is_container='container', yang_name="isis", rest_name="isis", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS Protocol (ISIS)', u'callpoint': u'IsisBasic', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'config-isis-router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_ospf(self):
    """
    Getter method for ospf, mapped from YANG variable /routing_system/router/ospf (list)
    """
    return self.__ospf
      
  def _set_ospf(self, v, load=False):
    """
    Setter method for ospf, mapped from YANG variable /routing_system/router/ospf (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("vrf",ospf.ospf, yang_name="ospf", rest_name="ospf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf', extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}), is_container='list', yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vrf",ospf.ospf, yang_name="ospf", rest_name="ospf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf', extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}), is_container='list', yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)""",
        })

    self.__ospf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf(self):
    self.__ospf = YANGDynClass(base=YANGListType("vrf",ospf.ospf, yang_name="ospf", rest_name="ospf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf', extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}), is_container='list', yang_name="ospf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF)', u'cli-run-template-enter': u' router ospf$($(vrf)==default-vrf?: vrf $(vrf))\n', u'sort-priority': u'76', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'OSPFConfigCallPoint', u'cli-mode-name': u'config-router-ospf-vrf-$(vrf)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='list', is_config=True)


  def _get_hide_pim_holder(self):
    """
    Getter method for hide_pim_holder, mapped from YANG variable /routing_system/router/hide_pim_holder (container)
    """
    return self.__hide_pim_holder
      
  def _set_hide_pim_holder(self, v, load=False):
    """
    Setter method for hide_pim_holder, mapped from YANG variable /routing_system/router/hide_pim_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hide_pim_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hide_pim_holder() directly.
    """
    try:
      t = YANGDynClass(v,base=hide_pim_holder.hide_pim_holder, is_container='container', yang_name="hide-pim-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hide_pim_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hide_pim_holder.hide_pim_holder, is_container='container', yang_name="hide-pim-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)""",
        })

    self.__hide_pim_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hide_pim_holder(self):
    self.__hide_pim_holder = YANGDynClass(base=hide_pim_holder.hide_pim_holder, is_container='container', yang_name="hide-pim-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)

  router_bgp = __builtin__.property(_get_router_bgp, _set_router_bgp)
  isis = __builtin__.property(_get_isis, _set_isis)
  ospf = __builtin__.property(_get_ospf, _set_ospf)
  hide_pim_holder = __builtin__.property(_get_hide_pim_holder, _set_hide_pim_holder)


  _pyangbind_elements = {'router_bgp': router_bgp, 'isis': isis, 'ospf': ospf, 'hide_pim_holder': hide_pim_holder, }


