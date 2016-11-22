
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class direction_in(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/default-vrf/neighbor/af-ipv4-neighbor-peergroup-holder/af-ipv4-neighbor-peergroup/filter-list/direction-in. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__filter_list_direction_in_acl_name','__filter_list_name_direction_in',)

  _yang_name = 'direction-in'
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
    self.__filter_list_direction_in_acl_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="filter-list-direction-in-acl-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ip-filter-name', is_config=True)
    self.__filter_list_name_direction_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="filter-list-name-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf', u'neighbor', u'af-ipv4-neighbor-peergroup-holder', u'af-ipv4-neighbor-peergroup', u'filter-list', u'direction-in']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'neighbor', u'filter-list']

  def _get_filter_list_direction_in_acl_name(self):
    """
    Getter method for filter_list_direction_in_acl_name, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/filter_list/direction_in/filter_list_direction_in_acl_name (ip-filter-name)
    """
    return self.__filter_list_direction_in_acl_name
      
  def _set_filter_list_direction_in_acl_name(self, v, load=False):
    """
    Setter method for filter_list_direction_in_acl_name, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/filter_list/direction_in/filter_list_direction_in_acl_name (ip-filter-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_list_direction_in_acl_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_list_direction_in_acl_name() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="filter-list-direction-in-acl-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ip-filter-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_list_direction_in_acl_name must be of a type compatible with ip-filter-name""",
          'defined-type': "brocade-bgp:ip-filter-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="filter-list-direction-in-acl-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ip-filter-name', is_config=True)""",
        })

    self.__filter_list_direction_in_acl_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_list_direction_in_acl_name(self):
    self.__filter_list_direction_in_acl_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="filter-list-direction-in-acl-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ip-filter-name', is_config=True)


  def _get_filter_list_name_direction_in(self):
    """
    Getter method for filter_list_name_direction_in, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/filter_list/direction_in/filter_list_name_direction_in (empty)
    """
    return self.__filter_list_name_direction_in
      
  def _set_filter_list_name_direction_in(self, v, load=False):
    """
    Setter method for filter_list_name_direction_in, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/filter_list/direction_in/filter_list_name_direction_in (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_filter_list_name_direction_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_filter_list_name_direction_in() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="filter-list-name-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """filter_list_name_direction_in must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="filter-list-name-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__filter_list_name_direction_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_filter_list_name_direction_in(self):
    self.__filter_list_name_direction_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="filter-list-name-direction-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter incoming routes', u'alt-name': u'in'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  filter_list_direction_in_acl_name = __builtin__.property(_get_filter_list_direction_in_acl_name, _set_filter_list_direction_in_acl_name)
  filter_list_name_direction_in = __builtin__.property(_get_filter_list_name_direction_in, _set_filter_list_name_direction_in)


  _pyangbind_elements = {'filter_list_direction_in_acl_name': filter_list_direction_in_acl_name, 'filter_list_name_direction_in': filter_list_name_direction_in, }


