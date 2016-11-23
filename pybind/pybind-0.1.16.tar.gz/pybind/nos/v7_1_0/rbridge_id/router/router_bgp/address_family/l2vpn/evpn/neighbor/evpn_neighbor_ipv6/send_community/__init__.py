
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class send_community(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/l2vpn/evpn/neighbor/evpn-neighbor-ipv6/send-community. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__send_community_status','__both','__extended','__standard',)

  _yang_name = 'send-community'
  _rest_name = 'send-community'

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
    self.__both = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Send Standard and Extended Community attributes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__extended = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Extended Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(../extended?neighbor $(../../evpn-neighbor-ipv6-address) send-community extended\n:\\r)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__send_community_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="send-community-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?\\r:\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__standard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Standard Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(neighbor $(../../evpn-neighbor-ipv6-address) send-community standard\n)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor', u'evpn-neighbor-ipv6', u'send-community']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor', u'send-community']

  def _get_send_community_status(self):
    """
    Getter method for send_community_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/send_community_status (empty)
    """
    return self.__send_community_status
      
  def _set_send_community_status(self, v, load=False):
    """
    Setter method for send_community_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/send_community_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_community_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_community_status() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="send-community-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?\\r:\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_community_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="send-community-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?\\r:\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__send_community_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_community_status(self):
    self.__send_community_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="send-community-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?\\r:\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_both(self):
    """
    Getter method for both, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/both (empty)
    """
    return self.__both
      
  def _set_both(self, v, load=False):
    """
    Setter method for both, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/both (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_both is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_both() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Send Standard and Extended Community attributes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """both must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Send Standard and Extended Community attributes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__both = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_both(self):
    self.__both = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="both", rest_name="both", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Send Standard and Extended Community attributes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_extended(self):
    """
    Getter method for extended, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/extended (empty)
    """
    return self.__extended
      
  def _set_extended(self, v, load=False):
    """
    Setter method for extended, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/extended (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Extended Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(../extended?neighbor $(../../evpn-neighbor-ipv6-address) send-community extended\n:\\r)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Extended Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(../extended?neighbor $(../../evpn-neighbor-ipv6-address) send-community extended\n:\\r)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__extended = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended(self):
    self.__extended = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Extended Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(../extended?neighbor $(../../evpn-neighbor-ipv6-address) send-community extended\n:\\r)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_standard(self):
    """
    Getter method for standard, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/standard (empty)
    """
    return self.__standard
      
  def _set_standard(self, v, load=False):
    """
    Setter method for standard, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_neighbor_ipv6/send_community/standard (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_standard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_standard() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Standard Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(neighbor $(../../evpn-neighbor-ipv6-address) send-community standard\n)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """standard must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Standard Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(neighbor $(../../evpn-neighbor-ipv6-address) send-community standard\n)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__standard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_standard(self):
    self.__standard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send Standard Community attribute', u'cli-run-template': u'$(.?$(../both?\\r:$(neighbor $(../../evpn-neighbor-ipv6-address) send-community standard\n)):\\r)', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  send_community_status = __builtin__.property(_get_send_community_status, _set_send_community_status)
  both = __builtin__.property(_get_both, _set_both)
  extended = __builtin__.property(_get_extended, _set_extended)
  standard = __builtin__.property(_get_standard, _set_standard)


  _pyangbind_elements = {'send_community_status': send_community_status, 'both': both, 'extended': extended, 'standard': standard, }


