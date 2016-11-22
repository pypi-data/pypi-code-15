
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cluster_id(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/router-bgp-attributes/cluster-id. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cluster_id_value','__cluster_id_ipv4_address',)

  _yang_name = 'cluster-id'
  _rest_name = 'cluster-id'

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
    self.__cluster_id_ipv4_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="cluster-id-ipv4-address", rest_name="ipv4-address", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id-ipv4-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as IP address', u'alt-name': u'ipv4-address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)
    self.__cluster_id_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id-value", rest_name="id", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as 32 bit quantity', u'cli-drop-node-name': None, u'alt-name': u'id'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='decimal-number', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'router-bgp-attributes', u'cluster-id']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'cluster-id']

  def _get_cluster_id_value(self):
    """
    Getter method for cluster_id_value, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/cluster_id/cluster_id_value (decimal-number)
    """
    return self.__cluster_id_value
      
  def _set_cluster_id_value(self, v, load=False):
    """
    Setter method for cluster_id_value, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/cluster_id/cluster_id_value (decimal-number)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_id_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_id_value() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id-value", rest_name="id", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as 32 bit quantity', u'cli-drop-node-name': None, u'alt-name': u'id'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='decimal-number', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_id_value must be of a type compatible with decimal-number""",
          'defined-type': "brocade-bgp:decimal-number",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id-value", rest_name="id", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as 32 bit quantity', u'cli-drop-node-name': None, u'alt-name': u'id'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='decimal-number', is_config=True)""",
        })

    self.__cluster_id_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_id_value(self):
    self.__cluster_id_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="cluster-id-value", rest_name="id", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as 32 bit quantity', u'cli-drop-node-name': None, u'alt-name': u'id'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='decimal-number', is_config=True)


  def _get_cluster_id_ipv4_address(self):
    """
    Getter method for cluster_id_ipv4_address, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/cluster_id/cluster_id_ipv4_address (inet:ipv4-address)
    """
    return self.__cluster_id_ipv4_address
      
  def _set_cluster_id_ipv4_address(self, v, load=False):
    """
    Setter method for cluster_id_ipv4_address, mapped from YANG variable /rbridge_id/router/router_bgp/router_bgp_attributes/cluster_id/cluster_id_ipv4_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_id_ipv4_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_id_ipv4_address() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="cluster-id-ipv4-address", rest_name="ipv4-address", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id-ipv4-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as IP address', u'alt-name': u'ipv4-address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_id_ipv4_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="cluster-id-ipv4-address", rest_name="ipv4-address", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id-ipv4-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as IP address', u'alt-name': u'ipv4-address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__cluster_id_ipv4_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_id_ipv4_address(self):
    self.__cluster_id_ipv4_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="cluster-id-ipv4-address", rest_name="ipv4-address", parent=self, choice=(u'ch-cluster-id', u'ca-cluster-id-ipv4-address'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route-Reflector Cluster-ID as IP address', u'alt-name': u'ipv4-address'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv4-address', is_config=True)

  cluster_id_value = __builtin__.property(_get_cluster_id_value, _set_cluster_id_value)
  cluster_id_ipv4_address = __builtin__.property(_get_cluster_id_ipv4_address, _set_cluster_id_ipv4_address)

  __choices__ = {u'ch-cluster-id': {u'ca-cluster-id': [u'cluster_id_value'], u'ca-cluster-id-ipv4-address': [u'cluster_id_ipv4_address']}}
  _pyangbind_elements = {'cluster_id_value': cluster_id_value, 'cluster_id_ipv4_address': cluster_id_ipv4_address, }


