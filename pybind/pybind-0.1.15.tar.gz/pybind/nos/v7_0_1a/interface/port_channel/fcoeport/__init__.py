
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fcoeport(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/fcoeport. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcoeport_map','__ns_ip_registration',)

  _yang_name = 'fcoeport'
  _rest_name = 'fcoeport'

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
    self.__fcoeport_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="fcoeport-map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'map'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-map-name-type', is_config=True)
    self.__ns_ip_registration = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ns-ip-registration", rest_name="ns-ip-registration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)

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
      return [u'interface', u'port-channel', u'fcoeport']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'fcoeport']

  def _get_fcoeport_map(self):
    """
    Getter method for fcoeport_map, mapped from YANG variable /interface/port_channel/fcoeport/fcoeport_map (fcoe-map-name-type)
    """
    return self.__fcoeport_map
      
  def _set_fcoeport_map(self, v, load=False):
    """
    Setter method for fcoeport_map, mapped from YANG variable /interface/port_channel/fcoeport/fcoeport_map (fcoe-map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoeport_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoeport_map() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="fcoeport-map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'map'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoeport_map must be of a type compatible with fcoe-map-name-type""",
          'defined-type': "brocade-fcoe:fcoe-map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="fcoeport-map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'map'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-map-name-type', is_config=True)""",
        })

    self.__fcoeport_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoeport_map(self):
    self.__fcoeport_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..32']}), is_leaf=True, yang_name="fcoeport-map", rest_name="map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'map'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='fcoe-map-name-type', is_config=True)


  def _get_ns_ip_registration(self):
    """
    Getter method for ns_ip_registration, mapped from YANG variable /interface/port_channel/fcoeport/ns_ip_registration (empty)

    YANG Description:  To Enable or disable the NPIV regitration.
    """
    return self.__ns_ip_registration
      
  def _set_ns_ip_registration(self, v, load=False):
    """
    Setter method for ns_ip_registration, mapped from YANG variable /interface/port_channel/fcoeport/ns_ip_registration (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ns_ip_registration is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ns_ip_registration() directly.

    YANG Description:  To Enable or disable the NPIV regitration.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ns-ip-registration", rest_name="ns-ip-registration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ns_ip_registration must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ns-ip-registration", rest_name="ns-ip-registration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)""",
        })

    self.__ns_ip_registration = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ns_ip_registration(self):
    self.__ns_ip_registration = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ns-ip-registration", rest_name="ns-ip-registration", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-optional-in-sequence': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)

  fcoeport_map = __builtin__.property(_get_fcoeport_map, _set_fcoeport_map)
  ns_ip_registration = __builtin__.property(_get_ns_ip_registration, _set_ns_ip_registration)


  _pyangbind_elements = {'fcoeport_map': fcoeport_map, 'ns_ip_registration': ns_ip_registration, }


