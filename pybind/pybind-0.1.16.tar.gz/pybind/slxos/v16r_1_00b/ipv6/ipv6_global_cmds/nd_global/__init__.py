
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dad
import dns_server_global
import domain_name_global
class nd_global(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ipv6/ipv6-global-cmds/nd-global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dad','__global_suppress_ra','__dns_server_global','__domain_name_global',)

  _yang_name = 'nd-global'
  _rest_name = 'nd'

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
    self.__dad = YANGDynClass(base=dad.dad, is_container='container', yang_name="dad", rest_name="dad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'duplicate address detection', u'hidden': u'full', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    self.__global_suppress_ra = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-suppress-ra", rest_name="global-suppress-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Globally suppress-ra', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__dns_server_global = YANGDynClass(base=YANGListType("dns_server_prefix_global",dns_server_global.dns_server_global, yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dns-server-prefix-global', extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}), is_container='list', yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)
    self.__domain_name_global = YANGDynClass(base=YANGListType("domain_name_string_global",domain_name_global.domain_name_global, yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name-string-global', extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}), is_container='list', yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)

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
      return [u'ipv6', u'ipv6-global-cmds', u'nd-global']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6', u'nd']

  def _get_dad(self):
    """
    Getter method for dad, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dad (container)
    """
    return self.__dad
      
  def _set_dad(self, v, load=False):
    """
    Setter method for dad, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dad (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dad is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dad() directly.
    """
    try:
      t = YANGDynClass(v,base=dad.dad, is_container='container', yang_name="dad", rest_name="dad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'duplicate address detection', u'hidden': u'full', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dad must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dad.dad, is_container='container', yang_name="dad", rest_name="dad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'duplicate address detection', u'hidden': u'full', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)""",
        })

    self.__dad = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dad(self):
    self.__dad = YANGDynClass(base=dad.dad, is_container='container', yang_name="dad", rest_name="dad", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'duplicate address detection', u'hidden': u'full', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)


  def _get_global_suppress_ra(self):
    """
    Getter method for global_suppress_ra, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/global_suppress_ra (empty)
    """
    return self.__global_suppress_ra
      
  def _set_global_suppress_ra(self, v, load=False):
    """
    Setter method for global_suppress_ra, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/global_suppress_ra (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_global_suppress_ra is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_global_suppress_ra() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="global-suppress-ra", rest_name="global-suppress-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Globally suppress-ra', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """global_suppress_ra must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-suppress-ra", rest_name="global-suppress-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Globally suppress-ra', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__global_suppress_ra = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_global_suppress_ra(self):
    self.__global_suppress_ra = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="global-suppress-ra", rest_name="global-suppress-ra", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set Globally suppress-ra', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_dns_server_global(self):
    """
    Getter method for dns_server_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dns_server_global (list)
    """
    return self.__dns_server_global
      
  def _set_dns_server_global(self, v, load=False):
    """
    Setter method for dns_server_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/dns_server_global (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dns_server_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dns_server_global() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("dns_server_prefix_global",dns_server_global.dns_server_global, yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dns-server-prefix-global', extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}), is_container='list', yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dns_server_global must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("dns_server_prefix_global",dns_server_global.dns_server_global, yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dns-server-prefix-global', extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}), is_container='list', yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)""",
        })

    self.__dns_server_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dns_server_global(self):
    self.__dns_server_global = YANGDynClass(base=YANGListType("dns_server_prefix_global",dns_server_global.dns_server_global, yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='dns-server-prefix-global', extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}), is_container='list', yang_name="dns-server-global", rest_name="ra-dns-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global DNS server option applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'ra-dns-server', u'cli-suppress-key-abbreviation': None, u'callpoint': u'IpV6NdRaDnsServerGlobal'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)


  def _get_domain_name_global(self):
    """
    Getter method for domain_name_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/domain_name_global (list)
    """
    return self.__domain_name_global
      
  def _set_domain_name_global(self, v, load=False):
    """
    Setter method for domain_name_global, mapped from YANG variable /ipv6/ipv6_global_cmds/nd_global/domain_name_global (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domain_name_global is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domain_name_global() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("domain_name_string_global",domain_name_global.domain_name_global, yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name-string-global', extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}), is_container='list', yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domain_name_global must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("domain_name_string_global",domain_name_global.domain_name_global, yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name-string-global', extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}), is_container='list', yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)""",
        })

    self.__domain_name_global = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domain_name_global(self):
    self.__domain_name_global = YANGDynClass(base=YANGListType("domain_name_string_global",domain_name_global.domain_name_global, yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='domain-name-string-global', extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}), is_container='list', yang_name="domain-name-global", rest_name="ra-domain-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set global domain name option that applied on all ND6 interfaces', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'callpoint': u'IpV6NdRaDomainNameGlobal', u'cli-suppress-key-abbreviation': None, u'alt-name': u'ra-domain-name'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)

  dad = __builtin__.property(_get_dad, _set_dad)
  global_suppress_ra = __builtin__.property(_get_global_suppress_ra, _set_global_suppress_ra)
  dns_server_global = __builtin__.property(_get_dns_server_global, _set_dns_server_global)
  domain_name_global = __builtin__.property(_get_domain_name_global, _set_domain_name_global)


  _pyangbind_elements = {'dad': dad, 'global_suppress_ra': global_suppress_ra, 'dns_server_global': dns_server_global, 'domain_name_global': domain_name_global, }


