
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class trust(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/qos/trust. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__trust_cos','__trust_dscp',)

  _yang_name = 'trust'
  _rest_name = 'trust'

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
    self.__trust_cos = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L2 CoS field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)
    self.__trust_dscp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust-dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L3 DSCP field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'dscp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'qos', u'trust']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'qos', u'trust']

  def _get_trust_cos(self):
    """
    Getter method for trust_cos, mapped from YANG variable /interface/hundredgigabitethernet/qos/trust/trust_cos (empty)
    """
    return self.__trust_cos
      
  def _set_trust_cos(self, v, load=False):
    """
    Setter method for trust_cos, mapped from YANG variable /interface/hundredgigabitethernet/qos/trust/trust_cos (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trust_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trust_cos() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="trust-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L2 CoS field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trust_cos must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L2 CoS field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)""",
        })

    self.__trust_cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trust_cos(self):
    self.__trust_cos = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust-cos", rest_name="cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L2 CoS field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'cos', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)


  def _get_trust_dscp(self):
    """
    Getter method for trust_dscp, mapped from YANG variable /interface/hundredgigabitethernet/qos/trust/trust_dscp (empty)
    """
    return self.__trust_dscp
      
  def _set_trust_dscp(self, v, load=False):
    """
    Setter method for trust_dscp, mapped from YANG variable /interface/hundredgigabitethernet/qos/trust/trust_dscp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trust_dscp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trust_dscp() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="trust-dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L3 DSCP field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'dscp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trust_dscp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust-dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L3 DSCP field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'dscp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)""",
        })

    self.__trust_dscp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trust_dscp(self):
    self.__trust_dscp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="trust-dscp", rest_name="dscp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Trust L3 DSCP field in incoming packets for deriving internal Traffic Class', u'cli-full-command': None, u'alt-name': u'dscp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='empty', is_config=True)

  trust_cos = __builtin__.property(_get_trust_cos, _set_trust_cos)
  trust_dscp = __builtin__.property(_get_trust_dscp, _set_trust_dscp)


  _pyangbind_elements = {'trust_cos': trust_cos, 'trust_dscp': trust_dscp, }


