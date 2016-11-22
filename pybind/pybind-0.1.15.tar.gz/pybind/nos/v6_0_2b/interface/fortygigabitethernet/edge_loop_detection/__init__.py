
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class edge_loop_detection(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/edge-loop-detection. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__eldprio','__eldvlan',)

  _yang_name = 'edge-loop-detection'
  _rest_name = 'edge-loop-detection'

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
    self.__eldprio = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..256']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(128), is_leaf=True, yang_name="eldprio", rest_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ELD-priority value to interface', u'alt-name': u'port-priority'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    self.__eldvlan = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="eldvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable for specific VLAN on selected interface', u'alt-name': u'vlan', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-eldvlan-range', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'edge-loop-detection']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'edge-loop-detection']

  def _get_eldprio(self):
    """
    Getter method for eldprio, mapped from YANG variable /interface/fortygigabitethernet/edge_loop_detection/eldprio (uint32)
    """
    return self.__eldprio
      
  def _set_eldprio(self, v, load=False):
    """
    Setter method for eldprio, mapped from YANG variable /interface/fortygigabitethernet/edge_loop_detection/eldprio (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_eldprio is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_eldprio() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..256']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(128), is_leaf=True, yang_name="eldprio", rest_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ELD-priority value to interface', u'alt-name': u'port-priority'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """eldprio must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..256']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(128), is_leaf=True, yang_name="eldprio", rest_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ELD-priority value to interface', u'alt-name': u'port-priority'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)""",
        })

    self.__eldprio = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_eldprio(self):
    self.__eldprio = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..256']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(128), is_leaf=True, yang_name="eldprio", rest_name="port-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set ELD-priority value to interface', u'alt-name': u'port-priority'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)


  def _get_eldvlan(self):
    """
    Getter method for eldvlan, mapped from YANG variable /interface/fortygigabitethernet/edge_loop_detection/eldvlan (ui32-eldvlan-range)
    """
    return self.__eldvlan
      
  def _set_eldvlan(self, v, load=False):
    """
    Setter method for eldvlan, mapped from YANG variable /interface/fortygigabitethernet/edge_loop_detection/eldvlan (ui32-eldvlan-range)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_eldvlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_eldvlan() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="eldvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable for specific VLAN on selected interface', u'alt-name': u'vlan', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-eldvlan-range', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """eldvlan must be of a type compatible with ui32-eldvlan-range""",
          'defined-type': "brocade-interface:ui32-eldvlan-range",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="eldvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable for specific VLAN on selected interface', u'alt-name': u'vlan', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-eldvlan-range', is_config=True)""",
        })

    self.__eldvlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_eldvlan(self):
    self.__eldvlan = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="eldvlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable for specific VLAN on selected interface', u'alt-name': u'vlan', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-eldvlan-range', is_config=True)

  eldprio = __builtin__.property(_get_eldprio, _set_eldprio)
  eldvlan = __builtin__.property(_get_eldvlan, _set_eldvlan)


  _pyangbind_elements = {'eldprio': eldprio, 'eldvlan': eldvlan, }


