
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import member_entry
class zone(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-zone - based on the path /zoning/defined-configuration/zone. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__zone_name','__member_entry',)

  _yang_name = 'zone'
  _rest_name = 'zone'

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
    self.__zone_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-zA-Z_]{1,64}', 'length': [u'1..64']}), is_leaf=True, yang_name="zone-name", rest_name="zone-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD>;;Zone-Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)
    self.__member_entry = YANGDynClass(base=YANGListType("entry_name",member_entry.member_entry, yang_name="member-entry", rest_name="member-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entry-name', extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}), is_container='list', yang_name="member-entry", rest_name="member-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)

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
      return [u'zoning', u'defined-configuration', u'zone']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'zoning', u'defined-configuration', u'zone']

  def _get_zone_name(self):
    """
    Getter method for zone_name, mapped from YANG variable /zoning/defined_configuration/zone/zone_name (string)
    """
    return self.__zone_name
      
  def _set_zone_name(self, v, load=False):
    """
    Setter method for zone_name, mapped from YANG variable /zoning/defined_configuration/zone/zone_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_zone_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_zone_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-zA-Z_]{1,64}', 'length': [u'1..64']}), is_leaf=True, yang_name="zone-name", rest_name="zone-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD>;;Zone-Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """zone_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-zA-Z_]{1,64}', 'length': [u'1..64']}), is_leaf=True, yang_name="zone-name", rest_name="zone-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD>;;Zone-Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)""",
        })

    self.__zone_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_zone_name(self):
    self.__zone_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9a-zA-Z_]{1,64}', 'length': [u'1..64']}), is_leaf=True, yang_name="zone-name", rest_name="zone-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<WORD>;;Zone-Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='string', is_config=True)


  def _get_member_entry(self):
    """
    Getter method for member_entry, mapped from YANG variable /zoning/defined_configuration/zone/member_entry (list)
    """
    return self.__member_entry
      
  def _set_member_entry(self, v, load=False):
    """
    Setter method for member_entry, mapped from YANG variable /zoning/defined_configuration/zone/member_entry (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_member_entry is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_member_entry() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("entry_name",member_entry.member_entry, yang_name="member-entry", rest_name="member-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entry-name', extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}), is_container='list', yang_name="member-entry", rest_name="member-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """member_entry must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("entry_name",member_entry.member_entry, yang_name="member-entry", rest_name="member-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entry-name', extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}), is_container='list', yang_name="member-entry", rest_name="member-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)""",
        })

    self.__member_entry = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_member_entry(self):
    self.__member_entry = YANGDynClass(base=YANGListType("entry_name",member_entry.member_entry, yang_name="member-entry", rest_name="member-entry", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='entry-name', extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}), is_container='list', yang_name="member-entry", rest_name="member-entry", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'List of Zone Members for Zone', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-suppress-key-abbreviation': None, u'hidden': u'wyser-write-hook', u'callpoint': u'zone_defined_zone_member'}}, namespace='urn:brocade.com:mgmt:brocade-zone', defining_module='brocade-zone', yang_type='list', is_config=True)

  zone_name = __builtin__.property(_get_zone_name, _set_zone_name)
  member_entry = __builtin__.property(_get_member_entry, _set_member_entry)


  _pyangbind_elements = {'zone_name': zone_name, 'member_entry': member_entry, }


