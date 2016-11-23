
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import counter
import timeout
import nport_menu
import pg
class ag(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ag. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__enable','__counter','__timeout','__nport_menu','__pg',)

  _yang_name = 'ag'
  _rest_name = 'ag'

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
    self.__nport_menu = YANGDynClass(base=nport_menu.nport_menu, is_container='container', yang_name="nport-menu", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set N_Port properties.', u'alt-name': u'nport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable AG mode', u'cli-show-no': None, u'callpoint': u'ag_enable_callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='empty', is_config=True)
    self.__pg = YANGDynClass(base=YANGListType("pgid",pg.pg, yang_name="pg", rest_name="pg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pgid', extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}), is_container='list', yang_name="pg", rest_name="pg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='list', is_config=True)
    self.__timeout = YANGDynClass(base=timeout.timeout, is_container='container', yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Fabric Name Monitoring tov'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    self.__counter = YANGDynClass(base=counter.counter, is_container='container', yang_name="counter", rest_name="counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Reliability counter value'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'ag']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ag']

  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /rbridge_id/ag/enable (empty)
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /rbridge_id/ag/enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable AG mode', u'cli-show-no': None, u'callpoint': u'ag_enable_callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable AG mode', u'cli-show-no': None, u'callpoint': u'ag_enable_callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='empty', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable AG mode', u'cli-show-no': None, u'callpoint': u'ag_enable_callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='empty', is_config=True)


  def _get_counter(self):
    """
    Getter method for counter, mapped from YANG variable /rbridge_id/ag/counter (container)
    """
    return self.__counter
      
  def _set_counter(self, v, load=False):
    """
    Setter method for counter, mapped from YANG variable /rbridge_id/ag/counter (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counter() directly.
    """
    try:
      t = YANGDynClass(v,base=counter.counter, is_container='container', yang_name="counter", rest_name="counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Reliability counter value'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """counter must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=counter.counter, is_container='container', yang_name="counter", rest_name="counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Reliability counter value'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)""",
        })

    self.__counter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_counter(self):
    self.__counter = YANGDynClass(base=counter.counter, is_container='container', yang_name="counter", rest_name="counter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Reliability counter value'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)


  def _get_timeout(self):
    """
    Getter method for timeout, mapped from YANG variable /rbridge_id/ag/timeout (container)
    """
    return self.__timeout
      
  def _set_timeout(self, v, load=False):
    """
    Setter method for timeout, mapped from YANG variable /rbridge_id/ag/timeout (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout() directly.
    """
    try:
      t = YANGDynClass(v,base=timeout.timeout, is_container='container', yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Fabric Name Monitoring tov'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=timeout.timeout, is_container='container', yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Fabric Name Monitoring tov'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)""",
        })

    self.__timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout(self):
    self.__timeout = YANGDynClass(base=timeout.timeout, is_container='container', yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Fabric Name Monitoring tov'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)


  def _get_nport_menu(self):
    """
    Getter method for nport_menu, mapped from YANG variable /rbridge_id/ag/nport_menu (container)
    """
    return self.__nport_menu
      
  def _set_nport_menu(self, v, load=False):
    """
    Setter method for nport_menu, mapped from YANG variable /rbridge_id/ag/nport_menu (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nport_menu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nport_menu() directly.
    """
    try:
      t = YANGDynClass(v,base=nport_menu.nport_menu, is_container='container', yang_name="nport-menu", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set N_Port properties.', u'alt-name': u'nport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nport_menu must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=nport_menu.nport_menu, is_container='container', yang_name="nport-menu", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set N_Port properties.', u'alt-name': u'nport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)""",
        })

    self.__nport_menu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nport_menu(self):
    self.__nport_menu = YANGDynClass(base=nport_menu.nport_menu, is_container='container', yang_name="nport-menu", rest_name="nport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set N_Port properties.', u'alt-name': u'nport'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='container', is_config=True)


  def _get_pg(self):
    """
    Getter method for pg, mapped from YANG variable /rbridge_id/ag/pg (list)
    """
    return self.__pg
      
  def _set_pg(self, v, load=False):
    """
    Setter method for pg, mapped from YANG variable /rbridge_id/ag/pg (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pg() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("pgid",pg.pg, yang_name="pg", rest_name="pg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pgid', extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}), is_container='list', yang_name="pg", rest_name="pg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pg must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("pgid",pg.pg, yang_name="pg", rest_name="pg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pgid', extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}), is_container='list', yang_name="pg", rest_name="pg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='list', is_config=True)""",
        })

    self.__pg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pg(self):
    self.__pg = YANGDynClass(base=YANGListType("pgid",pg.pg, yang_name="pg", rest_name="pg", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='pgid', extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}), is_container='list', yang_name="pg", rest_name="pg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Creates a new port group.', u'cli-full-command': None, u'callpoint': u'pg_callpoint', u'cli-mode-name': u'config-rbridge-id-ag-pg-$(pgid)'}}, namespace='urn:brocade.com:mgmt:brocade-ag', defining_module='brocade-ag', yang_type='list', is_config=True)

  enable = __builtin__.property(_get_enable, _set_enable)
  counter = __builtin__.property(_get_counter, _set_counter)
  timeout = __builtin__.property(_get_timeout, _set_timeout)
  nport_menu = __builtin__.property(_get_nport_menu, _set_nport_menu)
  pg = __builtin__.property(_get_pg, _set_pg)


  _pyangbind_elements = {'enable': enable, 'counter': counter, 'timeout': timeout, 'nport_menu': nport_menu, 'pg': pg, }


