
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_mpls_session_brief
import show_mpls_session_detail
import show_mpls_session_extensive
class mpls_rsvp_session_extensive(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-rsvp-session-extensive/output/mpls-rsvp-session-extensive. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_mpls_session_brief','__show_mpls_session_detail','__show_mpls_session_extensive',)

  _yang_name = 'mpls-rsvp-session-extensive'
  _rest_name = 'mpls-rsvp-session-extensive'

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
    self.__show_mpls_session_brief = YANGDynClass(base=show_mpls_session_brief.show_mpls_session_brief, is_container='container', yang_name="show-mpls-session-brief", rest_name="show-mpls-session-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_session_extensive = YANGDynClass(base=show_mpls_session_extensive.show_mpls_session_extensive, is_container='container', yang_name="show-mpls-session-extensive", rest_name="show-mpls-session-extensive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_session_detail = YANGDynClass(base=show_mpls_session_detail.show_mpls_session_detail, is_container='container', yang_name="show-mpls-session-detail", rest_name="show-mpls-session-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-rsvp-session-extensive', u'output', u'mpls-rsvp-session-extensive']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-rsvp-session-extensive', u'output', u'mpls-rsvp-session-extensive']

  def _get_show_mpls_session_brief(self):
    """
    Getter method for show_mpls_session_brief, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_session_extensive/output/mpls_rsvp_session_extensive/show_mpls_session_brief (container)
    """
    return self.__show_mpls_session_brief
      
  def _set_show_mpls_session_brief(self, v, load=False):
    """
    Setter method for show_mpls_session_brief, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_session_extensive/output/mpls_rsvp_session_extensive/show_mpls_session_brief (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_session_brief is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_session_brief() directly.
    """
    try:
      t = YANGDynClass(v,base=show_mpls_session_brief.show_mpls_session_brief, is_container='container', yang_name="show-mpls-session-brief", rest_name="show-mpls-session-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_session_brief must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_session_brief.show_mpls_session_brief, is_container='container', yang_name="show-mpls-session-brief", rest_name="show-mpls-session-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_session_brief = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_session_brief(self):
    self.__show_mpls_session_brief = YANGDynClass(base=show_mpls_session_brief.show_mpls_session_brief, is_container='container', yang_name="show-mpls-session-brief", rest_name="show-mpls-session-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_session_detail(self):
    """
    Getter method for show_mpls_session_detail, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_session_extensive/output/mpls_rsvp_session_extensive/show_mpls_session_detail (container)
    """
    return self.__show_mpls_session_detail
      
  def _set_show_mpls_session_detail(self, v, load=False):
    """
    Setter method for show_mpls_session_detail, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_session_extensive/output/mpls_rsvp_session_extensive/show_mpls_session_detail (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_session_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_session_detail() directly.
    """
    try:
      t = YANGDynClass(v,base=show_mpls_session_detail.show_mpls_session_detail, is_container='container', yang_name="show-mpls-session-detail", rest_name="show-mpls-session-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_session_detail must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_session_detail.show_mpls_session_detail, is_container='container', yang_name="show-mpls-session-detail", rest_name="show-mpls-session-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_session_detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_session_detail(self):
    self.__show_mpls_session_detail = YANGDynClass(base=show_mpls_session_detail.show_mpls_session_detail, is_container='container', yang_name="show-mpls-session-detail", rest_name="show-mpls-session-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_session_extensive(self):
    """
    Getter method for show_mpls_session_extensive, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_session_extensive/output/mpls_rsvp_session_extensive/show_mpls_session_extensive (container)
    """
    return self.__show_mpls_session_extensive
      
  def _set_show_mpls_session_extensive(self, v, load=False):
    """
    Setter method for show_mpls_session_extensive, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_session_extensive/output/mpls_rsvp_session_extensive/show_mpls_session_extensive (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_session_extensive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_session_extensive() directly.
    """
    try:
      t = YANGDynClass(v,base=show_mpls_session_extensive.show_mpls_session_extensive, is_container='container', yang_name="show-mpls-session-extensive", rest_name="show-mpls-session-extensive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_session_extensive must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_session_extensive.show_mpls_session_extensive, is_container='container', yang_name="show-mpls-session-extensive", rest_name="show-mpls-session-extensive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_session_extensive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_session_extensive(self):
    self.__show_mpls_session_extensive = YANGDynClass(base=show_mpls_session_extensive.show_mpls_session_extensive, is_container='container', yang_name="show-mpls-session-extensive", rest_name="show-mpls-session-extensive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  show_mpls_session_brief = __builtin__.property(_get_show_mpls_session_brief, _set_show_mpls_session_brief)
  show_mpls_session_detail = __builtin__.property(_get_show_mpls_session_detail, _set_show_mpls_session_detail)
  show_mpls_session_extensive = __builtin__.property(_get_show_mpls_session_extensive, _set_show_mpls_session_extensive)


  _pyangbind_elements = {'show_mpls_session_brief': show_mpls_session_brief, 'show_mpls_session_detail': show_mpls_session_detail, 'show_mpls_session_extensive': show_mpls_session_extensive, }


