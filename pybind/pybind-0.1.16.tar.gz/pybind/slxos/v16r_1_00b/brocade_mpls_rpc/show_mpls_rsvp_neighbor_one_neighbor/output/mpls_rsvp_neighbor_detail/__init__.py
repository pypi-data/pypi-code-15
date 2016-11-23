
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_mpls_neighbor_brief
import show_mpls_neighbor_detail
class mpls_rsvp_neighbor_detail(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-rsvp-neighbor-one-neighbor/output/mpls-rsvp-neighbor-detail. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_mpls_neighbor_brief','__show_mpls_neighbor_detail',)

  _yang_name = 'mpls-rsvp-neighbor-detail'
  _rest_name = 'mpls-rsvp-neighbor-detail'

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
    self.__show_mpls_neighbor_brief = YANGDynClass(base=show_mpls_neighbor_brief.show_mpls_neighbor_brief, is_container='container', yang_name="show-mpls-neighbor-brief", rest_name="show-mpls-neighbor-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_neighbor_detail = YANGDynClass(base=show_mpls_neighbor_detail.show_mpls_neighbor_detail, is_container='container', yang_name="show-mpls-neighbor-detail", rest_name="show-mpls-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-rsvp-neighbor-one-neighbor', u'output', u'mpls-rsvp-neighbor-detail']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-rsvp-neighbor-one-neighbor', u'output', u'mpls-rsvp-neighbor-detail']

  def _get_show_mpls_neighbor_brief(self):
    """
    Getter method for show_mpls_neighbor_brief, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_brief (container)
    """
    return self.__show_mpls_neighbor_brief
      
  def _set_show_mpls_neighbor_brief(self, v, load=False):
    """
    Setter method for show_mpls_neighbor_brief, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_brief (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_neighbor_brief is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_neighbor_brief() directly.
    """
    try:
      t = YANGDynClass(v,base=show_mpls_neighbor_brief.show_mpls_neighbor_brief, is_container='container', yang_name="show-mpls-neighbor-brief", rest_name="show-mpls-neighbor-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_neighbor_brief must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_neighbor_brief.show_mpls_neighbor_brief, is_container='container', yang_name="show-mpls-neighbor-brief", rest_name="show-mpls-neighbor-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_neighbor_brief = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_neighbor_brief(self):
    self.__show_mpls_neighbor_brief = YANGDynClass(base=show_mpls_neighbor_brief.show_mpls_neighbor_brief, is_container='container', yang_name="show-mpls-neighbor-brief", rest_name="show-mpls-neighbor-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_neighbor_detail(self):
    """
    Getter method for show_mpls_neighbor_detail, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail (container)
    """
    return self.__show_mpls_neighbor_detail
      
  def _set_show_mpls_neighbor_detail(self, v, load=False):
    """
    Setter method for show_mpls_neighbor_detail, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp_neighbor_one_neighbor/output/mpls_rsvp_neighbor_detail/show_mpls_neighbor_detail (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_neighbor_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_neighbor_detail() directly.
    """
    try:
      t = YANGDynClass(v,base=show_mpls_neighbor_detail.show_mpls_neighbor_detail, is_container='container', yang_name="show-mpls-neighbor-detail", rest_name="show-mpls-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_neighbor_detail must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_neighbor_detail.show_mpls_neighbor_detail, is_container='container', yang_name="show-mpls-neighbor-detail", rest_name="show-mpls-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_neighbor_detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_neighbor_detail(self):
    self.__show_mpls_neighbor_detail = YANGDynClass(base=show_mpls_neighbor_detail.show_mpls_neighbor_detail, is_container='container', yang_name="show-mpls-neighbor-detail", rest_name="show-mpls-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  show_mpls_neighbor_brief = __builtin__.property(_get_show_mpls_neighbor_brief, _set_show_mpls_neighbor_brief)
  show_mpls_neighbor_detail = __builtin__.property(_get_show_mpls_neighbor_detail, _set_show_mpls_neighbor_detail)


  _pyangbind_elements = {'show_mpls_neighbor_brief': show_mpls_neighbor_brief, 'show_mpls_neighbor_detail': show_mpls_neighbor_detail, }


