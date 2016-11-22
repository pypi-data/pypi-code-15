
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-fec-prefix-filtered/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_fec_prefix_filtered','__ldp_fec_prefix_filtered_in','__ldp_fec_prefix_filtered_out',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__ldp_fec_prefix_filtered_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-in", rest_name="ldp-fec-prefix-filtered-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__ldp_fec_prefix_filtered_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-out", rest_name="ldp-fec-prefix-filtered-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__ldp_fec_prefix_filtered = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered", rest_name="ldp-fec-prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-fec-prefix-filtered', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-ldp-fec-prefix-filtered', u'input']

  def _get_ldp_fec_prefix_filtered(self):
    """
    Getter method for ldp_fec_prefix_filtered, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_filtered/input/ldp_fec_prefix_filtered (boolean)

    YANG Description: Filtered prefix FEC
    """
    return self.__ldp_fec_prefix_filtered
      
  def _set_ldp_fec_prefix_filtered(self, v, load=False):
    """
    Setter method for ldp_fec_prefix_filtered, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_filtered/input/ldp_fec_prefix_filtered (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_prefix_filtered is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_prefix_filtered() directly.

    YANG Description: Filtered prefix FEC
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered", rest_name="ldp-fec-prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_prefix_filtered must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered", rest_name="ldp-fec-prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__ldp_fec_prefix_filtered = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_prefix_filtered(self):
    self.__ldp_fec_prefix_filtered = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered", rest_name="ldp-fec-prefix-filtered", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_ldp_fec_prefix_filtered_in(self):
    """
    Getter method for ldp_fec_prefix_filtered_in, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_filtered/input/ldp_fec_prefix_filtered_in (boolean)

    YANG Description: Inbound filtered prefix FEC
    """
    return self.__ldp_fec_prefix_filtered_in
      
  def _set_ldp_fec_prefix_filtered_in(self, v, load=False):
    """
    Setter method for ldp_fec_prefix_filtered_in, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_filtered/input/ldp_fec_prefix_filtered_in (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_prefix_filtered_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_prefix_filtered_in() directly.

    YANG Description: Inbound filtered prefix FEC
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-in", rest_name="ldp-fec-prefix-filtered-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_prefix_filtered_in must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-in", rest_name="ldp-fec-prefix-filtered-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__ldp_fec_prefix_filtered_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_prefix_filtered_in(self):
    self.__ldp_fec_prefix_filtered_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-in", rest_name="ldp-fec-prefix-filtered-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_ldp_fec_prefix_filtered_out(self):
    """
    Getter method for ldp_fec_prefix_filtered_out, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_filtered/input/ldp_fec_prefix_filtered_out (boolean)

    YANG Description: Outbound filtered prefix FEC
    """
    return self.__ldp_fec_prefix_filtered_out
      
  def _set_ldp_fec_prefix_filtered_out(self, v, load=False):
    """
    Setter method for ldp_fec_prefix_filtered_out, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_fec_prefix_filtered/input/ldp_fec_prefix_filtered_out (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_fec_prefix_filtered_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_fec_prefix_filtered_out() directly.

    YANG Description: Outbound filtered prefix FEC
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-out", rest_name="ldp-fec-prefix-filtered-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_fec_prefix_filtered_out must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-out", rest_name="ldp-fec-prefix-filtered-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__ldp_fec_prefix_filtered_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_fec_prefix_filtered_out(self):
    self.__ldp_fec_prefix_filtered_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-fec-prefix-filtered-out", rest_name="ldp-fec-prefix-filtered-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

  ldp_fec_prefix_filtered = __builtin__.property(_get_ldp_fec_prefix_filtered, _set_ldp_fec_prefix_filtered)
  ldp_fec_prefix_filtered_in = __builtin__.property(_get_ldp_fec_prefix_filtered_in, _set_ldp_fec_prefix_filtered_in)
  ldp_fec_prefix_filtered_out = __builtin__.property(_get_ldp_fec_prefix_filtered_out, _set_ldp_fec_prefix_filtered_out)


  _pyangbind_elements = {'ldp_fec_prefix_filtered': ldp_fec_prefix_filtered, 'ldp_fec_prefix_filtered_in': ldp_fec_prefix_filtered_in, 'ldp_fec_prefix_filtered_out': ldp_fec_prefix_filtered_out, }


