
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldp_fec_prefix_rec_list
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-fec-prefix-prefix-filter/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_tot_no_of_prefix_fec','__ldp_tot_no_of_prefix_fec_installed','__ldp_tot_no_of_prefix_fec_filtered','__ldp_tot_no_of_prefix_fec_lwd','__ldp_fec_prefix_rec_list',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__ldp_tot_no_of_prefix_fec = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec", rest_name="ldp-tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_tot_no_of_prefix_fec_installed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-installed", rest_name="ldp-tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_tot_no_of_prefix_fec_filtered = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-filtered", rest_name="ldp-tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_tot_no_of_prefix_fec_lwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-lwd", rest_name="ldp-tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_fec_prefix_rec_list = YANGDynClass(base=YANGListType("ldp_fec_destination",ldp_fec_prefix_rec_list.ldp_fec_prefix_rec_list, yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-destination', extensions=None), is_container='list', yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-fec-prefix-prefix-filter', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-ldp-fec-prefix-prefix-filter', u'output']

  def _get_ldp_tot_no_of_prefix_fec(self):
    """
    Getter method for ldp_tot_no_of_prefix_fec, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec (uint32)

    YANG Description: Total number of prefix FECs
    """
    return self.__ldp_tot_no_of_prefix_fec
      
  def _set_ldp_tot_no_of_prefix_fec(self, v, load=False):
    """
    Setter method for ldp_tot_no_of_prefix_fec, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tot_no_of_prefix_fec is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tot_no_of_prefix_fec() directly.

    YANG Description: Total number of prefix FECs
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec", rest_name="ldp-tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tot_no_of_prefix_fec must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec", rest_name="ldp-tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_tot_no_of_prefix_fec = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tot_no_of_prefix_fec(self):
    self.__ldp_tot_no_of_prefix_fec = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec", rest_name="ldp-tot-no-of-prefix-fec", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_tot_no_of_prefix_fec_installed(self):
    """
    Getter method for ldp_tot_no_of_prefix_fec_installed, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec_installed (uint32)

    YANG Description: Total number of prefix FECs installed
    """
    return self.__ldp_tot_no_of_prefix_fec_installed
      
  def _set_ldp_tot_no_of_prefix_fec_installed(self, v, load=False):
    """
    Setter method for ldp_tot_no_of_prefix_fec_installed, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec_installed (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tot_no_of_prefix_fec_installed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tot_no_of_prefix_fec_installed() directly.

    YANG Description: Total number of prefix FECs installed
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-installed", rest_name="ldp-tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tot_no_of_prefix_fec_installed must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-installed", rest_name="ldp-tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_tot_no_of_prefix_fec_installed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tot_no_of_prefix_fec_installed(self):
    self.__ldp_tot_no_of_prefix_fec_installed = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-installed", rest_name="ldp-tot-no-of-prefix-fec-installed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_tot_no_of_prefix_fec_filtered(self):
    """
    Getter method for ldp_tot_no_of_prefix_fec_filtered, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec_filtered (uint32)

    YANG Description: Total number of prefix FECs filtered(in/out)
    """
    return self.__ldp_tot_no_of_prefix_fec_filtered
      
  def _set_ldp_tot_no_of_prefix_fec_filtered(self, v, load=False):
    """
    Setter method for ldp_tot_no_of_prefix_fec_filtered, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec_filtered (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tot_no_of_prefix_fec_filtered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tot_no_of_prefix_fec_filtered() directly.

    YANG Description: Total number of prefix FECs filtered(in/out)
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-filtered", rest_name="ldp-tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tot_no_of_prefix_fec_filtered must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-filtered", rest_name="ldp-tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_tot_no_of_prefix_fec_filtered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tot_no_of_prefix_fec_filtered(self):
    self.__ldp_tot_no_of_prefix_fec_filtered = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-filtered", rest_name="ldp-tot-no-of-prefix-fec-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_tot_no_of_prefix_fec_lwd(self):
    """
    Getter method for ldp_tot_no_of_prefix_fec_lwd, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec_lwd (uint32)

    YANG Description: Total number of prefix FECs with LWD timer running
    """
    return self.__ldp_tot_no_of_prefix_fec_lwd
      
  def _set_ldp_tot_no_of_prefix_fec_lwd(self, v, load=False):
    """
    Setter method for ldp_tot_no_of_prefix_fec_lwd, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_tot_no_of_prefix_fec_lwd (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tot_no_of_prefix_fec_lwd is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tot_no_of_prefix_fec_lwd() directly.

    YANG Description: Total number of prefix FECs with LWD timer running
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-lwd", rest_name="ldp-tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tot_no_of_prefix_fec_lwd must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-lwd", rest_name="ldp-tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_tot_no_of_prefix_fec_lwd = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tot_no_of_prefix_fec_lwd(self):
    self.__ldp_tot_no_of_prefix_fec_lwd = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-tot-no-of-prefix-fec-lwd", rest_name="ldp-tot-no-of-prefix-fec-lwd", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_ldp_fec_prefix_rec_list(self):
    """
    Getter method for ldp_fec_prefix_rec_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list (list)
    """
    return self.__ldp_fec_prefix_rec_list
      
  def _set_ldp_fec_prefix_rec_list(self, v, load=False):
    """
    Setter method for ldp_fec_prefix_rec_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_prefix_filter/output/ldp_fec_prefix_rec_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_prefix_rec_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_prefix_rec_list() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("ldp_fec_destination",ldp_fec_prefix_rec_list.ldp_fec_prefix_rec_list, yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-destination', extensions=None), is_container='list', yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_prefix_rec_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ldp_fec_destination",ldp_fec_prefix_rec_list.ldp_fec_prefix_rec_list, yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-destination', extensions=None), is_container='list', yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__ldp_fec_prefix_rec_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_prefix_rec_list(self):
    self.__ldp_fec_prefix_rec_list = YANGDynClass(base=YANGListType("ldp_fec_destination",ldp_fec_prefix_rec_list.ldp_fec_prefix_rec_list, yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-fec-destination', extensions=None), is_container='list', yang_name="ldp-fec-prefix-rec-list", rest_name="ldp-fec-prefix-rec-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  ldp_tot_no_of_prefix_fec = __builtin__.property(_get_ldp_tot_no_of_prefix_fec, _set_ldp_tot_no_of_prefix_fec)
  ldp_tot_no_of_prefix_fec_installed = __builtin__.property(_get_ldp_tot_no_of_prefix_fec_installed, _set_ldp_tot_no_of_prefix_fec_installed)
  ldp_tot_no_of_prefix_fec_filtered = __builtin__.property(_get_ldp_tot_no_of_prefix_fec_filtered, _set_ldp_tot_no_of_prefix_fec_filtered)
  ldp_tot_no_of_prefix_fec_lwd = __builtin__.property(_get_ldp_tot_no_of_prefix_fec_lwd, _set_ldp_tot_no_of_prefix_fec_lwd)
  ldp_fec_prefix_rec_list = __builtin__.property(_get_ldp_fec_prefix_rec_list, _set_ldp_fec_prefix_rec_list)


  _pyangbind_elements = {'ldp_tot_no_of_prefix_fec': ldp_tot_no_of_prefix_fec, 'ldp_tot_no_of_prefix_fec_installed': ldp_tot_no_of_prefix_fec_installed, 'ldp_tot_no_of_prefix_fec_filtered': ldp_tot_no_of_prefix_fec_filtered, 'ldp_tot_no_of_prefix_fec_lwd': ldp_tot_no_of_prefix_fec_lwd, 'ldp_fec_prefix_rec_list': ldp_fec_prefix_rec_list, }


