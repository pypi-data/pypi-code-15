
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import isis_router_entry
class host_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/host-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The set of IS-IS Host names and Router ID
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hostname_enabled','__isis_router_entry',)

  _yang_name = 'host-table'
  _rest_name = 'host-table'

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
    self.__isis_router_entry = YANGDynClass(base=YANGListType("system_id",isis_router_entry.isis_router_entry, yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='system-id', extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    self.__hostname_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hostname-enabled", rest_name="hostname-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)

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
      return [u'isis-state', u'host-table']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'host-table']

  def _get_hostname_enabled(self):
    """
    Getter method for hostname_enabled, mapped from YANG variable /isis_state/host_table/hostname_enabled (boolean)

    YANG Description: If IS-IS Dynamic Host Name Mapping enabled
    """
    return self.__hostname_enabled
      
  def _set_hostname_enabled(self, v, load=False):
    """
    Setter method for hostname_enabled, mapped from YANG variable /isis_state/host_table/hostname_enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostname_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostname_enabled() directly.

    YANG Description: If IS-IS Dynamic Host Name Mapping enabled
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="hostname-enabled", rest_name="hostname-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostname_enabled must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hostname-enabled", rest_name="hostname-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)""",
        })

    self.__hostname_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostname_enabled(self):
    self.__hostname_enabled = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="hostname-enabled", rest_name="hostname-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='boolean', is_config=False)


  def _get_isis_router_entry(self):
    """
    Getter method for isis_router_entry, mapped from YANG variable /isis_state/host_table/isis_router_entry (list)

    YANG Description: Each entry tracks information about one Intermediate System at one level
    """
    return self.__isis_router_entry
      
  def _set_isis_router_entry(self, v, load=False):
    """
    Setter method for isis_router_entry, mapped from YANG variable /isis_state/host_table/isis_router_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isis_router_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isis_router_entry() directly.

    YANG Description: Each entry tracks information about one Intermediate System at one level
    """
    try:
      t = YANGDynClass(v,base=YANGListType("system_id",isis_router_entry.isis_router_entry, yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='system-id', extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isis_router_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("system_id",isis_router_entry.isis_router_entry, yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='system-id', extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)""",
        })

    self.__isis_router_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isis_router_entry(self):
    self.__isis_router_entry = YANGDynClass(base=YANGListType("system_id",isis_router_entry.isis_router_entry, yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='system-id', extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}), is_container='list', yang_name="isis-router-entry", rest_name="isis-router-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-router-entry', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

  hostname_enabled = __builtin__.property(_get_hostname_enabled)
  isis_router_entry = __builtin__.property(_get_isis_router_entry)


  _pyangbind_elements = {'hostname_enabled': hostname_enabled, 'isis_router_entry': isis_router_entry, }


