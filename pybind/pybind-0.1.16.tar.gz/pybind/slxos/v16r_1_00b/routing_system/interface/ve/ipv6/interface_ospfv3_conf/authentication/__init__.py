
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipsec_auth_key_config
import ipsec
class authentication(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/interface-ospfv3-conf/authentication. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure ipsec authentication for the interface.The interface IPsec configuration takes precedence over the area IPsec configuration when an area and an interface within that area use IPsec. Therefore, if you configure IPsec for an interface and an area configuration also exists that includes this interface, the interface's IPsec configuration is used by that interface. However, if you disable IPsec on an interface, IPsec is disabled on the interface even if the interface has its own, specific authentication.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipsec_auth_key_config','__ipsec',)

  _yang_name = 'authentication'
  _rest_name = 'authentication'

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
    self.__ipsec_auth_key_config = YANGDynClass(base=ipsec_auth_key_config.ipsec_auth_key_config, is_container='container', yang_name="ipsec-auth-key-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__ipsec = YANGDynClass(base=ipsec.ipsec, is_container='container', yang_name="ipsec", rest_name="ipsec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipsec authentication for the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'interface-ospfv3-conf', u'authentication']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'ospf', u'authentication']

  def _get_ipsec_auth_key_config(self):
    """
    Getter method for ipsec_auth_key_config, mapped from YANG variable /routing_system/interface/ve/ipv6/interface_ospfv3_conf/authentication/ipsec_auth_key_config (container)
    """
    return self.__ipsec_auth_key_config
      
  def _set_ipsec_auth_key_config(self, v, load=False):
    """
    Setter method for ipsec_auth_key_config, mapped from YANG variable /routing_system/interface/ve/ipv6/interface_ospfv3_conf/authentication/ipsec_auth_key_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipsec_auth_key_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipsec_auth_key_config() directly.
    """
    try:
      t = YANGDynClass(v,base=ipsec_auth_key_config.ipsec_auth_key_config, is_container='container', yang_name="ipsec-auth-key-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipsec_auth_key_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipsec_auth_key_config.ipsec_auth_key_config, is_container='container', yang_name="ipsec-auth-key-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__ipsec_auth_key_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipsec_auth_key_config(self):
    self.__ipsec_auth_key_config = YANGDynClass(base=ipsec_auth_key_config.ipsec_auth_key_config, is_container='container', yang_name="ipsec-auth-key-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)


  def _get_ipsec(self):
    """
    Getter method for ipsec, mapped from YANG variable /routing_system/interface/ve/ipv6/interface_ospfv3_conf/authentication/ipsec (container)

    YANG Description: Configure ipsec authentication for the interface
    """
    return self.__ipsec
      
  def _set_ipsec(self, v, load=False):
    """
    Setter method for ipsec, mapped from YANG variable /routing_system/interface/ve/ipv6/interface_ospfv3_conf/authentication/ipsec (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipsec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipsec() directly.

    YANG Description: Configure ipsec authentication for the interface
    """
    try:
      t = YANGDynClass(v,base=ipsec.ipsec, is_container='container', yang_name="ipsec", rest_name="ipsec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipsec authentication for the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipsec must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipsec.ipsec, is_container='container', yang_name="ipsec", rest_name="ipsec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipsec authentication for the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__ipsec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipsec(self):
    self.__ipsec = YANGDynClass(base=ipsec.ipsec, is_container='container', yang_name="ipsec", rest_name="ipsec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipsec authentication for the interface'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  ipsec_auth_key_config = __builtin__.property(_get_ipsec_auth_key_config, _set_ipsec_auth_key_config)
  ipsec = __builtin__.property(_get_ipsec, _set_ipsec)


  _pyangbind_elements = {'ipsec_auth_key_config': ipsec_auth_key_config, 'ipsec': ipsec, }


