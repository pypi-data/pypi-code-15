
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_map
import prefix_list
class distribute_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/ipv6/router/ospf/distribute-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: By configuring distribution lists we can filter the routes to be placed in the OSPFv3 route table.OSPFv3 distribution lists can filter routes using information specified in an IPv6 prefix list or a route map.Filtering using route maps has higher priority over filtering using global prefix lists.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__route_map','__prefix_list',)

  _yang_name = 'distribute-list'
  _rest_name = 'distribute-list'

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
    self.__route_map = YANGDynClass(base=route_map.route_map, is_container='container', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use route-map to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__prefix_list = YANGDynClass(base=prefix_list.prefix_list, is_container='container', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use prefix list to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

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
      return [u'routing-system', u'ipv6', u'router', u'ospf', u'distribute-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'router', u'ospf', u'distribute-list']

  def _get_route_map(self):
    """
    Getter method for route_map, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/route_map (container)

    YANG Description: Use route-map to control routes learned by OSPFv3
    """
    return self.__route_map
      
  def _set_route_map(self, v, load=False):
    """
    Setter method for route_map, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/route_map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_map() directly.

    YANG Description: Use route-map to control routes learned by OSPFv3
    """
    try:
      t = YANGDynClass(v,base=route_map.route_map, is_container='container', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use route-map to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_map must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_map.route_map, is_container='container', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use route-map to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_map(self):
    self.__route_map = YANGDynClass(base=route_map.route_map, is_container='container', yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use route-map to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_prefix_list(self):
    """
    Getter method for prefix_list, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/prefix_list (container)

    YANG Description: Use prefix list to control routes learned by OSPFv3
    """
    return self.__prefix_list
      
  def _set_prefix_list(self, v, load=False):
    """
    Setter method for prefix_list, mapped from YANG variable /routing_system/ipv6/router/ospf/distribute_list/prefix_list (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_list() directly.

    YANG Description: Use prefix list to control routes learned by OSPFv3
    """
    try:
      t = YANGDynClass(v,base=prefix_list.prefix_list, is_container='container', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use prefix list to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_list must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_list.prefix_list, is_container='container', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use prefix list to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_list(self):
    self.__prefix_list = YANGDynClass(base=prefix_list.prefix_list, is_container='container', yang_name="prefix-list", rest_name="prefix-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'Use prefix list to control routes learned by OSPFv3', u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  route_map = __builtin__.property(_get_route_map, _set_route_map)
  prefix_list = __builtin__.property(_get_prefix_list, _set_prefix_list)


  _pyangbind_elements = {'route_map': route_map, 'prefix_list': prefix_list, }


