
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vcs_details(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vcs - based on the path /brocade_vcs_rpc/get-vcs-details/output/vcs-details. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__principal_switch_wwn','__co_ordinator_wwn','__local_switch_wwn','__node_vcs_mode','__node_vcs_type','__node_vcs_id',)

  _yang_name = 'vcs-details'
  _rest_name = 'vcs-details'

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
    self.__principal_switch_wwn = YANGDynClass(base=unicode, is_leaf=True, yang_name="principal-switch-wwn", rest_name="principal-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)
    self.__local_switch_wwn = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-switch-wwn", rest_name="local-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)
    self.__node_vcs_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="node-vcs-id", rest_name="node-vcs-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint32', is_config=True)
    self.__node_vcs_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vcs-fabric-cluster': {'value': 3}, u'vcs-unknown-cluster': {'value': 1}, u'vcs-stand-alone': {'value': 2}, u'vcs-management-cluster': {'value': 4}},), is_leaf=True, yang_name="node-vcs-type", rest_name="node-vcs-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='vcs-cluster-type', is_config=True)
    self.__node_vcs_mode = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="node-vcs-mode", rest_name="node-vcs-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='boolean', is_config=True)
    self.__co_ordinator_wwn = YANGDynClass(base=unicode, is_leaf=True, yang_name="co-ordinator-wwn", rest_name="co-ordinator-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)

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
      return [u'brocade_vcs_rpc', u'get-vcs-details', u'output', u'vcs-details']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-vcs-details', u'output', u'vcs-details']

  def _get_principal_switch_wwn(self):
    """
    Getter method for principal_switch_wwn, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/principal_switch_wwn (string)

    YANG Description: WWN of principal switch
    """
    return self.__principal_switch_wwn
      
  def _set_principal_switch_wwn(self, v, load=False):
    """
    Setter method for principal_switch_wwn, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/principal_switch_wwn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_principal_switch_wwn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_principal_switch_wwn() directly.

    YANG Description: WWN of principal switch
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="principal-switch-wwn", rest_name="principal-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """principal_switch_wwn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="principal-switch-wwn", rest_name="principal-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)""",
        })

    self.__principal_switch_wwn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_principal_switch_wwn(self):
    self.__principal_switch_wwn = YANGDynClass(base=unicode, is_leaf=True, yang_name="principal-switch-wwn", rest_name="principal-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)


  def _get_co_ordinator_wwn(self):
    """
    Getter method for co_ordinator_wwn, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/co_ordinator_wwn (string)

    YANG Description: WWN of Co-ordinator switch
    """
    return self.__co_ordinator_wwn
      
  def _set_co_ordinator_wwn(self, v, load=False):
    """
    Setter method for co_ordinator_wwn, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/co_ordinator_wwn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_co_ordinator_wwn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_co_ordinator_wwn() directly.

    YANG Description: WWN of Co-ordinator switch
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="co-ordinator-wwn", rest_name="co-ordinator-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """co_ordinator_wwn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="co-ordinator-wwn", rest_name="co-ordinator-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)""",
        })

    self.__co_ordinator_wwn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_co_ordinator_wwn(self):
    self.__co_ordinator_wwn = YANGDynClass(base=unicode, is_leaf=True, yang_name="co-ordinator-wwn", rest_name="co-ordinator-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)


  def _get_local_switch_wwn(self):
    """
    Getter method for local_switch_wwn, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/local_switch_wwn (string)

    YANG Description: WWN of local switch
    """
    return self.__local_switch_wwn
      
  def _set_local_switch_wwn(self, v, load=False):
    """
    Setter method for local_switch_wwn, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/local_switch_wwn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_switch_wwn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_switch_wwn() directly.

    YANG Description: WWN of local switch
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="local-switch-wwn", rest_name="local-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_switch_wwn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="local-switch-wwn", rest_name="local-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)""",
        })

    self.__local_switch_wwn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_switch_wwn(self):
    self.__local_switch_wwn = YANGDynClass(base=unicode, is_leaf=True, yang_name="local-switch-wwn", rest_name="local-switch-wwn", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='string', is_config=True)


  def _get_node_vcs_mode(self):
    """
    Getter method for node_vcs_mode, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/node_vcs_mode (boolean)

    YANG Description: Node's VCS mode
    """
    return self.__node_vcs_mode
      
  def _set_node_vcs_mode(self, v, load=False):
    """
    Setter method for node_vcs_mode, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/node_vcs_mode (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node_vcs_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node_vcs_mode() directly.

    YANG Description: Node's VCS mode
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="node-vcs-mode", rest_name="node-vcs-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node_vcs_mode must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="node-vcs-mode", rest_name="node-vcs-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='boolean', is_config=True)""",
        })

    self.__node_vcs_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node_vcs_mode(self):
    self.__node_vcs_mode = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="node-vcs-mode", rest_name="node-vcs-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='boolean', is_config=True)


  def _get_node_vcs_type(self):
    """
    Getter method for node_vcs_type, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/node_vcs_type (vcs-cluster-type)

    YANG Description: Vcs Type
    """
    return self.__node_vcs_type
      
  def _set_node_vcs_type(self, v, load=False):
    """
    Setter method for node_vcs_type, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/node_vcs_type (vcs-cluster-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node_vcs_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node_vcs_type() directly.

    YANG Description: Vcs Type
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vcs-fabric-cluster': {'value': 3}, u'vcs-unknown-cluster': {'value': 1}, u'vcs-stand-alone': {'value': 2}, u'vcs-management-cluster': {'value': 4}},), is_leaf=True, yang_name="node-vcs-type", rest_name="node-vcs-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='vcs-cluster-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node_vcs_type must be of a type compatible with vcs-cluster-type""",
          'defined-type': "brocade-vcs:vcs-cluster-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vcs-fabric-cluster': {'value': 3}, u'vcs-unknown-cluster': {'value': 1}, u'vcs-stand-alone': {'value': 2}, u'vcs-management-cluster': {'value': 4}},), is_leaf=True, yang_name="node-vcs-type", rest_name="node-vcs-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='vcs-cluster-type', is_config=True)""",
        })

    self.__node_vcs_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node_vcs_type(self):
    self.__node_vcs_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vcs-fabric-cluster': {'value': 3}, u'vcs-unknown-cluster': {'value': 1}, u'vcs-stand-alone': {'value': 2}, u'vcs-management-cluster': {'value': 4}},), is_leaf=True, yang_name="node-vcs-type", rest_name="node-vcs-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='vcs-cluster-type', is_config=True)


  def _get_node_vcs_id(self):
    """
    Getter method for node_vcs_id, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/node_vcs_id (uint32)

    YANG Description: Vcs Id
    """
    return self.__node_vcs_id
      
  def _set_node_vcs_id(self, v, load=False):
    """
    Setter method for node_vcs_id, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details/output/vcs_details/node_vcs_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_node_vcs_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_node_vcs_id() directly.

    YANG Description: Vcs Id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="node-vcs-id", rest_name="node-vcs-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """node_vcs_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="node-vcs-id", rest_name="node-vcs-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint32', is_config=True)""",
        })

    self.__node_vcs_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_node_vcs_id(self):
    self.__node_vcs_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="node-vcs-id", rest_name="node-vcs-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='uint32', is_config=True)

  principal_switch_wwn = __builtin__.property(_get_principal_switch_wwn, _set_principal_switch_wwn)
  co_ordinator_wwn = __builtin__.property(_get_co_ordinator_wwn, _set_co_ordinator_wwn)
  local_switch_wwn = __builtin__.property(_get_local_switch_wwn, _set_local_switch_wwn)
  node_vcs_mode = __builtin__.property(_get_node_vcs_mode, _set_node_vcs_mode)
  node_vcs_type = __builtin__.property(_get_node_vcs_type, _set_node_vcs_type)
  node_vcs_id = __builtin__.property(_get_node_vcs_id, _set_node_vcs_id)


  _pyangbind_elements = {'principal_switch_wwn': principal_switch_wwn, 'co_ordinator_wwn': co_ordinator_wwn, 'local_switch_wwn': local_switch_wwn, 'node_vcs_mode': node_vcs_mode, 'node_vcs_type': node_vcs_type, 'node_vcs_id': node_vcs_id, }


