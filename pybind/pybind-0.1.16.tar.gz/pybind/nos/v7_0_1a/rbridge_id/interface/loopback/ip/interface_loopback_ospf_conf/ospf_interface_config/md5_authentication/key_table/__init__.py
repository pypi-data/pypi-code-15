
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class key_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/loopback/ip/interface-loopback-ospf-conf/ospf-interface-config/md5-authentication/key-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__key_id','__key','__md5_authentication_key',)

  _yang_name = 'key-table'
  _rest_name = 'key-id'

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
    self.__key_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="key-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The key ID of the MD5 key', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    self.__key = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa': {'value': 0}, u'ecdsa': {'value': 2}, u'dsa': {'value': 1}},), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Authentication password (key)', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)
    self.__md5_authentication_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="md5-authentication-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'MD5 authentication ID'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)

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
      return [u'rbridge-id', u'interface', u'loopback', u'ip', u'interface-loopback-ospf-conf', u'ospf-interface-config', u'md5-authentication', u'key-table']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Loopback', u'ip', u'ospf', u'md5-authentication', u'key-id']

  def _get_key_id(self):
    """
    Getter method for key_id, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config/md5_authentication/key_table/key_id (uint32)
    """
    return self.__key_id
      
  def _set_key_id(self, v, load=False):
    """
    Setter method for key_id, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config/md5_authentication/key_table/key_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_id() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="key-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The key ID of the MD5 key', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="key-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The key ID of the MD5 key', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)""",
        })

    self.__key_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_id(self):
    self.__key_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="key-id", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The key ID of the MD5 key', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='uint32', is_config=True)


  def _get_key(self):
    """
    Getter method for key, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config/md5_authentication/key_table/key (key-type)

    YANG Description: MD5 Authentication password (key)
    """
    return self.__key
      
  def _set_key(self, v, load=False):
    """
    Setter method for key, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config/md5_authentication/key_table/key (key-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key() directly.

    YANG Description: MD5 Authentication password (key)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa': {'value': 0}, u'ecdsa': {'value': 2}, u'dsa': {'value': 1}},), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Authentication password (key)', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key must be of a type compatible with key-type""",
          'defined-type': "brocade-ospf:key-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa': {'value': 0}, u'ecdsa': {'value': 2}, u'dsa': {'value': 1}},), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Authentication password (key)', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)""",
        })

    self.__key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key(self):
    self.__key = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rsa': {'value': 0}, u'ecdsa': {'value': 2}, u'dsa': {'value': 1}},), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Authentication password (key)', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)


  def _get_md5_authentication_key(self):
    """
    Getter method for md5_authentication_key, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config/md5_authentication/key_table/md5_authentication_key (ospf-auth-psswd-string)
    """
    return self.__md5_authentication_key
      
  def _set_md5_authentication_key(self, v, load=False):
    """
    Setter method for md5_authentication_key, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config/md5_authentication/key_table/md5_authentication_key (ospf-auth-psswd-string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_md5_authentication_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_md5_authentication_key() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="md5-authentication-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'MD5 authentication ID'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """md5_authentication_key must be of a type compatible with ospf-auth-psswd-string""",
          'defined-type': "brocade-ospf:ospf-auth-psswd-string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="md5-authentication-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'MD5 authentication ID'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)""",
        })

    self.__md5_authentication_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_md5_authentication_key(self):
    self.__md5_authentication_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="md5-authentication-key", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'MD5 authentication ID'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)

  key_id = __builtin__.property(_get_key_id, _set_key_id)
  key = __builtin__.property(_get_key, _set_key)
  md5_authentication_key = __builtin__.property(_get_md5_authentication_key, _set_md5_authentication_key)


  _pyangbind_elements = {'key_id': key_id, 'key': key, 'md5_authentication_key': md5_authentication_key, }


