
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rt(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/route-map/content/set/extcommunity/rt. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Route Target extended community
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ASN_NN_rt',)

  _yang_name = 'rt'
  _rest_name = 'rt'

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
    self.__ASN_NN_rt = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])):(([0-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)(( (additive))?)'}), is_leaf=True, yang_name="ASN-NN-rt", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ext-community-rt-expr-t', is_config=True)

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
      return [u'routing-system', u'route-map', u'content', u'set', u'extcommunity', u'rt']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'set', u'extcommunity', u'rt']

  def _get_ASN_NN_rt(self):
    """
    Getter method for ASN_NN_rt, mapped from YANG variable /routing_system/route_map/content/set/extcommunity/rt/ASN_NN_rt (ext-community-rt-expr-t)
    """
    return self.__ASN_NN_rt
      
  def _set_ASN_NN_rt(self, v, load=False):
    """
    Setter method for ASN_NN_rt, mapped from YANG variable /routing_system/route_map/content/set/extcommunity/rt/ASN_NN_rt (ext-community-rt-expr-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ASN_NN_rt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ASN_NN_rt() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])):(([0-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)(( (additive))?)'}), is_leaf=True, yang_name="ASN-NN-rt", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ext-community-rt-expr-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ASN_NN_rt must be of a type compatible with ext-community-rt-expr-t""",
          'defined-type': "brocade-ip-policy:ext-community-rt-expr-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])):(([0-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)(( (additive))?)'}), is_leaf=True, yang_name="ASN-NN-rt", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ext-community-rt-expr-t', is_config=True)""",
        })

    self.__ASN_NN_rt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ASN_NN_rt(self):
    self.__ASN_NN_rt = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((\\s*(((([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])):(([0-9][0-9]{0,8})|([1-3][0-9]{9})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])|(429496729[0-5])))|((([1-9][0-9]{0,8})|(4[0-1][0-9]{8})|(42[0-8][0-9]{7})|(429[0-3][0-9]{6})|(4294[0-8][0-9]{5})|(42949[0-5][0-9]{4})|(429496[0-6][0-9]{3})|(4294967[0-1][0-9]{2})|(42949672[0-8][0-9])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))|(((([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])):(([1-9][0-9]{0,3})|([1-5][0-9]{4})|(6[0-4][0-9]{3})|(65[0-4][0-9]{2})|(655[0-2][0-9])|(6553[0-5])))))*)(( (additive))?)'}), is_leaf=True, yang_name="ASN-NN-rt", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='ext-community-rt-expr-t', is_config=True)

  ASN_NN_rt = __builtin__.property(_get_ASN_NN_rt, _set_ASN_NN_rt)


  _pyangbind_elements = {'ASN_NN_rt': ASN_NN_rt, }


