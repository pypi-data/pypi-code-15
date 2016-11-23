
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import raslog_entries
class show_all_raslog(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras-ext - based on the path /brocade_ras_ext_rpc/show-raslog/output/show-all-raslog. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridge_id','__number_of_entries','__raslog_entries',)

  _yang_name = 'show-all-raslog'
  _rest_name = 'show-all-raslog'

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
    self.__raslog_entries = YANGDynClass(base=YANGListType(False,raslog_entries.raslog_entries, yang_name="raslog-entries", rest_name="raslog-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="raslog-entries", rest_name="raslog-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='list', is_config=True)
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)
    self.__number_of_entries = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", rest_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)

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
      return [u'brocade_ras_ext_rpc', u'show-raslog', u'output', u'show-all-raslog']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-raslog', u'output', u'show-all-raslog']

  def _get_rbridge_id(self):
    """
    Getter method for rbridge_id, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/rbridge_id (switchid-type)
    """
    return self.__rbridge_id
      
  def _set_rbridge_id(self, v, load=False):
    """
    Setter method for rbridge_id, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/rbridge_id (switchid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridge_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridge_id() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridge_id must be of a type compatible with switchid-type""",
          'defined-type': "brocade-ras-ext:switchid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)""",
        })

    self.__rbridge_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridge_id(self):
    self.__rbridge_id = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..3']}), is_leaf=True, yang_name="rbridge-id", rest_name="rbridge-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='switchid-type', is_config=True)


  def _get_number_of_entries(self):
    """
    Getter method for number_of_entries, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/number_of_entries (uint32)

    YANG Description: This specifies the number of entries in the  be fetched
    """
    return self.__number_of_entries
      
  def _set_number_of_entries(self, v, load=False):
    """
    Setter method for number_of_entries, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/number_of_entries (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_number_of_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_number_of_entries() directly.

    YANG Description: This specifies the number of entries in the  be fetched
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", rest_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """number_of_entries must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", rest_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)""",
        })

    self.__number_of_entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_number_of_entries(self):
    self.__number_of_entries = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="number-of-entries", rest_name="number-of-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='uint32', is_config=True)


  def _get_raslog_entries(self):
    """
    Getter method for raslog_entries, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries (list)
    """
    return self.__raslog_entries
      
  def _set_raslog_entries(self, v, load=False):
    """
    Setter method for raslog_entries, mapped from YANG variable /brocade_ras_ext_rpc/show_raslog/output/show_all_raslog/raslog_entries (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_raslog_entries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_raslog_entries() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType(False,raslog_entries.raslog_entries, yang_name="raslog-entries", rest_name="raslog-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="raslog-entries", rest_name="raslog-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """raslog_entries must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,raslog_entries.raslog_entries, yang_name="raslog-entries", rest_name="raslog-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="raslog-entries", rest_name="raslog-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='list', is_config=True)""",
        })

    self.__raslog_entries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_raslog_entries(self):
    self.__raslog_entries = YANGDynClass(base=YANGListType(False,raslog_entries.raslog_entries, yang_name="raslog-entries", rest_name="raslog-entries", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="raslog-entries", rest_name="raslog-entries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-ras-ext', defining_module='brocade-ras-ext', yang_type='list', is_config=True)

  rbridge_id = __builtin__.property(_get_rbridge_id, _set_rbridge_id)
  number_of_entries = __builtin__.property(_get_number_of_entries, _set_number_of_entries)
  raslog_entries = __builtin__.property(_get_raslog_entries, _set_raslog_entries)


  _pyangbind_elements = {'rbridge_id': rbridge_id, 'number_of_entries': number_of_entries, 'raslog_entries': raslog_entries, }


