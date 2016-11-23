
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vrrp_rbridge_global(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vrrpv3 - based on the path /vrrp-rbridge-global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrrp_acceptmode_disable',)

  _yang_name = 'vrrp-rbridge-global'
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
    self.__vrrp_acceptmode_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-acceptmode-disable", rest_name="vrrp-acceptmode-disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable accept mode  for the non owner vrrp vip'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)

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
      return [u'vrrp-rbridge-global']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_vrrp_acceptmode_disable(self):
    """
    Getter method for vrrp_acceptmode_disable, mapped from YANG variable /vrrp_rbridge_global/vrrp_acceptmode_disable (empty)

    YANG Description: Disable accept mode  for the non owner vrrp vip
    """
    return self.__vrrp_acceptmode_disable
      
  def _set_vrrp_acceptmode_disable(self, v, load=False):
    """
    Setter method for vrrp_acceptmode_disable, mapped from YANG variable /vrrp_rbridge_global/vrrp_acceptmode_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrrp_acceptmode_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrrp_acceptmode_disable() directly.

    YANG Description: Disable accept mode  for the non owner vrrp vip
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="vrrp-acceptmode-disable", rest_name="vrrp-acceptmode-disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable accept mode  for the non owner vrrp vip'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrrp_acceptmode_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-acceptmode-disable", rest_name="vrrp-acceptmode-disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable accept mode  for the non owner vrrp vip'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)""",
        })

    self.__vrrp_acceptmode_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrrp_acceptmode_disable(self):
    self.__vrrp_acceptmode_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="vrrp-acceptmode-disable", rest_name="vrrp-acceptmode-disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable accept mode  for the non owner vrrp vip'}}, namespace='urn:brocade.com:mgmt:brocade-vrrpv3', defining_module='brocade-vrrpv3', yang_type='empty', is_config=True)

  vrrp_acceptmode_disable = __builtin__.property(_get_vrrp_acceptmode_disable, _set_vrrp_acceptmode_disable)


  _pyangbind_elements = {'vrrp_acceptmode_disable': vrrp_acceptmode_disable, }


