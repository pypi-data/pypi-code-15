
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_last_config_update_time
import show_vcs
import get_vcs_details
import vcs_rbridge_config
import vcs_rbridge_context
import no_vcs_rbridge_context
import get_last_config_update_time_for_xpaths
class brocade_vcs(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vcs - based on the path /brocade_vcs_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an instrumentation to manage  
Virtual Cluster Switching (VCS).
        
Glossary of the terms used:
--------------------------- 
VAL  - Virtual Access Layer, provided by VCS.
VCS  - Virtual Cluster Switching.
TRILL - Transparent Interconnection of Lot of Links.
TLS - Transparent LAN Services.
        
        
VCS refers to the ability of a group of physical Ethernet 
switches, inter-connected in arbitrary fashion via the regular 
front-end data ports, to present themselves as one unified and
transparent Ethernet switching service to the external network. 
The inter-connecting network that glues all these individual 
switches is refered as 'fabric', and the group of physical 
Ethernet switches in the fabric is refered to as 'cluster'. 
        
+--------+                                   +--------+
|External|                                   |External| 
|Non-VCS |                                   |Non-VCS |
|Switch  |                                   |Switch  |
+--------+                                   +--------+          
  |                                              |
  |                                              |
  |                                              |
+---+                                            |          
|   |                                            | 
|S1 |                                      ******************
+---+                                      * Logical Switch *  
  |<------ Fabric Port    \---->           *                *  
  |                       /---->           * (VCS Cluster)  *
+---+                                      ******************
|   |                                            |
|S2 |                                            |
+---+                                            |
  |<----- Edge Port                              |
  |                                              |
+-------+                                   +-------+
|Server |                                   |Server |
+-------+                                   +-------+

[Physical View]                            [Logical View]

As shown in the figure above, the fabric ports are transparent 
as far as the external devices connected to the VCS are 
concerned. In this sense the whole of the cluster behaves like 
a logical switch to the external network.         

  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__get_last_config_update_time','__show_vcs','__get_vcs_details','__vcs_rbridge_config','__vcs_rbridge_context','__no_vcs_rbridge_context','__get_last_config_update_time_for_xpaths',)

  _yang_name = 'brocade-vcs'
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
    self.__no_vcs_rbridge_context = YANGDynClass(base=no_vcs_rbridge_context.no_vcs_rbridge_context, is_leaf=True, yang_name="no-vcs-rbridge-context", rest_name="no-vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    self.__show_vcs = YANGDynClass(base=show_vcs.show_vcs, is_leaf=True, yang_name="show-vcs", rest_name="show-vcs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getclusterinfo-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    self.__get_vcs_details = YANGDynClass(base=get_vcs_details.get_vcs_details, is_leaf=True, yang_name="get-vcs-details", rest_name="get-vcs-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getvcsdetails-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    self.__get_last_config_update_time_for_xpaths = YANGDynClass(base=get_last_config_update_time_for_xpaths.get_last_config_update_time_for_xpaths, is_leaf=True, yang_name="get-last-config-update-time-for-xpaths", rest_name="get-last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    self.__vcs_rbridge_context = YANGDynClass(base=vcs_rbridge_context.vcs_rbridge_context, is_leaf=True, yang_name="vcs-rbridge-context", rest_name="vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    self.__get_last_config_update_time = YANGDynClass(base=get_last_config_update_time.get_last_config_update_time, is_leaf=True, yang_name="get-last-config-update-time", rest_name="get-last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    self.__vcs_rbridge_config = YANGDynClass(base=vcs_rbridge_config.vcs_rbridge_config, is_leaf=True, yang_name="vcs-rbridge-config", rest_name="vcs-rbridge-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcsenable-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)

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
      return [u'brocade_vcs_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_get_last_config_update_time(self):
    """
    Getter method for get_last_config_update_time, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time (rpc)

    YANG Description: This rpc function provides time-stamp of the last 
configutation change done on the managed device.
    """
    return self.__get_last_config_update_time
      
  def _set_get_last_config_update_time(self, v, load=False):
    """
    Setter method for get_last_config_update_time, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_last_config_update_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_last_config_update_time() directly.

    YANG Description: This rpc function provides time-stamp of the last 
configutation change done on the managed device.
    """
    try:
      t = YANGDynClass(v,base=get_last_config_update_time.get_last_config_update_time, is_leaf=True, yang_name="get-last-config-update-time", rest_name="get-last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_last_config_update_time must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_last_config_update_time.get_last_config_update_time, is_leaf=True, yang_name="get-last-config-update-time", rest_name="get-last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)""",
        })

    self.__get_last_config_update_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_last_config_update_time(self):
    self.__get_last_config_update_time = YANGDynClass(base=get_last_config_update_time.get_last_config_update_time, is_leaf=True, yang_name="get-last-config-update-time", rest_name="get-last-config-update-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)


  def _get_show_vcs(self):
    """
    Getter method for show_vcs, mapped from YANG variable /brocade_vcs_rpc/show_vcs (rpc)
    """
    return self.__show_vcs
      
  def _set_show_vcs(self, v, load=False):
    """
    Setter method for show_vcs, mapped from YANG variable /brocade_vcs_rpc/show_vcs (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_vcs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_vcs() directly.
    """
    try:
      t = YANGDynClass(v,base=show_vcs.show_vcs, is_leaf=True, yang_name="show-vcs", rest_name="show-vcs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getclusterinfo-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_vcs must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=show_vcs.show_vcs, is_leaf=True, yang_name="show-vcs", rest_name="show-vcs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getclusterinfo-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)""",
        })

    self.__show_vcs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_vcs(self):
    self.__show_vcs = YANGDynClass(base=show_vcs.show_vcs, is_leaf=True, yang_name="show-vcs", rest_name="show-vcs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getclusterinfo-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)


  def _get_get_vcs_details(self):
    """
    Getter method for get_vcs_details, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details (rpc)
    """
    return self.__get_vcs_details
      
  def _set_get_vcs_details(self, v, load=False):
    """
    Setter method for get_vcs_details, mapped from YANG variable /brocade_vcs_rpc/get_vcs_details (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_vcs_details is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_vcs_details() directly.
    """
    try:
      t = YANGDynClass(v,base=get_vcs_details.get_vcs_details, is_leaf=True, yang_name="get-vcs-details", rest_name="get-vcs-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getvcsdetails-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_vcs_details must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_vcs_details.get_vcs_details, is_leaf=True, yang_name="get-vcs-details", rest_name="get-vcs-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getvcsdetails-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)""",
        })

    self.__get_vcs_details = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_vcs_details(self):
    self.__get_vcs_details = YANGDynClass(base=get_vcs_details.get_vcs_details, is_leaf=True, yang_name="get-vcs-details", rest_name="get-vcs-details", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'getvcsdetails-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)


  def _get_vcs_rbridge_config(self):
    """
    Getter method for vcs_rbridge_config, mapped from YANG variable /brocade_vcs_rpc/vcs_rbridge_config (rpc)
    """
    return self.__vcs_rbridge_config
      
  def _set_vcs_rbridge_config(self, v, load=False):
    """
    Setter method for vcs_rbridge_config, mapped from YANG variable /brocade_vcs_rpc/vcs_rbridge_config (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vcs_rbridge_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vcs_rbridge_config() directly.
    """
    try:
      t = YANGDynClass(v,base=vcs_rbridge_config.vcs_rbridge_config, is_leaf=True, yang_name="vcs-rbridge-config", rest_name="vcs-rbridge-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcsenable-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vcs_rbridge_config must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vcs_rbridge_config.vcs_rbridge_config, is_leaf=True, yang_name="vcs-rbridge-config", rest_name="vcs-rbridge-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcsenable-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)""",
        })

    self.__vcs_rbridge_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vcs_rbridge_config(self):
    self.__vcs_rbridge_config = YANGDynClass(base=vcs_rbridge_config.vcs_rbridge_config, is_leaf=True, yang_name="vcs-rbridge-config", rest_name="vcs-rbridge-config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcsenable-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)


  def _get_vcs_rbridge_context(self):
    """
    Getter method for vcs_rbridge_context, mapped from YANG variable /brocade_vcs_rpc/vcs_rbridge_context (rpc)
    """
    return self.__vcs_rbridge_context
      
  def _set_vcs_rbridge_context(self, v, load=False):
    """
    Setter method for vcs_rbridge_context, mapped from YANG variable /brocade_vcs_rpc/vcs_rbridge_context (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vcs_rbridge_context is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vcs_rbridge_context() directly.
    """
    try:
      t = YANGDynClass(v,base=vcs_rbridge_context.vcs_rbridge_context, is_leaf=True, yang_name="vcs-rbridge-context", rest_name="vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vcs_rbridge_context must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=vcs_rbridge_context.vcs_rbridge_context, is_leaf=True, yang_name="vcs-rbridge-context", rest_name="vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)""",
        })

    self.__vcs_rbridge_context = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vcs_rbridge_context(self):
    self.__vcs_rbridge_context = YANGDynClass(base=vcs_rbridge_context.vcs_rbridge_context, is_leaf=True, yang_name="vcs-rbridge-context", rest_name="vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)


  def _get_no_vcs_rbridge_context(self):
    """
    Getter method for no_vcs_rbridge_context, mapped from YANG variable /brocade_vcs_rpc/no_vcs_rbridge_context (rpc)
    """
    return self.__no_vcs_rbridge_context
      
  def _set_no_vcs_rbridge_context(self, v, load=False):
    """
    Setter method for no_vcs_rbridge_context, mapped from YANG variable /brocade_vcs_rpc/no_vcs_rbridge_context (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_vcs_rbridge_context is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_vcs_rbridge_context() directly.
    """
    try:
      t = YANGDynClass(v,base=no_vcs_rbridge_context.no_vcs_rbridge_context, is_leaf=True, yang_name="no-vcs-rbridge-context", rest_name="no-vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_vcs_rbridge_context must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=no_vcs_rbridge_context.no_vcs_rbridge_context, is_leaf=True, yang_name="no-vcs-rbridge-context", rest_name="no-vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)""",
        })

    self.__no_vcs_rbridge_context = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_vcs_rbridge_context(self):
    self.__no_vcs_rbridge_context = YANGDynClass(base=no_vcs_rbridge_context.no_vcs_rbridge_context, is_leaf=True, yang_name="no-vcs-rbridge-context", rest_name="no-vcs-rbridge-context", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'vcscontextrbridgeid-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)


  def _get_get_last_config_update_time_for_xpaths(self):
    """
    Getter method for get_last_config_update_time_for_xpaths, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths (rpc)
    """
    return self.__get_last_config_update_time_for_xpaths
      
  def _set_get_last_config_update_time_for_xpaths(self, v, load=False):
    """
    Setter method for get_last_config_update_time_for_xpaths, mapped from YANG variable /brocade_vcs_rpc/get_last_config_update_time_for_xpaths (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_last_config_update_time_for_xpaths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_last_config_update_time_for_xpaths() directly.
    """
    try:
      t = YANGDynClass(v,base=get_last_config_update_time_for_xpaths.get_last_config_update_time_for_xpaths, is_leaf=True, yang_name="get-last-config-update-time-for-xpaths", rest_name="get-last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_last_config_update_time_for_xpaths must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_last_config_update_time_for_xpaths.get_last_config_update_time_for_xpaths, is_leaf=True, yang_name="get-last-config-update-time-for-xpaths", rest_name="get-last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)""",
        })

    self.__get_last_config_update_time_for_xpaths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_last_config_update_time_for_xpaths(self):
    self.__get_last_config_update_time_for_xpaths = YANGDynClass(base=get_last_config_update_time_for_xpaths.get_last_config_update_time_for_xpaths, is_leaf=True, yang_name="get-last-config-update-time-for-xpaths", rest_name="get-last-config-update-time-for-xpaths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'last-config-update-time-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-vcs', defining_module='brocade-vcs', yang_type='rpc', is_config=True)

  get_last_config_update_time = __builtin__.property(_get_get_last_config_update_time, _set_get_last_config_update_time)
  show_vcs = __builtin__.property(_get_show_vcs, _set_show_vcs)
  get_vcs_details = __builtin__.property(_get_get_vcs_details, _set_get_vcs_details)
  vcs_rbridge_config = __builtin__.property(_get_vcs_rbridge_config, _set_vcs_rbridge_config)
  vcs_rbridge_context = __builtin__.property(_get_vcs_rbridge_context, _set_vcs_rbridge_context)
  no_vcs_rbridge_context = __builtin__.property(_get_no_vcs_rbridge_context, _set_no_vcs_rbridge_context)
  get_last_config_update_time_for_xpaths = __builtin__.property(_get_get_last_config_update_time_for_xpaths, _set_get_last_config_update_time_for_xpaths)


  _pyangbind_elements = {'get_last_config_update_time': get_last_config_update_time, 'show_vcs': show_vcs, 'get_vcs_details': get_vcs_details, 'vcs_rbridge_config': vcs_rbridge_config, 'vcs_rbridge_context': vcs_rbridge_context, 'no_vcs_rbridge_context': no_vcs_rbridge_context, 'get_last_config_update_time_for_xpaths': get_last_config_update_time_for_xpaths, }


