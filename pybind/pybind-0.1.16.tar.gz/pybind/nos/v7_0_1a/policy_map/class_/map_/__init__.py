
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class map_(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-policer - based on the path /policy-map/class/map. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cos_mutation','__cos_traffic_class','__dscp_cos','__dscp_traffic_class','__dscp_mutation','__sflow',)

  _yang_name = 'map'
  _rest_name = 'map'

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
    self.__cos_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-CoS mutation map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    self.__sflow = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow", rest_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure sflow profile map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    self.__dscp_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Dscp mutation map  \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    self.__dscp_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Traffic class map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    self.__cos_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-Traffic Class map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    self.__dscp_cos = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-CoS map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)

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
      return [u'policy-map', u'class', u'map']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'policy-map', u'class', u'map']

  def _get_cos_mutation(self):
    """
    Getter method for cos_mutation, mapped from YANG variable /policy_map/class/map/cos_mutation (map-name-type)

    YANG Description: This specifies the mapping between CoS 
to Cos.
    """
    return self.__cos_mutation
      
  def _set_cos_mutation(self, v, load=False):
    """
    Setter method for cos_mutation, mapped from YANG variable /policy_map/class/map/cos_mutation (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos_mutation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos_mutation() directly.

    YANG Description: This specifies the mapping between CoS 
to Cos.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-CoS mutation map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos_mutation must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-CoS mutation map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__cos_mutation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos_mutation(self):
    self.__cos_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-mutation", rest_name="cos-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-CoS mutation map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_cos_traffic_class(self):
    """
    Getter method for cos_traffic_class, mapped from YANG variable /policy_map/class/map/cos_traffic_class (map-name-type)

    YANG Description: This specifies the mapping between CoS 
to Traffic class.
    """
    return self.__cos_traffic_class
      
  def _set_cos_traffic_class(self, v, load=False):
    """
    Setter method for cos_traffic_class, mapped from YANG variable /policy_map/class/map/cos_traffic_class (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos_traffic_class() directly.

    YANG Description: This specifies the mapping between CoS 
to Traffic class.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-Traffic Class map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos_traffic_class must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-Traffic Class map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__cos_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos_traffic_class(self):
    self.__cos_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="cos-traffic-class", rest_name="cos-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure CoS-to-Traffic Class map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_dscp_cos(self):
    """
    Getter method for dscp_cos, mapped from YANG variable /policy_map/class/map/dscp_cos (map-name-type)

    YANG Description: This specifies the mapping between Dscp
to Cos.
    """
    return self.__dscp_cos
      
  def _set_dscp_cos(self, v, load=False):
    """
    Setter method for dscp_cos, mapped from YANG variable /policy_map/class/map/dscp_cos (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_cos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_cos() directly.

    YANG Description: This specifies the mapping between Dscp
to Cos.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-CoS map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_cos must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-CoS map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__dscp_cos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_cos(self):
    self.__dscp_cos = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-cos", rest_name="dscp-cos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-CoS map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_dscp_traffic_class(self):
    """
    Getter method for dscp_traffic_class, mapped from YANG variable /policy_map/class/map/dscp_traffic_class (map-name-type)

    YANG Description: This specifies the mapping between Dscp
to Traffic class.
    """
    return self.__dscp_traffic_class
      
  def _set_dscp_traffic_class(self, v, load=False):
    """
    Setter method for dscp_traffic_class, mapped from YANG variable /policy_map/class/map/dscp_traffic_class (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_traffic_class is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_traffic_class() directly.

    YANG Description: This specifies the mapping between Dscp
to Traffic class.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Traffic class map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_traffic_class must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Traffic class map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__dscp_traffic_class = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_traffic_class(self):
    self.__dscp_traffic_class = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-traffic-class", rest_name="dscp-traffic-class", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Traffic class map\n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_dscp_mutation(self):
    """
    Getter method for dscp_mutation, mapped from YANG variable /policy_map/class/map/dscp_mutation (map-name-type)

    YANG Description: This specifies the mapping between Dscp
to Dscp.
    """
    return self.__dscp_mutation
      
  def _set_dscp_mutation(self, v, load=False):
    """
    Setter method for dscp_mutation, mapped from YANG variable /policy_map/class/map/dscp_mutation (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dscp_mutation is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dscp_mutation() directly.

    YANG Description: This specifies the mapping between Dscp
to Dscp.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Dscp mutation map  \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dscp_mutation must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Dscp mutation map  \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__dscp_mutation = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dscp_mutation(self):
    self.__dscp_mutation = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="dscp-mutation", rest_name="dscp-mutation", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Dscp-to-Dscp mutation map  \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)


  def _get_sflow(self):
    """
    Getter method for sflow, mapped from YANG variable /policy_map/class/map/sflow (map-name-type)

    YANG Description: This specifies the sflow action.
    """
    return self.__sflow
      
  def _set_sflow(self, v, load=False):
    """
    Setter method for sflow, mapped from YANG variable /policy_map/class/map/sflow (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sflow is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sflow() directly.

    YANG Description: This specifies the sflow action.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow", rest_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure sflow profile map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sflow must be of a type compatible with map-name-type""",
          'defined-type': "brocade-policer:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow", rest_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure sflow profile map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)""",
        })

    self.__sflow = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sflow(self):
    self.__sflow = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="sflow", rest_name="sflow", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure sflow profile map \n(Max Size - 64)'}}, namespace='urn:brocade.com:mgmt:brocade-policer', defining_module='brocade-policer', yang_type='map-name-type', is_config=True)

  cos_mutation = __builtin__.property(_get_cos_mutation, _set_cos_mutation)
  cos_traffic_class = __builtin__.property(_get_cos_traffic_class, _set_cos_traffic_class)
  dscp_cos = __builtin__.property(_get_dscp_cos, _set_dscp_cos)
  dscp_traffic_class = __builtin__.property(_get_dscp_traffic_class, _set_dscp_traffic_class)
  dscp_mutation = __builtin__.property(_get_dscp_mutation, _set_dscp_mutation)
  sflow = __builtin__.property(_get_sflow, _set_sflow)


  _pyangbind_elements = {'cos_mutation': cos_mutation, 'cos_traffic_class': cos_traffic_class, 'dscp_cos': dscp_cos, 'dscp_traffic_class': dscp_traffic_class, 'dscp_mutation': dscp_mutation, 'sflow': sflow, }


