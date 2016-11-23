
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import out_segments
class ldp_tunnels(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/tunnels/ldp-tunnels. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: ldp tunnel
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tunnel_interface_index','__tunnel_metric','__name','__tunnel_vif','__protocol_type','__out_segments','__tunnel_destination','__prefix_length',)

  _yang_name = 'ldp-tunnels'
  _rest_name = 'ldp-tunnels'

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
    self.__out_segments = YANGDynClass(base=YANGListType("outgoing_interface",out_segments.out_segments, yang_name="out-segments", rest_name="out-segments", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-interface', extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}), is_container='list', yang_name="out-segments", rest_name="out-segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    self.__tunnel_destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__tunnel_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-metric", rest_name="tunnel-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__tunnel_vif = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-vif", rest_name="tunnel-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__protocol_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'staticp': {'value': 0}, u'ldp': {'value': 2}, u'rsvp': {'value': 1}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol-type', is_config=False)
    self.__tunnel_interface_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-interface-index", rest_name="tunnel-interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'ldp', u'tunnels', u'ldp-tunnels']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'tunnels', u'ldp-tunnels']

  def _get_tunnel_interface_index(self):
    """
    Getter method for tunnel_interface_index, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_interface_index (uint32)

    YANG Description: tunnel interface index
    """
    return self.__tunnel_interface_index
      
  def _set_tunnel_interface_index(self, v, load=False):
    """
    Setter method for tunnel_interface_index, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_interface_index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel_interface_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel_interface_index() directly.

    YANG Description: tunnel interface index
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-interface-index", rest_name="tunnel-interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel_interface_index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-interface-index", rest_name="tunnel-interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tunnel_interface_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel_interface_index(self):
    self.__tunnel_interface_index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-interface-index", rest_name="tunnel-interface-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_tunnel_metric(self):
    """
    Getter method for tunnel_metric, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_metric (uint32)

    YANG Description: tunnel metric
    """
    return self.__tunnel_metric
      
  def _set_tunnel_metric(self, v, load=False):
    """
    Setter method for tunnel_metric, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel_metric() directly.

    YANG Description: tunnel metric
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-metric", rest_name="tunnel-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-metric", rest_name="tunnel-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tunnel_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel_metric(self):
    self.__tunnel_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-metric", rest_name="tunnel-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/name (string)

    YANG Description: name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_tunnel_vif(self):
    """
    Getter method for tunnel_vif, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_vif (uint32)

    YANG Description: Tunnel vif
    """
    return self.__tunnel_vif
      
  def _set_tunnel_vif(self, v, load=False):
    """
    Setter method for tunnel_vif, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_vif (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel_vif is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel_vif() directly.

    YANG Description: Tunnel vif
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-vif", rest_name="tunnel-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel_vif must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-vif", rest_name="tunnel-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__tunnel_vif = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel_vif(self):
    self.__tunnel_vif = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="tunnel-vif", rest_name="tunnel-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_protocol_type(self):
    """
    Getter method for protocol_type, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/protocol_type (mpls-protocol-type)

    YANG Description: Protocol Type
    """
    return self.__protocol_type
      
  def _set_protocol_type(self, v, load=False):
    """
    Setter method for protocol_type, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/protocol_type (mpls-protocol-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_type() directly.

    YANG Description: Protocol Type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'staticp': {'value': 0}, u'ldp': {'value': 2}, u'rsvp': {'value': 1}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_type must be of a type compatible with mpls-protocol-type""",
          'defined-type': "brocade-mpls-operational:mpls-protocol-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'staticp': {'value': 0}, u'ldp': {'value': 2}, u'rsvp': {'value': 1}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol-type', is_config=False)""",
        })

    self.__protocol_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_type(self):
    self.__protocol_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'staticp': {'value': 0}, u'ldp': {'value': 2}, u'rsvp': {'value': 1}},), is_leaf=True, yang_name="protocol-type", rest_name="protocol-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='mpls-protocol-type', is_config=False)


  def _get_out_segments(self):
    """
    Getter method for out_segments, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/out_segments (list)

    YANG Description: out segment
    """
    return self.__out_segments
      
  def _set_out_segments(self, v, load=False):
    """
    Setter method for out_segments, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/out_segments (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_segments is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_segments() directly.

    YANG Description: out segment
    """
    try:
      t = YANGDynClass(v,base=YANGListType("outgoing_interface",out_segments.out_segments, yang_name="out-segments", rest_name="out-segments", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-interface', extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}), is_container='list', yang_name="out-segments", rest_name="out-segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_segments must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("outgoing_interface",out_segments.out_segments, yang_name="out-segments", rest_name="out-segments", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-interface', extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}), is_container='list', yang_name="out-segments", rest_name="out-segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__out_segments = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_segments(self):
    self.__out_segments = YANGDynClass(base=YANGListType("outgoing_interface",out_segments.out_segments, yang_name="out-segments", rest_name="out-segments", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='outgoing-interface', extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}), is_container='list', yang_name="out-segments", rest_name="out-segments", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-out-segment', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)


  def _get_tunnel_destination(self):
    """
    Getter method for tunnel_destination, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_destination (inet:ipv4-address)

    YANG Description: tunnel destination
    """
    return self.__tunnel_destination
      
  def _set_tunnel_destination(self, v, load=False):
    """
    Setter method for tunnel_destination, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/tunnel_destination (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel_destination() directly.

    YANG Description: tunnel destination
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel_destination must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__tunnel_destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel_destination(self):
    self.__tunnel_destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="tunnel-destination", rest_name="tunnel-destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_prefix_length(self):
    """
    Getter method for prefix_length, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/prefix_length (uint32)

    YANG Description: prefix length
    """
    return self.__prefix_length
      
  def _set_prefix_length(self, v, load=False):
    """
    Setter method for prefix_length, mapped from YANG variable /mpls_state/ldp/tunnels/ldp_tunnels/prefix_length (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_length() directly.

    YANG Description: prefix length
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_length must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__prefix_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_length(self):
    self.__prefix_length = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="prefix-length", rest_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  tunnel_interface_index = __builtin__.property(_get_tunnel_interface_index)
  tunnel_metric = __builtin__.property(_get_tunnel_metric)
  name = __builtin__.property(_get_name)
  tunnel_vif = __builtin__.property(_get_tunnel_vif)
  protocol_type = __builtin__.property(_get_protocol_type)
  out_segments = __builtin__.property(_get_out_segments)
  tunnel_destination = __builtin__.property(_get_tunnel_destination)
  prefix_length = __builtin__.property(_get_prefix_length)


  _pyangbind_elements = {'tunnel_interface_index': tunnel_interface_index, 'tunnel_metric': tunnel_metric, 'name': name, 'tunnel_vif': tunnel_vif, 'protocol_type': protocol_type, 'out_segments': out_segments, 'tunnel_destination': tunnel_destination, 'prefix_length': prefix_length, }


