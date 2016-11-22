
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class flow_action_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/flow/flow-info-list/flow-action-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Details of an action
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__action_idx','__group_id','__queue_id','__out_ports','__vlan_id','__action_vlan_upbits','__out_vlan_tag','__out_vlan_etype',)

  _yang_name = 'flow-action-list'
  _rest_name = 'flow-action-list'

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
    self.__out_vlan_tag = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)
    self.__out_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-ports", rest_name="out-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__out_vlan_etype = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__action_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-idx", rest_name="action-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__queue_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__action_vlan_upbits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-vlan-upbits", rest_name="action-vlan-upbits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

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
      return [u'openflow-state', u'flow', u'flow-info-list', u'flow-action-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'flow', u'flow-info-list', u'flow-action-list']

  def _get_action_idx(self):
    """
    Getter method for action_idx, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/action_idx (uint32)

    YANG Description: Action index
    """
    return self.__action_idx
      
  def _set_action_idx(self, v, load=False):
    """
    Setter method for action_idx, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/action_idx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_idx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_idx() directly.

    YANG Description: Action index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-idx", rest_name="action-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_idx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-idx", rest_name="action-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__action_idx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_idx(self):
    self.__action_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-idx", rest_name="action-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_group_id(self):
    """
    Getter method for group_id, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/group_id (uint32)

    YANG Description: Out Group
    """
    return self.__group_id
      
  def _set_group_id(self, v, load=False):
    """
    Setter method for group_id, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/group_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_id() directly.

    YANG Description: Out Group
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_id(self):
    self.__group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_queue_id(self):
    """
    Getter method for queue_id, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/queue_id (uint32)

    YANG Description: Queue id
    """
    return self.__queue_id
      
  def _set_queue_id(self, v, load=False):
    """
    Setter method for queue_id, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/queue_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_queue_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_queue_id() directly.

    YANG Description: Queue id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """queue_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__queue_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_queue_id(self):
    self.__queue_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="queue-id", rest_name="queue-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_out_ports(self):
    """
    Getter method for out_ports, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/out_ports (string)

    YANG Description: Out Port
    """
    return self.__out_ports
      
  def _set_out_ports(self, v, load=False):
    """
    Setter method for out_ports, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/out_ports (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_ports is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_ports() directly.

    YANG Description: Out Port
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="out-ports", rest_name="out-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_ports must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="out-ports", rest_name="out-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__out_ports = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_ports(self):
    self.__out_ports = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-ports", rest_name="out-ports", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/vlan_id (uint32)

    YANG Description: Vlan
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: Vlan
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_action_vlan_upbits(self):
    """
    Getter method for action_vlan_upbits, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/action_vlan_upbits (uint32)

    YANG Description: Vlan PCP
    """
    return self.__action_vlan_upbits
      
  def _set_action_vlan_upbits(self, v, load=False):
    """
    Setter method for action_vlan_upbits, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/action_vlan_upbits (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action_vlan_upbits is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action_vlan_upbits() directly.

    YANG Description: Vlan PCP
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-vlan-upbits", rest_name="action-vlan-upbits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action_vlan_upbits must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-vlan-upbits", rest_name="action-vlan-upbits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__action_vlan_upbits = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action_vlan_upbits(self):
    self.__action_vlan_upbits = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="action-vlan-upbits", rest_name="action-vlan-upbits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_out_vlan_tag(self):
    """
    Getter method for out_vlan_tag, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/out_vlan_tag (vlan-action)

    YANG Description: Vlan tag
    """
    return self.__out_vlan_tag
      
  def _set_out_vlan_tag(self, v, load=False):
    """
    Setter method for out_vlan_tag, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/out_vlan_tag (vlan-action)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_vlan_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_vlan_tag() directly.

    YANG Description: Vlan tag
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_vlan_tag must be of a type compatible with vlan-action""",
          'defined-type': "brocade-openflow-operational:vlan-action",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)""",
        })

    self.__out_vlan_tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_vlan_tag(self):
    self.__out_vlan_tag = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-vlan-action-pop': {'value': 2}, u'dcm-vlan-action-push': {'value': 1}, u'dcm-vlan-action-set': {'value': 0}},), is_leaf=True, yang_name="out-vlan-tag", rest_name="out-vlan-tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='vlan-action', is_config=False)


  def _get_out_vlan_etype(self):
    """
    Getter method for out_vlan_etype, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/out_vlan_etype (string)

    YANG Description: Vlan etype
    """
    return self.__out_vlan_etype
      
  def _set_out_vlan_etype(self, v, load=False):
    """
    Setter method for out_vlan_etype, mapped from YANG variable /openflow_state/flow/flow_info_list/flow_action_list/out_vlan_etype (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_vlan_etype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_vlan_etype() directly.

    YANG Description: Vlan etype
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_vlan_etype must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__out_vlan_etype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_vlan_etype(self):
    self.__out_vlan_etype = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-vlan-etype", rest_name="out-vlan-etype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

  action_idx = __builtin__.property(_get_action_idx)
  group_id = __builtin__.property(_get_group_id)
  queue_id = __builtin__.property(_get_queue_id)
  out_ports = __builtin__.property(_get_out_ports)
  vlan_id = __builtin__.property(_get_vlan_id)
  action_vlan_upbits = __builtin__.property(_get_action_vlan_upbits)
  out_vlan_tag = __builtin__.property(_get_out_vlan_tag)
  out_vlan_etype = __builtin__.property(_get_out_vlan_etype)


  _pyangbind_elements = {'action_idx': action_idx, 'group_id': group_id, 'queue_id': queue_id, 'out_ports': out_ports, 'vlan_id': vlan_id, 'action_vlan_upbits': action_vlan_upbits, 'out_vlan_tag': out_vlan_tag, 'out_vlan_etype': out_vlan_etype, }


