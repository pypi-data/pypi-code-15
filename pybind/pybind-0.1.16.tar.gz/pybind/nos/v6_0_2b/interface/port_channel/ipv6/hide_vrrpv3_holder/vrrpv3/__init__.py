
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import virtual_ip
import track
class vrrpv3(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/ipv6/hide-vrrpv3-holder/vrrpv3. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrid','__virtual_ip','__track','__advertisement_interval','__enable','__hold_time','__preempt_mode','__priority','__description',)

  _yang_name = 'vrrpv3'
  _rest_name = 'vrrp-group'

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
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface specific description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='string', is_config=True)
    self.__track = YANGDynClass(base=track.track, is_container='container', yang_name="track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to be tracked', u'callpoint': u'vrrpv3TrackPo', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)
    self.__vrid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrid", rest_name="vrid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='vrid-type', is_config=True)
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set router priority within virtual router'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)
    self.__advertisement_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..40900']}), is_leaf=True, yang_name="advertisement-interval", rest_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set advertisement interval'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)
    self.__virtual_ip = YANGDynClass(base=YANGListType("virtual_ipaddr",virtual_ip.virtual_ip, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-ipaddr', extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}), is_container='list', yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure hold time for this session'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)
    self.__preempt_mode = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="preempt-mode", rest_name="preempt-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set preempt mode for the session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)

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
      return [u'interface', u'port-channel', u'ipv6', u'hide-vrrpv3-holder', u'vrrpv3']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'ipv6', u'vrrp-group']

  def _get_vrid(self):
    """
    Getter method for vrid, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/vrid (vrid-type)
    """
    return self.__vrid
      
  def _set_vrid(self, v, load=False):
    """
    Setter method for vrid, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/vrid (vrid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrid() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrid", rest_name="vrid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='vrid-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrid must be of a type compatible with vrid-type""",
          'defined-type': "brocade-vrrpv3:vrid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrid", rest_name="vrid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='vrid-type', is_config=True)""",
        })

    self.__vrid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrid(self):
    self.__vrid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="vrid", rest_name="vrid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='vrid-type', is_config=True)


  def _get_virtual_ip(self):
    """
    Getter method for virtual_ip, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/virtual_ip (list)
    """
    return self.__virtual_ip
      
  def _set_virtual_ip(self, v, load=False):
    """
    Setter method for virtual_ip, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/virtual_ip (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("virtual_ipaddr",virtual_ip.virtual_ip, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-ipaddr', extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}), is_container='list', yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_ip must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("virtual_ipaddr",virtual_ip.virtual_ip, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-ipaddr', extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}), is_container='list', yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)""",
        })

    self.__virtual_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_ip(self):
    self.__virtual_ip = YANGDynClass(base=YANGListType("virtual_ipaddr",virtual_ip.virtual_ip, yang_name="virtual-ip", rest_name="virtual-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='virtual-ipaddr', extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}), is_container='list', yang_name="virtual-ip", rest_name="virtual-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set virtual IPv6 address', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-full-no': None, u'cli-no-match-completion': None, u'callpoint': u'vrrpv3VirtualIPPo'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='list', is_config=True)


  def _get_track(self):
    """
    Getter method for track, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/track (container)

    YANG Description: Interface to be tracked
    """
    return self.__track
      
  def _set_track(self, v, load=False):
    """
    Setter method for track, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/track (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_track is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_track() directly.

    YANG Description: Interface to be tracked
    """
    try:
      t = YANGDynClass(v,base=track.track, is_container='container', yang_name="track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to be tracked', u'callpoint': u'vrrpv3TrackPo', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """track must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=track.track, is_container='container', yang_name="track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to be tracked', u'callpoint': u'vrrpv3TrackPo', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)""",
        })

    self.__track = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_track(self):
    self.__track = YANGDynClass(base=track.track, is_container='container', yang_name="track", rest_name="track", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface to be tracked', u'callpoint': u'vrrpv3TrackPo', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='container', is_config=True)


  def _get_advertisement_interval(self):
    """
    Getter method for advertisement_interval, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/advertisement_interval (uint32)

    YANG Description: Set advertisement interval
    """
    return self.__advertisement_interval
      
  def _set_advertisement_interval(self, v, load=False):
    """
    Setter method for advertisement_interval, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/advertisement_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_advertisement_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_advertisement_interval() directly.

    YANG Description: Set advertisement interval
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..40900']}), is_leaf=True, yang_name="advertisement-interval", rest_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set advertisement interval'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """advertisement_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..40900']}), is_leaf=True, yang_name="advertisement-interval", rest_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set advertisement interval'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)""",
        })

    self.__advertisement_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_advertisement_interval(self):
    self.__advertisement_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..40900']}), is_leaf=True, yang_name="advertisement-interval", rest_name="advertisement-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set advertisement interval'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)


  def _get_enable(self):
    """
    Getter method for enable, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/enable (empty)

    YANG Description: Enable Session
    """
    return self.__enable
      
  def _set_enable(self, v, load=False):
    """
    Setter method for enable, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable() directly.

    YANG Description: Enable Session
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)""",
        })

    self.__enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable(self):
    self.__enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable Session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)


  def _get_hold_time(self):
    """
    Getter method for hold_time, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/hold_time (uint32)

    YANG Description: Configure hold time for this session
    """
    return self.__hold_time
      
  def _set_hold_time(self, v, load=False):
    """
    Setter method for hold_time, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/hold_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hold_time() directly.

    YANG Description: Configure hold time for this session
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure hold time for this session'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hold_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure hold time for this session'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)""",
        })

    self.__hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hold_time(self):
    self.__hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="hold-time", rest_name="hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure hold time for this session'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint32', is_config=True)


  def _get_preempt_mode(self):
    """
    Getter method for preempt_mode, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/preempt_mode (empty)

    YANG Description: Set preempt mode for the session
    """
    return self.__preempt_mode
      
  def _set_preempt_mode(self, v, load=False):
    """
    Setter method for preempt_mode, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/preempt_mode (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_preempt_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_preempt_mode() directly.

    YANG Description: Set preempt mode for the session
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="preempt-mode", rest_name="preempt-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set preempt mode for the session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """preempt_mode must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="preempt-mode", rest_name="preempt-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set preempt mode for the session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)""",
        })

    self.__preempt_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_preempt_mode(self):
    self.__preempt_mode = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="preempt-mode", rest_name="preempt-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set preempt mode for the session', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/priority (uint8)

    YANG Description: Set router priority within virtual router
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/priority (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.

    YANG Description: Set router priority within virtual router
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set router priority within virtual router'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set router priority within virtual router'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1..254']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set router priority within virtual router'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='uint8', is_config=True)


  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/description (string)

    YANG Description: Interface specific description
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /interface/port_channel/ipv6/hide_vrrpv3_holder/vrrpv3/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.

    YANG Description: Interface specific description
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface specific description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface specific description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface specific description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='string', is_config=True)

  vrid = __builtin__.property(_get_vrid, _set_vrid)
  virtual_ip = __builtin__.property(_get_virtual_ip, _set_virtual_ip)
  track = __builtin__.property(_get_track, _set_track)
  advertisement_interval = __builtin__.property(_get_advertisement_interval, _set_advertisement_interval)
  enable = __builtin__.property(_get_enable, _set_enable)
  hold_time = __builtin__.property(_get_hold_time, _set_hold_time)
  preempt_mode = __builtin__.property(_get_preempt_mode, _set_preempt_mode)
  priority = __builtin__.property(_get_priority, _set_priority)
  description = __builtin__.property(_get_description, _set_description)


  _pyangbind_elements = {'vrid': vrid, 'virtual_ip': virtual_ip, 'track': track, 'advertisement_interval': advertisement_interval, 'enable': enable, 'hold_time': hold_time, 'preempt_mode': preempt_mode, 'priority': priority, 'description': description, }


