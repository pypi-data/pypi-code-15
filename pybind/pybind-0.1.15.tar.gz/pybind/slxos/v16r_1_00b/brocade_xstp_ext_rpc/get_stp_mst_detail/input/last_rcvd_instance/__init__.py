
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class last_rcvd_instance(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc/get-stp-mst-detail/input/last-rcvd-instance. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__instance_id',)

  _yang_name = 'last-rcvd-instance'
  _rest_name = 'last-rcvd-instance'

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
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)

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
      return [u'brocade_xstp_ext_rpc', u'get-stp-mst-detail', u'input', u'last-rcvd-instance']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-stp-mst-detail', u'input', u'last-rcvd-instance']

  def _get_instance_id(self):
    """
    Getter method for instance_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/input/last_rcvd_instance/instance_id (uint32)

    YANG Description: Instance id of the last received spanning-tree
instance.
    """
    return self.__instance_id
      
  def _set_instance_id(self, v, load=False):
    """
    Setter method for instance_id, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/input/last_rcvd_instance/instance_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance_id() directly.

    YANG Description: Instance id of the last received spanning-tree
instance.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)""",
        })

    self.__instance_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance_id(self):
    self.__instance_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="instance-id", rest_name="instance-id", parent=self, choice=(u'request-type', u'getnext-request'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='uint32', is_config=True)

  instance_id = __builtin__.property(_get_instance_id, _set_instance_id)

  __choices__ = {u'request-type': {u'getnext-request': [u'instance_id']}}
  _pyangbind_elements = {'instance_id': instance_id, }


