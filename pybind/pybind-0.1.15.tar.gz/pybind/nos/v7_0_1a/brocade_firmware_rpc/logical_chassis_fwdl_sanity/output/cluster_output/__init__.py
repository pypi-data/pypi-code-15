
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cluster_output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-firmware - based on the path /brocade_firmware_rpc/logical-chassis-fwdl-sanity/output/cluster-output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id','__fwdl_status','__fwdl_msg',)

  _yang_name = 'cluster-output'
  _rest_name = 'cluster-output'

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
    self.__fwdl_msg = YANGDynClass(base=unicode, is_leaf=True, yang_name="fwdl-msg", rest_name="fwdl-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Preinstall error string'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Rbridge-id of the node'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    self.__fwdl_status = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="fwdl-status", rest_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Status code for the preinstall check. 0 and 1 is success, else failure'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)

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
      return [u'brocade_firmware_rpc', u'logical-chassis-fwdl-sanity', u'output', u'cluster-output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logical-chassis-fwdl-sanity', u'output', u'cluster-output']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/output/cluster_output/rbridge_id (uint32)
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/output/cluster_output/rbridge_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Rbridge-id of the node'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Rbridge-id of the node'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Rbridge-id of the node'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='uint32', is_config=True)


  def _get_fwdl_status(self):
    """
    Getter method for fwdl_status, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/output/cluster_output/fwdl_status (int32)
    """
    return self.__fwdl_status
      
  def _set_fwdl_status(self, v, load=False):
    """
    Setter method for fwdl_status, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/output/cluster_output/fwdl_status (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fwdl_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fwdl_status() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="fwdl-status", rest_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Status code for the preinstall check. 0 and 1 is success, else failure'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fwdl_status must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="fwdl-status", rest_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Status code for the preinstall check. 0 and 1 is success, else failure'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)""",
        })

    self.__fwdl_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fwdl_status(self):
    self.__fwdl_status = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="fwdl-status", rest_name="fwdl-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Status code for the preinstall check. 0 and 1 is success, else failure'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='int32', is_config=True)


  def _get_fwdl_msg(self):
    """
    Getter method for fwdl_msg, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/output/cluster_output/fwdl_msg (string)
    """
    return self.__fwdl_msg
      
  def _set_fwdl_msg(self, v, load=False):
    """
    Setter method for fwdl_msg, mapped from YANG variable /brocade_firmware_rpc/logical_chassis_fwdl_sanity/output/cluster_output/fwdl_msg (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fwdl_msg is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fwdl_msg() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="fwdl-msg", rest_name="fwdl-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Preinstall error string'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fwdl_msg must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="fwdl-msg", rest_name="fwdl-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Preinstall error string'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)""",
        })

    self.__fwdl_msg = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fwdl_msg(self):
    self.__fwdl_msg = YANGDynClass(base=unicode, is_leaf=True, yang_name="fwdl-msg", rest_name="fwdl-msg", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Preinstall error string'}}, namespace='urn:brocade.com:mgmt:brocade-firmware', defining_module='brocade-firmware', yang_type='string', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  fwdl_status = __builtin__.property(_get_fwdl_status, _set_fwdl_status)
  fwdl_msg = __builtin__.property(_get_fwdl_msg, _set_fwdl_msg)


  _pyangbind_elements = {'rbridge_id': rbridge_id, 'fwdl_status': fwdl_status, 'fwdl_msg': fwdl_msg, }


