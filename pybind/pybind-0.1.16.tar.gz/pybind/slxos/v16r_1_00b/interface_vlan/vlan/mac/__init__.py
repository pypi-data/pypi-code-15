
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import access_group
class mac(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface-vlan/vlan/mac. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__access_group',)

  _yang_name = 'mac'
  _rest_name = 'mac'

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
    self.__access_group = YANGDynClass(base=YANGListType("mac_access_list mac_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-access-list mac-direction', extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)

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
      return [u'interface-vlan', u'vlan', u'mac']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vlan', u'mac']

  def _get_access_group(self):
    """
    Getter method for access_group, mapped from YANG variable /interface_vlan/vlan/mac/access_group (list)
    """
    return self.__access_group
      
  def _set_access_group(self, v, load=False):
    """
    Setter method for access_group, mapped from YANG variable /interface_vlan/vlan/mac/access_group (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_group() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("mac_access_list mac_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-access-list mac-direction', extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_group must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mac_access_list mac_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-access-list mac-direction', extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)""",
        })

    self.__access_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_group(self):
    self.__access_group = YANGDynClass(base=YANGListType("mac_access_list mac_direction",access_group.access_group, yang_name="access-group", rest_name="access-group", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mac-access-list mac-direction', extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}), is_container='list', yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC Access group', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-suppress-key-abbreviation': None}}, namespace='urn:brocade.com:mgmt:brocade-mac-access-list', defining_module='brocade-mac-access-list', yang_type='list', is_config=True)

  access_group = __builtin__.property(_get_access_group, _set_access_group)


  _pyangbind_elements = {'access_group': access_group, }


