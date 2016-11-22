
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class auth_key(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/router-isis-attributes/auth-key. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__auth_key_level1_str','__auth_key_level2_str',)

  _yang_name = 'auth-key'
  _rest_name = 'auth-key'

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
    self.__auth_key_level1_str = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level1-str", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-1 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)
    self.__auth_key_level2_str = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level2-str", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-2 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'router-isis-attributes', u'auth-key']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'auth-key']

  def _get_auth_key_level1_str(self):
    """
    Getter method for auth_key_level1_str, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_key/auth_key_level1_str (string)

    YANG Description: Auth-key for Level-1 ISIS Router
    """
    return self.__auth_key_level1_str
      
  def _set_auth_key_level1_str(self, v, load=False):
    """
    Setter method for auth_key_level1_str, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_key/auth_key_level1_str (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_key_level1_str is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_key_level1_str() directly.

    YANG Description: Auth-key for Level-1 ISIS Router
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level1-str", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-1 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_key_level1_str must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level1-str", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-1 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)""",
        })

    self.__auth_key_level1_str = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_key_level1_str(self):
    self.__auth_key_level1_str = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level1-str", rest_name="level-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-1 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-1'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)


  def _get_auth_key_level2_str(self):
    """
    Getter method for auth_key_level2_str, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_key/auth_key_level2_str (string)

    YANG Description: Auth-key for Level-2 ISIS Router
    """
    return self.__auth_key_level2_str
      
  def _set_auth_key_level2_str(self, v, load=False):
    """
    Setter method for auth_key_level2_str, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/router_isis_attributes/auth_key/auth_key_level2_str (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_key_level2_str is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_key_level2_str() directly.

    YANG Description: Auth-key for Level-2 ISIS Router
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level2-str", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-2 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_key_level2_str must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level2-str", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-2 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)""",
        })

    self.__auth_key_level2_str = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_key_level2_str(self):
    self.__auth_key_level2_str = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="auth-key-level2-str", rest_name="level-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Auth-key for Level-2 ISIS Router', u'cli-full-no': None, u'alt-name': u'level-2'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='string', is_config=True)

  auth_key_level1_str = __builtin__.property(_get_auth_key_level1_str, _set_auth_key_level1_str)
  auth_key_level2_str = __builtin__.property(_get_auth_key_level2_str, _set_auth_key_level2_str)


  _pyangbind_elements = {'auth_key_level1_str': auth_key_level1_str, 'auth_key_level2_str': auth_key_level2_str, }


