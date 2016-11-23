
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class node_active_server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ntp - based on the path /brocade_ntp_rpc/show-ntp/output/node-active-server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id_out','__active_server','__LOCL',)

  _yang_name = 'node-active-server'
  _rest_name = 'node-active-server'

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
    self.__rbridge_id_out = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id-out", rest_name="rbridge-id-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='common-def:rbridge-id-type', is_config=True)
    self.__active_server = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="active-server", rest_name="active-server", parent=self, choice=(u'ip4-6-or-local', u'ipv4-6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='inet:ip-address', is_config=True)
    self.__LOCL = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="LOCL", rest_name="LOCL", parent=self, choice=(u'ip4-6-or-local', u'local'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='boolean', is_config=True)

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
      return [u'brocade_ntp_rpc', u'show-ntp', u'output', u'node-active-server']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-ntp', u'output', u'node-active-server']

  def _get_rbridge_id_out(self):
    """
    Getter method for rbridge_id_out, mapped from YANG variable /brocade_ntp_rpc/show_ntp/output/node_active_server/rbridge_id_out (common-def:rbridge-id-type)
    """
    return self.__rbridge_id_out
      
  def _set_rbridge_id_out(self, v, load=False):
    """
    Setter method for rbridge_id_out, mapped from YANG variable /brocade_ntp_rpc/show_ntp/output/node_active_server/rbridge_id_out (common-def:rbridge-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id_out() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id-out", rest_name="rbridge-id-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='common-def:rbridge-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id_out must be of a type compatible with common-def:rbridge-id-type""",
          'defined-type': "common-def:rbridge-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id-out", rest_name="rbridge-id-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='common-def:rbridge-id-type', is_config=True)""",
        })

    self.__rbridge_id_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id_out(self):
    self.__rbridge_id_out = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridge-id-out", rest_name="rbridge-id-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='common-def:rbridge-id-type', is_config=True)


  def _get_active_server(self):
    """
    Getter method for active_server, mapped from YANG variable /brocade_ntp_rpc/show_ntp/output/node_active_server/active_server (inet:ip-address)
    """
    return self.__active_server
      
  def _set_active_server(self, v, load=False):
    """
    Setter method for active_server, mapped from YANG variable /brocade_ntp_rpc/show_ntp/output/node_active_server/active_server (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_active_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_active_server() directly.
    """
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="active-server", rest_name="active-server", parent=self, choice=(u'ip4-6-or-local', u'ipv4-6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """active_server must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="active-server", rest_name="active-server", parent=self, choice=(u'ip4-6-or-local', u'ipv4-6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__active_server = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_active_server(self):
    self.__active_server = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="active-server", rest_name="active-server", parent=self, choice=(u'ip4-6-or-local', u'ipv4-6'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='inet:ip-address', is_config=True)


  def _get_LOCL(self):
    """
    Getter method for LOCL, mapped from YANG variable /brocade_ntp_rpc/show_ntp/output/node_active_server/LOCL (boolean)
    """
    return self.__LOCL
      
  def _set_LOCL(self, v, load=False):
    """
    Setter method for LOCL, mapped from YANG variable /brocade_ntp_rpc/show_ntp/output/node_active_server/LOCL (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_LOCL is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_LOCL() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="LOCL", rest_name="LOCL", parent=self, choice=(u'ip4-6-or-local', u'local'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """LOCL must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="LOCL", rest_name="LOCL", parent=self, choice=(u'ip4-6-or-local', u'local'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='boolean', is_config=True)""",
        })

    self.__LOCL = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_LOCL(self):
    self.__LOCL = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="LOCL", rest_name="LOCL", parent=self, choice=(u'ip4-6-or-local', u'local'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='boolean', is_config=True)

  rbridge_id_out = __builtin__.property(_get_rbridge_id_out, _set_rbridge_id_out)
  active_server = __builtin__.property(_get_active_server, _set_active_server)
  LOCL = __builtin__.property(_get_LOCL, _set_LOCL)

  __choices__ = {u'ip4-6-or-local': {u'ipv4-6': [u'active_server'], u'local': [u'LOCL']}}
  _pyangbind_elements = {'rbridge_id_out': rbridge_id_out, 'active_server': active_server, 'LOCL': LOCL, }


