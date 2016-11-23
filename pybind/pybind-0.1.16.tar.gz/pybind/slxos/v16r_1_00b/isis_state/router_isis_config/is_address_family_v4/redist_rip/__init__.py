
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class redist_rip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/router-isis-config/is-address-family-v4/redist-rip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redist_enabled','__redist_level','__redist_metric','__redist_metric_type','__redist_routemap_name',)

  _yang_name = 'redist-rip'
  _rest_name = 'redist-rip'

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
    self.__redist_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="redist-level", rest_name="redist-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)
    self.__redist_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="redist-metric", rest_name="redist-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    self.__redist_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-metric-external': {'value': 1}, u'is-metric-internal': {'value': 0}},), is_leaf=True, yang_name="redist-metric-type", rest_name="redist-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='is-redist-metric-type', is_config=False)
    self.__redist_routemap_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-routemap-name", rest_name="redist-routemap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__redist_enabled = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-enabled", rest_name="redist-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)

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
      return [u'isis-state', u'router-isis-config', u'is-address-family-v4', u'redist-rip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'router-isis-config', u'is-address-family-v4', u'redist-rip']

  def _get_redist_enabled(self):
    """
    Getter method for redist_enabled, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_enabled (isis-status)

    YANG Description: If IS-IS redistribution enabled
    """
    return self.__redist_enabled
      
  def _set_redist_enabled(self, v, load=False):
    """
    Setter method for redist_enabled, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_enabled (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_enabled() directly.

    YANG Description: If IS-IS redistribution enabled
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-enabled", rest_name="redist-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_enabled must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-enabled", rest_name="redist-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__redist_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_enabled(self):
    self.__redist_enabled = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="redist-enabled", rest_name="redist-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_redist_level(self):
    """
    Getter method for redist_level, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_level (isis-level)

    YANG Description: Redistribute routes in the route-table at this level
    """
    return self.__redist_level
      
  def _set_redist_level(self, v, load=False):
    """
    Setter method for redist_level, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_level (isis-level)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_level() directly.

    YANG Description: Redistribute routes in the route-table at this level
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="redist-level", rest_name="redist-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_level must be of a type compatible with isis-level""",
          'defined-type': "brocade-isis-operational:isis-level",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="redist-level", rest_name="redist-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)""",
        })

    self.__redist_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_level(self):
    self.__redist_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="redist-level", rest_name="redist-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)


  def _get_redist_metric(self):
    """
    Getter method for redist_metric, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_metric (uint32)

    YANG Description: Metric for redistributed routes
    """
    return self.__redist_metric
      
  def _set_redist_metric(self, v, load=False):
    """
    Setter method for redist_metric, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_metric (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_metric() directly.

    YANG Description: Metric for redistributed routes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="redist-metric", rest_name="redist-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_metric must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="redist-metric", rest_name="redist-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)""",
        })

    self.__redist_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_metric(self):
    self.__redist_metric = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="redist-metric", rest_name="redist-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='uint32', is_config=False)


  def _get_redist_metric_type(self):
    """
    Getter method for redist_metric_type, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_metric_type (is-redist-metric-type)

    YANG Description: IS-IS metric type for redistributed routes
    """
    return self.__redist_metric_type
      
  def _set_redist_metric_type(self, v, load=False):
    """
    Setter method for redist_metric_type, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_metric_type (is-redist-metric-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_metric_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_metric_type() directly.

    YANG Description: IS-IS metric type for redistributed routes
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-metric-external': {'value': 1}, u'is-metric-internal': {'value': 0}},), is_leaf=True, yang_name="redist-metric-type", rest_name="redist-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='is-redist-metric-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_metric_type must be of a type compatible with is-redist-metric-type""",
          'defined-type': "brocade-isis-operational:is-redist-metric-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-metric-external': {'value': 1}, u'is-metric-internal': {'value': 0}},), is_leaf=True, yang_name="redist-metric-type", rest_name="redist-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='is-redist-metric-type', is_config=False)""",
        })

    self.__redist_metric_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_metric_type(self):
    self.__redist_metric_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-metric-external': {'value': 1}, u'is-metric-internal': {'value': 0}},), is_leaf=True, yang_name="redist-metric-type", rest_name="redist-metric-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='is-redist-metric-type', is_config=False)


  def _get_redist_routemap_name(self):
    """
    Getter method for redist_routemap_name, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_routemap_name (string)

    YANG Description: Route map reference to redistribute routes
    """
    return self.__redist_routemap_name
      
  def _set_redist_routemap_name(self, v, load=False):
    """
    Setter method for redist_routemap_name, mapped from YANG variable /isis_state/router_isis_config/is_address_family_v4/redist_rip/redist_routemap_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redist_routemap_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redist_routemap_name() directly.

    YANG Description: Route map reference to redistribute routes
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="redist-routemap-name", rest_name="redist-routemap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redist_routemap_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-routemap-name", rest_name="redist-routemap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__redist_routemap_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redist_routemap_name(self):
    self.__redist_routemap_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="redist-routemap-name", rest_name="redist-routemap-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)

  redist_enabled = __builtin__.property(_get_redist_enabled)
  redist_level = __builtin__.property(_get_redist_level)
  redist_metric = __builtin__.property(_get_redist_metric)
  redist_metric_type = __builtin__.property(_get_redist_metric_type)
  redist_routemap_name = __builtin__.property(_get_redist_routemap_name)


  _pyangbind_elements = {'redist_enabled': redist_enabled, 'redist_level': redist_level, 'redist_metric': redist_metric, 'redist_metric_type': redist_metric_type, 'redist_routemap_name': redist_routemap_name, }


