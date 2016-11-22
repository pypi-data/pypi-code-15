
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldp_protocol_errors_instance_total
import ldp_protocol_stats_instance_total
import ldp_protocol_stats_instance_since_clear
import ldp_protocol_errors_instance_since_clear
class statistics(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/statistics. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Global LDP stats
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_protocol_errors_instance_total','__ldp_protocol_stats_instance_total','__ldp_protocol_stats_instance_since_clear','__ldp_protocol_errors_instance_since_clear',)

  _yang_name = 'statistics'
  _rest_name = 'statistics'

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
    self.__ldp_protocol_errors_instance_total = YANGDynClass(base=ldp_protocol_errors_instance_total.ldp_protocol_errors_instance_total, is_container='container', yang_name="ldp-protocol-errors-instance-total", rest_name="ldp-protocol-errors-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__ldp_protocol_stats_instance_total = YANGDynClass(base=ldp_protocol_stats_instance_total.ldp_protocol_stats_instance_total, is_container='container', yang_name="ldp-protocol-stats-instance-total", rest_name="ldp-protocol-stats-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__ldp_protocol_errors_instance_since_clear = YANGDynClass(base=ldp_protocol_errors_instance_since_clear.ldp_protocol_errors_instance_since_clear, is_container='container', yang_name="ldp-protocol-errors-instance-since-clear", rest_name="ldp-protocol-errors-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    self.__ldp_protocol_stats_instance_since_clear = YANGDynClass(base=ldp_protocol_stats_instance_since_clear.ldp_protocol_stats_instance_since_clear, is_container='container', yang_name="ldp-protocol-stats-instance-since-clear", rest_name="ldp-protocol-stats-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

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
      return [u'mpls-state', u'ldp', u'statistics']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'statistics']

  def _get_ldp_protocol_errors_instance_total(self):
    """
    Getter method for ldp_protocol_errors_instance_total, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_errors_instance_total (container)
    """
    return self.__ldp_protocol_errors_instance_total
      
  def _set_ldp_protocol_errors_instance_total(self, v, load=False):
    """
    Setter method for ldp_protocol_errors_instance_total, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_errors_instance_total (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_protocol_errors_instance_total is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_protocol_errors_instance_total() directly.
    """
    try:
      t = YANGDynClass(v,base=ldp_protocol_errors_instance_total.ldp_protocol_errors_instance_total, is_container='container', yang_name="ldp-protocol-errors-instance-total", rest_name="ldp-protocol-errors-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_protocol_errors_instance_total must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_protocol_errors_instance_total.ldp_protocol_errors_instance_total, is_container='container', yang_name="ldp-protocol-errors-instance-total", rest_name="ldp-protocol-errors-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__ldp_protocol_errors_instance_total = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_protocol_errors_instance_total(self):
    self.__ldp_protocol_errors_instance_total = YANGDynClass(base=ldp_protocol_errors_instance_total.ldp_protocol_errors_instance_total, is_container='container', yang_name="ldp-protocol-errors-instance-total", rest_name="ldp-protocol-errors-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_ldp_protocol_stats_instance_total(self):
    """
    Getter method for ldp_protocol_stats_instance_total, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_stats_instance_total (container)
    """
    return self.__ldp_protocol_stats_instance_total
      
  def _set_ldp_protocol_stats_instance_total(self, v, load=False):
    """
    Setter method for ldp_protocol_stats_instance_total, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_stats_instance_total (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_protocol_stats_instance_total is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_protocol_stats_instance_total() directly.
    """
    try:
      t = YANGDynClass(v,base=ldp_protocol_stats_instance_total.ldp_protocol_stats_instance_total, is_container='container', yang_name="ldp-protocol-stats-instance-total", rest_name="ldp-protocol-stats-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_protocol_stats_instance_total must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_protocol_stats_instance_total.ldp_protocol_stats_instance_total, is_container='container', yang_name="ldp-protocol-stats-instance-total", rest_name="ldp-protocol-stats-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__ldp_protocol_stats_instance_total = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_protocol_stats_instance_total(self):
    self.__ldp_protocol_stats_instance_total = YANGDynClass(base=ldp_protocol_stats_instance_total.ldp_protocol_stats_instance_total, is_container='container', yang_name="ldp-protocol-stats-instance-total", rest_name="ldp-protocol-stats-instance-total", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-total-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_ldp_protocol_stats_instance_since_clear(self):
    """
    Getter method for ldp_protocol_stats_instance_since_clear, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_stats_instance_since_clear (container)
    """
    return self.__ldp_protocol_stats_instance_since_clear
      
  def _set_ldp_protocol_stats_instance_since_clear(self, v, load=False):
    """
    Setter method for ldp_protocol_stats_instance_since_clear, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_stats_instance_since_clear (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_protocol_stats_instance_since_clear is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_protocol_stats_instance_since_clear() directly.
    """
    try:
      t = YANGDynClass(v,base=ldp_protocol_stats_instance_since_clear.ldp_protocol_stats_instance_since_clear, is_container='container', yang_name="ldp-protocol-stats-instance-since-clear", rest_name="ldp-protocol-stats-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_protocol_stats_instance_since_clear must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_protocol_stats_instance_since_clear.ldp_protocol_stats_instance_since_clear, is_container='container', yang_name="ldp-protocol-stats-instance-since-clear", rest_name="ldp-protocol-stats-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__ldp_protocol_stats_instance_since_clear = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_protocol_stats_instance_since_clear(self):
    self.__ldp_protocol_stats_instance_since_clear = YANGDynClass(base=ldp_protocol_stats_instance_since_clear.ldp_protocol_stats_instance_since_clear, is_container='container', yang_name="ldp-protocol-stats-instance-since-clear", rest_name="ldp-protocol-stats-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-stats-instance-ldp-protocol-stats-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)


  def _get_ldp_protocol_errors_instance_since_clear(self):
    """
    Getter method for ldp_protocol_errors_instance_since_clear, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_errors_instance_since_clear (container)
    """
    return self.__ldp_protocol_errors_instance_since_clear
      
  def _set_ldp_protocol_errors_instance_since_clear(self, v, load=False):
    """
    Setter method for ldp_protocol_errors_instance_since_clear, mapped from YANG variable /mpls_state/ldp/statistics/ldp_protocol_errors_instance_since_clear (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_protocol_errors_instance_since_clear is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_protocol_errors_instance_since_clear() directly.
    """
    try:
      t = YANGDynClass(v,base=ldp_protocol_errors_instance_since_clear.ldp_protocol_errors_instance_since_clear, is_container='container', yang_name="ldp-protocol-errors-instance-since-clear", rest_name="ldp-protocol-errors-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_protocol_errors_instance_since_clear must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ldp_protocol_errors_instance_since_clear.ldp_protocol_errors_instance_since_clear, is_container='container', yang_name="ldp-protocol-errors-instance-since-clear", rest_name="ldp-protocol-errors-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)""",
        })

    self.__ldp_protocol_errors_instance_since_clear = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_protocol_errors_instance_since_clear(self):
    self.__ldp_protocol_errors_instance_since_clear = YANGDynClass(base=ldp_protocol_errors_instance_since_clear.ldp_protocol_errors_instance_since_clear, is_container='container', yang_name="ldp-protocol-errors-instance-since-clear", rest_name="ldp-protocol-errors-instance-since-clear", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-ldp-protocol-errors-instance-ldp-protocol-errors-instance-since-clear-1'}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='container', is_config=False)

  ldp_protocol_errors_instance_total = __builtin__.property(_get_ldp_protocol_errors_instance_total)
  ldp_protocol_stats_instance_total = __builtin__.property(_get_ldp_protocol_stats_instance_total)
  ldp_protocol_stats_instance_since_clear = __builtin__.property(_get_ldp_protocol_stats_instance_since_clear)
  ldp_protocol_errors_instance_since_clear = __builtin__.property(_get_ldp_protocol_errors_instance_since_clear)


  _pyangbind_elements = {'ldp_protocol_errors_instance_total': ldp_protocol_errors_instance_total, 'ldp_protocol_stats_instance_total': ldp_protocol_stats_instance_total, 'ldp_protocol_stats_instance_since_clear': ldp_protocol_stats_instance_since_clear, 'ldp_protocol_errors_instance_since_clear': ldp_protocol_errors_instance_since_clear, }


