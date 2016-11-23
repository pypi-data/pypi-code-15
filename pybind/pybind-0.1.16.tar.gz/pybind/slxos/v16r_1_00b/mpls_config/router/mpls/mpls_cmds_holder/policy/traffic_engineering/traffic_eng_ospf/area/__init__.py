
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class area(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/policy/traffic-engineering/traffic-eng-ospf/area. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ospf_area_as_ip_address','__ospf_area_as_decimal','__ospf_area_all',)

  _yang_name = 'area'
  _rest_name = 'area'

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
    self.__ospf_area_as_ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-as-ip-address", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-ip-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ospf_area_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-area-all", rest_name="all", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Advertise all OSPF areas', u'alt-name': u'all', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__ospf_area_as_decimal = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="ospf-area-as-decimal", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-decimal'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'policy', u'traffic-engineering', u'traffic-eng-ospf', u'area']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'policy', u'traffic-engineering', u'ospf', u'area']

  def _get_ospf_area_as_ip_address(self):
    """
    Getter method for ospf_area_as_ip_address, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf/area/ospf_area_as_ip_address (inet:ipv4-address)
    """
    return self.__ospf_area_as_ip_address
      
  def _set_ospf_area_as_ip_address(self, v, load=False):
    """
    Setter method for ospf_area_as_ip_address, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf/area/ospf_area_as_ip_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_area_as_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_area_as_ip_address() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-as-ip-address", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-ip-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_area_as_ip_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-as-ip-address", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-ip-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ospf_area_as_ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_area_as_ip_address(self):
    self.__ospf_area_as_ip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ospf-area-as-ip-address", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-ip-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ospf_area_as_decimal(self):
    """
    Getter method for ospf_area_as_decimal, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf/area/ospf_area_as_decimal (uint32)
    """
    return self.__ospf_area_as_decimal
      
  def _set_ospf_area_as_decimal(self, v, load=False):
    """
    Setter method for ospf_area_as_decimal, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf/area/ospf_area_as_decimal (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_area_as_decimal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_area_as_decimal() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="ospf-area-as-decimal", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-decimal'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_area_as_decimal must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="ospf-area-as-decimal", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-decimal'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ospf_area_as_decimal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_area_as_decimal(self):
    self.__ospf_area_as_decimal = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), is_leaf=True, yang_name="ospf-area-as-decimal", rest_name="", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-type-decimal'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ospf_area_all(self):
    """
    Getter method for ospf_area_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf/area/ospf_area_all (empty)
    """
    return self.__ospf_area_all
      
  def _set_ospf_area_all(self, v, load=False):
    """
    Setter method for ospf_area_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/traffic_engineering/traffic_eng_ospf/area/ospf_area_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_area_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_area_all() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ospf-area-all", rest_name="all", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Advertise all OSPF areas', u'alt-name': u'all', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_area_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-area-all", rest_name="all", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Advertise all OSPF areas', u'alt-name': u'all', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__ospf_area_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_area_all(self):
    self.__ospf_area_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-area-all", rest_name="all", parent=self, choice=(u'ch-ospf-area-type', u'ca-area-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Advertise all OSPF areas', u'alt-name': u'all', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

  ospf_area_as_ip_address = __builtin__.property(_get_ospf_area_as_ip_address, _set_ospf_area_as_ip_address)
  ospf_area_as_decimal = __builtin__.property(_get_ospf_area_as_decimal, _set_ospf_area_as_decimal)
  ospf_area_all = __builtin__.property(_get_ospf_area_all, _set_ospf_area_all)

  __choices__ = {u'ch-ospf-area-type': {u'ca-area-type-decimal': [u'ospf_area_as_decimal'], u'ca-area-type-ip-address': [u'ospf_area_as_ip_address'], u'ca-area-all': [u'ospf_area_all']}}
  _pyangbind_elements = {'ospf_area_as_ip_address': ospf_area_as_ip_address, 'ospf_area_as_decimal': ospf_area_as_decimal, 'ospf_area_all': ospf_area_all, }


