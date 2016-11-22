
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class gbc(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface-ext - based on the path /brocade_interface_ext_rpc/get-media-detail/output/interface/gbc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vendor_name','__vendor_oui','__vendor_pn','__vendor_rev',)

  _yang_name = 'gbc'
  _rest_name = 'gbc'

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
    self.__vendor_oui = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-oui", rest_name="vendor-oui", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__vendor_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-name", rest_name="vendor-name", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__vendor_rev = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-rev", rest_name="vendor-rev", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__vendor_pn = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-pn", rest_name="vendor-pn", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)

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
      return [u'brocade_interface_ext_rpc', u'get-media-detail', u'output', u'interface', u'gbc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-media-detail', u'output', u'interface', u'gbc']

  def _get_vendor_name(self):
    """
    Getter method for vendor_name, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_name (string)

    YANG Description: This indicates the Vendor of this interface.
    """
    return self.__vendor_name
      
  def _set_vendor_name(self, v, load=False):
    """
    Setter method for vendor_name, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vendor_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vendor_name() directly.

    YANG Description: This indicates the Vendor of this interface.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vendor-name", rest_name="vendor-name", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vendor_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-name", rest_name="vendor-name", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__vendor_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vendor_name(self):
    self.__vendor_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-name", rest_name="vendor-name", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_vendor_oui(self):
    """
    Getter method for vendor_oui, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_oui (string)

    YANG Description: This indicates the Vendor IEEE company ID.
    """
    return self.__vendor_oui
      
  def _set_vendor_oui(self, v, load=False):
    """
    Setter method for vendor_oui, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_oui (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vendor_oui is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vendor_oui() directly.

    YANG Description: This indicates the Vendor IEEE company ID.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vendor-oui", rest_name="vendor-oui", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vendor_oui must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-oui", rest_name="vendor-oui", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__vendor_oui = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vendor_oui(self):
    self.__vendor_oui = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-oui", rest_name="vendor-oui", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_vendor_pn(self):
    """
    Getter method for vendor_pn, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_pn (string)

    YANG Description: This indicates the Part number.
    """
    return self.__vendor_pn
      
  def _set_vendor_pn(self, v, load=False):
    """
    Setter method for vendor_pn, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_pn (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vendor_pn is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vendor_pn() directly.

    YANG Description: This indicates the Part number.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vendor-pn", rest_name="vendor-pn", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vendor_pn must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-pn", rest_name="vendor-pn", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__vendor_pn = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vendor_pn(self):
    self.__vendor_pn = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-pn", rest_name="vendor-pn", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_vendor_rev(self):
    """
    Getter method for vendor_rev, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_rev (string)

    YANG Description: This indicates the Revision level.
    """
    return self.__vendor_rev
      
  def _set_vendor_rev(self, v, load=False):
    """
    Setter method for vendor_rev, mapped from YANG variable /brocade_interface_ext_rpc/get_media_detail/output/interface/gbc/vendor_rev (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vendor_rev is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vendor_rev() directly.

    YANG Description: This indicates the Revision level.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vendor-rev", rest_name="vendor-rev", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vendor_rev must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-rev", rest_name="vendor-rev", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__vendor_rev = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vendor_rev(self):
    self.__vendor_rev = YANGDynClass(base=unicode, is_leaf=True, yang_name="vendor-rev", rest_name="vendor-rev", parent=self, choice=(u'interface-identifier', u'gbic'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)

  vendor_name = __builtin__.property(_get_vendor_name, _set_vendor_name)
  vendor_oui = __builtin__.property(_get_vendor_oui, _set_vendor_oui)
  vendor_pn = __builtin__.property(_get_vendor_pn, _set_vendor_pn)
  vendor_rev = __builtin__.property(_get_vendor_rev, _set_vendor_rev)

  __choices__ = {u'interface-identifier': {u'gbic': [u'vendor_name', u'vendor_oui', u'vendor_pn', u'vendor_rev']}}
  _pyangbind_elements = {'vendor_name': vendor_name, 'vendor_oui': vendor_oui, 'vendor_pn': vendor_pn, 'vendor_rev': vendor_rev, }


