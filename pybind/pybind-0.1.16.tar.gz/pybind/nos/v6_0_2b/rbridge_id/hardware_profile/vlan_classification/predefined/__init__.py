
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class predefined(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/hardware-profile/vlan-classification/predefined. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_profiletype',)

  _yang_name = 'predefined'
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
    self.__vlan_profiletype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tor-vxlan-gw': {'value': 2}, u'default': {'value': 0}, u'aggregator-basic': {'value': 3}, u'aggregator-vxlan-gw': {'value': 5}, u'aggregator-virtualfabric': {'value': 4}, u'tor-virtualfabric': {'value': 1}},), is_leaf=True, yang_name="vlan_profiletype", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='vlan-classification-subtype', is_config=True)

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
      return [u'rbridge-id', u'hardware-profile', u'vlan-classification', u'predefined']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'hardware-profile', u'vlan-classification']

  def _get_vlan_profiletype(self):
    """
    Getter method for vlan_profiletype, mapped from YANG variable /rbridge_id/hardware_profile/vlan_classification/predefined/vlan_profiletype (vlan-classification-subtype)
    """
    return self.__vlan_profiletype
      
  def _set_vlan_profiletype(self, v, load=False):
    """
    Setter method for vlan_profiletype, mapped from YANG variable /rbridge_id/hardware_profile/vlan_classification/predefined/vlan_profiletype (vlan-classification-subtype)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_profiletype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_profiletype() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tor-vxlan-gw': {'value': 2}, u'default': {'value': 0}, u'aggregator-basic': {'value': 3}, u'aggregator-vxlan-gw': {'value': 5}, u'aggregator-virtualfabric': {'value': 4}, u'tor-virtualfabric': {'value': 1}},), is_leaf=True, yang_name="vlan_profiletype", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='vlan-classification-subtype', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_profiletype must be of a type compatible with vlan-classification-subtype""",
          'defined-type': "brocade-hardware:vlan-classification-subtype",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tor-vxlan-gw': {'value': 2}, u'default': {'value': 0}, u'aggregator-basic': {'value': 3}, u'aggregator-vxlan-gw': {'value': 5}, u'aggregator-virtualfabric': {'value': 4}, u'tor-virtualfabric': {'value': 1}},), is_leaf=True, yang_name="vlan_profiletype", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='vlan-classification-subtype', is_config=True)""",
        })

    self.__vlan_profiletype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_profiletype(self):
    self.__vlan_profiletype = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'tor-vxlan-gw': {'value': 2}, u'default': {'value': 0}, u'aggregator-basic': {'value': 3}, u'aggregator-vxlan-gw': {'value': 5}, u'aggregator-virtualfabric': {'value': 4}, u'tor-virtualfabric': {'value': 1}},), is_leaf=True, yang_name="vlan_profiletype", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='vlan-classification-subtype', is_config=True)

  vlan_profiletype = __builtin__.property(_get_vlan_profiletype, _set_vlan_profiletype)


  _pyangbind_elements = {'vlan_profiletype': vlan_profiletype, }


