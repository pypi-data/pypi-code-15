
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class threshold_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/default-vrf/neighbor/af-ipv4-neighbor-peergroup-holder/af-ipv4-neighbor-peergroup/maximum-prefix/threshold-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__threshold','__teardown',)

  _yang_name = 'threshold-holder'
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
    self.__threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-threshold', is_config=True)
    self.__teardown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="teardown", rest_name="teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Terminate the peering when limit is exceeded'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf', u'neighbor', u'af-ipv4-neighbor-peergroup-holder', u'af-ipv4-neighbor-peergroup', u'maximum-prefix', u'threshold-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'neighbor', u'maximum-prefix']

  def _get_threshold(self):
    """
    Getter method for threshold, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/maximum_prefix/threshold_holder/threshold (max-prefix-threshold)
    """
    return self.__threshold
      
  def _set_threshold(self, v, load=False):
    """
    Setter method for threshold, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/maximum_prefix/threshold_holder/threshold (max-prefix-threshold)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-threshold', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """threshold must be of a type compatible with max-prefix-threshold""",
          'defined-type': "brocade-bgp:max-prefix-threshold",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-threshold', is_config=True)""",
        })

    self.__threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_threshold(self):
    self.__threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100']}), is_leaf=True, yang_name="threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-threshold', is_config=True)


  def _get_teardown(self):
    """
    Getter method for teardown, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/maximum_prefix/threshold_holder/teardown (empty)
    """
    return self.__teardown
      
  def _set_teardown(self, v, load=False):
    """
    Setter method for teardown, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/maximum_prefix/threshold_holder/teardown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_teardown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_teardown() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="teardown", rest_name="teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Terminate the peering when limit is exceeded'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """teardown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="teardown", rest_name="teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Terminate the peering when limit is exceeded'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__teardown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_teardown(self):
    self.__teardown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="teardown", rest_name="teardown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Terminate the peering when limit is exceeded'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  threshold = __builtin__.property(_get_threshold, _set_threshold)
  teardown = __builtin__.property(_get_teardown, _set_teardown)


  _pyangbind_elements = {'threshold': threshold, 'teardown': teardown, }


