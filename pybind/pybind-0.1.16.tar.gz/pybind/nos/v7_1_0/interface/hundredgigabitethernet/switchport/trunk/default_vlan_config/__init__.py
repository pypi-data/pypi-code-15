
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class default_vlan_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/switchport/trunk/default-vlan-config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__default_transparent_vlan',)

  _yang_name = 'default-vlan-config'
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
    self.__default_transparent_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="default-transparent-vlan", rest_name="default-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'default transparent vlan', u'alt-name': u'default-vlan', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'switchport', u'trunk', u'default-vlan-config']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'switchport', u'trunk']

  def _get_default_transparent_vlan(self):
    """
    Getter method for default_transparent_vlan, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/default_vlan_config/default_transparent_vlan (non-dot1q-vlan-type)
    """
    return self.__default_transparent_vlan
      
  def _set_default_transparent_vlan(self, v, load=False):
    """
    Setter method for default_transparent_vlan, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/default_vlan_config/default_transparent_vlan (non-dot1q-vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_transparent_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_transparent_vlan() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="default-transparent-vlan", rest_name="default-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'default transparent vlan', u'alt-name': u'default-vlan', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_transparent_vlan must be of a type compatible with non-dot1q-vlan-type""",
          'defined-type': "brocade-interface:non-dot1q-vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="default-transparent-vlan", rest_name="default-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'default transparent vlan', u'alt-name': u'default-vlan', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)""",
        })

    self.__default_transparent_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_transparent_vlan(self):
    self.__default_transparent_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4096..8191']}), is_leaf=True, yang_name="default-transparent-vlan", rest_name="default-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'default transparent vlan', u'alt-name': u'default-vlan', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='non-dot1q-vlan-type', is_config=True)

  default_transparent_vlan = __builtin__.property(_get_default_transparent_vlan, _set_default_transparent_vlan)


  _pyangbind_elements = {'default_transparent_vlan': default_transparent_vlan, }


