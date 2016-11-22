
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import connection_addr
class nsx_controller(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /nsx-controller. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__name','__connection_addr','__reconnect_interval','__activate',)

  _yang_name = 'nsx-controller'
  _rest_name = 'nsx-controller'

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
    self.__connection_addr = YANGDynClass(base=connection_addr.connection_addr, is_container='container', yang_name="connection-addr", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address, port and connection method configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    self.__reconnect_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="reconnect-interval", rest_name="reconnect-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reconnect interval'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the connection'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='nvp-controller-name-type', is_config=True)

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
      return [u'nsx-controller']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'nsx-controller']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /nsx_controller/name (nvp-controller-name-type)

    YANG Description: NSX controller name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /nsx_controller/name (nvp-controller-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: NSX controller name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='nvp-controller-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with nvp-controller-name-type""",
          'defined-type': "brocade-tunnels:nvp-controller-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='nvp-controller-name-type', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_a-zA-Z0-9]{1,32}'}), is_leaf=True, yang_name="name", rest_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='nvp-controller-name-type', is_config=True)


  def _get_connection_addr(self):
    """
    Getter method for connection_addr, mapped from YANG variable /nsx_controller/connection_addr (container)

    YANG Description: Connection method, IP address and port information
    """
    return self.__connection_addr
      
  def _set_connection_addr(self, v, load=False):
    """
    Setter method for connection_addr, mapped from YANG variable /nsx_controller/connection_addr (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_connection_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_connection_addr() directly.

    YANG Description: Connection method, IP address and port information
    """
    try:
      t = YANGDynClass(v,base=connection_addr.connection_addr, is_container='container', yang_name="connection-addr", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address, port and connection method configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """connection_addr must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=connection_addr.connection_addr, is_container='container', yang_name="connection-addr", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address, port and connection method configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)""",
        })

    self.__connection_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_connection_addr(self):
    self.__connection_addr = YANGDynClass(base=connection_addr.connection_addr, is_container='container', yang_name="connection-addr", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'info': u'IP address, port and connection method configuration', u'cli-sequence-commands': None, u'alt-name': u'ip', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='container', is_config=True)


  def _get_reconnect_interval(self):
    """
    Getter method for reconnect_interval, mapped from YANG variable /nsx_controller/reconnect_interval (uint32)

    YANG Description: Configures the re-connect interval for the NSX
controller connection. If the connection to NSX is
broken for some reason, re-connections will be attempted
at this rate. Default value is 10 seconds.
    """
    return self.__reconnect_interval
      
  def _set_reconnect_interval(self, v, load=False):
    """
    Setter method for reconnect_interval, mapped from YANG variable /nsx_controller/reconnect_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reconnect_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reconnect_interval() directly.

    YANG Description: Configures the re-connect interval for the NSX
controller connection. If the connection to NSX is
broken for some reason, re-connections will be attempted
at this rate. Default value is 10 seconds.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="reconnect-interval", rest_name="reconnect-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reconnect interval'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reconnect_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="reconnect-interval", rest_name="reconnect-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reconnect interval'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)""",
        })

    self.__reconnect_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reconnect_interval(self):
    self.__reconnect_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..1000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(10), is_leaf=True, yang_name="reconnect-interval", rest_name="reconnect-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reconnect interval'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='uint32', is_config=True)


  def _get_activate(self):
    """
    Getter method for activate, mapped from YANG variable /nsx_controller/activate (empty)

    YANG Description: Activate the connection to NSX controller. At least the
IP address must have been configured before activating
the connection.
    """
    return self.__activate
      
  def _set_activate(self, v, load=False):
    """
    Setter method for activate, mapped from YANG variable /nsx_controller/activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_activate() directly.

    YANG Description: Activate the connection to NSX controller. At least the
IP address must have been configured before activating
the connection.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the connection'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the connection'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)""",
        })

    self.__activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_activate(self):
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Activate the connection'}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='empty', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  connection_addr = __builtin__.property(_get_connection_addr, _set_connection_addr)
  reconnect_interval = __builtin__.property(_get_reconnect_interval, _set_reconnect_interval)
  activate = __builtin__.property(_get_activate, _set_activate)


  _pyangbind_elements = {'name': name, 'connection_addr': connection_addr, 'reconnect_interval': reconnect_interval, 'activate': activate, }


