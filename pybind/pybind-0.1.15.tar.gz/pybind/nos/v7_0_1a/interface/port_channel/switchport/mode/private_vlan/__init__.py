
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import private_vlan_trunk
class private_vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/switchport/mode/private-vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__private_vlan_trunk','__promiscuous','__host',)

  _yang_name = 'private-vlan'
  _rest_name = 'private-vlan'

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
    self.__host = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan host', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__private_vlan_trunk = YANGDynClass(base=private_vlan_trunk.private_vlan_trunk, is_container='container', yang_name="private-vlan-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk', u'alt-name': u'trunk'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__promiscuous = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan promiscuous', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

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
      return [u'interface', u'port-channel', u'switchport', u'mode', u'private-vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'switchport', u'mode', u'private-vlan']

  def _get_private_vlan_trunk(self):
    """
    Getter method for private_vlan_trunk, mapped from YANG variable /interface/port_channel/switchport/mode/private_vlan/private_vlan_trunk (container)
    """
    return self.__private_vlan_trunk
      
  def _set_private_vlan_trunk(self, v, load=False):
    """
    Setter method for private_vlan_trunk, mapped from YANG variable /interface/port_channel/switchport/mode/private_vlan/private_vlan_trunk (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_private_vlan_trunk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_private_vlan_trunk() directly.
    """
    try:
      t = YANGDynClass(v,base=private_vlan_trunk.private_vlan_trunk, is_container='container', yang_name="private-vlan-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk', u'alt-name': u'trunk'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """private_vlan_trunk must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=private_vlan_trunk.private_vlan_trunk, is_container='container', yang_name="private-vlan-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk', u'alt-name': u'trunk'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__private_vlan_trunk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_private_vlan_trunk(self):
    self.__private_vlan_trunk = YANGDynClass(base=private_vlan_trunk.private_vlan_trunk, is_container='container', yang_name="private-vlan-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan trunk', u'alt-name': u'trunk'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_promiscuous(self):
    """
    Getter method for promiscuous, mapped from YANG variable /interface/port_channel/switchport/mode/private_vlan/promiscuous (empty)
    """
    return self.__promiscuous
      
  def _set_promiscuous(self, v, load=False):
    """
    Setter method for promiscuous, mapped from YANG variable /interface/port_channel/switchport/mode/private_vlan/promiscuous (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_promiscuous is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_promiscuous() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan promiscuous', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """promiscuous must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan promiscuous', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__promiscuous = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_promiscuous(self):
    self.__promiscuous = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="promiscuous", rest_name="promiscuous", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan promiscuous', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_host(self):
    """
    Getter method for host, mapped from YANG variable /interface/port_channel/switchport/mode/private_vlan/host (empty)
    """
    return self.__host
      
  def _set_host(self, v, load=False):
    """
    Setter method for host, mapped from YANG variable /interface/port_channel/switchport/mode/private_vlan/host (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_host is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_host() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan host', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """host must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan host', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__host = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_host(self):
    self.__host = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="host", rest_name="host", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as private-vlan host', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

  private_vlan_trunk = __builtin__.property(_get_private_vlan_trunk, _set_private_vlan_trunk)
  promiscuous = __builtin__.property(_get_promiscuous, _set_promiscuous)
  host = __builtin__.property(_get_host, _set_host)


  _pyangbind_elements = {'private_vlan_trunk': private_vlan_trunk, 'promiscuous': promiscuous, 'host': host, }


