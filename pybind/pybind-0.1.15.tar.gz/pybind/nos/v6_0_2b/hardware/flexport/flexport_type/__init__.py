
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class flexport_type(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-hardware - based on the path /hardware/flexport/flexport_type. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__type','__instance','__skip_deconfig',)

  _yang_name = 'flexport_type'
  _rest_name = ''

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
    self.__instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The instance to which the port should be configured.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='int32', is_config=True)
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type to be configured.'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='port-type', is_config=True)
    self.__skip_deconfig = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="skip_deconfig", rest_name="skip_deconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip Plugin deconfig errors.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)

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
      return [u'hardware', u'flexport', u'flexport_type']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'hardware', u'flexport']

  def _get_type(self):
    """
    Getter method for type, mapped from YANG variable /hardware/flexport/flexport_type/type (port-type)

    YANG Description: The type to be configured.
    """
    return self.__type
      
  def _set_type(self, v, load=False):
    """
    Setter method for type, mapped from YANG variable /hardware/flexport/flexport_type/type (port-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: The type to be configured.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type to be configured.'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='port-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type must be of a type compatible with port-type""",
          'defined-type': "brocade-hardware:port-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type to be configured.'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='port-type', is_config=True)""",
        })

    self.__type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type(self):
    self.__type = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="type", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type to be configured.'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='port-type', is_config=True)


  def _get_instance(self):
    """
    Getter method for instance, mapped from YANG variable /hardware/flexport/flexport_type/instance (int32)

    YANG Description: The instance to which the port should be configured.
    """
    return self.__instance
      
  def _set_instance(self, v, load=False):
    """
    Setter method for instance, mapped from YANG variable /hardware/flexport/flexport_type/instance (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_instance() directly.

    YANG Description: The instance to which the port should be configured.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The instance to which the port should be configured.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """instance must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The instance to which the port should be configured.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='int32', is_config=True)""",
        })

    self.__instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_instance(self):
    self.__instance = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), is_leaf=True, yang_name="instance", rest_name="instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The instance to which the port should be configured.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='int32', is_config=True)


  def _get_skip_deconfig(self):
    """
    Getter method for skip_deconfig, mapped from YANG variable /hardware/flexport/flexport_type/skip_deconfig (empty)

    YANG Description: Skip plugin notification Errors.
    """
    return self.__skip_deconfig
      
  def _set_skip_deconfig(self, v, load=False):
    """
    Setter method for skip_deconfig, mapped from YANG variable /hardware/flexport/flexport_type/skip_deconfig (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_skip_deconfig is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_skip_deconfig() directly.

    YANG Description: Skip plugin notification Errors.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="skip_deconfig", rest_name="skip_deconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip Plugin deconfig errors.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """skip_deconfig must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="skip_deconfig", rest_name="skip_deconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip Plugin deconfig errors.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)""",
        })

    self.__skip_deconfig = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_skip_deconfig(self):
    self.__skip_deconfig = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="skip_deconfig", rest_name="skip_deconfig", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Skip Plugin deconfig errors.', u'hidden': u'debug'}}, namespace='urn:brocade.com:mgmt:brocade-hardware', defining_module='brocade-hardware', yang_type='empty', is_config=True)

  type = __builtin__.property(_get_type, _set_type)
  instance = __builtin__.property(_get_instance, _set_instance)
  skip_deconfig = __builtin__.property(_get_skip_deconfig, _set_skip_deconfig)


  _pyangbind_elements = {'type': type, 'instance': instance, 'skip_deconfig': skip_deconfig, }


