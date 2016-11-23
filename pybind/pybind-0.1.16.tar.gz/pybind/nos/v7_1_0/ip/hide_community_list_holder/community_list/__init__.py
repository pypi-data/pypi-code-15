
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import standard
import extended
class community_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /ip/hide-community-list-holder/community-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__standard','__extended',)

  _yang_name = 'community-list'
  _rest_name = 'community-list'

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
    self.__extended = YANGDynClass(base=YANGListType("name seq_keyword instance",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    self.__standard = YANGDynClass(base=YANGListType("name seq_keyword instance",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

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
      return [u'ip', u'hide-community-list-holder', u'community-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ip', u'community-list']

  def _get_standard(self):
    """
    Getter method for standard, mapped from YANG variable /ip/hide_community_list_holder/community_list/standard (list)

    YANG Description: Standard community list.
    """
    return self.__standard
      
  def _set_standard(self, v, load=False):
    """
    Setter method for standard, mapped from YANG variable /ip/hide_community_list_holder/community_list/standard (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_standard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_standard() directly.

    YANG Description: Standard community list.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("name seq_keyword instance",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """standard must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name seq_keyword instance",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)""",
        })

    self.__standard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_standard(self):
    self.__standard = YANGDynClass(base=YANGListType("name seq_keyword instance",standard.standard, yang_name="standard", rest_name="standard", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}), is_container='list', yang_name="standard", rest_name="standard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Standard community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityStdAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)


  def _get_extended(self):
    """
    Getter method for extended, mapped from YANG variable /ip/hide_community_list_holder/community_list/extended (list)

    YANG Description: Extended community list.
    """
    return self.__extended
      
  def _set_extended(self, v, load=False):
    """
    Setter method for extended, mapped from YANG variable /ip/hide_community_list_holder/community_list/extended (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extended is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extended() directly.

    YANG Description: Extended community list.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("name seq_keyword instance",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extended must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("name seq_keyword instance",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)""",
        })

    self.__extended = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extended(self):
    self.__extended = YANGDynClass(base=YANGListType("name seq_keyword instance",extended.extended, yang_name="extended", rest_name="extended", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='name seq-keyword instance', extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}), is_container='list', yang_name="extended", rest_name="extended", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extended community list.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'callpoint': u'ipCommunityExtAccessList'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='list', is_config=True)

  standard = __builtin__.property(_get_standard, _set_standard)
  extended = __builtin__.property(_get_extended, _set_extended)


  _pyangbind_elements = {'standard': standard, 'extended': extended, }


