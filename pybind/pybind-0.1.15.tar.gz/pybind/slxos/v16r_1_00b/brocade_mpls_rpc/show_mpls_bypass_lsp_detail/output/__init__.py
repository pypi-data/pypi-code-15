
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bypass_lsp
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-bypass-lsp-detail/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bypass_lsp',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__bypass_lsp = YANGDynClass(base=bypass_lsp.bypass_lsp, is_container='container', yang_name="bypass-lsp", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-bypass-lsp-detail', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-bypass-lsp-detail', u'output']

  def _get_bypass_lsp(self):
    """
    Getter method for bypass_lsp, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp (container)
    """
    return self.__bypass_lsp
      
  def _set_bypass_lsp(self, v, load=False):
    """
    Setter method for bypass_lsp, mapped from YANG variable /brocade_mpls_rpc/show_mpls_bypass_lsp_detail/output/bypass_lsp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bypass_lsp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bypass_lsp() directly.
    """
    try:
      t = YANGDynClass(v,base=bypass_lsp.bypass_lsp, is_container='container', yang_name="bypass-lsp", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bypass_lsp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bypass_lsp.bypass_lsp, is_container='container', yang_name="bypass-lsp", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__bypass_lsp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bypass_lsp(self):
    self.__bypass_lsp = YANGDynClass(base=bypass_lsp.bypass_lsp, is_container='container', yang_name="bypass-lsp", rest_name="bypass-lsp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  bypass_lsp = __builtin__.property(_get_bypass_lsp, _set_bypass_lsp)


  _pyangbind_elements = {'bypass_lsp': bypass_lsp, }


