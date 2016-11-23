
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlan_statistics
import bridge_domain_statistics
class sub_interface_statistics_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /sub-interface-statistics-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: sub-interface statistics
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_statistics','__bridge_domain_statistics',)

  _yang_name = 'sub-interface-statistics-state'
  _rest_name = 'sub-interface-statistics-state'

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
    self.__bridge_domain_statistics = YANGDynClass(base=YANGListType("bd_id",bridge_domain_statistics.bridge_domain_statistics, yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    self.__vlan_statistics = YANGDynClass(base=YANGListType("vlan_id",vlan_statistics.vlan_statistics, yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

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
      return [u'sub-interface-statistics-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'sub-interface-statistics-state']

  def _get_vlan_statistics(self):
    """
    Getter method for vlan_statistics, mapped from YANG variable /sub_interface_statistics_state/vlan_statistics (list)

    YANG Description: vlan_statistics
    """
    return self.__vlan_statistics
      
  def _set_vlan_statistics(self, v, load=False):
    """
    Setter method for vlan_statistics, mapped from YANG variable /sub_interface_statistics_state/vlan_statistics (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_statistics is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_statistics() directly.

    YANG Description: vlan_statistics
    """
    try:
      t = YANGDynClass(v,base=YANGListType("vlan_id",vlan_statistics.vlan_statistics, yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_statistics must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vlan_id",vlan_statistics.vlan_statistics, yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__vlan_statistics = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_statistics(self):
    self.__vlan_statistics = YANGDynClass(base=YANGListType("vlan_id",vlan_statistics.vlan_statistics, yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vlan-id', extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vlan-statistics", rest_name="vlan-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vlan-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)


  def _get_bridge_domain_statistics(self):
    """
    Getter method for bridge_domain_statistics, mapped from YANG variable /sub_interface_statistics_state/bridge_domain_statistics (list)

    YANG Description: bridge-domain statistics
    """
    return self.__bridge_domain_statistics
      
  def _set_bridge_domain_statistics(self, v, load=False):
    """
    Setter method for bridge_domain_statistics, mapped from YANG variable /sub_interface_statistics_state/bridge_domain_statistics (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge_domain_statistics is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge_domain_statistics() directly.

    YANG Description: bridge-domain statistics
    """
    try:
      t = YANGDynClass(v,base=YANGListType("bd_id",bridge_domain_statistics.bridge_domain_statistics, yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge_domain_statistics must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("bd_id",bridge_domain_statistics.bridge_domain_statistics, yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__bridge_domain_statistics = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge_domain_statistics(self):
    self.__bridge_domain_statistics = YANGDynClass(base=YANGListType("bd_id",bridge_domain_statistics.bridge_domain_statistics, yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bd-id', extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="bridge-domain-statistics", rest_name="bridge-domain-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-bridge-domain-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

  vlan_statistics = __builtin__.property(_get_vlan_statistics)
  bridge_domain_statistics = __builtin__.property(_get_bridge_domain_statistics)


  _pyangbind_elements = {'vlan_statistics': vlan_statistics, 'bridge_domain_statistics': bridge_domain_statistics, }


