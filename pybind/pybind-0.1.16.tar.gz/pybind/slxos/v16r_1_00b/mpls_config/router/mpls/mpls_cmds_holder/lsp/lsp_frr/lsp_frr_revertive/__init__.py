
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class lsp_frr_revertive(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/lsp/lsp-frr/lsp-frr-revertive. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lsp_frr_revertive_holdtime','__lsp_frr_revertive_mode_global',)

  _yang_name = 'lsp-frr-revertive'
  _rest_name = 'revertive'

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
    self.__lsp_frr_revertive_mode_global = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="lsp-frr-revertive-mode-global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global revertive mode', u'cli-full-no': None, u'alt-name': u'global'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)
    self.__lsp_frr_revertive_holdtime = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="lsp-frr-revertive-holdtime", rest_name="holdtime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure revertive hold time for the LSP', u'cli-full-no': None, u'alt-name': u'holdtime'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'lsp', u'lsp-frr', u'lsp-frr-revertive']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'lsp', u'frr', u'revertive']

  def _get_lsp_frr_revertive_holdtime(self):
    """
    Getter method for lsp_frr_revertive_holdtime, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_revertive/lsp_frr_revertive_holdtime (uint8)
    """
    return self.__lsp_frr_revertive_holdtime
      
  def _set_lsp_frr_revertive_holdtime(self, v, load=False):
    """
    Setter method for lsp_frr_revertive_holdtime, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_revertive/lsp_frr_revertive_holdtime (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_revertive_holdtime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_revertive_holdtime() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="lsp-frr-revertive-holdtime", rest_name="holdtime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure revertive hold time for the LSP', u'cli-full-no': None, u'alt-name': u'holdtime'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_revertive_holdtime must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="lsp-frr-revertive-holdtime", rest_name="holdtime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure revertive hold time for the LSP', u'cli-full-no': None, u'alt-name': u'holdtime'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)""",
        })

    self.__lsp_frr_revertive_holdtime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_revertive_holdtime(self):
    self.__lsp_frr_revertive_holdtime = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="lsp-frr-revertive-holdtime", rest_name="holdtime", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure revertive hold time for the LSP', u'cli-full-no': None, u'alt-name': u'holdtime'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint8', is_config=True)


  def _get_lsp_frr_revertive_mode_global(self):
    """
    Getter method for lsp_frr_revertive_mode_global, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_revertive/lsp_frr_revertive_mode_global (enable-disable)
    """
    return self.__lsp_frr_revertive_mode_global
      
  def _set_lsp_frr_revertive_mode_global(self, v, load=False):
    """
    Setter method for lsp_frr_revertive_mode_global, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/lsp/lsp_frr/lsp_frr_revertive/lsp_frr_revertive_mode_global (enable-disable)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lsp_frr_revertive_mode_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lsp_frr_revertive_mode_global() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="lsp-frr-revertive-mode-global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global revertive mode', u'cli-full-no': None, u'alt-name': u'global'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lsp_frr_revertive_mode_global must be of a type compatible with enable-disable""",
          'defined-type': "brocade-mpls:enable-disable",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="lsp-frr-revertive-mode-global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global revertive mode', u'cli-full-no': None, u'alt-name': u'global'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)""",
        })

    self.__lsp_frr_revertive_mode_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lsp_frr_revertive_mode_global(self):
    self.__lsp_frr_revertive_mode_global = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="lsp-frr-revertive-mode-global", rest_name="global", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable global revertive mode', u'cli-full-no': None, u'alt-name': u'global'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)

  lsp_frr_revertive_holdtime = __builtin__.property(_get_lsp_frr_revertive_holdtime, _set_lsp_frr_revertive_holdtime)
  lsp_frr_revertive_mode_global = __builtin__.property(_get_lsp_frr_revertive_mode_global, _set_lsp_frr_revertive_mode_global)


  _pyangbind_elements = {'lsp_frr_revertive_holdtime': lsp_frr_revertive_holdtime, 'lsp_frr_revertive_mode_global': lsp_frr_revertive_mode_global, }


