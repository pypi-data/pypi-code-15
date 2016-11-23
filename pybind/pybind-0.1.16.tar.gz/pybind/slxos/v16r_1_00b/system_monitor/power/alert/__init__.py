
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class alert(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-monitor - based on the path /system-monitor/power/alert. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__state','__action',)

  _yang_name = 'alert'
  _rest_name = 'alert'

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
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action that may be taken when\ncomponent:POWER SUPPLY changes configured state'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-actions', is_config=True)
    self.__state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 2}, u'none': {'value': 5}, u'faulty': {'value': 4}, u'all': {'value': 6}, u'removed': {'value': 0}, u'inserted': {'value': 1}},), is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Supported states for component:\nPOWER-SUPPLY that may be monitored'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-state', is_config=True)

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
      return [u'system-monitor', u'power', u'alert']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'system-monitor', u'power', u'alert']

  def _get_state(self):
    """
    Getter method for state, mapped from YANG variable /system_monitor/power/alert/state (supported-state)
    """
    return self.__state
      
  def _set_state(self, v, load=False):
    """
    Setter method for state, mapped from YANG variable /system_monitor/power/alert/state (supported-state)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 2}, u'none': {'value': 5}, u'faulty': {'value': 4}, u'all': {'value': 6}, u'removed': {'value': 0}, u'inserted': {'value': 1}},), is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Supported states for component:\nPOWER-SUPPLY that may be monitored'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-state', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """state must be of a type compatible with supported-state""",
          'defined-type': "brocade-system-monitor:supported-state",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 2}, u'none': {'value': 5}, u'faulty': {'value': 4}, u'all': {'value': 6}, u'removed': {'value': 0}, u'inserted': {'value': 1}},), is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Supported states for component:\nPOWER-SUPPLY that may be monitored'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-state', is_config=True)""",
        })

    self.__state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_state(self):
    self.__state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 2}, u'none': {'value': 5}, u'faulty': {'value': 4}, u'all': {'value': 6}, u'removed': {'value': 0}, u'inserted': {'value': 1}},), is_leaf=True, yang_name="state", rest_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Supported states for component:\nPOWER-SUPPLY that may be monitored'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-state', is_config=True)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /system_monitor/power/alert/action (supported-actions)
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /system_monitor/power/alert/action (supported-actions)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action that may be taken when\ncomponent:POWER SUPPLY changes configured state'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-actions', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with supported-actions""",
          'defined-type': "brocade-system-monitor:supported-actions",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action that may be taken when\ncomponent:POWER SUPPLY changes configured state'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-actions', is_config=True)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {'value': 0}, u'all': {'value': 1}, u'raslog': {'value': 3}, u'email': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Action that may be taken when\ncomponent:POWER SUPPLY changes configured state'}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='supported-actions', is_config=True)

  state = __builtin__.property(_get_state, _set_state)
  action = __builtin__.property(_get_action, _set_action)


  _pyangbind_elements = {'state': state, 'action': action, }


