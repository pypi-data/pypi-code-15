
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vnetwork_hosts
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vswitch - based on the path /brocade_vswitch_rpc/get-vnetwork-hosts/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vnetwork_hosts','__has_more','__instance_id',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='boolean', is_config=True)
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)
    self.__vnetwork_hosts = YANGDynClass(base=YANGListType(False,vnetwork_hosts.vnetwork_hosts, yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='list', is_config=True)

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
      return [u'brocade_vswitch_rpc', u'get-vnetwork-hosts', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-vnetwork-hosts', u'output']

  def _get_vnetwork_hosts(self):
    """
    Getter method for vnetwork_hosts, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts (list)
    """
    return self.__vnetwork_hosts
      
  def _set_vnetwork_hosts(self, v, load=False):
    """
    Setter method for vnetwork_hosts, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/vnetwork_hosts (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vnetwork_hosts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vnetwork_hosts() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,vnetwork_hosts.vnetwork_hosts, yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vnetwork_hosts must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,vnetwork_hosts.vnetwork_hosts, yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='list', is_config=True)""",
        })

    self.__vnetwork_hosts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vnetwork_hosts(self):
    self.__vnetwork_hosts = YANGDynClass(base=YANGListType(False,vnetwork_hosts.vnetwork_hosts, yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="vnetwork-hosts", rest_name="vnetwork-hosts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='list', is_config=True)


  def _get_has_more(self):
    """
    Getter method for has_more, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/has_more (boolean)
    """
    return self.__has_more
      
  def _set_has_more(self, v, load=False):
    """
    Setter method for has_more, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/has_more (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_has_more is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_has_more() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """has_more must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='boolean', is_config=True)""",
        })

    self.__has_more = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_has_more(self):
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='boolean', is_config=True)


  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/instance_id (uint32)
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /brocade_vswitch_rpc/get_vnetwork_hosts/output/instance_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='uint32', is_config=True)

  vnetwork_hosts = __builtin__.property(_get_vnetwork_hosts, _set_vnetwork_hosts)
  has_more = __builtin__.property(_get_has_more, _set_has_more)
  instance_id = __builtin__.property(_get_instance_id, _set_instance_id)


  _pyangbind_elements = {'vnetwork_hosts': vnetwork_hosts, 'has_more': has_more, 'instance_id': instance_id, }


