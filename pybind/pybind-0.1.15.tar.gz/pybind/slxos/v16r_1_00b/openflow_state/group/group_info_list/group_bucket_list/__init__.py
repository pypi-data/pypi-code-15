
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import group_action_list
class group_bucket_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/group/group-info-list/group-bucket-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Group Bucket Info
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bucket_id','__weight','__watch_port','__group_action_list',)

  _yang_name = 'group-bucket-list'
  _rest_name = 'group-bucket-list'

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
    self.__group_action_list = YANGDynClass(base=YANGListType("action_id",group_action_list.group_action_list, yang_name="group-action-list", rest_name="group-action-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-action-list", rest_name="group-action-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__bucket_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bucket-id", rest_name="bucket-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__watch_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="watch-port", rest_name="watch-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)

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
      return [u'openflow-state', u'group', u'group-info-list', u'group-bucket-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'group', u'group-info-list', u'group-bucket-list']

  def _get_bucket_id(self):
    """
    Getter method for bucket_id, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/bucket_id (uint32)

    YANG Description: Bucket
    """
    return self.__bucket_id
      
  def _set_bucket_id(self, v, load=False):
    """
    Setter method for bucket_id, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/bucket_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bucket_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bucket_id() directly.

    YANG Description: Bucket
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bucket-id", rest_name="bucket-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bucket_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bucket-id", rest_name="bucket-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__bucket_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bucket_id(self):
    self.__bucket_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="bucket-id", rest_name="bucket-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_weight(self):
    """
    Getter method for weight, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/weight (uint32)

    YANG Description: Weight
    """
    return self.__weight
      
  def _set_weight(self, v, load=False):
    """
    Setter method for weight, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/weight (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_weight is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_weight() directly.

    YANG Description: Weight
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """weight must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__weight = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_weight(self):
    self.__weight = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="weight", rest_name="weight", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_watch_port(self):
    """
    Getter method for watch_port, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/watch_port (string)

    YANG Description: Watch port
    """
    return self.__watch_port
      
  def _set_watch_port(self, v, load=False):
    """
    Setter method for watch_port, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/watch_port (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_watch_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_watch_port() directly.

    YANG Description: Watch port
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="watch-port", rest_name="watch-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """watch_port must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="watch-port", rest_name="watch-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__watch_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_watch_port(self):
    self.__watch_port = YANGDynClass(base=unicode, is_leaf=True, yang_name="watch-port", rest_name="watch-port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_group_action_list(self):
    """
    Getter method for group_action_list, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list (list)

    YANG Description: group action info
    """
    return self.__group_action_list
      
  def _set_group_action_list(self, v, load=False):
    """
    Setter method for group_action_list, mapped from YANG variable /openflow_state/group/group_info_list/group_bucket_list/group_action_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_action_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_action_list() directly.

    YANG Description: group action info
    """
    try:
      t = YANGDynClass(v,base=YANGListType("action_id",group_action_list.group_action_list, yang_name="group-action-list", rest_name="group-action-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-action-list", rest_name="group-action-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_action_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("action_id",group_action_list.group_action_list, yang_name="group-action-list", rest_name="group-action-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-action-list", rest_name="group-action-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__group_action_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_action_list(self):
    self.__group_action_list = YANGDynClass(base=YANGListType("action_id",group_action_list.group_action_list, yang_name="group-action-list", rest_name="group-action-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='action-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-action-list", rest_name="group-action-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-action-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  bucket_id = __builtin__.property(_get_bucket_id)
  weight = __builtin__.property(_get_weight)
  watch_port = __builtin__.property(_get_watch_port)
  group_action_list = __builtin__.property(_get_group_action_list)


  _pyangbind_elements = {'bucket_id': bucket_id, 'weight': weight, 'watch_port': watch_port, 'group_action_list': group_action_list, }


