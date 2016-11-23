
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface
class servers(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/ipv6/interface-phy-dhcp-conf/dhcp/relay/servers. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__relay_ip_addr','__server_vrf_name','__interface',)

  _yang_name = 'servers'
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
    self.__relay_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="relay-ip-addr", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcp-ipv6-address', is_config=True)
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface.', u'cli-compact-syntax': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)
    self.__server_vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="server-vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF name of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='common-def:vrf-name', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'ipv6', u'interface-phy-dhcp-conf', u'dhcp', u'relay', u'servers']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'ipv6', u'dhcp', u'relay']

  def _get_relay_ip_addr(self):
    """
    Getter method for relay_ip_addr, mapped from YANG variable /interface/gigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/relay_ip_addr (dhcp-ipv6-address)

    YANG Description: DHCPv6 server IPv6 address
    """
    return self.__relay_ip_addr
      
  def _set_relay_ip_addr(self, v, load=False):
    """
    Setter method for relay_ip_addr, mapped from YANG variable /interface/gigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/relay_ip_addr (dhcp-ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_relay_ip_addr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_relay_ip_addr() directly.

    YANG Description: DHCPv6 server IPv6 address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="relay-ip-addr", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcp-ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """relay_ip_addr must be of a type compatible with dhcp-ipv6-address""",
          'defined-type': "brocade-dhcpv6:dhcp-ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="relay-ip-addr", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcp-ipv6-address', is_config=True)""",
        })

    self.__relay_ip_addr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_relay_ip_addr(self):
    self.__relay_ip_addr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="relay-ip-addr", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IPv6 address of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'address', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='dhcp-ipv6-address', is_config=True)


  def _get_server_vrf_name(self):
    """
    Getter method for server_vrf_name, mapped from YANG variable /interface/gigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/server_vrf_name (common-def:vrf-name)

    YANG Description: Name of the VRF that the DHCPv6 server is within
    """
    return self.__server_vrf_name
      
  def _set_server_vrf_name(self, v, load=False):
    """
    Setter method for server_vrf_name, mapped from YANG variable /interface/gigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/server_vrf_name (common-def:vrf-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server_vrf_name() directly.

    YANG Description: Name of the VRF that the DHCPv6 server is within
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="server-vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF name of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='common-def:vrf-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """server_vrf_name must be of a type compatible with common-def:vrf-name""",
          'defined-type': "common-def:vrf-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="server-vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF name of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='common-def:vrf-name', is_config=True)""",
        })

    self.__server_vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_server_vrf_name(self):
    self.__server_vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..32']}), is_leaf=True, yang_name="server-vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'VRF name of the DHCPv6 server', u'cli-run-template': u'ipv6 dhcp relay address$(relay-ip-addr) $($(server-vrf-name)==.?: use-vrf $(server-vrf-name))\n', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='common-def:vrf-name', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /interface/gigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/interface (container)

    YANG Description: Interface.
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /interface/gigabitethernet/ipv6/interface_phy_dhcp_conf/dhcp/relay/servers/interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Interface.
    """
    try:
      t = YANGDynClass(v,base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface.', u'cli-compact-syntax': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface.', u'cli-compact-syntax': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=interface.interface, is_container='container', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface.', u'cli-compact-syntax': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcpv6', defining_module='brocade-dhcpv6', yang_type='container', is_config=True)

  relay_ip_addr = __builtin__.property(_get_relay_ip_addr, _set_relay_ip_addr)
  server_vrf_name = __builtin__.property(_get_server_vrf_name, _set_server_vrf_name)
  interface = __builtin__.property(_get_interface, _set_interface)


  _pyangbind_elements = {'relay_ip_addr': relay_ip_addr, 'server_vrf_name': server_vrf_name, 'interface': interface, }


