
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import virtual
import virtual_fabric
class vcs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vcs - based on the path /vcs. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__virtual','__virtual_fabric',)

  _yang_name = 'vcs'
  _rest_name = 'vcs'

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
    self.__virtual_fabric = YANGDynClass(base=virtual_fabric.virtual_fabric, is_container='container', yang_name="virtual-fabric", rest_name="virtual-fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vcs Virtual Fabric configuration', u'display-when': u'((/vcsmode/vcs-mode = "true") and (/vcsmode/vcs-cluster-mode = "true"))', u'cli-incomplete-no': None, u'callpoint': u'vcs-virtual-fabric-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)
    self.__virtual = YANGDynClass(base=virtual.virtual, is_container='container', yang_name="virtual", rest_name="virtual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Cluster Switching Configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)

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
      return [u'vcs']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vcs']

  def _get_virtual(self):
    """
    Getter method for virtual, mapped from YANG variable /vcs/virtual (container)
    """
    return self.__virtual
      
  def _set_virtual(self, v, load=False):
    """
    Setter method for virtual, mapped from YANG variable /vcs/virtual (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual() directly.
    """
    try:
      t = YANGDynClass(v,base=virtual.virtual, is_container='container', yang_name="virtual", rest_name="virtual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Cluster Switching Configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=virtual.virtual, is_container='container', yang_name="virtual", rest_name="virtual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Cluster Switching Configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)""",
        })

    self.__virtual = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual(self):
    self.__virtual = YANGDynClass(base=virtual.virtual, is_container='container', yang_name="virtual", rest_name="virtual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Virtual Cluster Switching Configuration', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)


  def _get_virtual_fabric(self):
    """
    Getter method for virtual_fabric, mapped from YANG variable /vcs/virtual_fabric (container)

    YANG Description: Vcs Virtual Fabric configuration
    """
    return self.__virtual_fabric
      
  def _set_virtual_fabric(self, v, load=False):
    """
    Setter method for virtual_fabric, mapped from YANG variable /vcs/virtual_fabric (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_fabric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_fabric() directly.

    YANG Description: Vcs Virtual Fabric configuration
    """
    try:
      t = YANGDynClass(v,base=virtual_fabric.virtual_fabric, is_container='container', yang_name="virtual-fabric", rest_name="virtual-fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vcs Virtual Fabric configuration', u'display-when': u'((/vcsmode/vcs-mode = "true") and (/vcsmode/vcs-cluster-mode = "true"))', u'cli-incomplete-no': None, u'callpoint': u'vcs-virtual-fabric-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_fabric must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=virtual_fabric.virtual_fabric, is_container='container', yang_name="virtual-fabric", rest_name="virtual-fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vcs Virtual Fabric configuration', u'display-when': u'((/vcsmode/vcs-mode = "true") and (/vcsmode/vcs-cluster-mode = "true"))', u'cli-incomplete-no': None, u'callpoint': u'vcs-virtual-fabric-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)""",
        })

    self.__virtual_fabric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_fabric(self):
    self.__virtual_fabric = YANGDynClass(base=virtual_fabric.virtual_fabric, is_container='container', yang_name="virtual-fabric", rest_name="virtual-fabric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vcs Virtual Fabric configuration', u'display-when': u'((/vcsmode/vcs-mode = "true") and (/vcsmode/vcs-cluster-mode = "true"))', u'cli-incomplete-no': None, u'callpoint': u'vcs-virtual-fabric-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='container', is_config=True)

  virtual = __builtin__.property(_get_virtual, _set_virtual)
  virtual_fabric = __builtin__.property(_get_virtual_fabric, _set_virtual_fabric)


  _pyangbind_elements = {'virtual': virtual, 'virtual_fabric': virtual_fabric, }


