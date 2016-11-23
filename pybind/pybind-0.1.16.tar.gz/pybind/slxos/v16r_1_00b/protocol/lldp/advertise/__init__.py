
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import optional_tlv
class advertise(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/lldp/advertise. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dcbx_fcoe_app_tlv','__dcbx_fcoe_logical_link_tlv','__dcbx_iscsi_app_tlv','__dcbx_tlv','__dot1_tlv','__dot3_tlv','__optional_tlv',)

  _yang_name = 'advertise'
  _rest_name = 'advertise'

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
    self.__dcbx_fcoe_logical_link_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-logical-link-tlv", rest_name="dcbx-fcoe-logical-link-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Logical \nLink TLV', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    self.__dot1_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot1-tlv", rest_name="dot1-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.1 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    self.__optional_tlv = YANGDynClass(base=optional_tlv.optional_tlv, is_container='container', yang_name="optional-tlv", rest_name="optional-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Optional TLVs.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    self.__dcbx_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-tlv", rest_name="dcbx-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange TLV.', u'hidden': u'full', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    self.__dcbx_fcoe_app_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-app-tlv", rest_name="dcbx-fcoe-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Application\nTLV.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    self.__dcbx_iscsi_app_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-iscsi-app-tlv", rest_name="dcbx-iscsi-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange iSCSI Application\nTLV.', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    self.__dot3_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot3-tlv", rest_name="dot3-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.3 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)

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
      return [u'protocol', u'lldp', u'advertise']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'lldp', u'advertise']

  def _get_dcbx_fcoe_app_tlv(self):
    """
    Getter method for dcbx_fcoe_app_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_fcoe_app_tlv (empty)
    """
    return self.__dcbx_fcoe_app_tlv
      
  def _set_dcbx_fcoe_app_tlv(self, v, load=False):
    """
    Setter method for dcbx_fcoe_app_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_fcoe_app_tlv (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dcbx_fcoe_app_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dcbx_fcoe_app_tlv() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-app-tlv", rest_name="dcbx-fcoe-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Application\nTLV.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dcbx_fcoe_app_tlv must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-app-tlv", rest_name="dcbx-fcoe-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Application\nTLV.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__dcbx_fcoe_app_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dcbx_fcoe_app_tlv(self):
    self.__dcbx_fcoe_app_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-app-tlv", rest_name="dcbx-fcoe-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Application\nTLV.', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_dcbx_fcoe_logical_link_tlv(self):
    """
    Getter method for dcbx_fcoe_logical_link_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_fcoe_logical_link_tlv (empty)
    """
    return self.__dcbx_fcoe_logical_link_tlv
      
  def _set_dcbx_fcoe_logical_link_tlv(self, v, load=False):
    """
    Setter method for dcbx_fcoe_logical_link_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_fcoe_logical_link_tlv (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dcbx_fcoe_logical_link_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dcbx_fcoe_logical_link_tlv() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-logical-link-tlv", rest_name="dcbx-fcoe-logical-link-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Logical \nLink TLV', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dcbx_fcoe_logical_link_tlv must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-logical-link-tlv", rest_name="dcbx-fcoe-logical-link-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Logical \nLink TLV', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__dcbx_fcoe_logical_link_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dcbx_fcoe_logical_link_tlv(self):
    self.__dcbx_fcoe_logical_link_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-fcoe-logical-link-tlv", rest_name="dcbx-fcoe-logical-link-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange FCoE Logical \nLink TLV', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_dcbx_iscsi_app_tlv(self):
    """
    Getter method for dcbx_iscsi_app_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_iscsi_app_tlv (empty)
    """
    return self.__dcbx_iscsi_app_tlv
      
  def _set_dcbx_iscsi_app_tlv(self, v, load=False):
    """
    Setter method for dcbx_iscsi_app_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_iscsi_app_tlv (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dcbx_iscsi_app_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dcbx_iscsi_app_tlv() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dcbx-iscsi-app-tlv", rest_name="dcbx-iscsi-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange iSCSI Application\nTLV.', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dcbx_iscsi_app_tlv must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-iscsi-app-tlv", rest_name="dcbx-iscsi-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange iSCSI Application\nTLV.', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__dcbx_iscsi_app_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dcbx_iscsi_app_tlv(self):
    self.__dcbx_iscsi_app_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-iscsi-app-tlv", rest_name="dcbx-iscsi-app-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange iSCSI Application\nTLV.', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_dcbx_tlv(self):
    """
    Getter method for dcbx_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_tlv (empty)
    """
    return self.__dcbx_tlv
      
  def _set_dcbx_tlv(self, v, load=False):
    """
    Setter method for dcbx_tlv, mapped from YANG variable /protocol/lldp/advertise/dcbx_tlv (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dcbx_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dcbx_tlv() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dcbx-tlv", rest_name="dcbx-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange TLV.', u'hidden': u'full', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dcbx_tlv must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-tlv", rest_name="dcbx-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange TLV.', u'hidden': u'full', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__dcbx_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dcbx_tlv(self):
    self.__dcbx_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dcbx-tlv", rest_name="dcbx-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE Data Center Bridging eXchange TLV.', u'hidden': u'full', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_dot1_tlv(self):
    """
    Getter method for dot1_tlv, mapped from YANG variable /protocol/lldp/advertise/dot1_tlv (empty)
    """
    return self.__dot1_tlv
      
  def _set_dot1_tlv(self, v, load=False):
    """
    Setter method for dot1_tlv, mapped from YANG variable /protocol/lldp/advertise/dot1_tlv (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot1_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot1_tlv() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dot1-tlv", rest_name="dot1-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.1 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot1_tlv must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot1-tlv", rest_name="dot1-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.1 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__dot1_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot1_tlv(self):
    self.__dot1_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot1-tlv", rest_name="dot1-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.1 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_dot3_tlv(self):
    """
    Getter method for dot3_tlv, mapped from YANG variable /protocol/lldp/advertise/dot3_tlv (empty)
    """
    return self.__dot3_tlv
      
  def _set_dot3_tlv(self, v, load=False):
    """
    Setter method for dot3_tlv, mapped from YANG variable /protocol/lldp/advertise/dot3_tlv (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dot3_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dot3_tlv() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="dot3-tlv", rest_name="dot3-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.3 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dot3_tlv must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot3-tlv", rest_name="dot3-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.3 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__dot3_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dot3_tlv(self):
    self.__dot3_tlv = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="dot3-tlv", rest_name="dot3-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'IEEE 802.3 Organizationally Specific TLV'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_optional_tlv(self):
    """
    Getter method for optional_tlv, mapped from YANG variable /protocol/lldp/advertise/optional_tlv (container)
    """
    return self.__optional_tlv
      
  def _set_optional_tlv(self, v, load=False):
    """
    Setter method for optional_tlv, mapped from YANG variable /protocol/lldp/advertise/optional_tlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_optional_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_optional_tlv() directly.
    """
    try:
      t = YANGDynClass(v,base=optional_tlv.optional_tlv, is_container='container', yang_name="optional-tlv", rest_name="optional-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Optional TLVs.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """optional_tlv must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=optional_tlv.optional_tlv, is_container='container', yang_name="optional-tlv", rest_name="optional-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Optional TLVs.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)""",
        })

    self.__optional_tlv = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_optional_tlv(self):
    self.__optional_tlv = YANGDynClass(base=optional_tlv.optional_tlv, is_container='container', yang_name="optional-tlv", rest_name="optional-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Optional TLVs.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)

  dcbx_fcoe_app_tlv = __builtin__.property(_get_dcbx_fcoe_app_tlv, _set_dcbx_fcoe_app_tlv)
  dcbx_fcoe_logical_link_tlv = __builtin__.property(_get_dcbx_fcoe_logical_link_tlv, _set_dcbx_fcoe_logical_link_tlv)
  dcbx_iscsi_app_tlv = __builtin__.property(_get_dcbx_iscsi_app_tlv, _set_dcbx_iscsi_app_tlv)
  dcbx_tlv = __builtin__.property(_get_dcbx_tlv, _set_dcbx_tlv)
  dot1_tlv = __builtin__.property(_get_dot1_tlv, _set_dot1_tlv)
  dot3_tlv = __builtin__.property(_get_dot3_tlv, _set_dot3_tlv)
  optional_tlv = __builtin__.property(_get_optional_tlv, _set_optional_tlv)


  _pyangbind_elements = {'dcbx_fcoe_app_tlv': dcbx_fcoe_app_tlv, 'dcbx_fcoe_logical_link_tlv': dcbx_fcoe_logical_link_tlv, 'dcbx_iscsi_app_tlv': dcbx_iscsi_app_tlv, 'dcbx_tlv': dcbx_tlv, 'dot1_tlv': dot1_tlv, 'dot3_tlv': dot3_tlv, 'optional_tlv': optional_tlv, }


