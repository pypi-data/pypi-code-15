
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import hdr_start
import bos
import speculate_mpls
class hash(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag/lag/hash. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hdr_start','__bos','__hdr_count','__rotate','__normalize','__srcport','__pwctrlword','__speculate_mpls',)

  _yang_name = 'hash'
  _rest_name = 'hash'

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
    self.__normalize = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normalize", rest_name="normalize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable using the same hash in both directions of a flow', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__rotate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="rotate", rest_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Hash Rotate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)
    self.__bos = YANGDynClass(base=bos.bos, is_container='container', yang_name="bos", rest_name="bos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include/Exclude BOS label', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    self.__srcport = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="srcport", rest_name="srcport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude Source port', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__pwctrlword = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pwctrlword", rest_name="pwctrlword", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude PW control word in hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__hdr_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), is_leaf=True, yang_name="hdr-count", rest_name="hdr-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of headers to be considered for LAG hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)
    self.__hdr_start = YANGDynClass(base=hdr_start.hdr_start, is_container='container', yang_name="hdr-start", rest_name="hdr-start", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define where to start picking headers for the key generation', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    self.__speculate_mpls = YANGDynClass(base=speculate_mpls.speculate_mpls, is_container='container', yang_name="speculate-mpls", rest_name="speculate-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MPLS speculate or Ethernet/IP'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)

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
      return [u'load-balance-lag', u'lag', u'hash']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'lag', u'hash']

  def _get_hdr_start(self):
    """
    Getter method for hdr_start, mapped from YANG variable /load_balance_lag/lag/hash/hdr_start (container)
    """
    return self.__hdr_start
      
  def _set_hdr_start(self, v, load=False):
    """
    Setter method for hdr_start, mapped from YANG variable /load_balance_lag/lag/hash/hdr_start (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hdr_start is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hdr_start() directly.
    """
    try:
      t = YANGDynClass(v,base=hdr_start.hdr_start, is_container='container', yang_name="hdr-start", rest_name="hdr-start", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define where to start picking headers for the key generation', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hdr_start must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hdr_start.hdr_start, is_container='container', yang_name="hdr-start", rest_name="hdr-start", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define where to start picking headers for the key generation', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__hdr_start = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hdr_start(self):
    self.__hdr_start = YANGDynClass(base=hdr_start.hdr_start, is_container='container', yang_name="hdr-start", rest_name="hdr-start", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Define where to start picking headers for the key generation', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)


  def _get_bos(self):
    """
    Getter method for bos, mapped from YANG variable /load_balance_lag/lag/hash/bos (container)
    """
    return self.__bos
      
  def _set_bos(self, v, load=False):
    """
    Setter method for bos, mapped from YANG variable /load_balance_lag/lag/hash/bos (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bos() directly.
    """
    try:
      t = YANGDynClass(v,base=bos.bos, is_container='container', yang_name="bos", rest_name="bos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include/Exclude BOS label', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bos must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bos.bos, is_container='container', yang_name="bos", rest_name="bos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include/Exclude BOS label', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__bos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bos(self):
    self.__bos = YANGDynClass(base=bos.bos, is_container='container', yang_name="bos", rest_name="bos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Include/Exclude BOS label', u'cli-compact-syntax': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)


  def _get_hdr_count(self):
    """
    Getter method for hdr_count, mapped from YANG variable /load_balance_lag/lag/hash/hdr_count (uint32)
    """
    return self.__hdr_count
      
  def _set_hdr_count(self, v, load=False):
    """
    Setter method for hdr_count, mapped from YANG variable /load_balance_lag/lag/hash/hdr_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hdr_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hdr_count() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), is_leaf=True, yang_name="hdr-count", rest_name="hdr-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of headers to be considered for LAG hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hdr_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), is_leaf=True, yang_name="hdr-count", rest_name="hdr-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of headers to be considered for LAG hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)""",
        })

    self.__hdr_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hdr_count(self):
    self.__hdr_count = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3']}), is_leaf=True, yang_name="hdr-count", rest_name="hdr-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of headers to be considered for LAG hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)


  def _get_rotate(self):
    """
    Getter method for rotate, mapped from YANG variable /load_balance_lag/lag/hash/rotate (uint32)
    """
    return self.__rotate
      
  def _set_rotate(self, v, load=False):
    """
    Setter method for rotate, mapped from YANG variable /load_balance_lag/lag/hash/rotate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rotate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rotate() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="rotate", rest_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Hash Rotate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rotate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="rotate", rest_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Hash Rotate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)""",
        })

    self.__rotate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rotate(self):
    self.__rotate = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..15']}), is_leaf=True, yang_name="rotate", rest_name="rotate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Hash Rotate', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='uint32', is_config=True)


  def _get_normalize(self):
    """
    Getter method for normalize, mapped from YANG variable /load_balance_lag/lag/hash/normalize (empty)
    """
    return self.__normalize
      
  def _set_normalize(self, v, load=False):
    """
    Setter method for normalize, mapped from YANG variable /load_balance_lag/lag/hash/normalize (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_normalize is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_normalize() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="normalize", rest_name="normalize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable using the same hash in both directions of a flow', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """normalize must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normalize", rest_name="normalize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable using the same hash in both directions of a flow', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__normalize = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_normalize(self):
    self.__normalize = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="normalize", rest_name="normalize", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable/Disable using the same hash in both directions of a flow', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_srcport(self):
    """
    Getter method for srcport, mapped from YANG variable /load_balance_lag/lag/hash/srcport (empty)
    """
    return self.__srcport
      
  def _set_srcport(self, v, load=False):
    """
    Setter method for srcport, mapped from YANG variable /load_balance_lag/lag/hash/srcport (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_srcport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_srcport() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="srcport", rest_name="srcport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude Source port', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """srcport must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="srcport", rest_name="srcport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude Source port', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__srcport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_srcport(self):
    self.__srcport = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="srcport", rest_name="srcport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude Source port', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_pwctrlword(self):
    """
    Getter method for pwctrlword, mapped from YANG variable /load_balance_lag/lag/hash/pwctrlword (empty)
    """
    return self.__pwctrlword
      
  def _set_pwctrlword(self, v, load=False):
    """
    Setter method for pwctrlword, mapped from YANG variable /load_balance_lag/lag/hash/pwctrlword (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pwctrlword is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pwctrlword() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="pwctrlword", rest_name="pwctrlword", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude PW control word in hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pwctrlword must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pwctrlword", rest_name="pwctrlword", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude PW control word in hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__pwctrlword = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pwctrlword(self):
    self.__pwctrlword = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pwctrlword", rest_name="pwctrlword", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Include/Exclude PW control word in hashing', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_speculate_mpls(self):
    """
    Getter method for speculate_mpls, mapped from YANG variable /load_balance_lag/lag/hash/speculate_mpls (container)
    """
    return self.__speculate_mpls
      
  def _set_speculate_mpls(self, v, load=False):
    """
    Setter method for speculate_mpls, mapped from YANG variable /load_balance_lag/lag/hash/speculate_mpls (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_speculate_mpls is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_speculate_mpls() directly.
    """
    try:
      t = YANGDynClass(v,base=speculate_mpls.speculate_mpls, is_container='container', yang_name="speculate-mpls", rest_name="speculate-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MPLS speculate or Ethernet/IP'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """speculate_mpls must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=speculate_mpls.speculate_mpls, is_container='container', yang_name="speculate-mpls", rest_name="speculate-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MPLS speculate or Ethernet/IP'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)""",
        })

    self.__speculate_mpls = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_speculate_mpls(self):
    self.__speculate_mpls = YANGDynClass(base=speculate_mpls.speculate_mpls, is_container='container', yang_name="speculate-mpls", rest_name="speculate-mpls", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable MPLS speculate or Ethernet/IP'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='container', is_config=True)

  hdr_start = __builtin__.property(_get_hdr_start, _set_hdr_start)
  bos = __builtin__.property(_get_bos, _set_bos)
  hdr_count = __builtin__.property(_get_hdr_count, _set_hdr_count)
  rotate = __builtin__.property(_get_rotate, _set_rotate)
  normalize = __builtin__.property(_get_normalize, _set_normalize)
  srcport = __builtin__.property(_get_srcport, _set_srcport)
  pwctrlword = __builtin__.property(_get_pwctrlword, _set_pwctrlword)
  speculate_mpls = __builtin__.property(_get_speculate_mpls, _set_speculate_mpls)


  _pyangbind_elements = {'hdr_start': hdr_start, 'bos': bos, 'hdr_count': hdr_count, 'rotate': rotate, 'normalize': normalize, 'srcport': srcport, 'pwctrlword': pwctrlword, 'speculate_mpls': speculate_mpls, }


