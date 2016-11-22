
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fcoe_fabric_map
import fcoe_map
class fcoe(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe - based on the path /fcoe. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This provides the grouping of all FCoE map configuration
elements.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcoe_fabric_map','__fcoe_map',)

  _yang_name = 'fcoe'
  _rest_name = 'fcoe'

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
    self.__fcoe_map = YANGDynClass(base=YANGListType("fcoe_map_name",fcoe_map.fcoe_map, yang_name="fcoe-map", rest_name="fcoe-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}), is_container='list', yang_name="fcoe-map", rest_name="fcoe-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)
    self.__fcoe_fabric_map = YANGDynClass(base=YANGListType("fcoe_fabric_map_name",fcoe_fabric_map.fcoe_fabric_map, yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-fabric-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}), is_container='list', yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)

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
      return [u'fcoe']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'fcoe']

  def _get_fcoe_fabric_map(self):
    """
    Getter method for fcoe_fabric_map, mapped from YANG variable /fcoe/fcoe_fabric_map (list)

    YANG Description: List of FCoE fabric map parameters.
    """
    return self.__fcoe_fabric_map
      
  def _set_fcoe_fabric_map(self, v, load=False):
    """
    Setter method for fcoe_fabric_map, mapped from YANG variable /fcoe/fcoe_fabric_map (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_fabric_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_fabric_map() directly.

    YANG Description: List of FCoE fabric map parameters.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("fcoe_fabric_map_name",fcoe_fabric_map.fcoe_fabric_map, yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-fabric-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}), is_container='list', yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_fabric_map must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("fcoe_fabric_map_name",fcoe_fabric_map.fcoe_fabric_map, yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-fabric-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}), is_container='list', yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)""",
        })

    self.__fcoe_fabric_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_fabric_map(self):
    self.__fcoe_fabric_map = YANGDynClass(base=YANGListType("fcoe_fabric_map_name",fcoe_fabric_map.fcoe_fabric_map, yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-fabric-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}), is_container='list', yang_name="fcoe-fabric-map", rest_name="fabric-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Fabric-map parameters', u'cli-no-key-completion': None, u'alt-name': u'fabric-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'callpoint': u'fcoe_fabric_map_cp', u'cli-mode-name': u'config-fcoe-fabric-map-$(fcoe-fabric-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)


  def _get_fcoe_map(self):
    """
    Getter method for fcoe_map, mapped from YANG variable /fcoe/fcoe_map (list)

    YANG Description: The list of FCoE maps.Each row contains the FCoE map
name and the list of FCoE fabric maps and CEE maps.
    """
    return self.__fcoe_map
      
  def _set_fcoe_map(self, v, load=False):
    """
    Setter method for fcoe_map, mapped from YANG variable /fcoe/fcoe_map (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_map() directly.

    YANG Description: The list of FCoE maps.Each row contains the FCoE map
name and the list of FCoE fabric maps and CEE maps.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("fcoe_map_name",fcoe_map.fcoe_map, yang_name="fcoe-map", rest_name="fcoe-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}), is_container='list', yang_name="fcoe-map", rest_name="fcoe-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_map must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("fcoe_map_name",fcoe_map.fcoe_map, yang_name="fcoe-map", rest_name="fcoe-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}), is_container='list', yang_name="fcoe-map", rest_name="fcoe-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)""",
        })

    self.__fcoe_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_map(self):
    self.__fcoe_map = YANGDynClass(base=YANGListType("fcoe_map_name",fcoe_map.fcoe_map, yang_name="fcoe-map", rest_name="fcoe-map", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='fcoe-map-name', extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}), is_container='list', yang_name="fcoe-map", rest_name="fcoe-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure an FCoE Map', u'alt-name': u'fcoe-map', u'cli-suppress-list-no': None, u'cli-full-command': None, u'hidden': u'debug', u'callpoint': u'fcoe_map_cp', u'cli-mode-name': u'config-fcoe-map-$(fcoe-map-name)'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='list', is_config=True)

  fcoe_fabric_map = __builtin__.property(_get_fcoe_fabric_map, _set_fcoe_fabric_map)
  fcoe_map = __builtin__.property(_get_fcoe_map, _set_fcoe_map)


  _pyangbind_elements = {'fcoe_fabric_map': fcoe_fabric_map, 'fcoe_map': fcoe_map, }


