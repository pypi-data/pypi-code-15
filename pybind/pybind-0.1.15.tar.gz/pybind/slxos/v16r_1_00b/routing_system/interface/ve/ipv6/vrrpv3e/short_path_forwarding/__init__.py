
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class short_path_forwarding(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/vrrpv3e/short-path-forwarding. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Enable backup router to send traffic
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__basic','__revert_priority',)

  _yang_name = 'short-path-forwarding'
  _rest_name = 'short-path-forwarding'

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
    self.__revert_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="revert-priority", rest_name="revert-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set revert priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)
    self.__basic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'vrrpv3e', u'short-path-forwarding']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'vrrp-extended-group', u'short-path-forwarding']

  def _get_basic(self):
    """
    Getter method for basic, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/short_path_forwarding/basic (empty)
    """
    return self.__basic
      
  def _set_basic(self, v, load=False):
    """
    Setter method for basic, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/short_path_forwarding/basic (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_basic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_basic() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """basic must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)""",
        })

    self.__basic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_basic(self):
    self.__basic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="basic", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)


  def _get_revert_priority(self):
    """
    Getter method for revert_priority, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/short_path_forwarding/revert_priority (uint8)

    YANG Description: Set revert priority
    """
    return self.__revert_priority
      
  def _set_revert_priority(self, v, load=False):
    """
    Setter method for revert_priority, mapped from YANG variable /routing_system/interface/ve/ipv6/vrrpv3e/short_path_forwarding/revert_priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_revert_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_revert_priority() directly.

    YANG Description: Set revert priority
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="revert-priority", rest_name="revert-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set revert priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """revert_priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="revert-priority", rest_name="revert-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set revert priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)""",
        })

    self.__revert_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_revert_priority(self):
    self.__revert_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="revert-priority", rest_name="revert-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set revert priority'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)

  basic = __builtin__.property(_get_basic, _set_basic)
  revert_priority = __builtin__.property(_get_revert_priority, _set_revert_priority)


  _pyangbind_elements = {'basic': basic, 'revert_priority': revert_priority, }


