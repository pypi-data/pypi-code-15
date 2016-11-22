
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class suppressing_address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/ipv6-nd-ra/ipv6-intf-cmds/nd/address/suppressing-address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__suppress_ipv6_address','__suppress_per_address',)

  _yang_name = 'suppressing-address'
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
    self.__suppress_per_address = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-per-address", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress all IPv6 addresses in router advertisement', u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__suppress_ipv6_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="suppress-ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds', u'nd', u'address', u'suppressing-address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'nd', u'address']

  def _get_suppress_ipv6_address(self):
    """
    Getter method for suppress_ipv6_address, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/suppressing_address/suppress_ipv6_address (inet:ipv6-address)
    """
    return self.__suppress_ipv6_address
      
  def _set_suppress_ipv6_address(self, v, load=False):
    """
    Setter method for suppress_ipv6_address, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/suppressing_address/suppress_ipv6_address (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_ipv6_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_ipv6_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="suppress-ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_ipv6_address must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="suppress-ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__suppress_ipv6_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_ipv6_address(self):
    self.__suppress_ipv6_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="suppress-ipv6-address", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='inet:ipv6-address', is_config=True)


  def _get_suppress_per_address(self):
    """
    Getter method for suppress_per_address, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/suppressing_address/suppress_per_address (empty)
    """
    return self.__suppress_per_address
      
  def _set_suppress_per_address(self, v, load=False):
    """
    Setter method for suppress_per_address, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/suppressing_address/suppress_per_address (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_per_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_per_address() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="suppress-per-address", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress all IPv6 addresses in router advertisement', u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_per_address must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-per-address", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress all IPv6 addresses in router advertisement', u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__suppress_per_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_per_address(self):
    self.__suppress_per_address = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="suppress-per-address", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Suppress all IPv6 addresses in router advertisement', u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

  suppress_ipv6_address = __builtin__.property(_get_suppress_ipv6_address, _set_suppress_ipv6_address)
  suppress_per_address = __builtin__.property(_get_suppress_per_address, _set_suppress_per_address)


  _pyangbind_elements = {'suppress_ipv6_address': suppress_ipv6_address, 'suppress_per_address': suppress_per_address, }


