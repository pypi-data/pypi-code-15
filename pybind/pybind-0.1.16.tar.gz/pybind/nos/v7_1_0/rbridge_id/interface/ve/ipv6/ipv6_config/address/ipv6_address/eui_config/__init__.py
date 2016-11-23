
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class eui_config(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/ve/ipv6/ipv6-config/address/ipv6-address/eui-config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__eui64','__eui_secondary',)

  _yang_name = 'eui-config'
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
    self.__eui64 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 address with an automatically computed EUI-64 interface Id', u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)
    self.__eui_secondary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="eui-secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Secondary eui-64 ipv6 address on an interface', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'interface', u've', u'ipv6', u'ipv6-config', u'address', u'ipv6-address', u'eui-config']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Ve', u'ipv6', u'address']

  def _get_eui64(self):
    """
    Getter method for eui64, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_config/address/ipv6_address/eui_config/eui64 (empty)
    """
    return self.__eui64
      
  def _set_eui64(self, v, load=False):
    """
    Setter method for eui64, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_config/address/ipv6_address/eui_config/eui64 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_eui64 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_eui64() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 address with an automatically computed EUI-64 interface Id', u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """eui64 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 address with an automatically computed EUI-64 interface Id', u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)""",
        })

    self.__eui64 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_eui64(self):
    self.__eui64 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="eui64", rest_name="eui-64", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ipv6 address with an automatically computed EUI-64 interface Id', u'alt-name': u'eui-64'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)


  def _get_eui_secondary(self):
    """
    Getter method for eui_secondary, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_config/address/ipv6_address/eui_config/eui_secondary (empty)
    """
    return self.__eui_secondary
      
  def _set_eui_secondary(self, v, load=False):
    """
    Setter method for eui_secondary, mapped from YANG variable /rbridge_id/interface/ve/ipv6/ipv6_config/address/ipv6_address/eui_config/eui_secondary (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_eui_secondary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_eui_secondary() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="eui-secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Secondary eui-64 ipv6 address on an interface', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """eui_secondary must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="eui-secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Secondary eui-64 ipv6 address on an interface', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)""",
        })

    self.__eui_secondary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_eui_secondary(self):
    self.__eui_secondary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="eui-secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Secondary eui-64 ipv6 address on an interface', u'alt-name': u'secondary'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='empty', is_config=True)

  eui64 = __builtin__.property(_get_eui64, _set_eui64)
  eui_secondary = __builtin__.property(_get_eui_secondary, _set_eui_secondary)


  _pyangbind_elements = {'eui64': eui64, 'eui_secondary': eui_secondary, }


