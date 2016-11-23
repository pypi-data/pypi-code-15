
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class interval(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/neighbor/neighbor-ips/neighbor-addr/bfd/interval. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure BFD desired min transmit interval in milliseconds.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__min_tx','__min_rx','__multiplier',)

  _yang_name = 'interval'
  _rest_name = 'interval'

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
    self.__min_tx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-tx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-tx-interval-type', is_config=True)
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure BFD detection time multiplier.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-multiplier-type', is_config=True)
    self.__min_rx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD required min receive interval in milliseconds.', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-rx-interval-type', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor', u'neighbor-ips', u'neighbor-addr', u'bfd', u'interval']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'neighbor', u'bfd', u'interval']

  def _get_min_tx(self):
    """
    Getter method for min_tx, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval/min_tx (bfd-tx-interval-type)

    YANG Description: Configure BFD desired min transmit interval in milliseconds.
    """
    return self.__min_tx
      
  def _set_min_tx(self, v, load=False):
    """
    Setter method for min_tx, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval/min_tx (bfd-tx-interval-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_tx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_tx() directly.

    YANG Description: Configure BFD desired min transmit interval in milliseconds.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-tx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-tx-interval-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_tx must be of a type compatible with bfd-tx-interval-type""",
          'defined-type': "brocade-bgp:bfd-tx-interval-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-tx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-tx-interval-type', is_config=True)""",
        })

    self.__min_tx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_tx(self):
    self.__min_tx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-tx", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD desired min transmit interval in milliseconds.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-tx-interval-type', is_config=True)


  def _get_min_rx(self):
    """
    Getter method for min_rx, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval/min_rx (bfd-rx-interval-type)

    YANG Description: Configure BFD required min receive interval in milliseconds.
    """
    return self.__min_rx
      
  def _set_min_rx(self, v, load=False):
    """
    Setter method for min_rx, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval/min_rx (bfd-rx-interval-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_rx() directly.

    YANG Description: Configure BFD required min receive interval in milliseconds.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD required min receive interval in milliseconds.', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-rx-interval-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_rx must be of a type compatible with bfd-rx-interval-type""",
          'defined-type': "brocade-bgp:bfd-rx-interval-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD required min receive interval in milliseconds.', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-rx-interval-type', is_config=True)""",
        })

    self.__min_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_rx(self):
    self.__min_rx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure BFD required min receive interval in milliseconds.', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-rx-interval-type', is_config=True)


  def _get_multiplier(self):
    """
    Getter method for multiplier, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval/multiplier (bfd-multiplier-type)

    YANG Description: Configure BFD detection time multiplier.
    """
    return self.__multiplier
      
  def _set_multiplier(self, v, load=False):
    """
    Setter method for multiplier, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips/neighbor_addr/bfd/interval/multiplier (bfd-multiplier-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multiplier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multiplier() directly.

    YANG Description: Configure BFD detection time multiplier.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure BFD detection time multiplier.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-multiplier-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multiplier must be of a type compatible with bfd-multiplier-type""",
          'defined-type': "brocade-bgp:bfd-multiplier-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure BFD detection time multiplier.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-multiplier-type', is_config=True)""",
        })

    self.__multiplier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multiplier(self):
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure BFD detection time multiplier.'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bfd-multiplier-type', is_config=True)

  min_tx = __builtin__.property(_get_min_tx, _set_min_tx)
  min_rx = __builtin__.property(_get_min_rx, _set_min_rx)
  multiplier = __builtin__.property(_get_multiplier, _set_multiplier)


  _pyangbind_elements = {'min_tx': min_tx, 'min_rx': min_rx, 'multiplier': multiplier, }


