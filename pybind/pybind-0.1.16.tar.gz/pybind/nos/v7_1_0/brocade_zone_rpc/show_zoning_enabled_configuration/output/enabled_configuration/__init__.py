
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import enabled_zone
class enabled_configuration(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-zone - based on the path /brocade_zone_rpc/show-zoning-enabled-configuration/output/enabled-configuration. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cfg_name','__enabled_zone','__has_more',)

  _yang_name = 'enabled-configuration'
  _rest_name = 'enabled-configuration'

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
    self.__cfg_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="cfg-name", rest_name="cfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'<WORD>;;Enabled-CFG-Name'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)
    self.__enabled_zone = YANGDynClass(base=YANGListType("zone_name",enabled_zone.enabled_zone, yang_name="enabled-zone", rest_name="enabled-zone", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='zone-name', extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}), is_container='list', yang_name="enabled-zone", rest_name="enabled-zone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='boolean', is_config=True)

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
      return [u'brocade_zone_rpc', u'show-zoning-enabled-configuration', u'output', u'enabled-configuration']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-zoning-enabled-configuration', u'output', u'enabled-configuration']

  def _get_cfg_name(self):
    """
    Getter method for cfg_name, mapped from YANG variable /brocade_zone_rpc/show_zoning_enabled_configuration/output/enabled_configuration/cfg_name (string)
    """
    return self.__cfg_name
      
  def _set_cfg_name(self, v, load=False):
    """
    Setter method for cfg_name, mapped from YANG variable /brocade_zone_rpc/show_zoning_enabled_configuration/output/enabled_configuration/cfg_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cfg_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cfg_name() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cfg-name", rest_name="cfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'<WORD>;;Enabled-CFG-Name'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cfg_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cfg-name", rest_name="cfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'<WORD>;;Enabled-CFG-Name'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)""",
        })

    self.__cfg_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cfg_name(self):
    self.__cfg_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="cfg-name", rest_name="cfg-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'<WORD>;;Enabled-CFG-Name'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)


  def _get_enabled_zone(self):
    """
    Getter method for enabled_zone, mapped from YANG variable /brocade_zone_rpc/show_zoning_enabled_configuration/output/enabled_configuration/enabled_zone (list)
    """
    return self.__enabled_zone
      
  def _set_enabled_zone(self, v, load=False):
    """
    Setter method for enabled_zone, mapped from YANG variable /brocade_zone_rpc/show_zoning_enabled_configuration/output/enabled_configuration/enabled_zone (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled_zone is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled_zone() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("zone_name",enabled_zone.enabled_zone, yang_name="enabled-zone", rest_name="enabled-zone", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='zone-name', extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}), is_container='list', yang_name="enabled-zone", rest_name="enabled-zone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enabled_zone must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("zone_name",enabled_zone.enabled_zone, yang_name="enabled-zone", rest_name="enabled-zone", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='zone-name', extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}), is_container='list', yang_name="enabled-zone", rest_name="enabled-zone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)""",
        })

    self.__enabled_zone = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enabled_zone(self):
    self.__enabled_zone = YANGDynClass(base=YANGListType("zone_name",enabled_zone.enabled_zone, yang_name="enabled-zone", rest_name="enabled-zone", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='zone-name', extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}), is_container='list', yang_name="enabled-zone", rest_name="enabled-zone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'List of enabled Zones'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)


  def _get_has_more(self):
    """
    Getter method for has_more, mapped from YANG variable /brocade_zone_rpc/show_zoning_enabled_configuration/output/enabled_configuration/has_more (boolean)

    YANG Description: Informs whether backend has more
zoning output that is not part of 
the current response. Based on this
flag remaining enabled-zones can be 
fetched with another request
    """
    return self.__has_more
      
  def _set_has_more(self, v, load=False):
    """
    Setter method for has_more, mapped from YANG variable /brocade_zone_rpc/show_zoning_enabled_configuration/output/enabled_configuration/has_more (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_has_more is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_has_more() directly.

    YANG Description: Informs whether backend has more
zoning output that is not part of 
the current response. Based on this
flag remaining enabled-zones can be 
fetched with another request
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """has_more must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='boolean', is_config=True)""",
        })

    self.__has_more = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_has_more(self):
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='boolean', is_config=True)

  cfg_name = __builtin__.property(_get_cfg_name, _set_cfg_name)
  enabled_zone = __builtin__.property(_get_enabled_zone, _set_enabled_zone)
  has_more = __builtin__.property(_get_has_more, _set_has_more)


  _pyangbind_elements = {'cfg_name': cfg_name, 'enabled_zone': enabled_zone, 'has_more': has_more, }


