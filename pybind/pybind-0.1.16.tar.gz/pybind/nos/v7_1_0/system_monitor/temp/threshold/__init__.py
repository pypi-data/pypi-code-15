
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class threshold(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-monitor - based on the path /system-monitor/temp/threshold. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__marginal_threshold','__down_threshold',)

  _yang_name = 'threshold'
  _rest_name = 'threshold'

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
    self.__down_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="down-threshold", rest_name="down-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to DOWN\nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)
    self.__marginal_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="marginal-threshold", rest_name="marginal-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to MARGINAL \nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)

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
      return [u'system-monitor', u'temp', u'threshold']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'system-monitor', u'temp', u'threshold']

  def _get_marginal_threshold(self):
    """
    Getter method for marginal_threshold, mapped from YANG variable /system_monitor/temp/threshold/marginal_threshold (uint32)
    """
    return self.__marginal_threshold
      
  def _set_marginal_threshold(self, v, load=False):
    """
    Setter method for marginal_threshold, mapped from YANG variable /system_monitor/temp/threshold/marginal_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_marginal_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_marginal_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="marginal-threshold", rest_name="marginal-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to MARGINAL \nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """marginal_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="marginal-threshold", rest_name="marginal-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to MARGINAL \nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__marginal_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_marginal_threshold(self):
    self.__marginal_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="marginal-threshold", rest_name="marginal-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to MARGINAL \nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)


  def _get_down_threshold(self):
    """
    Getter method for down_threshold, mapped from YANG variable /system_monitor/temp/threshold/down_threshold (uint32)
    """
    return self.__down_threshold
      
  def _set_down_threshold(self, v, load=False):
    """
    Setter method for down_threshold, mapped from YANG variable /system_monitor/temp/threshold/down_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_down_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_down_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="down-threshold", rest_name="down-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to DOWN\nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """down_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="down-threshold", rest_name="down-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to DOWN\nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)""",
        })

    self.__down_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_down_threshold(self):
    self.__down_threshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="down-threshold", rest_name="down-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Minimum number contributing to DOWN\nstate of component:TEMPERATURE SENSOR'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='uint32', is_config=True)

  marginal_threshold = __builtin__.property(_get_marginal_threshold, _set_marginal_threshold)
  down_threshold = __builtin__.property(_get_down_threshold, _set_down_threshold)


  _pyangbind_elements = {'marginal_threshold': marginal_threshold, 'down_threshold': down_threshold, }


