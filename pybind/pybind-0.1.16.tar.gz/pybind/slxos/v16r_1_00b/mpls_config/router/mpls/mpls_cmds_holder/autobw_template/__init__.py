
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class autobw_template(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/autobw-template. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__autobw_template_name','__adjustment_interval','__adjustment_threshold','__min_bandwidth','__max_bandwidth','__overflow_limit','__mode','__sample_recording','__underflow_limit',)

  _yang_name = 'autobw-template'
  _rest_name = 'autobw-template'

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
    self.__adjustment_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="adjustment-threshold", rest_name="adjustment-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment threshold', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__overflow_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="overflow-limit", rest_name="overflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Overflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__max_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2147483647), is_leaf=True, yang_name="max-bandwidth", rest_name="max-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Maximum bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__adjustment_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'300..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="adjustment-interval", rest_name="adjustment-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor-and-signal': {'value': 0}, u'monitor-only': {'value': 1}},), default=unicode("monitor-and-signal"), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Mode of autobandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='autobw-mode', is_config=True)
    self.__sample_recording = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="sample-recording", rest_name="sample-recording", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set sample recording for this lsp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)
    self.__underflow_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="underflow-limit", rest_name="underflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Underflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__autobw_template_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="autobw-template-name", rest_name="autobw-template-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__min_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="min-bandwidth", rest_name="min-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Minimum Bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'autobw-template']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'autobw-template']

  def _get_autobw_template_name(self):
    """
    Getter method for autobw_template_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/autobw_template_name (string)
    """
    return self.__autobw_template_name
      
  def _set_autobw_template_name(self, v, load=False):
    """
    Setter method for autobw_template_name, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/autobw_template_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autobw_template_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autobw_template_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="autobw-template-name", rest_name="autobw-template-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autobw_template_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="autobw-template-name", rest_name="autobw-template-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__autobw_template_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autobw_template_name(self):
    self.__autobw_template_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..64']}), is_leaf=True, yang_name="autobw-template-name", rest_name="autobw-template-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ASCII string;;Name (up to 64 characters)'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_adjustment_interval(self):
    """
    Getter method for adjustment_interval, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_interval (uint32)
    """
    return self.__adjustment_interval
      
  def _set_adjustment_interval(self, v, load=False):
    """
    Setter method for adjustment_interval, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjustment_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjustment_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'300..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="adjustment-interval", rest_name="adjustment-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjustment_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'300..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="adjustment-interval", rest_name="adjustment-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__adjustment_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjustment_interval(self):
    self.__adjustment_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'300..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(86400), is_leaf=True, yang_name="adjustment-interval", rest_name="adjustment-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment interval', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_adjustment_threshold(self):
    """
    Getter method for adjustment_threshold, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_threshold (uint32)
    """
    return self.__adjustment_threshold
      
  def _set_adjustment_threshold(self, v, load=False):
    """
    Setter method for adjustment_threshold, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/adjustment_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjustment_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjustment_threshold() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="adjustment-threshold", rest_name="adjustment-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment threshold', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjustment_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="adjustment-threshold", rest_name="adjustment-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment threshold', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__adjustment_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjustment_threshold(self):
    self.__adjustment_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..100']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="adjustment-threshold", rest_name="adjustment-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Adjustment threshold', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_min_bandwidth(self):
    """
    Getter method for min_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/min_bandwidth (uint32)
    """
    return self.__min_bandwidth
      
  def _set_min_bandwidth(self, v, load=False):
    """
    Setter method for min_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/min_bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_bandwidth() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="min-bandwidth", rest_name="min-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Minimum Bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="min-bandwidth", rest_name="min-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Minimum Bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__min_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_bandwidth(self):
    self.__min_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="min-bandwidth", rest_name="min-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Minimum Bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_max_bandwidth(self):
    """
    Getter method for max_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/max_bandwidth (uint32)
    """
    return self.__max_bandwidth
      
  def _set_max_bandwidth(self, v, load=False):
    """
    Setter method for max_bandwidth, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/max_bandwidth (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_bandwidth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_bandwidth() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2147483647), is_leaf=True, yang_name="max-bandwidth", rest_name="max-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Maximum bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_bandwidth must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2147483647), is_leaf=True, yang_name="max-bandwidth", rest_name="max-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Maximum bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__max_bandwidth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_bandwidth(self):
    self.__max_bandwidth = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..2147483647']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2147483647), is_leaf=True, yang_name="max-bandwidth", rest_name="max-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Maximum bandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_overflow_limit(self):
    """
    Getter method for overflow_limit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/overflow_limit (uint32)
    """
    return self.__overflow_limit
      
  def _set_overflow_limit(self, v, load=False):
    """
    Setter method for overflow_limit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/overflow_limit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overflow_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overflow_limit() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="overflow-limit", rest_name="overflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Overflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overflow_limit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="overflow-limit", rest_name="overflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Overflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__overflow_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overflow_limit(self):
    self.__overflow_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="overflow-limit", rest_name="overflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Overflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/mode (autobw-mode)
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/mode (autobw-mode)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor-and-signal': {'value': 0}, u'monitor-only': {'value': 1}},), default=unicode("monitor-and-signal"), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Mode of autobandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='autobw-mode', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with autobw-mode""",
          'defined-type': "brocade-mpls:autobw-mode",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor-and-signal': {'value': 0}, u'monitor-only': {'value': 1}},), default=unicode("monitor-and-signal"), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Mode of autobandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='autobw-mode', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'monitor-and-signal': {'value': 0}, u'monitor-only': {'value': 1}},), default=unicode("monitor-and-signal"), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Mode of autobandwidth', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='autobw-mode', is_config=True)


  def _get_sample_recording(self):
    """
    Getter method for sample_recording, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/sample_recording (enable-disable)
    """
    return self.__sample_recording
      
  def _set_sample_recording(self, v, load=False):
    """
    Setter method for sample_recording, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/sample_recording (enable-disable)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sample_recording is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sample_recording() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="sample-recording", rest_name="sample-recording", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set sample recording for this lsp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sample_recording must be of a type compatible with enable-disable""",
          'defined-type': "brocade-mpls:enable-disable",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="sample-recording", rest_name="sample-recording", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set sample recording for this lsp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)""",
        })

    self.__sample_recording = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sample_recording(self):
    self.__sample_recording = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'enable': {'value': 1}, u'disable': {'value': 0}},), is_leaf=True, yang_name="sample-recording", rest_name="sample-recording", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set sample recording for this lsp', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='enable-disable', is_config=True)


  def _get_underflow_limit(self):
    """
    Getter method for underflow_limit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/underflow_limit (uint32)
    """
    return self.__underflow_limit
      
  def _set_underflow_limit(self, v, load=False):
    """
    Setter method for underflow_limit, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/autobw_template/underflow_limit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_underflow_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_underflow_limit() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="underflow-limit", rest_name="underflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Underflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """underflow_limit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="underflow-limit", rest_name="underflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Underflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__underflow_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_underflow_limit(self):
    self.__underflow_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="underflow-limit", rest_name="underflow-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Underflow limit', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  autobw_template_name = __builtin__.property(_get_autobw_template_name, _set_autobw_template_name)
  adjustment_interval = __builtin__.property(_get_adjustment_interval, _set_adjustment_interval)
  adjustment_threshold = __builtin__.property(_get_adjustment_threshold, _set_adjustment_threshold)
  min_bandwidth = __builtin__.property(_get_min_bandwidth, _set_min_bandwidth)
  max_bandwidth = __builtin__.property(_get_max_bandwidth, _set_max_bandwidth)
  overflow_limit = __builtin__.property(_get_overflow_limit, _set_overflow_limit)
  mode = __builtin__.property(_get_mode, _set_mode)
  sample_recording = __builtin__.property(_get_sample_recording, _set_sample_recording)
  underflow_limit = __builtin__.property(_get_underflow_limit, _set_underflow_limit)


  _pyangbind_elements = {'autobw_template_name': autobw_template_name, 'adjustment_interval': adjustment_interval, 'adjustment_threshold': adjustment_threshold, 'min_bandwidth': min_bandwidth, 'max_bandwidth': max_bandwidth, 'overflow_limit': overflow_limit, 'mode': mode, 'sample_recording': sample_recording, 'underflow_limit': underflow_limit, }


