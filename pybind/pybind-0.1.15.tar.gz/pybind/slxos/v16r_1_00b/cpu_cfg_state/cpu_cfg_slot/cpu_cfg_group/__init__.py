
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cpu_cfg_prio
import cpu_cfg_data
class cpu_cfg_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-operational - based on the path /cpu-cfg-state/cpu-cfg-slot/cpu-cfg-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: CPU group shaper/burst/wfq config
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__group_id','__cpu_cfg_prio','__cpu_cfg_data',)

  _yang_name = 'cpu-cfg-group'
  _rest_name = 'cpu-cfg-group'

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
    self.__cpu_cfg_data = YANGDynClass(base=YANGListType("shaper_rate",cpu_cfg_data.cpu_cfg_data, yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='shaper-rate', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}), is_container='list', yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)
    self.__cpu_cfg_prio = YANGDynClass(base=YANGListType("prio_id",cpu_cfg_prio.cpu_cfg_prio, yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prio-id', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)
    self.__group_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint8', is_config=False)

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
      return [u'cpu-cfg-state', u'cpu-cfg-slot', u'cpu-cfg-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cpu-cfg-state', u'cpu-cfg-slot', u'cpu-cfg-group']

  def _get_group_id(self):
    """
    Getter method for group_id, mapped from YANG variable /cpu_cfg_state/cpu_cfg_slot/cpu_cfg_group/group_id (uint8)

    YANG Description: CPU Group ID
    """
    return self.__group_id
      
  def _set_group_id(self, v, load=False):
    """
    Setter method for group_id, mapped from YANG variable /cpu_cfg_state/cpu_cfg_slot/cpu_cfg_group/group_id (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_id() directly.

    YANG Description: CPU Group ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_id must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint8', is_config=False)""",
        })

    self.__group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_id(self):
    self.__group_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='uint8', is_config=False)


  def _get_cpu_cfg_prio(self):
    """
    Getter method for cpu_cfg_prio, mapped from YANG variable /cpu_cfg_state/cpu_cfg_slot/cpu_cfg_group/cpu_cfg_prio (list)

    YANG Description: CPU prio shaper/burst/wfq config
    """
    return self.__cpu_cfg_prio
      
  def _set_cpu_cfg_prio(self, v, load=False):
    """
    Setter method for cpu_cfg_prio, mapped from YANG variable /cpu_cfg_state/cpu_cfg_slot/cpu_cfg_group/cpu_cfg_prio (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu_cfg_prio is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu_cfg_prio() directly.

    YANG Description: CPU prio shaper/burst/wfq config
    """
    try:
      t = YANGDynClass(v,base=YANGListType("prio_id",cpu_cfg_prio.cpu_cfg_prio, yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prio-id', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu_cfg_prio must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("prio_id",cpu_cfg_prio.cpu_cfg_prio, yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prio-id', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)""",
        })

    self.__cpu_cfg_prio = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu_cfg_prio(self):
    self.__cpu_cfg_prio = YANGDynClass(base=YANGListType("prio_id",cpu_cfg_prio.cpu_cfg_prio, yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='prio-id', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}), is_container='list', yang_name="cpu-cfg-prio", rest_name="cpu-cfg-prio", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-prio', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)


  def _get_cpu_cfg_data(self):
    """
    Getter method for cpu_cfg_data, mapped from YANG variable /cpu_cfg_state/cpu_cfg_slot/cpu_cfg_group/cpu_cfg_data (list)
    """
    return self.__cpu_cfg_data
      
  def _set_cpu_cfg_data(self, v, load=False):
    """
    Setter method for cpu_cfg_data, mapped from YANG variable /cpu_cfg_state/cpu_cfg_slot/cpu_cfg_group/cpu_cfg_data (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cpu_cfg_data is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cpu_cfg_data() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("shaper_rate",cpu_cfg_data.cpu_cfg_data, yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='shaper-rate', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}), is_container='list', yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cpu_cfg_data must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("shaper_rate",cpu_cfg_data.cpu_cfg_data, yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='shaper-rate', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}), is_container='list', yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)""",
        })

    self.__cpu_cfg_data = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cpu_cfg_data(self):
    self.__cpu_cfg_data = YANGDynClass(base=YANGListType("shaper_rate",cpu_cfg_data.cpu_cfg_data, yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='shaper-rate', extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}), is_container='list', yang_name="cpu-cfg-data", rest_name="cpu-cfg-data", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'qos-cpu-cfg-data-cpu-cfg-data-2'}}, namespace='urn:brocade.com:mgmt:brocade-qos-operational', defining_module='brocade-qos-operational', yang_type='list', is_config=False)

  group_id = __builtin__.property(_get_group_id)
  cpu_cfg_prio = __builtin__.property(_get_cpu_cfg_prio)
  cpu_cfg_data = __builtin__.property(_get_cpu_cfg_data)


  _pyangbind_elements = {'group_id': group_id, 'cpu_cfg_prio': cpu_cfg_prio, 'cpu_cfg_data': cpu_cfg_data, }


