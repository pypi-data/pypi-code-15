
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rev_metric_common_attributes(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/interface-eth-isis-conf/intf-isis/interface-isis/interface-reverse-metric/rev-metric-common-attributes. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rev_metric_val','__rev_metric_whole_lan','__rev_metric_te_def_metric',)

  _yang_name = 'rev-metric-common-attributes'
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
    self.__rev_metric_whole_lan = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change metric for whole LAN', u'alt-name': u'whole-lan'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__rev_metric_te_def_metric = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Update TE default metric sub-tlv', u'alt-name': u'te-def-metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    self.__rev_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rev-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IS-IS reverse metric value', u'cli-drop-node-name': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)

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
      return [u'interface', u'ethernet', u'interface-eth-isis-conf', u'intf-isis', u'interface-isis', u'interface-reverse-metric', u'rev-metric-common-attributes']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'isis', u'reverse-metric']

  def _get_rev_metric_val(self):
    """
    Getter method for rev_metric_val, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes/rev_metric_val (uint32)
    """
    return self.__rev_metric_val
      
  def _set_rev_metric_val(self, v, load=False):
    """
    Setter method for rev_metric_val, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes/rev_metric_val (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rev_metric_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rev_metric_val() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rev-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IS-IS reverse metric value', u'cli-drop-node-name': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rev_metric_val must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rev-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IS-IS reverse metric value', u'cli-drop-node-name': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__rev_metric_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rev_metric_val(self):
    self.__rev_metric_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..16777214']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="rev-metric-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IS-IS reverse metric value', u'cli-drop-node-name': None, u'cli-break-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)


  def _get_rev_metric_whole_lan(self):
    """
    Getter method for rev_metric_whole_lan, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes/rev_metric_whole_lan (empty)
    """
    return self.__rev_metric_whole_lan
      
  def _set_rev_metric_whole_lan(self, v, load=False):
    """
    Setter method for rev_metric_whole_lan, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes/rev_metric_whole_lan (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rev_metric_whole_lan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rev_metric_whole_lan() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change metric for whole LAN', u'alt-name': u'whole-lan'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rev_metric_whole_lan must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change metric for whole LAN', u'alt-name': u'whole-lan'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__rev_metric_whole_lan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rev_metric_whole_lan(self):
    self.__rev_metric_whole_lan = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rev-metric-whole-lan", rest_name="whole-lan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Change metric for whole LAN', u'alt-name': u'whole-lan'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)


  def _get_rev_metric_te_def_metric(self):
    """
    Getter method for rev_metric_te_def_metric, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes/rev_metric_te_def_metric (empty)
    """
    return self.__rev_metric_te_def_metric
      
  def _set_rev_metric_te_def_metric(self, v, load=False):
    """
    Setter method for rev_metric_te_def_metric, mapped from YANG variable /interface/ethernet/interface_eth_isis_conf/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes/rev_metric_te_def_metric (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rev_metric_te_def_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rev_metric_te_def_metric() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Update TE default metric sub-tlv', u'alt-name': u'te-def-metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rev_metric_te_def_metric must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Update TE default metric sub-tlv', u'alt-name': u'te-def-metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)""",
        })

    self.__rev_metric_te_def_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rev_metric_te_def_metric(self):
    self.__rev_metric_te_def_metric = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rev-metric-te-def-metric", rest_name="te-def-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Update TE default metric sub-tlv', u'alt-name': u'te-def-metric'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='empty', is_config=True)

  rev_metric_val = __builtin__.property(_get_rev_metric_val, _set_rev_metric_val)
  rev_metric_whole_lan = __builtin__.property(_get_rev_metric_whole_lan, _set_rev_metric_whole_lan)
  rev_metric_te_def_metric = __builtin__.property(_get_rev_metric_te_def_metric, _set_rev_metric_te_def_metric)


  _pyangbind_elements = {'rev_metric_val': rev_metric_val, 'rev_metric_whole_lan': rev_metric_whole_lan, 'rev_metric_te_def_metric': rev_metric_te_def_metric, }


