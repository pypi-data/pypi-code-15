
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class enable(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/maps/enable. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__policy','__actions',)

  _yang_name = 'enable'
  _rest_name = 'enable'

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
    self.__policy = YANGDynClass(base=unicode, is_leaf=True, yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS policy name'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    self.__actions = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {'value': 0}, u'SNMP': {'value': 1}, u'RASLOG': {'value': 7}, u'SFP_MARGINAL': {'value': 6}, u'EMAIL': {'value': 2}, u'USE-POLICY': {'value': 8}},), default=unicode("NONE"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS actions'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='maps-action-type', is_config=True)

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
      return [u'rbridge-id', u'maps', u'enable']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'maps', u'enable']

  def _get_policy(self):
    """
    Getter method for policy, mapped from YANG variable /rbridge_id/maps/enable/policy (string)
    """
    return self.__policy
      
  def _set_policy(self, v, load=False):
    """
    Setter method for policy, mapped from YANG variable /rbridge_id/maps/enable/policy (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policy() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS policy name'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policy must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS policy name'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)""",
        })

    self.__policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policy(self):
    self.__policy = YANGDynClass(base=unicode, is_leaf=True, yang_name="policy", rest_name="policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS policy name'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)


  def _get_actions(self):
    """
    Getter method for actions, mapped from YANG variable /rbridge_id/maps/enable/actions (maps-action-type)
    """
    return self.__actions
      
  def _set_actions(self, v, load=False):
    """
    Setter method for actions, mapped from YANG variable /rbridge_id/maps/enable/actions (maps-action-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_actions() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {'value': 0}, u'SNMP': {'value': 1}, u'RASLOG': {'value': 7}, u'SFP_MARGINAL': {'value': 6}, u'EMAIL': {'value': 2}, u'USE-POLICY': {'value': 8}},), default=unicode("NONE"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS actions'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='maps-action-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """actions must be of a type compatible with maps-action-type""",
          'defined-type': "brocade-maps:maps-action-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {'value': 0}, u'SNMP': {'value': 1}, u'RASLOG': {'value': 7}, u'SFP_MARGINAL': {'value': 6}, u'EMAIL': {'value': 2}, u'USE-POLICY': {'value': 8}},), default=unicode("NONE"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS actions'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='maps-action-type', is_config=True)""",
        })

    self.__actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_actions(self):
    self.__actions = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'NONE': {'value': 0}, u'SNMP': {'value': 1}, u'RASLOG': {'value': 7}, u'SFP_MARGINAL': {'value': 6}, u'EMAIL': {'value': 2}, u'USE-POLICY': {'value': 8}},), default=unicode("NONE"), is_leaf=True, yang_name="actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAPS actions'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='maps-action-type', is_config=True)

  policy = __builtin__.property(_get_policy, _set_policy)
  actions = __builtin__.property(_get_actions, _set_actions)


  _pyangbind_elements = {'policy': policy, 'actions': actions, }


