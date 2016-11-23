
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class summary(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/get-mpls-ldp-neighbor-brief/output/mpls-ldp-neighbor-brief/summary. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__neighbor_transport','__interface','__neighbor_ldp_id','__max_hold_time','__time_left',)

  _yang_name = 'summary'
  _rest_name = 'summary'

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
    self.__interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__time_left = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-left", rest_name="time-left", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__neighbor_ldp_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor-ldp-id", rest_name="neighbor-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__neighbor_transport = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="neighbor-transport", rest_name="neighbor-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__max_hold_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-hold-time", rest_name="max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'get-mpls-ldp-neighbor-brief', u'output', u'mpls-ldp-neighbor-brief', u'summary']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-mpls-ldp-neighbor-brief', u'output', u'mpls-ldp-neighbor-brief', u'summary']

  def _get_neighbor_transport(self):
    """
    Getter method for neighbor_transport, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/neighbor_transport (inet:ipv4-address)

    YANG Description: Neighbor transport address
    """
    return self.__neighbor_transport
      
  def _set_neighbor_transport(self, v, load=False):
    """
    Setter method for neighbor_transport, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/neighbor_transport (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_transport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_transport() directly.

    YANG Description: Neighbor transport address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="neighbor-transport", rest_name="neighbor-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_transport must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="neighbor-transport", rest_name="neighbor-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__neighbor_transport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_transport(self):
    self.__neighbor_transport = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="neighbor-transport", rest_name="neighbor-transport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/interface (string)

    YANG Description: Interface
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/interface (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Interface
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=unicode, is_leaf=True, yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_neighbor_ldp_id(self):
    """
    Getter method for neighbor_ldp_id, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/neighbor_ldp_id (string)

    YANG Description: Neighbor LDP ID
    """
    return self.__neighbor_ldp_id
      
  def _set_neighbor_ldp_id(self, v, load=False):
    """
    Setter method for neighbor_ldp_id, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/neighbor_ldp_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_ldp_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_ldp_id() directly.

    YANG Description: Neighbor LDP ID
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="neighbor-ldp-id", rest_name="neighbor-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_ldp_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor-ldp-id", rest_name="neighbor-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__neighbor_ldp_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_ldp_id(self):
    self.__neighbor_ldp_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="neighbor-ldp-id", rest_name="neighbor-ldp-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_max_hold_time(self):
    """
    Getter method for max_hold_time, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/max_hold_time (uint32)

    YANG Description: Max hold time
    """
    return self.__max_hold_time
      
  def _set_max_hold_time(self, v, load=False):
    """
    Setter method for max_hold_time, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/max_hold_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_hold_time() directly.

    YANG Description: Max hold time
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-hold-time", rest_name="max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_hold_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-hold-time", rest_name="max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__max_hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_hold_time(self):
    self.__max_hold_time = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="max-hold-time", rest_name="max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_time_left(self):
    """
    Getter method for time_left, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/time_left (uint32)

    YANG Description: Hold time left
    """
    return self.__time_left
      
  def _set_time_left(self, v, load=False):
    """
    Setter method for time_left, mapped from YANG variable /brocade_mpls_rpc/get_mpls_ldp_neighbor_brief/output/mpls_ldp_neighbor_brief/summary/time_left (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_time_left is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_time_left() directly.

    YANG Description: Hold time left
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-left", rest_name="time-left", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """time_left must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-left", rest_name="time-left", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__time_left = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_time_left(self):
    self.__time_left = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="time-left", rest_name="time-left", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  neighbor_transport = __builtin__.property(_get_neighbor_transport, _set_neighbor_transport)
  interface = __builtin__.property(_get_interface, _set_interface)
  neighbor_ldp_id = __builtin__.property(_get_neighbor_ldp_id, _set_neighbor_ldp_id)
  max_hold_time = __builtin__.property(_get_max_hold_time, _set_max_hold_time)
  time_left = __builtin__.property(_get_time_left, _set_time_left)


  _pyangbind_elements = {'neighbor_transport': neighbor_transport, 'interface': interface, 'neighbor_ldp_id': neighbor_ldp_id, 'max_hold_time': max_hold_time, 'time_left': time_left, }


