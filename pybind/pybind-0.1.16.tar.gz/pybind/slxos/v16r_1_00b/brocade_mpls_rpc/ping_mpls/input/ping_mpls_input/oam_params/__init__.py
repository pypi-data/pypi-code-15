
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class oam_params(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/ping-mpls/input/ping-mpls-input/oam-params. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__destination','__reply_mode','__reply_tos','__size','__source','__timeout',)

  _yang_name = 'oam-params'
  _rest_name = 'oam-params'

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
    self.__reply_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'router-alert': {}},), is_leaf=True, yang_name="reply-mode", rest_name="reply-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    self.__reply_tos = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reply-tos", rest_name="reply-tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="size", rest_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'ping-mpls', u'input', u'ping-mpls-input', u'oam-params']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ping-mpls', u'input', u'ping-mpls-input', u'oam-params']

  def _get_destination(self):
    """
    Getter method for destination, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/destination (mpls-ipv4-address)

    YANG Description: destination
    """
    return self.__destination
      
  def _set_destination(self, v, load=False):
    """
    Setter method for destination, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/destination (mpls-ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_destination is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_destination() directly.

    YANG Description: destination
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """destination must be of a type compatible with mpls-ipv4-address""",
          'defined-type': "brocade-mpls:mpls-ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)""",
        })

    self.__destination = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_destination(self):
    self.__destination = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="destination", rest_name="destination", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)


  def _get_reply_mode(self):
    """
    Getter method for reply_mode, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/reply_mode (enumeration)

    YANG Description: reply-mode
    """
    return self.__reply_mode
      
  def _set_reply_mode(self, v, load=False):
    """
    Setter method for reply_mode, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/reply_mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reply_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reply_mode() directly.

    YANG Description: reply-mode
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'router-alert': {}},), is_leaf=True, yang_name="reply-mode", rest_name="reply-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reply_mode must be of a type compatible with enumeration""",
          'defined-type': "brocade-mpls:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'router-alert': {}},), is_leaf=True, yang_name="reply-mode", rest_name="reply-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)""",
        })

    self.__reply_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reply_mode(self):
    self.__reply_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'router-alert': {}},), is_leaf=True, yang_name="reply-mode", rest_name="reply-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enumeration', is_config=True)


  def _get_reply_tos(self):
    """
    Getter method for reply_tos, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/reply_tos (uint8)

    YANG Description: reply-tos
    """
    return self.__reply_tos
      
  def _set_reply_tos(self, v, load=False):
    """
    Setter method for reply_tos, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/reply_tos (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reply_tos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reply_tos() directly.

    YANG Description: reply-tos
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reply-tos", rest_name="reply-tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reply_tos must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reply-tos", rest_name="reply-tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__reply_tos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reply_tos(self):
    self.__reply_tos = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="reply-tos", rest_name="reply-tos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_size(self):
    """
    Getter method for size, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/size (uint32)

    YANG Description: size
    """
    return self.__size
      
  def _set_size(self, v, load=False):
    """
    Setter method for size, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_size() directly.

    YANG Description: size
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="size", rest_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="size", rest_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_size(self):
    self.__size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="size", rest_name="size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_source(self):
    """
    Getter method for source, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/source (mpls-ipv4-address)

    YANG Description: source
    """
    return self.__source
      
  def _set_source(self, v, load=False):
    """
    Setter method for source, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/source (mpls-ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_source is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_source() directly.

    YANG Description: source
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """source must be of a type compatible with mpls-ipv4-address""",
          'defined-type': "brocade-mpls:mpls-ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)""",
        })

    self.__source = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_source(self):
    self.__source = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="source", rest_name="source", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='mpls-ipv4-address', is_config=True)


  def _get_timeout(self):
    """
    Getter method for timeout, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/timeout (uint32)

    YANG Description: timeout
    """
    return self.__timeout
      
  def _set_timeout(self, v, load=False):
    """
    Setter method for timeout, mapped from YANG variable /brocade_mpls_rpc/ping_mpls/input/ping_mpls_input/oam_params/timeout (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout() directly.

    YANG Description: timeout
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout(self):
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  destination = __builtin__.property(_get_destination, _set_destination)
  reply_mode = __builtin__.property(_get_reply_mode, _set_reply_mode)
  reply_tos = __builtin__.property(_get_reply_tos, _set_reply_tos)
  size = __builtin__.property(_get_size, _set_size)
  source = __builtin__.property(_get_source, _set_source)
  timeout = __builtin__.property(_get_timeout, _set_timeout)


  _pyangbind_elements = {'destination': destination, 'reply_mode': reply_mode, 'reply_tos': reply_tos, 'size': size, 'source': source, 'timeout': timeout, }


