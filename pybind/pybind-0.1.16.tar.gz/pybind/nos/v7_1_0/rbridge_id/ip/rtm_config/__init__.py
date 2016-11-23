
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route
class rtm_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ip/rtm-config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__router_id','__load_sharing','__route',)

  _yang_name = 'rtm-config'
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
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", rest_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Change the router ID already in use'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='inet:ipv4-address', is_config=True)
    self.__load_sharing = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="load-sharing", rest_name="load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable IP load sharing'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='uint32', is_config=True)
    self.__route = YANGDynClass(base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure static route', u'callpoint': u'rtm-config', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'ip', u'rtm-config']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ip']

  def _get_router_id(self):
    """
    Getter method for router_id, mapped from YANG variable /rbridge_id/ip/rtm_config/router_id (inet:ipv4-address)
    """
    return self.__router_id
      
  def _set_router_id(self, v, load=False):
    """
    Setter method for router_id, mapped from YANG variable /rbridge_id/ip/rtm_config/router_id (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_router_id() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", rest_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Change the router ID already in use'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """router_id must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", rest_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Change the router ID already in use'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_router_id(self):
    self.__router_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="router-id", rest_name="router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Change the router ID already in use'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='inet:ipv4-address', is_config=True)


  def _get_load_sharing(self):
    """
    Getter method for load_sharing, mapped from YANG variable /rbridge_id/ip/rtm_config/load_sharing (uint32)
    """
    return self.__load_sharing
      
  def _set_load_sharing(self, v, load=False):
    """
    Setter method for load_sharing, mapped from YANG variable /rbridge_id/ip/rtm_config/load_sharing (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_sharing is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_sharing() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="load-sharing", rest_name="load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable IP load sharing'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_sharing must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="load-sharing", rest_name="load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable IP load sharing'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='uint32', is_config=True)""",
        })

    self.__load_sharing = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_sharing(self):
    self.__load_sharing = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..32']}), is_leaf=True, yang_name="load-sharing", rest_name="load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable IP load sharing'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='uint32', is_config=True)


  def _get_route(self):
    """
    Getter method for route, mapped from YANG variable /rbridge_id/ip/rtm_config/route (container)
    """
    return self.__route
      
  def _set_route(self, v, load=False):
    """
    Setter method for route, mapped from YANG variable /rbridge_id/ip/rtm_config/route (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route() directly.
    """
    try:
      t = YANGDynClass(v,base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure static route', u'callpoint': u'rtm-config', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure static route', u'callpoint': u'rtm-config', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)""",
        })

    self.__route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route(self):
    self.__route = YANGDynClass(base=route.route, is_container='container', yang_name="route", rest_name="route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure static route', u'callpoint': u'rtm-config', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)

  router_id = __builtin__.property(_get_router_id, _set_router_id)
  load_sharing = __builtin__.property(_get_load_sharing, _set_load_sharing)
  route = __builtin__.property(_get_route, _set_route)


  _pyangbind_elements = {'router_id': router_id, 'load_sharing': load_sharing, 'route': route, }


