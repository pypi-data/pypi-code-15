
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class prefix_nexthops(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/fec/ldp-fec-prefix-prefix/prefix-nexthops. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__nexthop','__out_intf',)

  _yang_name = 'prefix-nexthops'
  _rest_name = 'prefix-nexthops'

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
    self.__nexthop = YANGDynClass(base=unicode, is_leaf=True, yang_name="nexthop", rest_name="nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    self.__out_intf = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-intf", rest_name="out-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)

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
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefix-prefix', u'prefix-nexthops']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'fec', u'ldp-fec-prefix-prefix', u'prefix-nexthops']

  def _get_nexthop(self):
    """
    Getter method for nexthop, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_nexthops/nexthop (string)

    YANG Description: nexthop
    """
    return self.__nexthop
      
  def _set_nexthop(self, v, load=False):
    """
    Setter method for nexthop, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_nexthops/nexthop (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nexthop is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nexthop() directly.

    YANG Description: nexthop
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="nexthop", rest_name="nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nexthop must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="nexthop", rest_name="nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__nexthop = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nexthop(self):
    self.__nexthop = YANGDynClass(base=unicode, is_leaf=True, yang_name="nexthop", rest_name="nexthop", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)


  def _get_out_intf(self):
    """
    Getter method for out_intf, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_nexthops/out_intf (string)

    YANG Description: out_intf
    """
    return self.__out_intf
      
  def _set_out_intf(self, v, load=False):
    """
    Setter method for out_intf, mapped from YANG variable /mpls_state/ldp/fec/ldp_fec_prefix_prefix/prefix_nexthops/out_intf (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_intf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_intf() directly.

    YANG Description: out_intf
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="out-intf", rest_name="out-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_intf must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="out-intf", rest_name="out-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)""",
        })

    self.__out_intf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_intf(self):
    self.__out_intf = YANGDynClass(base=unicode, is_leaf=True, yang_name="out-intf", rest_name="out-intf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='string', is_config=False)

  nexthop = __builtin__.property(_get_nexthop)
  out_intf = __builtin__.property(_get_out_intf)


  _pyangbind_elements = {'nexthop': nexthop, 'out_intf': out_intf, }


