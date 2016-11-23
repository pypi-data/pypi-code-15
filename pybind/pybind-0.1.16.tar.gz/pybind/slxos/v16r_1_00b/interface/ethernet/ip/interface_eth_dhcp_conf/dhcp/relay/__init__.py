
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import servers
class relay(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/ip/interface-eth-dhcp-conf/dhcp/relay. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__servers','__gateway',)

  _yang_name = 'relay'
  _rest_name = 'relay'

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
    self.__gateway = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Gateway address', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='dhcp-ipv4-address', is_config=True)
    self.__servers = YANGDynClass(base=YANGListType("relay_ip_addr server_vrf_name",servers.servers, yang_name="servers", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='relay-ip-addr server-vrf-name', extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}), is_container='list', yang_name="servers", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='list', is_config=True)

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
      return [u'interface', u'ethernet', u'ip', u'interface-eth-dhcp-conf', u'dhcp', u'relay']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'ip', u'dhcp', u'relay']

  def _get_servers(self):
    """
    Getter method for servers, mapped from YANG variable /interface/ethernet/ip/interface_eth_dhcp_conf/dhcp/relay/servers (list)
    """
    return self.__servers
      
  def _set_servers(self, v, load=False):
    """
    Setter method for servers, mapped from YANG variable /interface/ethernet/ip/interface_eth_dhcp_conf/dhcp/relay/servers (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_servers is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_servers() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("relay_ip_addr server_vrf_name",servers.servers, yang_name="servers", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='relay-ip-addr server-vrf-name', extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}), is_container='list', yang_name="servers", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """servers must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("relay_ip_addr server_vrf_name",servers.servers, yang_name="servers", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='relay-ip-addr server-vrf-name', extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}), is_container='list', yang_name="servers", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='list', is_config=True)""",
        })

    self.__servers = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_servers(self):
    self.__servers = YANGDynClass(base=YANGListType("relay_ip_addr server_vrf_name",servers.servers, yang_name="servers", rest_name="", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='relay-ip-addr server-vrf-name', extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}), is_container='list', yang_name="servers", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'DHCP Server IP Address', u'cli-run-template-enter': u' ip dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-drop-node-name': None, u'callpoint': u'DHCPRelayPhyInterfaceCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='list', is_config=True)


  def _get_gateway(self):
    """
    Getter method for gateway, mapped from YANG variable /interface/ethernet/ip/interface_eth_dhcp_conf/dhcp/relay/gateway (dhcp-ipv4-address)

    YANG Description: Gateway address
    """
    return self.__gateway
      
  def _set_gateway(self, v, load=False):
    """
    Setter method for gateway, mapped from YANG variable /interface/ethernet/ip/interface_eth_dhcp_conf/dhcp/relay/gateway (dhcp-ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gateway() directly.

    YANG Description: Gateway address
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Gateway address', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='dhcp-ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gateway must be of a type compatible with dhcp-ipv4-address""",
          'defined-type': "brocade-dhcp:dhcp-ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Gateway address', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='dhcp-ipv4-address', is_config=True)""",
        })

    self.__gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gateway(self):
    self.__gateway = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="gateway", rest_name="gateway", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Gateway address', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='dhcp-ipv4-address', is_config=True)

  servers = __builtin__.property(_get_servers, _set_servers)
  gateway = __builtin__.property(_get_gateway, _set_gateway)


  _pyangbind_elements = {'servers': servers, 'gateway': gateway, }


