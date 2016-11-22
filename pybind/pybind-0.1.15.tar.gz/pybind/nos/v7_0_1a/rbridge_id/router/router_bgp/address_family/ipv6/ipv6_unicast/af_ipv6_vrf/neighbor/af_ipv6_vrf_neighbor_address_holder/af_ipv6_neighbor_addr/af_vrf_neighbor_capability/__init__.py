
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import as4
import orf
import additional_paths
class af_vrf_neighbor_capability(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/neighbor/af-ipv6-vrf-neighbor-address-holder/af-ipv6-neighbor-addr/af-vrf-neighbor-capability. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__as4','__orf','__additional_paths',)

  _yang_name = 'af-vrf-neighbor-capability'
  _rest_name = 'capability'

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
    self.__orf = YANGDynClass(base=orf.orf, is_container='container', yang_name="orf", rest_name="orf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise ORF capability to the peer', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__additional_paths = YANGDynClass(base=additional_paths.additional_paths, is_container='container', yang_name="additional-paths", rest_name="additional-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Capability additional paths', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__as4 = YANGDynClass(base=as4.as4, is_container='container', yang_name="as4", rest_name="as4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set AS4 capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'neighbor', u'af-ipv6-vrf-neighbor-address-holder', u'af-ipv6-neighbor-addr', u'af-vrf-neighbor-capability']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'neighbor', u'capability']

  def _get_as4(self):
    """
    Getter method for as4, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/af_vrf_neighbor_capability/as4 (container)
    """
    return self.__as4
      
  def _set_as4(self, v, load=False):
    """
    Setter method for as4, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/af_vrf_neighbor_capability/as4 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as4 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as4() directly.
    """
    try:
      t = YANGDynClass(v,base=as4.as4, is_container='container', yang_name="as4", rest_name="as4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set AS4 capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as4 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=as4.as4, is_container='container', yang_name="as4", rest_name="as4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set AS4 capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__as4 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as4(self):
    self.__as4 = YANGDynClass(base=as4.as4, is_container='container', yang_name="as4", rest_name="as4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set AS4 capability', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_orf(self):
    """
    Getter method for orf, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/af_vrf_neighbor_capability/orf (container)
    """
    return self.__orf
      
  def _set_orf(self, v, load=False):
    """
    Setter method for orf, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/af_vrf_neighbor_capability/orf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_orf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_orf() directly.
    """
    try:
      t = YANGDynClass(v,base=orf.orf, is_container='container', yang_name="orf", rest_name="orf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise ORF capability to the peer', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """orf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=orf.orf, is_container='container', yang_name="orf", rest_name="orf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise ORF capability to the peer', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__orf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_orf(self):
    self.__orf = YANGDynClass(base=orf.orf, is_container='container', yang_name="orf", rest_name="orf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise ORF capability to the peer', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_additional_paths(self):
    """
    Getter method for additional_paths, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/af_vrf_neighbor_capability/additional_paths (container)
    """
    return self.__additional_paths
      
  def _set_additional_paths(self, v, load=False):
    """
    Setter method for additional_paths, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/af_vrf_neighbor_capability/additional_paths (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_additional_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_additional_paths() directly.
    """
    try:
      t = YANGDynClass(v,base=additional_paths.additional_paths, is_container='container', yang_name="additional-paths", rest_name="additional-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Capability additional paths', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """additional_paths must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=additional_paths.additional_paths, is_container='container', yang_name="additional-paths", rest_name="additional-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Capability additional paths', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__additional_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_additional_paths(self):
    self.__additional_paths = YANGDynClass(base=additional_paths.additional_paths, is_container='container', yang_name="additional-paths", rest_name="additional-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Capability additional paths', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  as4 = __builtin__.property(_get_as4, _set_as4)
  orf = __builtin__.property(_get_orf, _set_orf)
  additional_paths = __builtin__.property(_get_additional_paths, _set_additional_paths)


  _pyangbind_elements = {'as4': as4, 'orf': orf, 'additional_paths': additional_paths, }


