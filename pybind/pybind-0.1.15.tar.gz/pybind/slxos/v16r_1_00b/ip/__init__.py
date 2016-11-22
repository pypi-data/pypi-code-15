
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import icmp
import dns
import hide_prefix_holder
import hide_as_path_holder
import hide_community_list_holder
import hide_ext_community_list_holder
import rtm_config
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__icmp','__dns','__hide_prefix_holder','__hide_as_path_holder','__hide_community_list_holder','__hide_ext_community_list_holder','__rtm_config',)

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
    self.__hide_prefix_holder = YANGDynClass(base=hide_prefix_holder.hide_prefix_holder, is_container='container', yang_name="hide-prefix-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__rtm_config = YANGDynClass(base=rtm_config.rtm_config, is_container='container', yang_name="rtm-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'rtm-config'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)
    self.__hide_community_list_holder = YANGDynClass(base=hide_community_list_holder.hide_community_list_holder, is_container='container', yang_name="hide-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__hide_ext_community_list_holder = YANGDynClass(base=hide_ext_community_list_holder.hide_ext_community_list_holder, is_container='container', yang_name="hide-ext-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__hide_as_path_holder = YANGDynClass(base=hide_as_path_holder.hide_as_path_holder, is_container='container', yang_name="hide-as-path-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    self.__dns = YANGDynClass(base=dns.dns, is_container='container', yang_name="dns", rest_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain Name System (DNS) Server configurations\nin the system.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-administration', defining_module='brocade-ip-administration', yang_type='container', is_config=True)
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'hidden': u'full', u'callpoint': u'IcmpConfig'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)

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
      return [u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ip']

  def _get_icmp(self):
    """
    Getter method for icmp, mapped from YANG variable /ip/icmp (container)
    """
    return self.__icmp
      
  def _set_icmp(self, v, load=False):
    """
    Setter method for icmp, mapped from YANG variable /ip/icmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp() directly.
    """
    try:
      t = YANGDynClass(v,base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'hidden': u'full', u'callpoint': u'IcmpConfig'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'hidden': u'full', u'callpoint': u'IcmpConfig'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)""",
        })

    self.__icmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp(self):
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Internet Control Message Protocol(ICMP)', u'hidden': u'full', u'callpoint': u'IcmpConfig'}}, namespace='urn:brocade.com:mgmt:brocade-icmp', defining_module='brocade-icmp', yang_type='container', is_config=True)


  def _get_dns(self):
    """
    Getter method for dns, mapped from YANG variable /ip/dns (container)
    """
    return self.__dns
      
  def _set_dns(self, v, load=False):
    """
    Setter method for dns, mapped from YANG variable /ip/dns (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dns is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dns() directly.
    """
    try:
      t = YANGDynClass(v,base=dns.dns, is_container='container', yang_name="dns", rest_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain Name System (DNS) Server configurations\nin the system.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-administration', defining_module='brocade-ip-administration', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dns must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dns.dns, is_container='container', yang_name="dns", rest_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain Name System (DNS) Server configurations\nin the system.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-administration', defining_module='brocade-ip-administration', yang_type='container', is_config=True)""",
        })

    self.__dns = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dns(self):
    self.__dns = YANGDynClass(base=dns.dns, is_container='container', yang_name="dns", rest_name="dns", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain Name System (DNS) Server configurations\nin the system.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-administration', defining_module='brocade-ip-administration', yang_type='container', is_config=True)


  def _get_hide_prefix_holder(self):
    """
    Getter method for hide_prefix_holder, mapped from YANG variable /ip/hide_prefix_holder (container)
    """
    return self.__hide_prefix_holder
      
  def _set_hide_prefix_holder(self, v, load=False):
    """
    Setter method for hide_prefix_holder, mapped from YANG variable /ip/hide_prefix_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hide_prefix_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hide_prefix_holder() directly.
    """
    try:
      t = YANGDynClass(v,base=hide_prefix_holder.hide_prefix_holder, is_container='container', yang_name="hide-prefix-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hide_prefix_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hide_prefix_holder.hide_prefix_holder, is_container='container', yang_name="hide-prefix-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__hide_prefix_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hide_prefix_holder(self):
    self.__hide_prefix_holder = YANGDynClass(base=hide_prefix_holder.hide_prefix_holder, is_container='container', yang_name="hide-prefix-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_hide_as_path_holder(self):
    """
    Getter method for hide_as_path_holder, mapped from YANG variable /ip/hide_as_path_holder (container)
    """
    return self.__hide_as_path_holder
      
  def _set_hide_as_path_holder(self, v, load=False):
    """
    Setter method for hide_as_path_holder, mapped from YANG variable /ip/hide_as_path_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hide_as_path_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hide_as_path_holder() directly.
    """
    try:
      t = YANGDynClass(v,base=hide_as_path_holder.hide_as_path_holder, is_container='container', yang_name="hide-as-path-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hide_as_path_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hide_as_path_holder.hide_as_path_holder, is_container='container', yang_name="hide-as-path-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__hide_as_path_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hide_as_path_holder(self):
    self.__hide_as_path_holder = YANGDynClass(base=hide_as_path_holder.hide_as_path_holder, is_container='container', yang_name="hide-as-path-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_hide_community_list_holder(self):
    """
    Getter method for hide_community_list_holder, mapped from YANG variable /ip/hide_community_list_holder (container)
    """
    return self.__hide_community_list_holder
      
  def _set_hide_community_list_holder(self, v, load=False):
    """
    Setter method for hide_community_list_holder, mapped from YANG variable /ip/hide_community_list_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hide_community_list_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hide_community_list_holder() directly.
    """
    try:
      t = YANGDynClass(v,base=hide_community_list_holder.hide_community_list_holder, is_container='container', yang_name="hide-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hide_community_list_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hide_community_list_holder.hide_community_list_holder, is_container='container', yang_name="hide-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__hide_community_list_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hide_community_list_holder(self):
    self.__hide_community_list_holder = YANGDynClass(base=hide_community_list_holder.hide_community_list_holder, is_container='container', yang_name="hide-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_hide_ext_community_list_holder(self):
    """
    Getter method for hide_ext_community_list_holder, mapped from YANG variable /ip/hide_ext_community_list_holder (container)
    """
    return self.__hide_ext_community_list_holder
      
  def _set_hide_ext_community_list_holder(self, v, load=False):
    """
    Setter method for hide_ext_community_list_holder, mapped from YANG variable /ip/hide_ext_community_list_holder (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hide_ext_community_list_holder is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hide_ext_community_list_holder() directly.
    """
    try:
      t = YANGDynClass(v,base=hide_ext_community_list_holder.hide_ext_community_list_holder, is_container='container', yang_name="hide-ext-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hide_ext_community_list_holder must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=hide_ext_community_list_holder.hide_ext_community_list_holder, is_container='container', yang_name="hide-ext-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)""",
        })

    self.__hide_ext_community_list_holder = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hide_ext_community_list_holder(self):
    self.__hide_ext_community_list_holder = YANGDynClass(base=hide_ext_community_list_holder.hide_ext_community_list_holder, is_container='container', yang_name="hide-ext-community-list-holder", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='container', is_config=True)


  def _get_rtm_config(self):
    """
    Getter method for rtm_config, mapped from YANG variable /ip/rtm_config (container)
    """
    return self.__rtm_config
      
  def _set_rtm_config(self, v, load=False):
    """
    Setter method for rtm_config, mapped from YANG variable /ip/rtm_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rtm_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rtm_config() directly.
    """
    try:
      t = YANGDynClass(v,base=rtm_config.rtm_config, is_container='container', yang_name="rtm-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'rtm-config'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rtm_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rtm_config.rtm_config, is_container='container', yang_name="rtm-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'rtm-config'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)""",
        })

    self.__rtm_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rtm_config(self):
    self.__rtm_config = YANGDynClass(base=rtm_config.rtm_config, is_container='container', yang_name="rtm-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'rtm-config'}}, namespace='urn:brocade.com:mgmt:brocade-rtm', defining_module='brocade-rtm', yang_type='container', is_config=True)

  icmp = __builtin__.property(_get_icmp, _set_icmp)
  dns = __builtin__.property(_get_dns, _set_dns)
  hide_prefix_holder = __builtin__.property(_get_hide_prefix_holder, _set_hide_prefix_holder)
  hide_as_path_holder = __builtin__.property(_get_hide_as_path_holder, _set_hide_as_path_holder)
  hide_community_list_holder = __builtin__.property(_get_hide_community_list_holder, _set_hide_community_list_holder)
  hide_ext_community_list_holder = __builtin__.property(_get_hide_ext_community_list_holder, _set_hide_ext_community_list_holder)
  rtm_config = __builtin__.property(_get_rtm_config, _set_rtm_config)


  _pyangbind_elements = {'icmp': icmp, 'dns': dns, 'hide_prefix_holder': hide_prefix_holder, 'hide_as_path_holder': hide_as_path_holder, 'hide_community_list_holder': hide_community_list_holder, 'hide_ext_community_list_holder': hide_ext_community_list_holder, 'rtm_config': rtm_config, }


