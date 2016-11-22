
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class route_target(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vrf - based on the path /vrf/route-target. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Target extended communities. This functionality is not supported
in NOS4.0.0 release
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__action','__target_community',)

  _yang_name = 'route-target'
  _rest_name = 'route-target'

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
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'import': {'value': 1}, u'export': {'value': 0}, u'both': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='enumeration', is_config=True)
    self.__target_community = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASN:nn;; Target VPN Extended Community'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rt-type', is_config=True)

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
      return [u'vrf', u'route-target']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vrf', u'route-target']

  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /vrf/route_target/action (enumeration)
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /vrf/route_target/action (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'import': {'value': 1}, u'export': {'value': 0}, u'both': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with enumeration""",
          'defined-type': "brocade-vrf:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'import': {'value': 1}, u'export': {'value': 0}, u'both': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='enumeration', is_config=True)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'import': {'value': 1}, u'export': {'value': 0}, u'both': {'value': 2}},), is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='enumeration', is_config=True)


  def _get_target_community(self):
    """
    Getter method for target_community, mapped from YANG variable /vrf/route_target/target_community (rt-type)

    YANG Description: Target VPN Extended Community
    """
    return self.__target_community
      
  def _set_target_community(self, v, load=False):
    """
    Setter method for target_community, mapped from YANG variable /vrf/route_target/target_community (rt-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_target_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_target_community() directly.

    YANG Description: Target VPN Extended Community
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASN:nn;; Target VPN Extended Community'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rt-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """target_community must be of a type compatible with rt-type""",
          'defined-type': "brocade-vrf:rt-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASN:nn;; Target VPN Extended Community'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rt-type', is_config=True)""",
        })

    self.__target_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_target_community(self):
    self.__target_community = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)'}), is_leaf=True, yang_name="target-community", rest_name="target-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASN:nn;; Target VPN Extended Community'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrf', defining_module='brocade-vrf', yang_type='rt-type', is_config=True)

  action = __builtin__.property(_get_action, _set_action)
  target_community = __builtin__.property(_get_target_community, _set_target_community)


  _pyangbind_elements = {'action': action, 'target_community': target_community, }


