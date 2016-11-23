
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlan
import ve
class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The vlan interface configurations/data of this managed
device.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan','__ve',)

  _yang_name = 'interface'
  _rest_name = 'interface'

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
    self.__vlan = YANGDynClass(base=YANGListType("name",vlan.vlan, yang_name="vlan", rest_name="Vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}), is_container='list', yang_name="vlan", rest_name="Vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    self.__ve = YANGDynClass(base=YANGListType("gve_name",ve.ve, yang_name="ve", rest_name="Ve", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='gve-name', extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}), is_container='list', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)

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
      return [u'interface-vlan', u'interface']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface']

  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /interface_vlan/interface/vlan (list)

    YANG Description: The list of vlans in the managed device. Each row 
represents a vlan. User can create/delete an entry in 
to this list.
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /interface_vlan/interface/vlan (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.

    YANG Description: The list of vlans in the managed device. Each row 
represents a vlan. User can create/delete an entry in 
to this list.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("name",vlan.vlan, yang_name="vlan", rest_name="Vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}), is_container='list', yang_name="vlan", rest_name="Vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name",vlan.vlan, yang_name="vlan", rest_name="Vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}), is_container='list', yang_name="vlan", rest_name="Vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=YANGListType("name",vlan.vlan, yang_name="vlan", rest_name="Vlan", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name', extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}), is_container='list', yang_name="vlan", rest_name="Vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of vlans.', u'cli-no-key-completion': None, u'alt-name': u'Vlan', u'cli-suppress-show-path': None, u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'interface_vlan'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)


  def _get_ve(self):
    """
    Getter method for ve, mapped from YANG variable /interface_vlan/interface/ve (list)

    YANG Description: The list of ve interfaces in the managed device. Each row 
represents a ve interface. User can create/delete an entry in 
to this list.
    """
    return self.__ve
      
  def _set_ve(self, v, load=False):
    """
    Setter method for ve, mapped from YANG variable /interface_vlan/interface/ve (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ve is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ve() directly.

    YANG Description: The list of ve interfaces in the managed device. Each row 
represents a ve interface. User can create/delete an entry in 
to this list.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("gve_name",ve.ve, yang_name="ve", rest_name="Ve", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='gve-name', extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}), is_container='list', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ve must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("gve_name",ve.ve, yang_name="ve", rest_name="Ve", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='gve-name', extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}), is_container='list', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__ve = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ve(self):
    self.__ve = YANGDynClass(base=YANGListType("gve_name",ve.ve, yang_name="ve", rest_name="Ve", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='gve-name', extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}), is_container='list', yang_name="ve", rest_name="Ve", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The list of Global VEs.', u'cli-no-key-completion': None, u'alt-name': u'Ve', u'cli-suppress-list-no': None, u'cli-custom-range-actionpoint': u'NsmRangeCliActionpoint', u'cli-custom-range-enumerator': u'NsmRangeCliActionpoint', u'cli-suppress-key-abbreviation': None, u'cli-no-match-completion': None, u'cli-full-command': None, u'callpoint': u'AnycastGatewayGlobalVeConfig'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)

  vlan = __builtin__.property(_get_vlan, _set_vlan)
  ve = __builtin__.property(_get_ve, _set_ve)


  _pyangbind_elements = {'vlan': vlan, 've': ve, }


