
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class isns_primary_role(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isns-ext - based on the path /brocade_isns_ext_rpc/isns-get-server-role/output/isns-primary-role. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This is a list consisting of Rbridge-Id and server role stating 
whether it is a primary or secondary server. Key used here is Rbridge-Id
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__isns_rb_id','__isns_role',)

  _yang_name = 'isns-primary-role'
  _rest_name = 'isns-primary-role'

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
    self.__isns_rb_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isns-rb-id", rest_name="isns-rb-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='uint32', is_config=True)
    self.__isns_role = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,11}', 'length': [u'1..11']}), is_leaf=True, yang_name="isns-role", rest_name="isns-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-server-role-type', is_config=True)

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
      return [u'brocade_isns_ext_rpc', u'isns-get-server-role', u'output', u'isns-primary-role']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isns-get-server-role', u'output', u'isns-primary-role']

  def _get_isns_rb_id(self):
    """
    Getter method for isns_rb_id, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_server_role/output/isns_primary_role/isns_rb_id (uint32)

    YANG Description: This node indicates the rb-id.
    """
    return self.__isns_rb_id
      
  def _set_isns_rb_id(self, v, load=False):
    """
    Setter method for isns_rb_id, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_server_role/output/isns_primary_role/isns_rb_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_rb_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_rb_id() directly.

    YANG Description: This node indicates the rb-id.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isns-rb-id", rest_name="isns-rb-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_rb_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isns-rb-id", rest_name="isns-rb-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='uint32', is_config=True)""",
        })

    self.__isns_rb_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_rb_id(self):
    self.__isns_rb_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="isns-rb-id", rest_name="isns-rb-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='uint32', is_config=True)


  def _get_isns_role(self):
    """
    Getter method for isns_role, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_server_role/output/isns_primary_role/isns_role (isns-server-role-type)

    YANG Description: This node inidicates if it is a primary or secondary.
    """
    return self.__isns_role
      
  def _set_isns_role(self, v, load=False):
    """
    Setter method for isns_role, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_server_role/output/isns_primary_role/isns_role (isns-server-role-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_role is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_role() directly.

    YANG Description: This node inidicates if it is a primary or secondary.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,11}', 'length': [u'1..11']}), is_leaf=True, yang_name="isns-role", rest_name="isns-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-server-role-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_role must be of a type compatible with isns-server-role-type""",
          'defined-type': "brocade-isns-ext:isns-server-role-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,11}', 'length': [u'1..11']}), is_leaf=True, yang_name="isns-role", rest_name="isns-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-server-role-type', is_config=True)""",
        })

    self.__isns_role = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_role(self):
    self.__isns_role = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-.:0-9a-zA-Z]{1,11}', 'length': [u'1..11']}), is_leaf=True, yang_name="isns-role", rest_name="isns-role", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns-server-role-type', is_config=True)

  isns_rb_id = __builtin__.property(_get_isns_rb_id, _set_isns_rb_id)
  isns_role = __builtin__.property(_get_isns_role, _set_isns_role)


  _pyangbind_elements = {'isns_rb_id': isns_rb_id, 'isns_role': isns_role, }


