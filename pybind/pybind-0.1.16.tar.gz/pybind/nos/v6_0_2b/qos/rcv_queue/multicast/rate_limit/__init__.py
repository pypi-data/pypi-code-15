
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rate_limit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /qos/rcv-queue/multicast/rate-limit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__limit','__burst',)

  _yang_name = 'rate-limit'
  _rest_name = 'rate-limit'

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
    self.__limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'6500 .. 20000000']}), is_leaf=True, yang_name="limit", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    self.__burst = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'50 .. 65535']}), is_leaf=True, yang_name="burst", rest_name="burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst limit (packets)'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)

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
      return [u'qos', u'rcv-queue', u'multicast', u'rate-limit']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos', u'rcv-queue', u'multicast', u'rate-limit']

  def _get_limit(self):
    """
    Getter method for limit, mapped from YANG variable /qos/rcv_queue/multicast/rate_limit/limit (int32)
    """
    return self.__limit
      
  def _set_limit(self, v, load=False):
    """
    Setter method for limit, mapped from YANG variable /qos/rcv_queue/multicast/rate_limit/limit (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_limit() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'6500 .. 20000000']}), is_leaf=True, yang_name="limit", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """limit must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'6500 .. 20000000']}), is_leaf=True, yang_name="limit", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_limit(self):
    self.__limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'6500 .. 20000000']}), is_leaf=True, yang_name="limit", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)


  def _get_burst(self):
    """
    Getter method for burst, mapped from YANG variable /qos/rcv_queue/multicast/rate_limit/burst (int32)
    """
    return self.__burst
      
  def _set_burst(self, v, load=False):
    """
    Setter method for burst, mapped from YANG variable /qos/rcv_queue/multicast/rate_limit/burst (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_burst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_burst() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'50 .. 65535']}), is_leaf=True, yang_name="burst", rest_name="burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst limit (packets)'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """burst must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'50 .. 65535']}), is_leaf=True, yang_name="burst", rest_name="burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst limit (packets)'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)""",
        })

    self.__burst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_burst(self):
    self.__burst = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'50 .. 65535']}), is_leaf=True, yang_name="burst", rest_name="burst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Burst limit (packets)'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='int32', is_config=True)

  limit = __builtin__.property(_get_limit, _set_limit)
  burst = __builtin__.property(_get_burst, _set_burst)


  _pyangbind_elements = {'limit': limit, 'burst': burst, }


