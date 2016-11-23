
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class hide_vrrp_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/protocol/hide-vrrp-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrrp','__vrrp_extended',)

  _yang_name = 'hide-vrrp-holder'
  _rest_name = ''

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
    self.__vrrp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp", rest_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol (VRRP)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)
    self.__vrrp_extended = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-extended", rest_name="vrrp-extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol Extended (VRRP-E)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'protocol', u'hide-vrrp-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol']

  def _get_vrrp(self):
    """
    Getter method for vrrp, mapped from YANG variable /routing_system/protocol/hide_vrrp_holder/vrrp (empty)

    YANG Description: Virtual Router Redundacy Protocol (VRRP)
    """
    return self.__vrrp
      
  def _set_vrrp(self, v, load=False):
    """
    Setter method for vrrp, mapped from YANG variable /routing_system/protocol/hide_vrrp_holder/vrrp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrrp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrrp() directly.

    YANG Description: Virtual Router Redundacy Protocol (VRRP)
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vrrp", rest_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol (VRRP)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrrp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp", rest_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol (VRRP)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)""",
        })

    self.__vrrp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrrp(self):
    self.__vrrp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp", rest_name="vrrp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol (VRRP)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)


  def _get_vrrp_extended(self):
    """
    Getter method for vrrp_extended, mapped from YANG variable /routing_system/protocol/hide_vrrp_holder/vrrp_extended (empty)

    YANG Description: Virtual Router Redundacy Protocol Extended (VRRP-E)
    """
    return self.__vrrp_extended
      
  def _set_vrrp_extended(self, v, load=False):
    """
    Setter method for vrrp_extended, mapped from YANG variable /routing_system/protocol/hide_vrrp_holder/vrrp_extended (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrrp_extended is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrrp_extended() directly.

    YANG Description: Virtual Router Redundacy Protocol Extended (VRRP-E)
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vrrp-extended", rest_name="vrrp-extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol Extended (VRRP-E)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrrp_extended must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-extended", rest_name="vrrp-extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol Extended (VRRP-E)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)""",
        })

    self.__vrrp_extended = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrrp_extended(self):
    self.__vrrp_extended = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-extended", rest_name="vrrp-extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Virtual Router Redundacy Protocol Extended (VRRP-E)', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrp', defining_module='brocade-vrrp', yang_type='empty', is_config=True)

  vrrp = __builtin__.property(_get_vrrp, _set_vrrp)
  vrrp_extended = __builtin__.property(_get_vrrp_extended, _set_vrrp_extended)


  _pyangbind_elements = {'vrrp': vrrp, 'vrrp_extended': vrrp_extended, }


