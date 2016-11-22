
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ether_stats_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/rmon/collection/ether-stats-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ether_stats_index','__ether_stats_owner',)

  _yang_name = 'ether-stats-entry'
  _rest_name = 'stats'

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
    self.__ether_stats_owner = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="ether-stats-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)
    self.__ether_stats_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="ether-stats-index", rest_name="ether-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='ether-stats-index-type', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'rmon', u'collection', u'ether-stats-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'rmon', u'collection', u'stats']

  def _get_ether_stats_index(self):
    """
    Getter method for ether_stats_index, mapped from YANG variable /interface/fortygigabitethernet/rmon/collection/ether_stats_entry/ether_stats_index (ether-stats-index-type)
    """
    return self.__ether_stats_index
      
  def _set_ether_stats_index(self, v, load=False):
    """
    Setter method for ether_stats_index, mapped from YANG variable /interface/fortygigabitethernet/rmon/collection/ether_stats_entry/ether_stats_index (ether-stats-index-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ether_stats_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ether_stats_index() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="ether-stats-index", rest_name="ether-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='ether-stats-index-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ether_stats_index must be of a type compatible with ether-stats-index-type""",
          'defined-type': "brocade-rmon:ether-stats-index-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="ether-stats-index", rest_name="ether-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='ether-stats-index-type', is_config=True)""",
        })

    self.__ether_stats_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ether_stats_index(self):
    self.__ether_stats_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="ether-stats-index", rest_name="ether-stats-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='ether-stats-index-type', is_config=True)


  def _get_ether_stats_owner(self):
    """
    Getter method for ether_stats_owner, mapped from YANG variable /interface/fortygigabitethernet/rmon/collection/ether_stats_entry/ether_stats_owner (owner-string)
    """
    return self.__ether_stats_owner
      
  def _set_ether_stats_owner(self, v, load=False):
    """
    Setter method for ether_stats_owner, mapped from YANG variable /interface/fortygigabitethernet/rmon/collection/ether_stats_entry/ether_stats_owner (owner-string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ether_stats_owner is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ether_stats_owner() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="ether-stats-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ether_stats_owner must be of a type compatible with owner-string""",
          'defined-type': "brocade-rmon:owner-string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="ether-stats-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)""",
        })

    self.__ether_stats_owner = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ether_stats_owner(self):
    self.__ether_stats_owner = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="ether-stats-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)

  ether_stats_index = __builtin__.property(_get_ether_stats_index, _set_ether_stats_index)
  ether_stats_owner = __builtin__.property(_get_ether_stats_owner, _set_ether_stats_owner)


  _pyangbind_elements = {'ether_stats_index': ether_stats_index, 'ether_stats_owner': ether_stats_owner, }


