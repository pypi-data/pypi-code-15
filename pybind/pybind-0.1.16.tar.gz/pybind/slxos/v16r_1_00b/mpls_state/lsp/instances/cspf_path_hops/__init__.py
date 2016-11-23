
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cspf_path_hops(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/lsp/instances/cspf-path-hops. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hop_index','__hop_address','__type','__hop_is_router_id','__protection','__node_protection','__bandwidth_protection','__protection_in_use',)

  _yang_name = 'cspf-path-hops'
  _rest_name = 'cspf-path-hops'

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
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='hop-type', is_config=False)
    self.__hop_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hop-index", rest_name="hop-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protection", rest_name="protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__protection_in_use = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protection-in-use", rest_name="protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__node_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="node-protection", rest_name="node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__bandwidth_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bandwidth-protection", rest_name="bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    self.__hop_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="hop-address", rest_name="hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__hop_is_router_id = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hop-is-router-id", rest_name="hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

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
      return [u'mpls-state', u'lsp', u'instances', u'cspf-path-hops']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'lsp', u'instances', u'cspf-path-hops']

  def _get_hop_index(self):
    """
    Getter method for hop_index, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/hop_index (uint32)

    YANG Description: HOP index
    """
    return self.__hop_index
      
  def _set_hop_index(self, v, load=False):
    """
    Setter method for hop_index, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/hop_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hop_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hop_index() directly.

    YANG Description: HOP index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hop-index", rest_name="hop-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hop_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hop-index", rest_name="hop-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__hop_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hop_index(self):
    self.__hop_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hop-index", rest_name="hop-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_hop_address(self):
    """
    Getter method for hop_address, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/hop_address (inet:ipv4-address)

    YANG Description: lsp_hop_address
    """
    return self.__hop_address
      
  def _set_hop_address(self, v, load=False):
    """
    Setter method for hop_address, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/hop_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hop_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hop_address() directly.

    YANG Description: lsp_hop_address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="hop-address", rest_name="hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hop_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="hop-address", rest_name="hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__hop_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hop_address(self):
    self.__hop_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="hop-address", rest_name="hop-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/type (hop-type)

    YANG Description: Hop Type
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/type (hop-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: Hop Type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='hop-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with hop-type""",
          'defined-type': "brocade-mpls-operational:hop-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='hop-type', is_config=False)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'strict': {'value': 1}, u'loose': {'value': 2}},), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='hop-type', is_config=False)


  def _get_hop_is_router_id(self):
    """
    Getter method for hop_is_router_id, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/hop_is_router_id (boolean)

    YANG Description: lsp_hop_is_router_id
    """
    return self.__hop_is_router_id
      
  def _set_hop_is_router_id(self, v, load=False):
    """
    Setter method for hop_is_router_id, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/hop_is_router_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hop_is_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hop_is_router_id() directly.

    YANG Description: lsp_hop_is_router_id
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="hop-is-router-id", rest_name="hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hop_is_router_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hop-is-router-id", rest_name="hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__hop_is_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hop_is_router_id(self):
    self.__hop_is_router_id = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hop-is-router-id", rest_name="hop-is-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_protection(self):
    """
    Getter method for protection, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/protection (boolean)

    YANG Description: lsp_hop_has_protection
    """
    return self.__protection
      
  def _set_protection(self, v, load=False):
    """
    Setter method for protection, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/protection (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protection() directly.

    YANG Description: lsp_hop_has_protection
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="protection", rest_name="protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protection must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protection", rest_name="protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protection(self):
    self.__protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protection", rest_name="protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_node_protection(self):
    """
    Getter method for node_protection, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/node_protection (boolean)

    YANG Description: lsp_hop_has_node_protection
    """
    return self.__node_protection
      
  def _set_node_protection(self, v, load=False):
    """
    Setter method for node_protection, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/node_protection (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node_protection() directly.

    YANG Description: lsp_hop_has_node_protection
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="node-protection", rest_name="node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node_protection must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="node-protection", rest_name="node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__node_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node_protection(self):
    self.__node_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="node-protection", rest_name="node-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_bandwidth_protection(self):
    """
    Getter method for bandwidth_protection, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/bandwidth_protection (boolean)

    YANG Description: lsp_hop_has_bandwidth_protection
    """
    return self.__bandwidth_protection
      
  def _set_bandwidth_protection(self, v, load=False):
    """
    Setter method for bandwidth_protection, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/bandwidth_protection (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bandwidth_protection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bandwidth_protection() directly.

    YANG Description: lsp_hop_has_bandwidth_protection
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bandwidth-protection", rest_name="bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bandwidth_protection must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bandwidth-protection", rest_name="bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__bandwidth_protection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bandwidth_protection(self):
    self.__bandwidth_protection = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bandwidth-protection", rest_name="bandwidth-protection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)


  def _get_protection_in_use(self):
    """
    Getter method for protection_in_use, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/protection_in_use (boolean)

    YANG Description: lsp_hop_has_protection_in_use
    """
    return self.__protection_in_use
      
  def _set_protection_in_use(self, v, load=False):
    """
    Setter method for protection_in_use, mapped from YANG variable /mpls_state/lsp/instances/cspf_path_hops/protection_in_use (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protection_in_use is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protection_in_use() directly.

    YANG Description: lsp_hop_has_protection_in_use
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="protection-in-use", rest_name="protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protection_in_use must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protection-in-use", rest_name="protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)""",
        })

    self.__protection_in_use = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protection_in_use(self):
    self.__protection_in_use = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="protection-in-use", rest_name="protection-in-use", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='boolean', is_config=False)

  hop_index = __builtin__.property(_get_hop_index)
  hop_address = __builtin__.property(_get_hop_address)
  type = __builtin__.property(_get_type)
  hop_is_router_id = __builtin__.property(_get_hop_is_router_id)
  protection = __builtin__.property(_get_protection)
  node_protection = __builtin__.property(_get_node_protection)
  bandwidth_protection = __builtin__.property(_get_bandwidth_protection)
  protection_in_use = __builtin__.property(_get_protection_in_use)


  _pyangbind_elements = {'hop_index': hop_index, 'hop_address': hop_address, 'type': type, 'hop_is_router_id': hop_is_router_id, 'protection': protection, 'node_protection': node_protection, 'bandwidth_protection': bandwidth_protection, 'protection_in_use': protection_in_use, }


