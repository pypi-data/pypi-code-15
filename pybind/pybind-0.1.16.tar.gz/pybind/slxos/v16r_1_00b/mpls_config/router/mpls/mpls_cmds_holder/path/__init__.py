
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import path_hop
import path_insert
class path(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__path_name','__path_hop','__path_insert',)

  _yang_name = 'path'
  _rest_name = 'path'

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
    self.__path_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__path_insert = YANGDynClass(base=YANGListType("path_insert_ip",path_insert.path_insert, yang_name="path-insert", rest_name="insert", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-insert-ip', extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}), is_container='list', yang_name="path-insert", rest_name="insert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__path_hop = YANGDynClass(base=YANGListType("path_hop_ip",path_hop.path_hop, yang_name="path-hop", rest_name="hop", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='path-hop-ip', extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}), is_container='list', yang_name="path-hop", rest_name="hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'path']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'path']

  def _get_path_name(self):
    """
    Getter method for path_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_name (string)
    """
    return self.__path_name
      
  def _set_path_name(self, v, load=False):
    """
    Setter method for path_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__path_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_name(self):
    self.__path_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="path-name", rest_name="path-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_path_hop(self):
    """
    Getter method for path_hop, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_hop (list)
    """
    return self.__path_hop
      
  def _set_path_hop(self, v, load=False):
    """
    Setter method for path_hop, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_hop (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_hop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_hop() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("path_hop_ip",path_hop.path_hop, yang_name="path-hop", rest_name="hop", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='path-hop-ip', extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}), is_container='list', yang_name="path-hop", rest_name="hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_hop must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("path_hop_ip",path_hop.path_hop, yang_name="path-hop", rest_name="hop", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='path-hop-ip', extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}), is_container='list', yang_name="path-hop", rest_name="hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__path_hop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_hop(self):
    self.__path_hop = YANGDynClass(base=YANGListType("path_hop_ip",path_hop.path_hop, yang_name="path-hop", rest_name="hop", parent=self, is_container='list', user_ordered=True, path_helper=self._path_helper, yang_keys='path-hop-ip', extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}), is_container='list', yang_name="path-hop", rest_name="hop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure path strict or loose hops', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-full-no': None, u'alt-name': u'hop', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathHop'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)


  def _get_path_insert(self):
    """
    Getter method for path_insert, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert (list)
    """
    return self.__path_insert
      
  def _set_path_insert(self, v, load=False):
    """
    Setter method for path_insert, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/path/path_insert (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_path_insert is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_path_insert() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("path_insert_ip",path_insert.path_insert, yang_name="path-insert", rest_name="insert", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-insert-ip', extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}), is_container='list', yang_name="path-insert", rest_name="insert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """path_insert must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("path_insert_ip",path_insert.path_insert, yang_name="path-insert", rest_name="insert", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-insert-ip', extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}), is_container='list', yang_name="path-insert", rest_name="insert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__path_insert = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_path_insert(self):
    self.__path_insert = YANGDynClass(base=YANGListType("path_insert_ip",path_insert.path_insert, yang_name="path-insert", rest_name="insert", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='path-insert-ip', extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}), is_container='list', yang_name="path-insert", rest_name="insert", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Insert path strict or loose hops', u'cli-suppress-mode': None, u'cli-suppress-no': None, u'alt-name': u'insert', u'cli-sequence-commands': None, u'cli-incomplete-command': None, u'callpoint': u'MplsPathInsert'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  path_name = __builtin__.property(_get_path_name, _set_path_name)
  path_hop = __builtin__.property(_get_path_hop, _set_path_hop)
  path_insert = __builtin__.property(_get_path_insert, _set_path_insert)


  _pyangbind_elements = {'path_name': path_name, 'path_hop': path_hop, 'path_insert': path_insert, }


