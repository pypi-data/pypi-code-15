
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import arp
import igmpPIM
import igmp
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/interface/vlan/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IP configurations for an interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__arp','__igmpPIM','__igmp',)

  _yang_name = 'ip'
  _rest_name = 'ip'

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
    self.__arp = YANGDynClass(base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP', u'callpoint': u'interface_vlan', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)
    self.__igmpPIM = YANGDynClass(base=igmpPIM.igmpPIM, is_container='container', yang_name="igmpPIM", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMPS : Ip PIM Snooping', u'hidden': u'full', u'callpoint': u'IgmpsVlan', u'cli-incomplete-no': None, u'alt-name': u'pim'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    self.__igmp = YANGDynClass(base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'cli-incomplete-no': None, u'callpoint': u'IgmpsVlan', u'sort-priority': u'118'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)

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
      return [u'interface-vlan', u'interface', u'vlan', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Vlan', u'ip']

  def _get_arp(self):
    """
    Getter method for arp, mapped from YANG variable /interface_vlan/interface/vlan/ip/arp (container)
    """
    return self.__arp
      
  def _set_arp(self, v, load=False):
    """
    Setter method for arp, mapped from YANG variable /interface_vlan/interface/vlan/ip/arp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_arp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_arp() directly.
    """
    try:
      t = YANGDynClass(v,base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP', u'callpoint': u'interface_vlan', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """arp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP', u'callpoint': u'interface_vlan', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)""",
        })

    self.__arp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_arp(self):
    self.__arp = YANGDynClass(base=arp.arp, is_container='container', yang_name="arp", rest_name="arp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ARP', u'callpoint': u'interface_vlan', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dai', defining_module='brocade-dai', yang_type='container', is_config=True)


  def _get_igmpPIM(self):
    """
    Getter method for igmpPIM, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmpPIM (container)
    """
    return self.__igmpPIM
      
  def _set_igmpPIM(self, v, load=False):
    """
    Setter method for igmpPIM, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmpPIM (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmpPIM is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmpPIM() directly.
    """
    try:
      t = YANGDynClass(v,base=igmpPIM.igmpPIM, is_container='container', yang_name="igmpPIM", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMPS : Ip PIM Snooping', u'hidden': u'full', u'callpoint': u'IgmpsVlan', u'cli-incomplete-no': None, u'alt-name': u'pim'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmpPIM must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igmpPIM.igmpPIM, is_container='container', yang_name="igmpPIM", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMPS : Ip PIM Snooping', u'hidden': u'full', u'callpoint': u'IgmpsVlan', u'cli-incomplete-no': None, u'alt-name': u'pim'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)""",
        })

    self.__igmpPIM = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmpPIM(self):
    self.__igmpPIM = YANGDynClass(base=igmpPIM.igmpPIM, is_container='container', yang_name="igmpPIM", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGMPS : Ip PIM Snooping', u'hidden': u'full', u'callpoint': u'IgmpsVlan', u'cli-incomplete-no': None, u'alt-name': u'pim'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)


  def _get_igmp(self):
    """
    Getter method for igmp, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp (container)
    """
    return self.__igmp
      
  def _set_igmp(self, v, load=False):
    """
    Setter method for igmp, mapped from YANG variable /interface_vlan/interface/vlan/ip/igmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp() directly.
    """
    try:
      t = YANGDynClass(v,base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'cli-incomplete-no': None, u'callpoint': u'IgmpsVlan', u'sort-priority': u'118'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'cli-incomplete-no': None, u'callpoint': u'IgmpsVlan', u'sort-priority': u'118'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)""",
        })

    self.__igmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp(self):
    self.__igmp = YANGDynClass(base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'cli-incomplete-no': None, u'callpoint': u'IgmpsVlan', u'sort-priority': u'118'}}, namespace='urn:brocade.com:mgmt:brocade-igmp-snooping', defining_module='brocade-igmp-snooping', yang_type='container', is_config=True)

  arp = __builtin__.property(_get_arp, _set_arp)
  igmpPIM = __builtin__.property(_get_igmpPIM, _set_igmpPIM)
  igmp = __builtin__.property(_get_igmp, _set_igmp)


  _pyangbind_elements = {'arp': arp, 'igmpPIM': igmpPIM, 'igmp': igmp, }


