
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fwdl_entries(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/logical-chassis-fwdl-status/output/cluster-fwdl-entries/fwdl-entries. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__index','__message_id','__date_and_time_info','__message','__blade_slot','__blade_swbd','__blade_name','__blade_state','__blade_app',)

  _yang_name = 'fwdl-entries'
  _rest_name = 'fwdl-entries'

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
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    self.__blade_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 0}, u'standby': {'value': 1}},), is_leaf=True, yang_name="blade-state", rest_name="blade-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    self.__blade_app = YANGDynClass(base=unicode, is_leaf=True, yang_name="blade-app", rest_name="blade-app", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The name of the application firmware being downloaded on the blade, e.g. BFOS, CFOS, etc. if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__date_and_time_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__blade_slot = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-slot", rest_name="blade-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The slot number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    self.__message_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Message indentifier'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    self.__blade_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="blade-name", rest_name="blade-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__blade_swbd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-swbd", rest_name="blade-swbd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The SWBD number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)

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
      return [u'brocade_firmware_rpc', u'logical-chassis-fwdl-status', u'output', u'cluster-fwdl-entries', u'fwdl-entries']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logical-chassis-fwdl-status', u'output', u'cluster-fwdl-entries', u'fwdl-entries']

  def _get_index(self):
    """
    Getter method for index, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/index (uint32)
    """
    return self.__index
      
  def _set_index(self, v, load=False):
    """
    Setter method for index, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/index (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_index() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """index must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)""",
        })

    self.__index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_index(self):
    self.__index = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="index", rest_name="index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Sequence number for the message'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)


  def _get_message_id(self):
    """
    Getter method for message_id, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/message_id (int32)
    """
    return self.__message_id
      
  def _set_message_id(self, v, load=False):
    """
    Setter method for message_id, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/message_id (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message_id() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Message indentifier'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message_id must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Message indentifier'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)""",
        })

    self.__message_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message_id(self):
    self.__message_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="message-id", rest_name="message-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Message indentifier'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)


  def _get_date_and_time_info(self):
    """
    Getter method for date_and_time_info, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/date_and_time_info (string)
    """
    return self.__date_and_time_info
      
  def _set_date_and_time_info(self, v, load=False):
    """
    Setter method for date_and_time_info, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/date_and_time_info (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_date_and_time_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_date_and_time_info() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """date_and_time_info must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__date_and_time_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_date_and_time_info(self):
    self.__date_and_time_info = YANGDynClass(base=unicode, is_leaf=True, yang_name="date-and-time-info", rest_name="date-and-time-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Date and time of the message. The format is YYYY-MM-DD/HH:MM:SS.SSSS (micro seconds)'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_message(self):
    """
    Getter method for message, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/message (string)
    """
    return self.__message
      
  def _set_message(self, v, load=False):
    """
    Setter method for message, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/message (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_message() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """message must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_message(self):
    self.__message = YANGDynClass(base=unicode, is_leaf=True, yang_name="message", rest_name="message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Textual description of the status'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_blade_slot(self):
    """
    Getter method for blade_slot, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_slot (int32)
    """
    return self.__blade_slot
      
  def _set_blade_slot(self, v, load=False):
    """
    Setter method for blade_slot, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_slot (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blade_slot is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blade_slot() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-slot", rest_name="blade-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The slot number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blade_slot must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-slot", rest_name="blade-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The slot number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)""",
        })

    self.__blade_slot = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blade_slot(self):
    self.__blade_slot = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-slot", rest_name="blade-slot", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The slot number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)


  def _get_blade_swbd(self):
    """
    Getter method for blade_swbd, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_swbd (int32)
    """
    return self.__blade_swbd
      
  def _set_blade_swbd(self, v, load=False):
    """
    Setter method for blade_swbd, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_swbd (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blade_swbd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blade_swbd() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-swbd", rest_name="blade-swbd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The SWBD number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blade_swbd must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-swbd", rest_name="blade-swbd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The SWBD number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)""",
        })

    self.__blade_swbd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blade_swbd(self):
    self.__blade_swbd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="blade-swbd", rest_name="blade-swbd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The SWBD number of the blade being upgraded if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)


  def _get_blade_name(self):
    """
    Getter method for blade_name, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_name (string)
    """
    return self.__blade_name
      
  def _set_blade_name(self, v, load=False):
    """
    Setter method for blade_name, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blade_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blade_name() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="blade-name", rest_name="blade-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blade_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="blade-name", rest_name="blade-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__blade_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blade_name(self):
    self.__blade_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="blade-name", rest_name="blade-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)


  def _get_blade_state(self):
    """
    Getter method for blade_state, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_state (enumeration)
    """
    return self.__blade_state
      
  def _set_blade_state(self, v, load=False):
    """
    Setter method for blade_state, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blade_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blade_state() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 0}, u'standby': {'value': 1}},), is_leaf=True, yang_name="blade-state", rest_name="blade-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blade_state must be of a type compatible with enumeration""",
          'defined-type': "brocade-firmware:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 0}, u'standby': {'value': 1}},), is_leaf=True, yang_name="blade-state", rest_name="blade-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)""",
        })

    self.__blade_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blade_state(self):
    self.__blade_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 0}, u'standby': {'value': 1}},), is_leaf=True, yang_name="blade-state", rest_name="blade-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='enumeration', is_config=True)


  def _get_blade_app(self):
    """
    Getter method for blade_app, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_app (string)
    """
    return self.__blade_app
      
  def _set_blade_app(self, v, load=False):
    """
    Setter method for blade_app, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_status/output/cluster_fwdl_entries/fwdl_entries/blade_app (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_blade_app is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_blade_app() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="blade-app", rest_name="blade-app", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The name of the application firmware being downloaded on the blade, e.g. BFOS, CFOS, etc. if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """blade_app must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="blade-app", rest_name="blade-app", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The name of the application firmware being downloaded on the blade, e.g. BFOS, CFOS, etc. if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__blade_app = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_blade_app(self):
    self.__blade_app = YANGDynClass(base=unicode, is_leaf=True, yang_name="blade-app", rest_name="blade-app", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'The name of the application firmware being downloaded on the blade, e.g. BFOS, CFOS, etc. if applicable'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)

  index = __builtin__.property(_get_index, _set_index)
  message_id = __builtin__.property(_get_message_id, _set_message_id)
  date_and_time_info = __builtin__.property(_get_date_and_time_info, _set_date_and_time_info)
  message = __builtin__.property(_get_message, _set_message)
  blade_slot = __builtin__.property(_get_blade_slot, _set_blade_slot)
  blade_swbd = __builtin__.property(_get_blade_swbd, _set_blade_swbd)
  blade_name = __builtin__.property(_get_blade_name, _set_blade_name)
  blade_state = __builtin__.property(_get_blade_state, _set_blade_state)
  blade_app = __builtin__.property(_get_blade_app, _set_blade_app)


  _pyangbind_elements = {'index': index, 'message_id': message_id, 'date_and_time_info': date_and_time_info, 'message': message, 'blade_slot': blade_slot, 'blade_swbd': blade_swbd, 'blade_name': blade_name, 'blade_state': blade_state, 'blade_app': blade_app, }


