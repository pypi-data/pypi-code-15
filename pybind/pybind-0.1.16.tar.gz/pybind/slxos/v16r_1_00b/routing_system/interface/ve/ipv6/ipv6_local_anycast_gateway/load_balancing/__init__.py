
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class load_balancing(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/ipv6-local-anycast-gateway/load-balancing. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__basic','__threshold_priority',)

  _yang_name = 'load-balancing'
  _rest_name = 'load-balancing'

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
    self.__threshold_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="threshold-priority", rest_name="threshold-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold Priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)
    self.__basic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-local-anycast-gateway', u'load-balancing']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'fabric-virtual-gateway', u'load-balancing']

  def _get_basic(self):
    """
    Getter method for basic, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/load_balancing/basic (empty)
    """
    return self.__basic
      
  def _set_basic(self, v, load=False):
    """
    Setter method for basic, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/load_balancing/basic (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_basic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_basic() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """basic must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)""",
        })

    self.__basic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_basic(self):
    self.__basic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='empty', is_config=True)


  def _get_threshold_priority(self):
    """
    Getter method for threshold_priority, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/load_balancing/threshold_priority (uint32)

    YANG Description: Threshold Priority
    """
    return self.__threshold_priority
      
  def _set_threshold_priority(self, v, load=False):
    """
    Setter method for threshold_priority, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_local_anycast_gateway/load_balancing/threshold_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_threshold_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_threshold_priority() directly.

    YANG Description: Threshold Priority
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="threshold-priority", rest_name="threshold-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold Priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """threshold_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="threshold-priority", rest_name="threshold-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold Priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)""",
        })

    self.__threshold_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_threshold_priority(self):
    self.__threshold_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="threshold-priority", rest_name="threshold-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Threshold Priority'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='uint32', is_config=True)

  basic = __builtin__.property(_get_basic, _set_basic)
  threshold_priority = __builtin__.property(_get_threshold_priority, _set_threshold_priority)


  _pyangbind_elements = {'basic': basic, 'threshold_priority': threshold_priority, }


