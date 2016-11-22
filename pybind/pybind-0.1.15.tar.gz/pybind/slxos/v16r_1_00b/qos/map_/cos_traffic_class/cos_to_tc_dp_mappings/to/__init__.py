
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class to(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mls - based on the path /qos/map/cos-traffic-class/cos-to-tc-dp-mappings/to. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__to_traffic_class','__to_drop_precedence',)

  _yang_name = 'to'
  _rest_name = 'to'

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
    self.__to_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="to-traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Traffic-Class', u'alt-name': u'traffic-class', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)
    self.__to_drop_precedence = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 3']}), is_leaf=True, yang_name="to-drop-precedence", rest_name="drop-precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Drop-Precedence', u'cli-optional-in-sequence': None, u'alt-name': u'drop-precedence', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='drop-precedence-id-type', is_config=True)

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
      return [u'qos', u'map', u'cos-traffic-class', u'cos-to-tc-dp-mappings', u'to']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'map', u'cos-traffic-class', u'map', u'to']

  def _get_to_traffic_class(self):
    """
    Getter method for to_traffic_class, mapped from YANG variable /qos/map/cos_traffic_class/cos_to_tc_dp_mappings/to/to_traffic_class (traffic-class-id-type)
    """
    return self.__to_traffic_class
      
  def _set_to_traffic_class(self, v, load=False):
    """
    Setter method for to_traffic_class, mapped from YANG variable /qos/map/cos_traffic_class/cos_to_tc_dp_mappings/to/to_traffic_class (traffic-class-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_to_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_to_traffic_class() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="to-traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Traffic-Class', u'alt-name': u'traffic-class', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """to_traffic_class must be of a type compatible with traffic-class-id-type""",
          'defined-type': "brocade-qos-mls:traffic-class-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="to-traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Traffic-Class', u'alt-name': u'traffic-class', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)""",
        })

    self.__to_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_to_traffic_class(self):
    self.__to_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="to-traffic-class", rest_name="traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Traffic-Class', u'alt-name': u'traffic-class', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='traffic-class-id-type', is_config=True)


  def _get_to_drop_precedence(self):
    """
    Getter method for to_drop_precedence, mapped from YANG variable /qos/map/cos_traffic_class/cos_to_tc_dp_mappings/to/to_drop_precedence (drop-precedence-id-type)
    """
    return self.__to_drop_precedence
      
  def _set_to_drop_precedence(self, v, load=False):
    """
    Setter method for to_drop_precedence, mapped from YANG variable /qos/map/cos_traffic_class/cos_to_tc_dp_mappings/to/to_drop_precedence (drop-precedence-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_to_drop_precedence is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_to_drop_precedence() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 3']}), is_leaf=True, yang_name="to-drop-precedence", rest_name="drop-precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Drop-Precedence', u'cli-optional-in-sequence': None, u'alt-name': u'drop-precedence', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='drop-precedence-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """to_drop_precedence must be of a type compatible with drop-precedence-id-type""",
          'defined-type': "brocade-qos-mls:drop-precedence-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 3']}), is_leaf=True, yang_name="to-drop-precedence", rest_name="drop-precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Drop-Precedence', u'cli-optional-in-sequence': None, u'alt-name': u'drop-precedence', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='drop-precedence-id-type', is_config=True)""",
        })

    self.__to_drop_precedence = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_to_drop_precedence(self):
    self.__to_drop_precedence = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 3']}), is_leaf=True, yang_name="to-drop-precedence", rest_name="drop-precedence", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Out Drop-Precedence', u'cli-optional-in-sequence': None, u'alt-name': u'drop-precedence', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mls', defining_module='brocade-qos-mls', yang_type='drop-precedence-id-type', is_config=True)

  to_traffic_class = __builtin__.property(_get_to_traffic_class, _set_to_traffic_class)
  to_drop_precedence = __builtin__.property(_get_to_drop_precedence, _set_to_drop_precedence)


  _pyangbind_elements = {'to_traffic_class': to_traffic_class, 'to_drop_precedence': to_drop_precedence, }


