
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class authentication_key(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ntp - based on the path /ntp/authentication-key. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__keyid','__md5','__sha1','__encryption_level',)

  _yang_name = 'authentication-key'
  _rest_name = 'authentication-key'

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
    self.__encryption_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the md5 key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='enumeration', is_config=True)
    self.__sha1 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="sha1", rest_name="sha1", parent=self, choice=(u'encryption-type', u'sha1-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SHA1 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)
    self.__keyid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="keyid", rest_name="keyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='uint32', is_config=True)
    self.__md5 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="md5", rest_name="md5", parent=self, choice=(u'encryption-type', u'md5-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)

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
      return [u'ntp', u'authentication-key']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ntp', u'authentication-key']

  def _get_keyid(self):
    """
    Getter method for keyid, mapped from YANG variable /ntp/authentication_key/keyid (uint32)
    """
    return self.__keyid
      
  def _set_keyid(self, v, load=False):
    """
    Setter method for keyid, mapped from YANG variable /ntp/authentication_key/keyid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_keyid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_keyid() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="keyid", rest_name="keyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """keyid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="keyid", rest_name="keyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='uint32', is_config=True)""",
        })

    self.__keyid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_keyid(self):
    self.__keyid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="keyid", rest_name="keyid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='uint32', is_config=True)


  def _get_md5(self):
    """
    Getter method for md5, mapped from YANG variable /ntp/authentication_key/md5 (string)
    """
    return self.__md5
      
  def _set_md5(self, v, load=False):
    """
    Setter method for md5, mapped from YANG variable /ntp/authentication_key/md5 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_md5 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_md5() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="md5", rest_name="md5", parent=self, choice=(u'encryption-type', u'md5-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """md5 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="md5", rest_name="md5", parent=self, choice=(u'encryption-type', u'md5-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)""",
        })

    self.__md5 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_md5(self):
    self.__md5 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="md5", rest_name="md5", parent=self, choice=(u'encryption-type', u'md5-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'MD5 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)


  def _get_sha1(self):
    """
    Getter method for sha1, mapped from YANG variable /ntp/authentication_key/sha1 (string)
    """
    return self.__sha1
      
  def _set_sha1(self, v, load=False):
    """
    Setter method for sha1, mapped from YANG variable /ntp/authentication_key/sha1 (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sha1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sha1() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="sha1", rest_name="sha1", parent=self, choice=(u'encryption-type', u'sha1-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SHA1 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sha1 must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="sha1", rest_name="sha1", parent=self, choice=(u'encryption-type', u'sha1-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SHA1 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)""",
        })

    self.__sha1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sha1(self):
    self.__sha1 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="sha1", rest_name="sha1", parent=self, choice=(u'encryption-type', u'sha1-type'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SHA1 Encryption'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='string', is_config=True)


  def _get_encryption_level(self):
    """
    Getter method for encryption_level, mapped from YANG variable /ntp/authentication_key/encryption_level (enumeration)
    """
    return self.__encryption_level
      
  def _set_encryption_level(self, v, load=False):
    """
    Setter method for encryption_level, mapped from YANG variable /ntp/authentication_key/encryption_level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encryption_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encryption_level() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the md5 key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encryption_level must be of a type compatible with enumeration""",
          'defined-type': "brocade-ntp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the md5 key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='enumeration', is_config=True)""",
        })

    self.__encryption_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encryption_level(self):
    self.__encryption_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the md5 key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-ntp', defining_module='brocade-ntp', yang_type='enumeration', is_config=True)

  keyid = __builtin__.property(_get_keyid, _set_keyid)
  md5 = __builtin__.property(_get_md5, _set_md5)
  sha1 = __builtin__.property(_get_sha1, _set_sha1)
  encryption_level = __builtin__.property(_get_encryption_level, _set_encryption_level)

  __choices__ = {u'encryption-type': {u'md5-type': [u'md5'], u'sha1-type': [u'sha1']}}
  _pyangbind_elements = {'keyid': keyid, 'md5': md5, 'sha1': sha1, 'encryption_level': encryption_level, }


