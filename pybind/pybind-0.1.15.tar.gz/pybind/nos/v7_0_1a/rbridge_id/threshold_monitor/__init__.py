
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import sfp
import security
import Cpu
import Memory
import interface
class threshold_monitor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/threshold-monitor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sfp','__security','__Cpu','__Memory','__interface',)

  _yang_name = 'threshold-monitor'
  _rest_name = 'threshold-monitor'

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
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor Interface class', u'callpoint': u'interfaceconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    self.__security = YANGDynClass(base=security.security, is_container='container', yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor security class', u'callpoint': u'securityconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    self.__Cpu = YANGDynClass(base=Cpu.Cpu, is_container='container', yang_name="Cpu", rest_name="Cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:CPU', u'cli-compact-syntax': None, u'callpoint': u'CpuMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    self.__sfp = YANGDynClass(base=sfp.sfp, is_container='container', yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor SFP class', u'callpoint': u'sfpconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    self.__Memory = YANGDynClass(base=Memory.Memory, is_container='container', yang_name="Memory", rest_name="Memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:MEMORY', u'cli-compact-syntax': None, u'callpoint': u'MemoryMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'threshold-monitor']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'threshold-monitor']

  def _get_sfp(self):
    """
    Getter method for sfp, mapped from YANG variable /rbridge_id/threshold_monitor/sfp (container)
    """
    return self.__sfp
      
  def _set_sfp(self, v, load=False):
    """
    Setter method for sfp, mapped from YANG variable /rbridge_id/threshold_monitor/sfp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sfp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sfp() directly.
    """
    try:
      t = YANGDynClass(v,base=sfp.sfp, is_container='container', yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor SFP class', u'callpoint': u'sfpconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sfp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sfp.sfp, is_container='container', yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor SFP class', u'callpoint': u'sfpconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__sfp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sfp(self):
    self.__sfp = YANGDynClass(base=sfp.sfp, is_container='container', yang_name="sfp", rest_name="sfp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor SFP class', u'callpoint': u'sfpconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)


  def _get_security(self):
    """
    Getter method for security, mapped from YANG variable /rbridge_id/threshold_monitor/security (container)
    """
    return self.__security
      
  def _set_security(self, v, load=False):
    """
    Setter method for security, mapped from YANG variable /rbridge_id/threshold_monitor/security (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_security is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_security() directly.
    """
    try:
      t = YANGDynClass(v,base=security.security, is_container='container', yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor security class', u'callpoint': u'securityconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """security must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=security.security, is_container='container', yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor security class', u'callpoint': u'securityconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__security = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_security(self):
    self.__security = YANGDynClass(base=security.security, is_container='container', yang_name="security", rest_name="security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor security class', u'callpoint': u'securityconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)


  def _get_Cpu(self):
    """
    Getter method for Cpu, mapped from YANG variable /rbridge_id/threshold_monitor/Cpu (container)
    """
    return self.__Cpu
      
  def _set_Cpu(self, v, load=False):
    """
    Setter method for Cpu, mapped from YANG variable /rbridge_id/threshold_monitor/Cpu (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_Cpu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_Cpu() directly.
    """
    try:
      t = YANGDynClass(v,base=Cpu.Cpu, is_container='container', yang_name="Cpu", rest_name="Cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:CPU', u'cli-compact-syntax': None, u'callpoint': u'CpuMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """Cpu must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=Cpu.Cpu, is_container='container', yang_name="Cpu", rest_name="Cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:CPU', u'cli-compact-syntax': None, u'callpoint': u'CpuMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__Cpu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_Cpu(self):
    self.__Cpu = YANGDynClass(base=Cpu.Cpu, is_container='container', yang_name="Cpu", rest_name="Cpu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:CPU', u'cli-compact-syntax': None, u'callpoint': u'CpuMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)


  def _get_Memory(self):
    """
    Getter method for Memory, mapped from YANG variable /rbridge_id/threshold_monitor/Memory (container)
    """
    return self.__Memory
      
  def _set_Memory(self, v, load=False):
    """
    Setter method for Memory, mapped from YANG variable /rbridge_id/threshold_monitor/Memory (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_Memory is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_Memory() directly.
    """
    try:
      t = YANGDynClass(v,base=Memory.Memory, is_container='container', yang_name="Memory", rest_name="Memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:MEMORY', u'cli-compact-syntax': None, u'callpoint': u'MemoryMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """Memory must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=Memory.Memory, is_container='container', yang_name="Memory", rest_name="Memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:MEMORY', u'cli-compact-syntax': None, u'callpoint': u'MemoryMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__Memory = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_Memory(self):
    self.__Memory = YANGDynClass(base=Memory.Memory, is_container='container', yang_name="Memory", rest_name="Memory", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure settings for component:MEMORY', u'cli-compact-syntax': None, u'callpoint': u'MemoryMonitor', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /rbridge_id/threshold_monitor/interface (container)
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /rbridge_id/threshold_monitor/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.
    """
    try:
      t = YANGDynClass(v,base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor Interface class', u'callpoint': u'interfaceconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor Interface class', u'callpoint': u'interfaceconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Monitor Interface class', u'callpoint': u'interfaceconfiguration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-threshold-monitor', defining_module='brocade-threshold-monitor', yang_type='container', is_config=True)

  sfp = __builtin__.property(_get_sfp, _set_sfp)
  security = __builtin__.property(_get_security, _set_security)
  Cpu = __builtin__.property(_get_Cpu, _set_Cpu)
  Memory = __builtin__.property(_get_Memory, _set_Memory)
  interface = __builtin__.property(_get_interface, _set_interface)


  _pyangbind_elements = {'sfp': sfp, 'security': security, 'Cpu': Cpu, 'Memory': Memory, 'interface': interface, }


