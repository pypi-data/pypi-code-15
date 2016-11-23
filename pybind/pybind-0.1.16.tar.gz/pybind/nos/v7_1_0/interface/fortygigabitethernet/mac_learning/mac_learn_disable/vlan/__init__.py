
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/mac-learning/mac-learn-disable/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mac_learning_vlan_add','__mac_learning_vlan_remove',)

  _yang_name = 'vlan'
  _rest_name = 'vlan'

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
    self.__mac_learning_vlan_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to remove', u'alt-name': u'remove', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)
    self.__mac_learning_vlan_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to add', u'alt-name': u'add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'mac-learning', u'mac-learn-disable', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'mac-learning', u'disable', u'vlan']

  def _get_mac_learning_vlan_add(self):
    """
    Getter method for mac_learning_vlan_add, mapped from YANG variable /interface/fortygigabitethernet/mac_learning/mac_learn_disable/vlan/mac_learning_vlan_add (ui32-range-8091)
    """
    return self.__mac_learning_vlan_add
      
  def _set_mac_learning_vlan_add(self, v, load=False):
    """
    Setter method for mac_learning_vlan_add, mapped from YANG variable /interface/fortygigabitethernet/mac_learning/mac_learn_disable/vlan/mac_learning_vlan_add (ui32-range-8091)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_learning_vlan_add is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_learning_vlan_add() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to add', u'alt-name': u'add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_learning_vlan_add must be of a type compatible with ui32-range-8091""",
          'defined-type': "brocade-interface:ui32-range-8091",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to add', u'alt-name': u'add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)""",
        })

    self.__mac_learning_vlan_add = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_learning_vlan_add(self):
    self.__mac_learning_vlan_add = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-add", rest_name="add", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to add', u'alt-name': u'add', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)


  def _get_mac_learning_vlan_remove(self):
    """
    Getter method for mac_learning_vlan_remove, mapped from YANG variable /interface/fortygigabitethernet/mac_learning/mac_learn_disable/vlan/mac_learning_vlan_remove (ui32-range-8091)
    """
    return self.__mac_learning_vlan_remove
      
  def _set_mac_learning_vlan_remove(self, v, load=False):
    """
    Setter method for mac_learning_vlan_remove, mapped from YANG variable /interface/fortygigabitethernet/mac_learning/mac_learn_disable/vlan/mac_learning_vlan_remove (ui32-range-8091)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_learning_vlan_remove is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_learning_vlan_remove() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to remove', u'alt-name': u'remove', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_learning_vlan_remove must be of a type compatible with ui32-range-8091""",
          'defined-type': "brocade-interface:ui32-range-8091",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to remove', u'alt-name': u'remove', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)""",
        })

    self.__mac_learning_vlan_remove = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_learning_vlan_remove(self):
    self.__mac_learning_vlan_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9][0-9]{0,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?((,(([2-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01]))(-(([3-9])|([1-9][0-9]{1,2})|([1-7][0-9]{3})|(80[0-9]{2})|(81[0-8][0-9])|(819[01])))?)?)*', 'length': [u'1..253']}), is_leaf=True, yang_name="mac-learning-vlan-remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'RANGE;;Range of vlans to remove', u'alt-name': u'remove', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='ui32-range-8091', is_config=True)

  mac_learning_vlan_add = __builtin__.property(_get_mac_learning_vlan_add, _set_mac_learning_vlan_add)
  mac_learning_vlan_remove = __builtin__.property(_get_mac_learning_vlan_remove, _set_mac_learning_vlan_remove)


  _pyangbind_elements = {'mac_learning_vlan_add': mac_learning_vlan_add, 'mac_learning_vlan_remove': mac_learning_vlan_remove, }


