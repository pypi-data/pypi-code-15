
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_attributes
class static_route_oif(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ipv6/route/static-route-oif. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__static_route_dest','__static_route_oif_type','__static_route_oif_name','__route_attributes',)

  _yang_name = 'static-route-oif'
  _rest_name = ''

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
    self.__route_attributes = YANGDynClass(base=route_attributes.route_attributes, is_container='container', yang_name="route-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    self.__static_route_oif_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="static-route-oif-type", rest_name="static-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)
    self.__static_route_oif_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="static-route-oif-name", rest_name="InterfaceNumber", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'InterfaceNumber'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)
    self.__static_route_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-dest", rest_name="static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)

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
      return [u'ipv6', u'route', u'static-route-oif']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'route']

  def _get_static_route_dest(self):
    """
    Getter method for static_route_dest, mapped from YANG variable /ipv6/route/static_route_oif/static_route_dest (inet:ipv6-prefix)
    """
    return self.__static_route_dest
      
  def _set_static_route_dest(self, v, load=False):
    """
    Setter method for static_route_dest, mapped from YANG variable /ipv6/route/static_route_oif/static_route_dest (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_dest is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_dest() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-dest", rest_name="static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_dest must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-dest", rest_name="static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__static_route_dest = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_dest(self):
    self.__static_route_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="static-route-dest", rest_name="static-route-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D/LEN ;; Destination IPv6 Prefix'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-prefix', is_config=True)


  def _get_static_route_oif_type(self):
    """
    Getter method for static_route_oif_type, mapped from YANG variable /ipv6/route/static_route_oif/static_route_oif_type (enumeration)
    """
    return self.__static_route_oif_type
      
  def _set_static_route_oif_type(self, v, load=False):
    """
    Setter method for static_route_oif_type, mapped from YANG variable /ipv6/route/static_route_oif/static_route_oif_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_oif_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_oif_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="static-route-oif-type", rest_name="static-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_oif_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-ipv6-rtm:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="static-route-oif-type", rest_name="static-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)""",
        })

    self.__static_route_oif_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_oif_type(self):
    self.__static_route_oif_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'ethernet': {'value': 1}, u'null': {'value': 5}, u've': {'value': 4}},), is_leaf=True, yang_name="static-route-oif-type", rest_name="static-route-oif-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)


  def _get_static_route_oif_name(self):
    """
    Getter method for static_route_oif_name, mapped from YANG variable /ipv6/route/static_route_oif/static_route_oif_name (string)
    """
    return self.__static_route_oif_name
      
  def _set_static_route_oif_name(self, v, load=False):
    """
    Setter method for static_route_oif_name, mapped from YANG variable /ipv6/route/static_route_oif/static_route_oif_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_static_route_oif_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_static_route_oif_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="static-route-oif-name", rest_name="InterfaceNumber", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'InterfaceNumber'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """static_route_oif_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="static-route-oif-name", rest_name="InterfaceNumber", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'InterfaceNumber'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)""",
        })

    self.__static_route_oif_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_static_route_oif_name(self):
    self.__static_route_oif_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="static-route-oif-name", rest_name="InterfaceNumber", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'InterfaceNumber'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)


  def _get_route_attributes(self):
    """
    Getter method for route_attributes, mapped from YANG variable /ipv6/route/static_route_oif/route_attributes (container)
    """
    return self.__route_attributes
      
  def _set_route_attributes(self, v, load=False):
    """
    Setter method for route_attributes, mapped from YANG variable /ipv6/route/static_route_oif/route_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_attributes() directly.
    """
    try:
      t = YANGDynClass(v,base=route_attributes.route_attributes, is_container='container', yang_name="route-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_attributes.route_attributes, is_container='container', yang_name="route-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)""",
        })

    self.__route_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_attributes(self):
    self.__route_attributes = YANGDynClass(base=route_attributes.route_attributes, is_container='container', yang_name="route-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)

  static_route_dest = __builtin__.property(_get_static_route_dest, _set_static_route_dest)
  static_route_oif_type = __builtin__.property(_get_static_route_oif_type, _set_static_route_oif_type)
  static_route_oif_name = __builtin__.property(_get_static_route_oif_name, _set_static_route_oif_name)
  route_attributes = __builtin__.property(_get_route_attributes, _set_route_attributes)


  _pyangbind_elements = {'static_route_dest': static_route_dest, 'static_route_oif_type': static_route_oif_type, 'static_route_oif_name': static_route_oif_name, 'route_attributes': route_attributes, }


