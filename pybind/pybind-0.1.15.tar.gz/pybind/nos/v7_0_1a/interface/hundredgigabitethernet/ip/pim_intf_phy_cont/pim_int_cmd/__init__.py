
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pim
class pim_int_cmd(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/ip/pim-intf-phy-cont/pim-int-cmd. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pim_sparse','__pim','__mcast_bdry_prefix_list',)

  _yang_name = 'pim-int-cmd'
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
    self.__pim_sparse = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pim-sparse", rest_name="pim-sparse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Sparse Mode (PIM-SM)'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)
    self.__pim = YANGDynClass(base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PIM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)
    self.__mcast_bdry_prefix_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="mcast-bdry-prefix-list", rest_name="multicast-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Prefix list', u'alt-name': u'multicast-boundary'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='ip-prefix-name-t', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'ip', u'pim-intf-phy-cont', u'pim-int-cmd']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'ip']

  def _get_pim_sparse(self):
    """
    Getter method for pim_sparse, mapped from YANG variable /interface/hundredgigabitethernet/ip/pim_intf_phy_cont/pim_int_cmd/pim_sparse (empty)
    """
    return self.__pim_sparse
      
  def _set_pim_sparse(self, v, load=False):
    """
    Setter method for pim_sparse, mapped from YANG variable /interface/hundredgigabitethernet/ip/pim_intf_phy_cont/pim_int_cmd/pim_sparse (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_sparse is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_sparse() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="pim-sparse", rest_name="pim-sparse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Sparse Mode (PIM-SM)'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_sparse must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pim-sparse", rest_name="pim-sparse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Sparse Mode (PIM-SM)'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)""",
        })

    self.__pim_sparse = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_sparse(self):
    self.__pim_sparse = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="pim-sparse", rest_name="pim-sparse", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Sparse Mode (PIM-SM)'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='empty', is_config=True)


  def _get_pim(self):
    """
    Getter method for pim, mapped from YANG variable /interface/hundredgigabitethernet/ip/pim_intf_phy_cont/pim_int_cmd/pim (container)
    """
    return self.__pim
      
  def _set_pim(self, v, load=False):
    """
    Setter method for pim, mapped from YANG variable /interface/hundredgigabitethernet/ip/pim_intf_phy_cont/pim_int_cmd/pim (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim() directly.
    """
    try:
      t = YANGDynClass(v,base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PIM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PIM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)""",
        })

    self.__pim = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim(self):
    self.__pim = YANGDynClass(base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure PIM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='container', is_config=True)


  def _get_mcast_bdry_prefix_list(self):
    """
    Getter method for mcast_bdry_prefix_list, mapped from YANG variable /interface/hundredgigabitethernet/ip/pim_intf_phy_cont/pim_int_cmd/mcast_bdry_prefix_list (ip-prefix-name-t)
    """
    return self.__mcast_bdry_prefix_list
      
  def _set_mcast_bdry_prefix_list(self, v, load=False):
    """
    Setter method for mcast_bdry_prefix_list, mapped from YANG variable /interface/hundredgigabitethernet/ip/pim_intf_phy_cont/pim_int_cmd/mcast_bdry_prefix_list (ip-prefix-name-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mcast_bdry_prefix_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mcast_bdry_prefix_list() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="mcast-bdry-prefix-list", rest_name="multicast-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Prefix list', u'alt-name': u'multicast-boundary'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='ip-prefix-name-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mcast_bdry_prefix_list must be of a type compatible with ip-prefix-name-t""",
          'defined-type': "brocade-pim:ip-prefix-name-t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="mcast-bdry-prefix-list", rest_name="multicast-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Prefix list', u'alt-name': u'multicast-boundary'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='ip-prefix-name-t', is_config=True)""",
        })

    self.__mcast_bdry_prefix_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mcast_bdry_prefix_list(self):
    self.__mcast_bdry_prefix_list = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31})'}), is_leaf=True, yang_name="mcast-bdry-prefix-list", rest_name="multicast-boundary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Prefix list', u'alt-name': u'multicast-boundary'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='ip-prefix-name-t', is_config=True)

  pim_sparse = __builtin__.property(_get_pim_sparse, _set_pim_sparse)
  pim = __builtin__.property(_get_pim, _set_pim)
  mcast_bdry_prefix_list = __builtin__.property(_get_mcast_bdry_prefix_list, _set_mcast_bdry_prefix_list)


  _pyangbind_elements = {'pim_sparse': pim_sparse, 'pim': pim, 'mcast_bdry_prefix_list': mcast_bdry_prefix_list, }


