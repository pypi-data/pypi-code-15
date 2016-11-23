
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import prefixlist
class orf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv4/ipv4-unicast/default-vrf/neighbor/af-ipv4-neighbor-address-holder/af-ipv4-neighbor-address/af-neighbor-capability/orf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__prefixlist',)

  _yang_name = 'orf'
  _rest_name = 'orf'

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
    self.__prefixlist = YANGDynClass(base=prefixlist.prefixlist, is_container='container', yang_name="prefixlist", rest_name="prefixlist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise prefixlist ORF capability to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf', u'neighbor', u'af-ipv4-neighbor-address-holder', u'af-ipv4-neighbor-address', u'af-neighbor-capability', u'orf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'neighbor', u'capability', u'orf']

  def _get_prefixlist(self):
    """
    Getter method for prefixlist, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_address_holder/af_ipv4_neighbor_address/af_neighbor_capability/orf/prefixlist (container)
    """
    return self.__prefixlist
      
  def _set_prefixlist(self, v, load=False):
    """
    Setter method for prefixlist, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_address_holder/af_ipv4_neighbor_address/af_neighbor_capability/orf/prefixlist (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefixlist is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefixlist() directly.
    """
    try:
      t = YANGDynClass(v,base=prefixlist.prefixlist, is_container='container', yang_name="prefixlist", rest_name="prefixlist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise prefixlist ORF capability to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefixlist must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefixlist.prefixlist, is_container='container', yang_name="prefixlist", rest_name="prefixlist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise prefixlist ORF capability to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__prefixlist = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefixlist(self):
    self.__prefixlist = YANGDynClass(base=prefixlist.prefixlist, is_container='container', yang_name="prefixlist", rest_name="prefixlist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise prefixlist ORF capability to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  prefixlist = __builtin__.property(_get_prefixlist, _set_prefixlist)


  _pyangbind_elements = {'prefixlist': prefixlist, }


