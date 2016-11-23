
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface
import message
import module
class raslog(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /logging/raslog. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface','__message','__module','__console',)

  _yang_name = 'raslog'
  _rest_name = 'raslog'

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
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog interface message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__message = YANGDynClass(base=message.message, is_container='container', yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message configurations', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__console = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="console", rest_name="console", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RASLOG console severity: <CRITICAL|ERROR|WARNING|INFO>', u'cli-full-command': None, u'callpoint': u'RASGlobalConfigCallPoint', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='raslog-console', is_config=True)
    self.__module = YANGDynClass(base=module.module, is_container='container', yang_name="module", rest_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RAS module configurations', u'hidden': u'debug', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)

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
      return [u'logging', u'raslog']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logging', u'raslog']

  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /logging/raslog/interface (container)
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /logging/raslog/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.
    """
    try:
      t = YANGDynClass(v,base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog interface message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog interface message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure raslog interface message'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_message(self):
    """
    Getter method for message, mapped from YANG variable /logging/raslog/message (container)
    """
    return self.__message
      
  def _set_message(self, v, load=False):
    """
    Setter method for message, mapped from YANG variable /logging/raslog/message (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message() directly.
    """
    try:
      t = YANGDynClass(v,base=message.message, is_container='container', yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message configurations', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=message.message, is_container='container', yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message configurations', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message(self):
    self.__message = YANGDynClass(base=message.message, is_container='container', yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message configurations', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_module(self):
    """
    Getter method for module, mapped from YANG variable /logging/raslog/module (container)
    """
    return self.__module
      
  def _set_module(self, v, load=False):
    """
    Setter method for module, mapped from YANG variable /logging/raslog/module (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_module is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_module() directly.
    """
    try:
      t = YANGDynClass(v,base=module.module, is_container='container', yang_name="module", rest_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RAS module configurations', u'hidden': u'debug', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """module must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=module.module, is_container='container', yang_name="module", rest_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RAS module configurations', u'hidden': u'debug', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__module = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_module(self):
    self.__module = YANGDynClass(base=module.module, is_container='container', yang_name="module", rest_name="module", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RAS module configurations', u'hidden': u'debug', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_console(self):
    """
    Getter method for console, mapped from YANG variable /logging/raslog/console (raslog-console)
    """
    return self.__console
      
  def _set_console(self, v, load=False):
    """
    Setter method for console, mapped from YANG variable /logging/raslog/console (raslog-console)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_console is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_console() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="console", rest_name="console", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RASLOG console severity: <CRITICAL|ERROR|WARNING|INFO>', u'cli-full-command': None, u'callpoint': u'RASGlobalConfigCallPoint', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='raslog-console', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """console must be of a type compatible with raslog-console""",
          'defined-type': "brocade-ras:raslog-console",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="console", rest_name="console", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RASLOG console severity: <CRITICAL|ERROR|WARNING|INFO>', u'cli-full-command': None, u'callpoint': u'RASGlobalConfigCallPoint', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='raslog-console', is_config=True)""",
        })

    self.__console = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_console(self):
    self.__console = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'INFO': {'value': 1}, u'CRITICAL': {'value': 4}, u'WARNING': {'value': 3}, u'ERROR': {'value': 2}},), is_leaf=True, yang_name="console", rest_name="console", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure RASLOG console severity: <CRITICAL|ERROR|WARNING|INFO>', u'cli-full-command': None, u'callpoint': u'RASGlobalConfigCallPoint', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='raslog-console', is_config=True)

  interface = __builtin__.property(_get_interface, _set_interface)
  message = __builtin__.property(_get_message, _set_message)
  module = __builtin__.property(_get_module, _set_module)
  console = __builtin__.property(_get_console, _set_console)


  _pyangbind_elements = {'interface': interface, 'message': message, 'module': module, 'console': console, }


