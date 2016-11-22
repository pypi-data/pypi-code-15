
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class show_mpls_interface_brief(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-interface/output/mpls-interface/show-mpls-interface-brief. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mpls_interface_name','__mpls_interface_admin_grp','__mpls_interface_admin_status','__mpls_interface_oper_status','__mpls_interface_max_bw','__mpls_interface_max_resv_bw','__mpls_interface_bypass_lsp_count','__mpls_interface_ldp_status',)

  _yang_name = 'show-mpls-interface-brief'
  _rest_name = 'show-mpls-interface-brief'

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
    self.__mpls_interface_admin_grp = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-admin-grp", rest_name="mpls-interface-admin-grp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_bypass_lsp_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-bypass-lsp-count", rest_name="mpls-interface-bypass-lsp-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_max_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-bw", rest_name="mpls-interface-max-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_admin_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-admin-status", rest_name="mpls-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__mpls_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls_interface_name", rest_name="mpls_interface_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mpls_interface_oper_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-oper-status", rest_name="mpls-interface-oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__mpls_interface_max_resv_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-resv-bw", rest_name="mpls-interface-max-resv-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mpls_interface_ldp_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-status", rest_name="mpls-interface-ldp-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-interface', u'output', u'mpls-interface', u'show-mpls-interface-brief']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-interface', u'output', u'mpls-interface', u'show-mpls-interface-brief']

  def _get_mpls_interface_name(self):
    """
    Getter method for mpls_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_name (string)

    YANG Description: MPLS Interface name
    """
    return self.__mpls_interface_name
      
  def _set_mpls_interface_name(self, v, load=False):
    """
    Setter method for mpls_interface_name, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_name() directly.

    YANG Description: MPLS Interface name
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mpls_interface_name", rest_name="mpls_interface_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls_interface_name", rest_name="mpls_interface_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__mpls_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_name(self):
    self.__mpls_interface_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="mpls_interface_name", rest_name="mpls_interface_name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_mpls_interface_admin_grp(self):
    """
    Getter method for mpls_interface_admin_grp, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_admin_grp (uint32)

    YANG Description: Admin group for the MPLS interface
    """
    return self.__mpls_interface_admin_grp
      
  def _set_mpls_interface_admin_grp(self, v, load=False):
    """
    Setter method for mpls_interface_admin_grp, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_admin_grp (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_admin_grp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_admin_grp() directly.

    YANG Description: Admin group for the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-admin-grp", rest_name="mpls-interface-admin-grp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_admin_grp must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-admin-grp", rest_name="mpls-interface-admin-grp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_admin_grp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_admin_grp(self):
    self.__mpls_interface_admin_grp = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-admin-grp", rest_name="mpls-interface-admin-grp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_admin_status(self):
    """
    Getter method for mpls_interface_admin_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_admin_status (boolean)

    YANG Description: Administrative status of the MPLS interface
    """
    return self.__mpls_interface_admin_status
      
  def _set_mpls_interface_admin_status(self, v, load=False):
    """
    Setter method for mpls_interface_admin_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_admin_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_admin_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_admin_status() directly.

    YANG Description: Administrative status of the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-admin-status", rest_name="mpls-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_admin_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-admin-status", rest_name="mpls-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_interface_admin_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_admin_status(self):
    self.__mpls_interface_admin_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-admin-status", rest_name="mpls-interface-admin-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_mpls_interface_oper_status(self):
    """
    Getter method for mpls_interface_oper_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_oper_status (boolean)

    YANG Description: Operational status of the MPLS interface
    """
    return self.__mpls_interface_oper_status
      
  def _set_mpls_interface_oper_status(self, v, load=False):
    """
    Setter method for mpls_interface_oper_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_oper_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_oper_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_oper_status() directly.

    YANG Description: Operational status of the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-oper-status", rest_name="mpls-interface-oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_oper_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-oper-status", rest_name="mpls-interface-oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_interface_oper_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_oper_status(self):
    self.__mpls_interface_oper_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-oper-status", rest_name="mpls-interface-oper-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_mpls_interface_max_bw(self):
    """
    Getter method for mpls_interface_max_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_max_bw (uint32)

    YANG Description: Maximum Physical Bandwidth of the MPLS interface in kbits/sec
    """
    return self.__mpls_interface_max_bw
      
  def _set_mpls_interface_max_bw(self, v, load=False):
    """
    Setter method for mpls_interface_max_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_max_bw (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_max_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_max_bw() directly.

    YANG Description: Maximum Physical Bandwidth of the MPLS interface in kbits/sec
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-bw", rest_name="mpls-interface-max-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_max_bw must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-bw", rest_name="mpls-interface-max-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_max_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_max_bw(self):
    self.__mpls_interface_max_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-bw", rest_name="mpls-interface-max-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_max_resv_bw(self):
    """
    Getter method for mpls_interface_max_resv_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_max_resv_bw (uint32)

    YANG Description: Maximum Reservable Bandwidth of the MPLS interface in kbits/sec
    """
    return self.__mpls_interface_max_resv_bw
      
  def _set_mpls_interface_max_resv_bw(self, v, load=False):
    """
    Setter method for mpls_interface_max_resv_bw, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_max_resv_bw (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_max_resv_bw is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_max_resv_bw() directly.

    YANG Description: Maximum Reservable Bandwidth of the MPLS interface in kbits/sec
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-resv-bw", rest_name="mpls-interface-max-resv-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_max_resv_bw must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-resv-bw", rest_name="mpls-interface-max-resv-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_max_resv_bw = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_max_resv_bw(self):
    self.__mpls_interface_max_resv_bw = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-max-resv-bw", rest_name="mpls-interface-max-resv-bw", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_bypass_lsp_count(self):
    """
    Getter method for mpls_interface_bypass_lsp_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_bypass_lsp_count (uint32)

    YANG Description: Number of Bypass LSPs protecting the MPLS interface
    """
    return self.__mpls_interface_bypass_lsp_count
      
  def _set_mpls_interface_bypass_lsp_count(self, v, load=False):
    """
    Setter method for mpls_interface_bypass_lsp_count, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_bypass_lsp_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_bypass_lsp_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_bypass_lsp_count() directly.

    YANG Description: Number of Bypass LSPs protecting the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-bypass-lsp-count", rest_name="mpls-interface-bypass-lsp-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_bypass_lsp_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-bypass-lsp-count", rest_name="mpls-interface-bypass-lsp-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mpls_interface_bypass_lsp_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_bypass_lsp_count(self):
    self.__mpls_interface_bypass_lsp_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mpls-interface-bypass-lsp-count", rest_name="mpls-interface-bypass-lsp-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mpls_interface_ldp_status(self):
    """
    Getter method for mpls_interface_ldp_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_ldp_status (boolean)

    YANG Description: Operational status of LDP signalling on the MPLS interface
    """
    return self.__mpls_interface_ldp_status
      
  def _set_mpls_interface_ldp_status(self, v, load=False):
    """
    Setter method for mpls_interface_ldp_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_interface/output/mpls_interface/show_mpls_interface_brief/mpls_interface_ldp_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mpls_interface_ldp_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mpls_interface_ldp_status() directly.

    YANG Description: Operational status of LDP signalling on the MPLS interface
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-status", rest_name="mpls-interface-ldp-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mpls_interface_ldp_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-status", rest_name="mpls-interface-ldp-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__mpls_interface_ldp_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mpls_interface_ldp_status(self):
    self.__mpls_interface_ldp_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="mpls-interface-ldp-status", rest_name="mpls-interface-ldp-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

  mpls_interface_name = __builtin__.property(_get_mpls_interface_name, _set_mpls_interface_name)
  mpls_interface_admin_grp = __builtin__.property(_get_mpls_interface_admin_grp, _set_mpls_interface_admin_grp)
  mpls_interface_admin_status = __builtin__.property(_get_mpls_interface_admin_status, _set_mpls_interface_admin_status)
  mpls_interface_oper_status = __builtin__.property(_get_mpls_interface_oper_status, _set_mpls_interface_oper_status)
  mpls_interface_max_bw = __builtin__.property(_get_mpls_interface_max_bw, _set_mpls_interface_max_bw)
  mpls_interface_max_resv_bw = __builtin__.property(_get_mpls_interface_max_resv_bw, _set_mpls_interface_max_resv_bw)
  mpls_interface_bypass_lsp_count = __builtin__.property(_get_mpls_interface_bypass_lsp_count, _set_mpls_interface_bypass_lsp_count)
  mpls_interface_ldp_status = __builtin__.property(_get_mpls_interface_ldp_status, _set_mpls_interface_ldp_status)


  _pyangbind_elements = {'mpls_interface_name': mpls_interface_name, 'mpls_interface_admin_grp': mpls_interface_admin_grp, 'mpls_interface_admin_status': mpls_interface_admin_status, 'mpls_interface_oper_status': mpls_interface_oper_status, 'mpls_interface_max_bw': mpls_interface_max_bw, 'mpls_interface_max_resv_bw': mpls_interface_max_resv_bw, 'mpls_interface_bypass_lsp_count': mpls_interface_bypass_lsp_count, 'mpls_interface_ldp_status': mpls_interface_ldp_status, }


