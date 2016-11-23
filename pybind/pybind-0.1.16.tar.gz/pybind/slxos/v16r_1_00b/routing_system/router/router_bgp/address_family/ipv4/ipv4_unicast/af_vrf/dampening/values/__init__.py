
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class values(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv4/ipv4-unicast/af-vrf/dampening/values. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__half_time','__reuse_value','__start_suppress_time','__max_suppress_time',)

  _yang_name = 'values'
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
    self.__half_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..45']}), is_leaf=True, yang_name="half-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='htime', is_config=True)
    self.__start_suppress_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="start-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-start-suppress-value', is_config=True)
    self.__reuse_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="reuse-value", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-reuse-value', is_config=True)
    self.__max_suppress_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="max-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-max-suppress-value', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'af-vrf', u'dampening', u'values']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'vrf', u'dampening']

  def _get_half_time(self):
    """
    Getter method for half_time, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/half_time (htime)
    """
    return self.__half_time
      
  def _set_half_time(self, v, load=False):
    """
    Setter method for half_time, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/half_time (htime)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_half_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_half_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..45']}), is_leaf=True, yang_name="half-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='htime', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """half_time must be of a type compatible with htime""",
          'defined-type': "brocade-bgp:htime",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..45']}), is_leaf=True, yang_name="half-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='htime', is_config=True)""",
        })

    self.__half_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_half_time(self):
    self.__half_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..45']}), is_leaf=True, yang_name="half-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='htime', is_config=True)


  def _get_reuse_value(self):
    """
    Getter method for reuse_value, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/reuse_value (damp-reuse-value)
    """
    return self.__reuse_value
      
  def _set_reuse_value(self, v, load=False):
    """
    Setter method for reuse_value, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/reuse_value (damp-reuse-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reuse_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reuse_value() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="reuse-value", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-reuse-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reuse_value must be of a type compatible with damp-reuse-value""",
          'defined-type': "brocade-bgp:damp-reuse-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="reuse-value", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-reuse-value', is_config=True)""",
        })

    self.__reuse_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reuse_value(self):
    self.__reuse_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="reuse-value", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-reuse-value', is_config=True)


  def _get_start_suppress_time(self):
    """
    Getter method for start_suppress_time, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/start_suppress_time (damp-start-suppress-value)
    """
    return self.__start_suppress_time
      
  def _set_start_suppress_time(self, v, load=False):
    """
    Setter method for start_suppress_time, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/start_suppress_time (damp-start-suppress-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_start_suppress_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_start_suppress_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="start-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-start-suppress-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """start_suppress_time must be of a type compatible with damp-start-suppress-value""",
          'defined-type': "brocade-bgp:damp-start-suppress-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="start-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-start-suppress-value', is_config=True)""",
        })

    self.__start_suppress_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_start_suppress_time(self):
    self.__start_suppress_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..20000']}), is_leaf=True, yang_name="start-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-start-suppress-value', is_config=True)


  def _get_max_suppress_time(self):
    """
    Getter method for max_suppress_time, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/max_suppress_time (damp-max-suppress-value)
    """
    return self.__max_suppress_time
      
  def _set_max_suppress_time(self, v, load=False):
    """
    Setter method for max_suppress_time, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv4/ipv4_unicast/af_vrf/dampening/values/max_suppress_time (damp-max-suppress-value)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_suppress_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_suppress_time() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="max-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-max-suppress-value', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_suppress_time must be of a type compatible with damp-max-suppress-value""",
          'defined-type': "brocade-bgp:damp-max-suppress-value",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="max-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-max-suppress-value', is_config=True)""",
        })

    self.__max_suppress_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_suppress_time(self):
    self.__max_suppress_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="max-suppress-time", rest_name="", parent=self, choice=(u'ch-dampening-source', u'ca-dampening-specify-values'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='damp-max-suppress-value', is_config=True)

  half_time = __builtin__.property(_get_half_time, _set_half_time)
  reuse_value = __builtin__.property(_get_reuse_value, _set_reuse_value)
  start_suppress_time = __builtin__.property(_get_start_suppress_time, _set_start_suppress_time)
  max_suppress_time = __builtin__.property(_get_max_suppress_time, _set_max_suppress_time)

  __choices__ = {u'ch-dampening-source': {u'ca-dampening-specify-values': [u'half_time', u'reuse_value', u'start_suppress_time', u'max_suppress_time']}}
  _pyangbind_elements = {'half_time': half_time, 'reuse_value': reuse_value, 'start_suppress_time': start_suppress_time, 'max_suppress_time': max_suppress_time, }


