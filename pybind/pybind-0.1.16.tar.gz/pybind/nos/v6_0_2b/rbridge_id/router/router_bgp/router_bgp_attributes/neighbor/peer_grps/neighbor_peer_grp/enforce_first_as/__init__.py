
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class enforce_first_as(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/neighbor/peer-grps/neighbor-peer-grp/enforce-first-as. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__nei_enforce_first_as','__nei_enforce_first_as_disable',)

  _yang_name = 'enforce-first-as'
  _rest_name = 'enforce-first-as'

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
    self.__nei_enforce_first_as_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable enforce-first-as', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__nei_enforce_first_as = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable enforce-first-as', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'peer-grps', u'neighbor-peer-grp', u'enforce-first-as']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'neighbor', u'enforce-first-as']

  def _get_nei_enforce_first_as(self):
    """
    Getter method for nei_enforce_first_as, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/enforce_first_as/nei_enforce_first_as (empty)
    """
    return self.__nei_enforce_first_as
      
  def _set_nei_enforce_first_as(self, v, load=False):
    """
    Setter method for nei_enforce_first_as, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/enforce_first_as/nei_enforce_first_as (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nei_enforce_first_as is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nei_enforce_first_as() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable enforce-first-as', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nei_enforce_first_as must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable enforce-first-as', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__nei_enforce_first_as = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nei_enforce_first_as(self):
    self.__nei_enforce_first_as = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable enforce-first-as', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_nei_enforce_first_as_disable(self):
    """
    Getter method for nei_enforce_first_as_disable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/enforce_first_as/nei_enforce_first_as_disable (empty)
    """
    return self.__nei_enforce_first_as_disable
      
  def _set_nei_enforce_first_as_disable(self, v, load=False):
    """
    Setter method for nei_enforce_first_as_disable, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/peer_grps/neighbor_peer_grp/enforce_first_as/nei_enforce_first_as_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nei_enforce_first_as_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nei_enforce_first_as_disable() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable enforce-first-as', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nei_enforce_first_as_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable enforce-first-as', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__nei_enforce_first_as_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nei_enforce_first_as_disable(self):
    self.__nei_enforce_first_as_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="nei-enforce-first-as-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable enforce-first-as', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  nei_enforce_first_as = __builtin__.property(_get_nei_enforce_first_as, _set_nei_enforce_first_as)
  nei_enforce_first_as_disable = __builtin__.property(_get_nei_enforce_first_as_disable, _set_nei_enforce_first_as_disable)


  _pyangbind_elements = {'nei_enforce_first_as': nei_enforce_first_as, 'nei_enforce_first_as_disable': nei_enforce_first_as_disable, }


