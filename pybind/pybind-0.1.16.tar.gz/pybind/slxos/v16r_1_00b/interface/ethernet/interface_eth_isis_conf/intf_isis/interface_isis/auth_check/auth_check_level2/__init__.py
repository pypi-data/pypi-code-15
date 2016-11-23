
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class auth_check_level2(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/interface-eth-isis-conf/intf-isis/interface-isis/auth-check/auth-check-level2. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__interface_auth_check_level2_disable',)

  _yang_name = 'auth-check-level2'
  _rest_name = 'level-2'

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
    self.__interface_auth_check_level2_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="interface-auth-check-level2-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

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
      return [u'interface', u'ethernet', u'interface-eth-isis-conf', u'intf-isis', u'interface-isis', u'auth-check', u'auth-check-level2']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'isis', u'auth-check', u'level-2']

  def _get_interface_auth_check_level2_disable(self):
    """
    Getter method for interface_auth_check_level2_disable, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/auth_check/auth_check_level2/interface_auth_check_level2_disable (empty)
    """
    return self.__interface_auth_check_level2_disable
      
  def _set_interface_auth_check_level2_disable(self, v, load=False):
    """
    Setter method for interface_auth_check_level2_disable, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/auth_check/auth_check_level2/interface_auth_check_level2_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_auth_check_level2_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_auth_check_level2_disable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="interface-auth-check-level2-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_auth_check_level2_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="interface-auth-check-level2-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__interface_auth_check_level2_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_auth_check_level2_disable(self):
    self.__interface_auth_check_level2_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="interface-auth-check-level2-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

  interface_auth_check_level2_disable = __builtin__.property(_get_interface_auth_check_level2_disable, _set_interface_auth_check_level2_disable)


  _pyangbind_elements = {'interface_auth_check_level2_disable': interface_auth_check_level2_disable, }


