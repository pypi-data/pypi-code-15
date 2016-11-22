
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import area
class policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-threshold-monitor - based on the path /threshold-monitor-hidden/threshold-monitor/security/policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sec_policy_name','__area',)

  _yang_name = 'policy'
  _rest_name = 'policy'

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
    self.__sec_policy_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="sec_policy_name", rest_name="sec_policy_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='string', is_config=True)
    self.__area = YANGDynClass(base=YANGListType("sec_area_value",area.area, yang_name="area", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_area_value', extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}), is_container='list', yang_name="area", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)

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
      return [u'threshold-monitor-hidden', u'threshold-monitor', u'security', u'policy']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'threshold-monitor', u'security', u'policy']

  def _get_sec_policy_name(self):
    """
    Getter method for sec_policy_name, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/security/policy/sec_policy_name (string)
    """
    return self.__sec_policy_name
      
  def _set_sec_policy_name(self, v, load=False):
    """
    Setter method for sec_policy_name, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/security/policy/sec_policy_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sec_policy_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sec_policy_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="sec_policy_name", rest_name="sec_policy_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sec_policy_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="sec_policy_name", rest_name="sec_policy_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='string', is_config=True)""",
        })

    self.__sec_policy_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sec_policy_name(self):
    self.__sec_policy_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="sec_policy_name", rest_name="sec_policy_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='string', is_config=True)


  def _get_area(self):
    """
    Getter method for area, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/security/policy/area (list)
    """
    return self.__area
      
  def _set_area(self, v, load=False):
    """
    Setter method for area, mapped from YANG variable /threshold_monitor_hidden/threshold_monitor/security/policy/area (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_area is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_area() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("sec_area_value",area.area, yang_name="area", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_area_value', extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}), is_container='list', yang_name="area", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """area must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("sec_area_value",area.area, yang_name="area", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_area_value', extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}), is_container='list', yang_name="area", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)""",
        })

    self.__area = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_area(self):
    self.__area = YANGDynClass(base=YANGListType("sec_area_value",area.area, yang_name="area", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='sec_area_value', extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}), is_container='list', yang_name="area", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Areas that can be configured for Security monitoring', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'securitymonitoring'}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='list', is_config=True)

  sec_policy_name = __builtin__.property(_get_sec_policy_name, _set_sec_policy_name)
  area = __builtin__.property(_get_area, _set_area)


  _pyangbind_elements = {'sec_policy_name': sec_policy_name, 'area': area, }


