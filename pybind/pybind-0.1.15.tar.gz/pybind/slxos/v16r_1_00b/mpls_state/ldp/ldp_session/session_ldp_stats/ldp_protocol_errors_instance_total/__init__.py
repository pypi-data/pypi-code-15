
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import protocol_errors
class ldp_protocol_errors_instance_total(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/ldp-session/session-ldp-stats/ldp-protocol-errors-instance-total. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__protocol_errors',)

  _yang_name = 'ldp-protocol-errors-instance-total'
  _rest_name = 'ldp-protocol-errors-instance-total'

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
    self.__protocol_errors = YANGDynClass(base=YANGListType("error_type",protocol_errors.protocol_errors, yang_name="protocol-errors", rest_name="protocol-errors", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='error-type', extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}), is_container='list', yang_name="protocol-errors", rest_name="protocol-errors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

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
      return [u'mpls-state', u'ldp', u'ldp-session', u'session-ldp-stats', u'ldp-protocol-errors-instance-total']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'ldp-session', u'session-ldp-stats', u'ldp-protocol-errors-instance-total']

  def _get_protocol_errors(self):
    """
    Getter method for protocol_errors, mapped from YANG variable /mpls_state/ldp/ldp_session/session_ldp_stats/ldp_protocol_errors_instance_total/protocol_errors (list)

    YANG Description: protocol errors
    """
    return self.__protocol_errors
      
  def _set_protocol_errors(self, v, load=False):
    """
    Setter method for protocol_errors, mapped from YANG variable /mpls_state/ldp/ldp_session/session_ldp_stats/ldp_protocol_errors_instance_total/protocol_errors (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_errors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_errors() directly.

    YANG Description: protocol errors
    """
    try:
      t = YANGDynClass(v,base=YANGListType("error_type",protocol_errors.protocol_errors, yang_name="protocol-errors", rest_name="protocol-errors", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='error-type', extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}), is_container='list', yang_name="protocol-errors", rest_name="protocol-errors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_errors must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("error_type",protocol_errors.protocol_errors, yang_name="protocol-errors", rest_name="protocol-errors", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='error-type', extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}), is_container='list', yang_name="protocol-errors", rest_name="protocol-errors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)""",
        })

    self.__protocol_errors = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_errors(self):
    self.__protocol_errors = YANGDynClass(base=YANGListType("error_type",protocol_errors.protocol_errors, yang_name="protocol-errors", rest_name="protocol-errors", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='error-type', extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}), is_container='list', yang_name="protocol-errors", rest_name="protocol-errors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mpls-protocol-errors', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='list', is_config=False)

  protocol_errors = __builtin__.property(_get_protocol_errors)


  _pyangbind_elements = {'protocol_errors': protocol_errors, }


