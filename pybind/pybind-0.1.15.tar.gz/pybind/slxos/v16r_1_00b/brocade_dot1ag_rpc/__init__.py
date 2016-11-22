
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_show_cfm
class brocade_dot1ag(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag - based on the path /brocade_dot1ag_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an instrumentation to manage
CFM Protocol.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__get_show_cfm',)

  _yang_name = 'brocade-dot1ag'
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
    self.__get_show_cfm = YANGDynClass(base=get_show_cfm.get_show_cfm, is_leaf=True, yang_name="get-show-cfm", rest_name="get-show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'dot1agSummaryShowCfm'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='rpc', is_config=True)

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
      return [u'brocade_dot1ag_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_get_show_cfm(self):
    """
    Getter method for get_show_cfm, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm (rpc)
    """
    return self.__get_show_cfm
      
  def _set_get_show_cfm(self, v, load=False):
    """
    Setter method for get_show_cfm, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_show_cfm is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_show_cfm() directly.
    """
    try:
      t = YANGDynClass(v,base=get_show_cfm.get_show_cfm, is_leaf=True, yang_name="get-show-cfm", rest_name="get-show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'dot1agSummaryShowCfm'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_show_cfm must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=get_show_cfm.get_show_cfm, is_leaf=True, yang_name="get-show-cfm", rest_name="get-show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'dot1agSummaryShowCfm'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='rpc', is_config=True)""",
        })

    self.__get_show_cfm = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_show_cfm(self):
    self.__get_show_cfm = YANGDynClass(base=get_show_cfm.get_show_cfm, is_leaf=True, yang_name="get-show-cfm", rest_name="get-show-cfm", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'dot1agSummaryShowCfm'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='rpc', is_config=True)

  get_show_cfm = __builtin__.property(_get_get_show_cfm, _set_get_show_cfm)


  _pyangbind_elements = {'get_show_cfm': get_show_cfm, }


