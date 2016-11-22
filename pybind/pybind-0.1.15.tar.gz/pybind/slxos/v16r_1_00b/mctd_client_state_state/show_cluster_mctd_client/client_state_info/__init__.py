
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class client_state_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct-operational - based on the path /mctd-client-state-state/show-cluster-mctd-client/client-state-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: cluster client state
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__client_name','__client_id','__local_state','__remote_state','__local_esi_label','__remote_esi_label',)

  _yang_name = 'client-state-info'
  _rest_name = 'client-state-info'

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
    self.__remote_esi_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-esi-label", rest_name="remote-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__remote_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-state", rest_name="remote-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__local_esi_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-esi-label", rest_name="local-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__client_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)
    self.__local_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-state", rest_name="local-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)

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
      return [u'mctd-client-state-state', u'show-cluster-mctd-client', u'client-state-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mctd-client-state-state', u'show-cluster-mctd-client', u'client-state-info']

  def _get_client_name(self):
    """
    Getter method for client_name, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/client_name (string)

    YANG Description: Client name
    """
    return self.__client_name
      
  def _set_client_name(self, v, load=False):
    """
    Setter method for client_name, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/client_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_name() directly.

    YANG Description: Client name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)""",
        })

    self.__client_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_name(self):
    self.__client_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="client-name", rest_name="client-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='string', is_config=False)


  def _get_client_id(self):
    """
    Getter method for client_id, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/client_id (uint32)

    YANG Description: Client Id
    """
    return self.__client_id
      
  def _set_client_id(self, v, load=False):
    """
    Setter method for client_id, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/client_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_id() directly.

    YANG Description: Client Id
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__client_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_id(self):
    self.__client_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="client-id", rest_name="client-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_local_state(self):
    """
    Getter method for local_state, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/local_state (uint32)

    YANG Description: Client Local State
    """
    return self.__local_state
      
  def _set_local_state(self, v, load=False):
    """
    Setter method for local_state, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/local_state (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_state() directly.

    YANG Description: Client Local State
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-state", rest_name="local-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_state must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-state", rest_name="local-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__local_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_state(self):
    self.__local_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-state", rest_name="local-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_remote_state(self):
    """
    Getter method for remote_state, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/remote_state (uint32)

    YANG Description: Client Remote State
    """
    return self.__remote_state
      
  def _set_remote_state(self, v, load=False):
    """
    Setter method for remote_state, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/remote_state (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_state() directly.

    YANG Description: Client Remote State
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-state", rest_name="remote-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_state must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-state", rest_name="remote-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__remote_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_state(self):
    self.__remote_state = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-state", rest_name="remote-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_local_esi_label(self):
    """
    Getter method for local_esi_label, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/local_esi_label (uint32)

    YANG Description: Esi Local Label
    """
    return self.__local_esi_label
      
  def _set_local_esi_label(self, v, load=False):
    """
    Setter method for local_esi_label, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/local_esi_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_local_esi_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_local_esi_label() directly.

    YANG Description: Esi Local Label
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-esi-label", rest_name="local-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """local_esi_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-esi-label", rest_name="local-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__local_esi_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_local_esi_label(self):
    self.__local_esi_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="local-esi-label", rest_name="local-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_remote_esi_label(self):
    """
    Getter method for remote_esi_label, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/remote_esi_label (uint32)

    YANG Description: Esi Remote Label
    """
    return self.__remote_esi_label
      
  def _set_remote_esi_label(self, v, load=False):
    """
    Setter method for remote_esi_label, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info/remote_esi_label (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_esi_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_esi_label() directly.

    YANG Description: Esi Remote Label
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-esi-label", rest_name="remote-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_esi_label must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-esi-label", rest_name="remote-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__remote_esi_label = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_esi_label(self):
    self.__remote_esi_label = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="remote-esi-label", rest_name="remote-esi-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)

  client_name = __builtin__.property(_get_client_name)
  client_id = __builtin__.property(_get_client_id)
  local_state = __builtin__.property(_get_local_state)
  remote_state = __builtin__.property(_get_remote_state)
  local_esi_label = __builtin__.property(_get_local_esi_label)
  remote_esi_label = __builtin__.property(_get_remote_esi_label)


  _pyangbind_elements = {'client_name': client_name, 'client_id': client_id, 'local_state': local_state, 'remote_state': remote_state, 'local_esi_label': local_esi_label, 'remote_esi_label': remote_esi_label, }


