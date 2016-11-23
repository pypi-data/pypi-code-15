
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fabric_isl
import fabric_trunk
import neighbor_discovery
import fabric_dport
class fabric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/fabric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure the Fabric Protocol parameters
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fabric_isl','__fabric_trunk','__neighbor_discovery','__fabric_dport',)

  _yang_name = 'fabric'
  _rest_name = 'fabric'

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
    self.__fabric_isl = YANGDynClass(base=fabric_isl.fabric_isl, is_container='container', yang_name="fabric-isl", rest_name="isl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric isl status ', u'alt-name': u'isl', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    self.__fabric_dport = YANGDynClass(base=fabric_dport.fabric_dport, is_container='container', yang_name="fabric-dport", rest_name="dport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric D-port status ', u'hidden': u'debug', u'callpoint': u'fabric_dport_callpoint', u'cli-incomplete-no': None, u'alt-name': u'dport'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    self.__fabric_trunk = YANGDynClass(base=fabric_trunk.fabric_trunk, is_container='container', yang_name="fabric-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric trunk status ', u'alt-name': u'trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    self.__neighbor_discovery = YANGDynClass(base=neighbor_discovery.neighbor_discovery, is_container='container', yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor discovery at this port', u'callpoint': u'interface_tengigabite'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'fabric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'fabric']

  def _get_fabric_isl(self):
    """
    Getter method for fabric_isl, mapped from YANG variable /interface/tengigabitethernet/fabric/fabric_isl (container)

    YANG Description: Configure the Fabric Protocol ISL parameters
    """
    return self.__fabric_isl
      
  def _set_fabric_isl(self, v, load=False):
    """
    Setter method for fabric_isl, mapped from YANG variable /interface/tengigabitethernet/fabric/fabric_isl (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_isl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_isl() directly.

    YANG Description: Configure the Fabric Protocol ISL parameters
    """
    try:
      t = YANGDynClass(v,base=fabric_isl.fabric_isl, is_container='container', yang_name="fabric-isl", rest_name="isl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric isl status ', u'alt-name': u'isl', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_isl must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fabric_isl.fabric_isl, is_container='container', yang_name="fabric-isl", rest_name="isl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric isl status ', u'alt-name': u'isl', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)""",
        })

    self.__fabric_isl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_isl(self):
    self.__fabric_isl = YANGDynClass(base=fabric_isl.fabric_isl, is_container='container', yang_name="fabric-isl", rest_name="isl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric isl status ', u'alt-name': u'isl', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)


  def _get_fabric_trunk(self):
    """
    Getter method for fabric_trunk, mapped from YANG variable /interface/tengigabitethernet/fabric/fabric_trunk (container)

    YANG Description: Configure the Fabric Protocol Trunk parameters
    """
    return self.__fabric_trunk
      
  def _set_fabric_trunk(self, v, load=False):
    """
    Setter method for fabric_trunk, mapped from YANG variable /interface/tengigabitethernet/fabric/fabric_trunk (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_trunk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_trunk() directly.

    YANG Description: Configure the Fabric Protocol Trunk parameters
    """
    try:
      t = YANGDynClass(v,base=fabric_trunk.fabric_trunk, is_container='container', yang_name="fabric-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric trunk status ', u'alt-name': u'trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_trunk must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fabric_trunk.fabric_trunk, is_container='container', yang_name="fabric-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric trunk status ', u'alt-name': u'trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)""",
        })

    self.__fabric_trunk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_trunk(self):
    self.__fabric_trunk = YANGDynClass(base=fabric_trunk.fabric_trunk, is_container='container', yang_name="fabric-trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric trunk status ', u'alt-name': u'trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)


  def _get_neighbor_discovery(self):
    """
    Getter method for neighbor_discovery, mapped from YANG variable /interface/tengigabitethernet/fabric/neighbor_discovery (container)

    YANG Description: Neighbor discovery at this port
    """
    return self.__neighbor_discovery
      
  def _set_neighbor_discovery(self, v, load=False):
    """
    Setter method for neighbor_discovery, mapped from YANG variable /interface/tengigabitethernet/fabric/neighbor_discovery (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_discovery is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_discovery() directly.

    YANG Description: Neighbor discovery at this port
    """
    try:
      t = YANGDynClass(v,base=neighbor_discovery.neighbor_discovery, is_container='container', yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor discovery at this port', u'callpoint': u'interface_tengigabite'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_discovery must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbor_discovery.neighbor_discovery, is_container='container', yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor discovery at this port', u'callpoint': u'interface_tengigabite'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)""",
        })

    self.__neighbor_discovery = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_discovery(self):
    self.__neighbor_discovery = YANGDynClass(base=neighbor_discovery.neighbor_discovery, is_container='container', yang_name="neighbor-discovery", rest_name="neighbor-discovery", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Neighbor discovery at this port', u'callpoint': u'interface_tengigabite'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)


  def _get_fabric_dport(self):
    """
    Getter method for fabric_dport, mapped from YANG variable /interface/tengigabitethernet/fabric/fabric_dport (container)

    YANG Description: Configure the Fabric D-port parameters
    """
    return self.__fabric_dport
      
  def _set_fabric_dport(self, v, load=False):
    """
    Setter method for fabric_dport, mapped from YANG variable /interface/tengigabitethernet/fabric/fabric_dport (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_dport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_dport() directly.

    YANG Description: Configure the Fabric D-port parameters
    """
    try:
      t = YANGDynClass(v,base=fabric_dport.fabric_dport, is_container='container', yang_name="fabric-dport", rest_name="dport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric D-port status ', u'hidden': u'debug', u'callpoint': u'fabric_dport_callpoint', u'cli-incomplete-no': None, u'alt-name': u'dport'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_dport must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fabric_dport.fabric_dport, is_container='container', yang_name="fabric-dport", rest_name="dport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric D-port status ', u'hidden': u'debug', u'callpoint': u'fabric_dport_callpoint', u'cli-incomplete-no': None, u'alt-name': u'dport'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)""",
        })

    self.__fabric_dport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_dport(self):
    self.__fabric_dport = YANGDynClass(base=fabric_dport.fabric_dport, is_container='container', yang_name="fabric-dport", rest_name="dport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fabric D-port status ', u'hidden': u'debug', u'callpoint': u'fabric_dport_callpoint', u'cli-incomplete-no': None, u'alt-name': u'dport'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='container', is_config=True)

  fabric_isl = __builtin__.property(_get_fabric_isl, _set_fabric_isl)
  fabric_trunk = __builtin__.property(_get_fabric_trunk, _set_fabric_trunk)
  neighbor_discovery = __builtin__.property(_get_neighbor_discovery, _set_neighbor_discovery)
  fabric_dport = __builtin__.property(_get_fabric_dport, _set_fabric_dport)


  _pyangbind_elements = {'fabric_isl': fabric_isl, 'fabric_trunk': fabric_trunk, 'neighbor_discovery': neighbor_discovery, 'fabric_dport': fabric_dport, }


