
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import allowed
import trunk_vlan_classification
import default_vlan_config
import tag
import native_vlan_classification
import native_vlan_xtagged_config
import native_vlan_untagged_config
class trunk(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/fortygigabitethernet/switchport/trunk. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The trunking characteristics of this interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__allowed','__trunk_vlan_classification','__default_vlan_config','__tag','__native_vlan_classification','__native_vlan_xtagged_config','__native_vlan_untagged_config',)

  _yang_name = 'trunk'
  _rest_name = 'trunk'

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
    self.__native_vlan_classification = YANGDynClass(base=native_vlan_classification.native_vlan_classification, is_container='container', yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__trunk_vlan_classification = YANGDynClass(base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__native_vlan_untagged_config = YANGDynClass(base=native_vlan_untagged_config.native_vlan_untagged_config, is_container='container', yang_name="native-vlan-untagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__tag = YANGDynClass(base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'callpoint': u'native_vlan_phy_interface_conf', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__default_vlan_config = YANGDynClass(base=default_vlan_config.default_vlan_config, is_container='container', yang_name="default-vlan-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__allowed = YANGDynClass(base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__native_vlan_xtagged_config = YANGDynClass(base=native_vlan_xtagged_config.native_vlan_xtagged_config, is_container='container', yang_name="native-vlan-xtagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'fortygigabitethernet', u'switchport', u'trunk']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'FortyGigabitEthernet', u'switchport', u'trunk']

  def _get_allowed(self):
    """
    Getter method for allowed, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/allowed (container)

    YANG Description: Set the VLANs that will Xmit/Rx through the Layer2
interface
    """
    return self.__allowed
      
  def _set_allowed(self, v, load=False):
    """
    Setter method for allowed, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/allowed (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allowed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allowed() directly.

    YANG Description: Set the VLANs that will Xmit/Rx through the Layer2
interface
    """
    try:
      t = YANGDynClass(v,base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allowed must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__allowed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allowed(self):
    self.__allowed = YANGDynClass(base=allowed.allowed, is_container='container', yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_trunk_vlan_classification(self):
    """
    Getter method for trunk_vlan_classification, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/trunk_vlan_classification (container)
    """
    return self.__trunk_vlan_classification
      
  def _set_trunk_vlan_classification(self, v, load=False):
    """
    Setter method for trunk_vlan_classification, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/trunk_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_vlan_classification() directly.
    """
    try:
      t = YANGDynClass(v,base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__trunk_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_vlan_classification(self):
    self.__trunk_vlan_classification = YANGDynClass(base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_default_vlan_config(self):
    """
    Getter method for default_vlan_config, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/default_vlan_config (container)
    """
    return self.__default_vlan_config
      
  def _set_default_vlan_config(self, v, load=False):
    """
    Setter method for default_vlan_config, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/default_vlan_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_vlan_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_vlan_config() directly.
    """
    try:
      t = YANGDynClass(v,base=default_vlan_config.default_vlan_config, is_container='container', yang_name="default-vlan-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_vlan_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=default_vlan_config.default_vlan_config, is_container='container', yang_name="default-vlan-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__default_vlan_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_vlan_config(self):
    self.__default_vlan_config = YANGDynClass(base=default_vlan_config.default_vlan_config, is_container='container', yang_name="default-vlan-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_tag(self):
    """
    Getter method for tag, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/tag (container)

    YANG Description: This specifies vlan tagging characteristics for a 
trunk port.
    """
    return self.__tag
      
  def _set_tag(self, v, load=False):
    """
    Setter method for tag, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/tag (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tag() directly.

    YANG Description: This specifies vlan tagging characteristics for a 
trunk port.
    """
    try:
      t = YANGDynClass(v,base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'callpoint': u'native_vlan_phy_interface_conf', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tag must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'callpoint': u'native_vlan_phy_interface_conf', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__tag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tag(self):
    self.__tag = YANGDynClass(base=tag.tag, is_container='container', yang_name="tag", rest_name="tag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable tagging', u'callpoint': u'native_vlan_phy_interface_conf', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_native_vlan_classification(self):
    """
    Getter method for native_vlan_classification, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/native_vlan_classification (container)
    """
    return self.__native_vlan_classification
      
  def _set_native_vlan_classification(self, v, load=False):
    """
    Setter method for native_vlan_classification, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/native_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan_classification() directly.
    """
    try:
      t = YANGDynClass(v,base=native_vlan_classification.native_vlan_classification, is_container='container', yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=native_vlan_classification.native_vlan_classification, is_container='container', yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__native_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan_classification(self):
    self.__native_vlan_classification = YANGDynClass(base=native_vlan_classification.native_vlan_classification, is_container='container', yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_native_vlan_xtagged_config(self):
    """
    Getter method for native_vlan_xtagged_config, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/native_vlan_xtagged_config (container)
    """
    return self.__native_vlan_xtagged_config
      
  def _set_native_vlan_xtagged_config(self, v, load=False):
    """
    Setter method for native_vlan_xtagged_config, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/native_vlan_xtagged_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan_xtagged_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan_xtagged_config() directly.
    """
    try:
      t = YANGDynClass(v,base=native_vlan_xtagged_config.native_vlan_xtagged_config, is_container='container', yang_name="native-vlan-xtagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan_xtagged_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=native_vlan_xtagged_config.native_vlan_xtagged_config, is_container='container', yang_name="native-vlan-xtagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__native_vlan_xtagged_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan_xtagged_config(self):
    self.__native_vlan_xtagged_config = YANGDynClass(base=native_vlan_xtagged_config.native_vlan_xtagged_config, is_container='container', yang_name="native-vlan-xtagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_native_vlan_untagged_config(self):
    """
    Getter method for native_vlan_untagged_config, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/native_vlan_untagged_config (container)
    """
    return self.__native_vlan_untagged_config
      
  def _set_native_vlan_untagged_config(self, v, load=False):
    """
    Setter method for native_vlan_untagged_config, mapped from YANG variable /interface/fortygigabitethernet/switchport/trunk/native_vlan_untagged_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan_untagged_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan_untagged_config() directly.
    """
    try:
      t = YANGDynClass(v,base=native_vlan_untagged_config.native_vlan_untagged_config, is_container='container', yang_name="native-vlan-untagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan_untagged_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=native_vlan_untagged_config.native_vlan_untagged_config, is_container='container', yang_name="native-vlan-untagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__native_vlan_untagged_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan_untagged_config(self):
    self.__native_vlan_untagged_config = YANGDynClass(base=native_vlan_untagged_config.native_vlan_untagged_config, is_container='container', yang_name="native-vlan-untagged-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  allowed = __builtin__.property(_get_allowed, _set_allowed)
  trunk_vlan_classification = __builtin__.property(_get_trunk_vlan_classification, _set_trunk_vlan_classification)
  default_vlan_config = __builtin__.property(_get_default_vlan_config, _set_default_vlan_config)
  tag = __builtin__.property(_get_tag, _set_tag)
  native_vlan_classification = __builtin__.property(_get_native_vlan_classification, _set_native_vlan_classification)
  native_vlan_xtagged_config = __builtin__.property(_get_native_vlan_xtagged_config, _set_native_vlan_xtagged_config)
  native_vlan_untagged_config = __builtin__.property(_get_native_vlan_untagged_config, _set_native_vlan_untagged_config)


  _pyangbind_elements = {'allowed': allowed, 'trunk_vlan_classification': trunk_vlan_classification, 'default_vlan_config': default_vlan_config, 'tag': tag, 'native_vlan_classification': native_vlan_classification, 'native_vlan_xtagged_config': native_vlan_xtagged_config, 'native_vlan_untagged_config': native_vlan_untagged_config, }


