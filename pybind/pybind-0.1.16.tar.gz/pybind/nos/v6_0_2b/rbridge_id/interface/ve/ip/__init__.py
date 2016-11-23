
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ip_config
import ip_local_anycast_gateway
import interface_ve_dhcp_conf
import icmp
import igmp
import interface_vlan_ospf_conf
import pim_intf_vlan_cont
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/ve/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ip_config','__ip_local_anycast_gateway','__interface_ve_dhcp_conf','__icmp','__igmp','__interface_vlan_ospf_conf','__pim_intf_vlan_cont',)

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
    self.__igmp = YANGDynClass(base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'callpoint': u'IgmpSvi', u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)
    self.__interface_ve_dhcp_conf = YANGDynClass(base=interface_ve_dhcp_conf.interface_ve_dhcp_conf, is_container='container', yang_name="interface-ve-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)
    self.__pim_intf_vlan_cont = YANGDynClass(base=pim_intf_vlan_cont.pim_intf_vlan_cont, is_container='container', yang_name="pim-intf-vlan-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimVlanIntfCallpoint', u'sort-priority': u'115'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)
    self.__ip_config = YANGDynClass(base=ip_config.ip_config, is_container='container', yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'intf-vlan-ip-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    self.__ip_local_anycast_gateway = YANGDynClass(base=YANGListType("local_ip_gw_id",ip_local_anycast_gateway.ip_local_anycast_gateway, yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-ip-gw-id', extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}), is_container='list', yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'IcmpVeIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)
    self.__interface_vlan_ospf_conf = YANGDynClass(base=interface_vlan_ospf_conf.interface_vlan_ospf_conf, is_container='container', yang_name="interface-vlan-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFVlanInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'interface', u've', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Ve', u'ip']

  def _get_ip_config(self):
    """
    Getter method for ip_config, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_config (container)
    """
    return self.__ip_config
      
  def _set_ip_config(self, v, load=False):
    """
    Setter method for ip_config, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_config() directly.
    """
    try:
      t = YANGDynClass(v,base=ip_config.ip_config, is_container='container', yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'intf-vlan-ip-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip_config.ip_config, is_container='container', yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'intf-vlan-ip-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)""",
        })

    self.__ip_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_config(self):
    self.__ip_config = YANGDynClass(base=ip_config.ip_config, is_container='container', yang_name="ip-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'intf-vlan-ip-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)


  def _get_ip_local_anycast_gateway(self):
    """
    Getter method for ip_local_anycast_gateway, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway (list)
    """
    return self.__ip_local_anycast_gateway
      
  def _set_ip_local_anycast_gateway(self, v, load=False):
    """
    Setter method for ip_local_anycast_gateway, mapped from YANG variable /rbridge_id/interface/ve/ip/ip_local_anycast_gateway (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_local_anycast_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_local_anycast_gateway() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("local_ip_gw_id",ip_local_anycast_gateway.ip_local_anycast_gateway, yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-ip-gw-id', extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}), is_container='list', yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_local_anycast_gateway must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("local_ip_gw_id",ip_local_anycast_gateway.ip_local_anycast_gateway, yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-ip-gw-id', extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}), is_container='list', yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)""",
        })

    self.__ip_local_anycast_gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_local_anycast_gateway(self):
    self.__ip_local_anycast_gateway = YANGDynClass(base=YANGListType("local_ip_gw_id",ip_local_anycast_gateway.ip_local_anycast_gateway, yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-ip-gw-id', extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}), is_container='list', yang_name="ip-local-anycast-gateway", rest_name="fabric-virtual-gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv4 Fabric virtual gateway', u'cli-run-template-enter': u'$(.?:)', u'alt-name': u'fabric-virtual-gateway', u'callpoint': u'AnycastGatewayLocalIpv4Config', u'cli-full-command': None, u'cli-full-no': None, u'cli-mode-name': u'config-ip-fabric-virtual-gw'}}, namespace='urn:brocade.com:mgmt:brocade-anycast-gateway', defining_module='brocade-anycast-gateway', yang_type='list', is_config=True)


  def _get_interface_ve_dhcp_conf(self):
    """
    Getter method for interface_ve_dhcp_conf, mapped from YANG variable /rbridge_id/interface/ve/ip/interface_ve_dhcp_conf (container)
    """
    return self.__interface_ve_dhcp_conf
      
  def _set_interface_ve_dhcp_conf(self, v, load=False):
    """
    Setter method for interface_ve_dhcp_conf, mapped from YANG variable /rbridge_id/interface/ve/ip/interface_ve_dhcp_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ve_dhcp_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ve_dhcp_conf() directly.
    """
    try:
      t = YANGDynClass(v,base=interface_ve_dhcp_conf.interface_ve_dhcp_conf, is_container='container', yang_name="interface-ve-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ve_dhcp_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ve_dhcp_conf.interface_ve_dhcp_conf, is_container='container', yang_name="interface-ve-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)""",
        })

    self.__interface_ve_dhcp_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ve_dhcp_conf(self):
    self.__interface_ve_dhcp_conf = YANGDynClass(base=interface_ve_dhcp_conf.interface_ve_dhcp_conf, is_container='container', yang_name="interface-ve-dhcp-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)


  def _get_icmp(self):
    """
    Getter method for icmp, mapped from YANG variable /rbridge_id/interface/ve/ip/icmp (container)
    """
    return self.__icmp
      
  def _set_icmp(self, v, load=False):
    """
    Setter method for icmp, mapped from YANG variable /rbridge_id/interface/ve/ip/icmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp() directly.
    """
    try:
      t = YANGDynClass(v,base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'IcmpVeIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'IcmpVeIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)""",
        })

    self.__icmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp(self):
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'sort-priority': u'111', u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-incomplete-no': None, u'callpoint': u'IcmpVeIntfConfigCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)


  def _get_igmp(self):
    """
    Getter method for igmp, mapped from YANG variable /rbridge_id/interface/ve/ip/igmp (container)
    """
    return self.__igmp
      
  def _set_igmp(self, v, load=False):
    """
    Setter method for igmp, mapped from YANG variable /rbridge_id/interface/ve/ip/igmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp() directly.
    """
    try:
      t = YANGDynClass(v,base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'callpoint': u'IgmpSvi', u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'callpoint': u'IgmpSvi', u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)""",
        })

    self.__igmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp(self):
    self.__igmp = YANGDynClass(base=igmp.igmp, is_container='container', yang_name="igmp", rest_name="igmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Group Management Protocol (IGMP)', u'callpoint': u'IgmpSvi', u'sort-priority': u'116'}}, namespace='urn:brocade.com:mgmt:brocade-igmp', defining_module='brocade-igmp', yang_type='container', is_config=True)


  def _get_interface_vlan_ospf_conf(self):
    """
    Getter method for interface_vlan_ospf_conf, mapped from YANG variable /rbridge_id/interface/ve/ip/interface_vlan_ospf_conf (container)
    """
    return self.__interface_vlan_ospf_conf
      
  def _set_interface_vlan_ospf_conf(self, v, load=False):
    """
    Setter method for interface_vlan_ospf_conf, mapped from YANG variable /rbridge_id/interface/ve/ip/interface_vlan_ospf_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_vlan_ospf_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_vlan_ospf_conf() directly.
    """
    try:
      t = YANGDynClass(v,base=interface_vlan_ospf_conf.interface_vlan_ospf_conf, is_container='container', yang_name="interface-vlan-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFVlanInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_vlan_ospf_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_vlan_ospf_conf.interface_vlan_ospf_conf, is_container='container', yang_name="interface-vlan-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFVlanInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__interface_vlan_ospf_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_vlan_ospf_conf(self):
    self.__interface_vlan_ospf_conf = YANGDynClass(base=interface_vlan_ospf_conf.interface_vlan_ospf_conf, is_container='container', yang_name="interface-vlan-ospf-conf", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'OSPFVlanInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_pim_intf_vlan_cont(self):
    """
    Getter method for pim_intf_vlan_cont, mapped from YANG variable /rbridge_id/interface/ve/ip/pim_intf_vlan_cont (container)
    """
    return self.__pim_intf_vlan_cont
      
  def _set_pim_intf_vlan_cont(self, v, load=False):
    """
    Setter method for pim_intf_vlan_cont, mapped from YANG variable /rbridge_id/interface/ve/ip/pim_intf_vlan_cont (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_intf_vlan_cont is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_intf_vlan_cont() directly.
    """
    try:
      t = YANGDynClass(v,base=pim_intf_vlan_cont.pim_intf_vlan_cont, is_container='container', yang_name="pim-intf-vlan-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimVlanIntfCallpoint', u'sort-priority': u'115'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_intf_vlan_cont must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pim_intf_vlan_cont.pim_intf_vlan_cont, is_container='container', yang_name="pim-intf-vlan-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimVlanIntfCallpoint', u'sort-priority': u'115'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)""",
        })

    self.__pim_intf_vlan_cont = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_intf_vlan_cont(self):
    self.__pim_intf_vlan_cont = YANGDynClass(base=pim_intf_vlan_cont.pim_intf_vlan_cont, is_container='container', yang_name="pim-intf-vlan-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'PimVlanIntfCallpoint', u'sort-priority': u'115'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)

  ip_config = __builtin__.property(_get_ip_config, _set_ip_config)
  ip_local_anycast_gateway = __builtin__.property(_get_ip_local_anycast_gateway, _set_ip_local_anycast_gateway)
  interface_ve_dhcp_conf = __builtin__.property(_get_interface_ve_dhcp_conf, _set_interface_ve_dhcp_conf)
  icmp = __builtin__.property(_get_icmp, _set_icmp)
  igmp = __builtin__.property(_get_igmp, _set_igmp)
  interface_vlan_ospf_conf = __builtin__.property(_get_interface_vlan_ospf_conf, _set_interface_vlan_ospf_conf)
  pim_intf_vlan_cont = __builtin__.property(_get_pim_intf_vlan_cont, _set_pim_intf_vlan_cont)


  _pyangbind_elements = {'ip_config': ip_config, 'ip_local_anycast_gateway': ip_local_anycast_gateway, 'interface_ve_dhcp_conf': interface_ve_dhcp_conf, 'icmp': icmp, 'igmp': igmp, 'interface_vlan_ospf_conf': interface_vlan_ospf_conf, 'pim_intf_vlan_cont': pim_intf_vlan_cont, }


