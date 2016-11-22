
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ethernet(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge-lag - based on the path /load-balance-lag/load-balance/hash/ethernet. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__sa_mac','__da_mac','__vlan','__etype',)

  _yang_name = 'ethernet'
  _rest_name = 'ethernet'

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
    self.__etype = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="etype", rest_name="etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'etype', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet etype\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__vlan = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet vlan\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__sa_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sa-mac", rest_name="sa-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'sa-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet sa-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    self.__da_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="da-mac", rest_name="da-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'da-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet da-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

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
      return [u'load-balance-lag', u'load-balance', u'hash', u'ethernet']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'load-balance', u'hash', u'ethernet']

  def _get_sa_mac(self):
    """
    Getter method for sa_mac, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/sa_mac (empty)
    """
    return self.__sa_mac
      
  def _set_sa_mac(self, v, load=False):
    """
    Setter method for sa_mac, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/sa_mac (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sa_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sa_mac() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="sa-mac", rest_name="sa-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'sa-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet sa-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sa_mac must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sa-mac", rest_name="sa-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'sa-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet sa-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__sa_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sa_mac(self):
    self.__sa_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="sa-mac", rest_name="sa-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'sa-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet sa-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_da_mac(self):
    """
    Getter method for da_mac, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/da_mac (empty)
    """
    return self.__da_mac
      
  def _set_da_mac(self, v, load=False):
    """
    Setter method for da_mac, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/da_mac (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_da_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_da_mac() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="da-mac", rest_name="da-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'da-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet da-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """da_mac must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="da-mac", rest_name="da-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'da-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet da-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__da_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_da_mac(self):
    self.__da_mac = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="da-mac", rest_name="da-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'da-mac', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet da-mac\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/vlan (empty)
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/vlan (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet vlan\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet vlan\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'vlan', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet vlan\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)


  def _get_etype(self):
    """
    Getter method for etype, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/etype (empty)
    """
    return self.__etype
      
  def _set_etype(self, v, load=False):
    """
    Setter method for etype, mapped from YANG variable /load_balance_lag/load_balance/hash/ethernet/etype (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_etype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_etype() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="etype", rest_name="etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'etype', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet etype\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """etype must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="etype", rest_name="etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'etype', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet etype\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)""",
        })

    self.__etype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_etype(self):
    self.__etype = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="etype", rest_name="etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'etype', u'cli-full-command': None, u'cli-run-template': u'$(.?:no load-balance hash ethernet etype\n)'}}, namespace='urn:brocade.com:mgmt:brocade-rbridge-lag', defining_module='brocade-rbridge-lag', yang_type='empty', is_config=True)

  sa_mac = __builtin__.property(_get_sa_mac, _set_sa_mac)
  da_mac = __builtin__.property(_get_da_mac, _set_da_mac)
  vlan = __builtin__.property(_get_vlan, _set_vlan)
  etype = __builtin__.property(_get_etype, _set_etype)


  _pyangbind_elements = {'sa_mac': sa_mac, 'da_mac': da_mac, 'vlan': vlan, 'etype': etype, }


