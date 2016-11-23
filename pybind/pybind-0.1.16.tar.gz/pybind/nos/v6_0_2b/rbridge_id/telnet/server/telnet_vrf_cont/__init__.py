
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import use_vrf
class telnet_vrf_cont(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/telnet/server/telnet-vrf-cont. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__use_vrf',)

  _yang_name = 'telnet-vrf-cont'
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
    self.__use_vrf = YANGDynClass(base=YANGListType("use_vrf_name",use_vrf.use_vrf, yang_name="use-vrf", rest_name="use-vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='use-vrf-name', extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}), is_container='list', yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='list', is_config=True)

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
      return [u'rbridge-id', u'telnet', u'server', u'telnet-vrf-cont']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'telnet', u'server']

  def _get_use_vrf(self):
    """
    Getter method for use_vrf, mapped from YANG variable /rbridge_id/telnet/server/telnet_vrf_cont/use_vrf (list)
    """
    return self.__use_vrf
      
  def _set_use_vrf(self, v, load=False):
    """
    Setter method for use_vrf, mapped from YANG variable /rbridge_id/telnet/server/telnet_vrf_cont/use_vrf (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_vrf() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("use_vrf_name",use_vrf.use_vrf, yang_name="use-vrf", rest_name="use-vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='use-vrf-name', extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}), is_container='list', yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_vrf must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("use_vrf_name",use_vrf.use_vrf, yang_name="use-vrf", rest_name="use-vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='use-vrf-name', extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}), is_container='list', yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='list', is_config=True)""",
        })

    self.__use_vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_vrf(self):
    self.__use_vrf = YANGDynClass(base=YANGListType("use_vrf_name",use_vrf.use_vrf, yang_name="use-vrf", rest_name="use-vrf", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='use-vrf-name', extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}), is_container='list', yang_name="use-vrf", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure VRF Name **', u'cli-compact-syntax': None, u'callpoint': u'telnet_server_vrf_cp', u'cli-suppress-mode': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='list', is_config=True)

  use_vrf = __builtin__.property(_get_use_vrf, _set_use_vrf)


  _pyangbind_elements = {'use_vrf': use_vrf, }


