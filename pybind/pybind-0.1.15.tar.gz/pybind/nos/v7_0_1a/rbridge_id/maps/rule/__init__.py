
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rule(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/maps/rule. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rulename','__targetgroup','__monitor','__timebase','__op','__threshold',)

  _yang_name = 'rule'
  _rest_name = 'rule'

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
    self.__timebase = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {}, u'day': {}, u'hour': {}, u'min': {}},), is_leaf=True, yang_name="timebase", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)
    self.__monitor = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MEMORY_USAGE': {}, u'FLASH_USAGE': {}, u'HA_SYNC': {}, u'BAD_PWR': {}, u'BAD_TEMP': {}, u'BAD_FAN': {}, u'CPU': {}, u'SFP_TEMP': {}, u'SEC_TELNET': {}, u'TEMP': {}, u'RX_SYM_ERR': {}, u'CRCALN': {}, u'VOLTAGE': {}, u'SFP_STATE': {}, u'WWN_DOWN': {}, u'FAN_STATE': {}, u'CURRENT': {}, u'WWN': {}, u'RX_ABN_FRAME': {}, u'RXP': {}, u'FAULTY_BLADE': {}, u'BLADE_STATE': {}, u'ETH_MGMT_PORT_STATE': {}, u'PS_STATE': {}, u'SEC_LV': {}, u'TXP': {}, u'DOWN_SFM': {}},), is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)
    self.__rulename = YANGDynClass(base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure rule name', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    self.__threshold = YANGDynClass(base=unicode, is_leaf=True, yang_name="threshold", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'threshold value', u'alt-name': u'value'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    self.__targetgroup = YANGDynClass(base=unicode, is_leaf=True, yang_name="targetgroup", rest_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'target group for rule', u'alt-name': u'group', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    self.__op = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'le': {}, u'lt': {}, u'gt': {}, u'eq': {}, u'ge': {}},), is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)

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
      return [u'rbridge-id', u'maps', u'rule']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'maps', u'rule']

  def _get_rulename(self):
    """
    Getter method for rulename, mapped from YANG variable /rbridge_id/maps/rule/rulename (string)
    """
    return self.__rulename
      
  def _set_rulename(self, v, load=False):
    """
    Setter method for rulename, mapped from YANG variable /rbridge_id/maps/rule/rulename (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rulename is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rulename() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure rule name', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rulename must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure rule name', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)""",
        })

    self.__rulename = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rulename(self):
    self.__rulename = YANGDynClass(base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure rule name', u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)


  def _get_targetgroup(self):
    """
    Getter method for targetgroup, mapped from YANG variable /rbridge_id/maps/rule/targetgroup (string)
    """
    return self.__targetgroup
      
  def _set_targetgroup(self, v, load=False):
    """
    Setter method for targetgroup, mapped from YANG variable /rbridge_id/maps/rule/targetgroup (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_targetgroup is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_targetgroup() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="targetgroup", rest_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'target group for rule', u'alt-name': u'group', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """targetgroup must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="targetgroup", rest_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'target group for rule', u'alt-name': u'group', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)""",
        })

    self.__targetgroup = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_targetgroup(self):
    self.__targetgroup = YANGDynClass(base=unicode, is_leaf=True, yang_name="targetgroup", rest_name="group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'target group for rule', u'alt-name': u'group', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)


  def _get_monitor(self):
    """
    Getter method for monitor, mapped from YANG variable /rbridge_id/maps/rule/monitor (enumeration)
    """
    return self.__monitor
      
  def _set_monitor(self, v, load=False):
    """
    Setter method for monitor, mapped from YANG variable /rbridge_id/maps/rule/monitor (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_monitor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_monitor() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MEMORY_USAGE': {}, u'FLASH_USAGE': {}, u'HA_SYNC': {}, u'BAD_PWR': {}, u'BAD_TEMP': {}, u'BAD_FAN': {}, u'CPU': {}, u'SFP_TEMP': {}, u'SEC_TELNET': {}, u'TEMP': {}, u'RX_SYM_ERR': {}, u'CRCALN': {}, u'VOLTAGE': {}, u'SFP_STATE': {}, u'WWN_DOWN': {}, u'FAN_STATE': {}, u'CURRENT': {}, u'WWN': {}, u'RX_ABN_FRAME': {}, u'RXP': {}, u'FAULTY_BLADE': {}, u'BLADE_STATE': {}, u'ETH_MGMT_PORT_STATE': {}, u'PS_STATE': {}, u'SEC_LV': {}, u'TXP': {}, u'DOWN_SFM': {}},), is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """monitor must be of a type compatible with enumeration""",
          'defined-type': "brocade-maps:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MEMORY_USAGE': {}, u'FLASH_USAGE': {}, u'HA_SYNC': {}, u'BAD_PWR': {}, u'BAD_TEMP': {}, u'BAD_FAN': {}, u'CPU': {}, u'SFP_TEMP': {}, u'SEC_TELNET': {}, u'TEMP': {}, u'RX_SYM_ERR': {}, u'CRCALN': {}, u'VOLTAGE': {}, u'SFP_STATE': {}, u'WWN_DOWN': {}, u'FAN_STATE': {}, u'CURRENT': {}, u'WWN': {}, u'RX_ABN_FRAME': {}, u'RXP': {}, u'FAULTY_BLADE': {}, u'BLADE_STATE': {}, u'ETH_MGMT_PORT_STATE': {}, u'PS_STATE': {}, u'SEC_LV': {}, u'TXP': {}, u'DOWN_SFM': {}},), is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)""",
        })

    self.__monitor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_monitor(self):
    self.__monitor = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'MEMORY_USAGE': {}, u'FLASH_USAGE': {}, u'HA_SYNC': {}, u'BAD_PWR': {}, u'BAD_TEMP': {}, u'BAD_FAN': {}, u'CPU': {}, u'SFP_TEMP': {}, u'SEC_TELNET': {}, u'TEMP': {}, u'RX_SYM_ERR': {}, u'CRCALN': {}, u'VOLTAGE': {}, u'SFP_STATE': {}, u'WWN_DOWN': {}, u'FAN_STATE': {}, u'CURRENT': {}, u'WWN': {}, u'RX_ABN_FRAME': {}, u'RXP': {}, u'FAULTY_BLADE': {}, u'BLADE_STATE': {}, u'ETH_MGMT_PORT_STATE': {}, u'PS_STATE': {}, u'SEC_LV': {}, u'TXP': {}, u'DOWN_SFM': {}},), is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)


  def _get_timebase(self):
    """
    Getter method for timebase, mapped from YANG variable /rbridge_id/maps/rule/timebase (enumeration)
    """
    return self.__timebase
      
  def _set_timebase(self, v, load=False):
    """
    Setter method for timebase, mapped from YANG variable /rbridge_id/maps/rule/timebase (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timebase is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timebase() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {}, u'day': {}, u'hour': {}, u'min': {}},), is_leaf=True, yang_name="timebase", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timebase must be of a type compatible with enumeration""",
          'defined-type': "brocade-maps:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {}, u'day': {}, u'hour': {}, u'min': {}},), is_leaf=True, yang_name="timebase", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)""",
        })

    self.__timebase = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timebase(self):
    self.__timebase = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'none': {}, u'day': {}, u'hour': {}, u'min': {}},), is_leaf=True, yang_name="timebase", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)


  def _get_op(self):
    """
    Getter method for op, mapped from YANG variable /rbridge_id/maps/rule/op (enumeration)
    """
    return self.__op
      
  def _set_op(self, v, load=False):
    """
    Setter method for op, mapped from YANG variable /rbridge_id/maps/rule/op (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_op is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_op() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'le': {}, u'lt': {}, u'gt': {}, u'eq': {}, u'ge': {}},), is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """op must be of a type compatible with enumeration""",
          'defined-type': "brocade-maps:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'le': {}, u'lt': {}, u'gt': {}, u'eq': {}, u'ge': {}},), is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)""",
        })

    self.__op = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_op(self):
    self.__op = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'le': {}, u'lt': {}, u'gt': {}, u'eq': {}, u'ge': {}},), is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='enumeration', is_config=True)


  def _get_threshold(self):
    """
    Getter method for threshold, mapped from YANG variable /rbridge_id/maps/rule/threshold (string)
    """
    return self.__threshold
      
  def _set_threshold(self, v, load=False):
    """
    Setter method for threshold, mapped from YANG variable /rbridge_id/maps/rule/threshold (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="threshold", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'threshold value', u'alt-name': u'value'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """threshold must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="threshold", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'threshold value', u'alt-name': u'value'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)""",
        })

    self.__threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_threshold(self):
    self.__threshold = YANGDynClass(base=unicode, is_leaf=True, yang_name="threshold", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'threshold value', u'alt-name': u'value'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)

  rulename = __builtin__.property(_get_rulename, _set_rulename)
  targetgroup = __builtin__.property(_get_targetgroup, _set_targetgroup)
  monitor = __builtin__.property(_get_monitor, _set_monitor)
  timebase = __builtin__.property(_get_timebase, _set_timebase)
  op = __builtin__.property(_get_op, _set_op)
  threshold = __builtin__.property(_get_threshold, _set_threshold)


  _pyangbind_elements = {'rulename': rulename, 'targetgroup': targetgroup, 'monitor': monitor, 'timebase': timebase, 'op': op, 'threshold': threshold, }


