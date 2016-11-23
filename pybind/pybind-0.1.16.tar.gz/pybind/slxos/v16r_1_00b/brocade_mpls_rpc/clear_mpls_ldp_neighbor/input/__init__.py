
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/clear-mpls-ldp-neighbor/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mpls_clear_all_ldp_sessions','__mpls_clear_one_ldp_sessions',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__mpls_clear_one_ldp_sessions = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-one-ldp-sessions", rest_name="mpls-clear-one-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__mpls_clear_all_ldp_sessions = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-clear-all-ldp-sessions", rest_name="mpls-clear-all-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

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
      return [u'brocade_mpls_rpc', u'clear-mpls-ldp-neighbor', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'clear-mpls-ldp-neighbor', u'input']

  def _get_mpls_clear_all_ldp_sessions(self):
    """
    Getter method for mpls_clear_all_ldp_sessions, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_ldp_neighbor/input/mpls_clear_all_ldp_sessions (empty)

    YANG Description:  Clear All LDP neighbors
    """
    return self.__mpls_clear_all_ldp_sessions
      
  def _set_mpls_clear_all_ldp_sessions(self, v, load=False):
    """
    Setter method for mpls_clear_all_ldp_sessions, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_ldp_neighbor/input/mpls_clear_all_ldp_sessions (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_all_ldp_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_all_ldp_sessions() directly.

    YANG Description:  Clear All LDP neighbors
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-clear-all-ldp-sessions", rest_name="mpls-clear-all-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_all_ldp_sessions must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-clear-all-ldp-sessions", rest_name="mpls-clear-all-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__mpls_clear_all_ldp_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_all_ldp_sessions(self):
    self.__mpls_clear_all_ldp_sessions = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-clear-all-ldp-sessions", rest_name="mpls-clear-all-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_mpls_clear_one_ldp_sessions(self):
    """
    Getter method for mpls_clear_one_ldp_sessions, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_ldp_neighbor/input/mpls_clear_one_ldp_sessions (inet:ipv4-address)

    YANG Description: LDP neighbors IP to be cleared
    """
    return self.__mpls_clear_one_ldp_sessions
      
  def _set_mpls_clear_one_ldp_sessions(self, v, load=False):
    """
    Setter method for mpls_clear_one_ldp_sessions, mapped from YANG variable /brocade_mpls_rpc/clear_mpls_ldp_neighbor/input/mpls_clear_one_ldp_sessions (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_clear_one_ldp_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_clear_one_ldp_sessions() directly.

    YANG Description: LDP neighbors IP to be cleared
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-one-ldp-sessions", rest_name="mpls-clear-one-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_clear_one_ldp_sessions must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-one-ldp-sessions", rest_name="mpls-clear-one-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__mpls_clear_one_ldp_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_clear_one_ldp_sessions(self):
    self.__mpls_clear_one_ldp_sessions = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="mpls-clear-one-ldp-sessions", rest_name="mpls-clear-one-ldp-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)

  mpls_clear_all_ldp_sessions = __builtin__.property(_get_mpls_clear_all_ldp_sessions, _set_mpls_clear_all_ldp_sessions)
  mpls_clear_one_ldp_sessions = __builtin__.property(_get_mpls_clear_one_ldp_sessions, _set_mpls_clear_one_ldp_sessions)


  _pyangbind_elements = {'mpls_clear_all_ldp_sessions': mpls_clear_all_ldp_sessions, 'mpls_clear_one_ldp_sessions': mpls_clear_one_ldp_sessions, }


