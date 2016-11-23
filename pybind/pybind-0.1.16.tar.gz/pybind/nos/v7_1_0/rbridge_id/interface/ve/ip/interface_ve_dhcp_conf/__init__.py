
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import dhcp
class interface_ve_dhcp_conf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/ve/ip/interface-ve-dhcp-conf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__dhcp',)

  _yang_name = 'interface-ve-dhcp-conf'
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
    self.__dhcp = YANGDynClass(base=dhcp.dhcp, is_container='container', yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dynamic Host Configuration Protocol (DHCP).', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'interface', u've', u'ip', u'interface-ve-dhcp-conf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Ve', u'ip']

  def _get_dhcp(self):
    """
    Getter method for dhcp, mapped from YANG variable /rbridge_id/interface/ve/ip/interface_ve_dhcp_conf/dhcp (container)
    """
    return self.__dhcp
      
  def _set_dhcp(self, v, load=False):
    """
    Setter method for dhcp, mapped from YANG variable /rbridge_id/interface/ve/ip/interface_ve_dhcp_conf/dhcp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dhcp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dhcp() directly.
    """
    try:
      t = YANGDynClass(v,base=dhcp.dhcp, is_container='container', yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dynamic Host Configuration Protocol (DHCP).', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dhcp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=dhcp.dhcp, is_container='container', yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dynamic Host Configuration Protocol (DHCP).', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)""",
        })

    self.__dhcp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dhcp(self):
    self.__dhcp = YANGDynClass(base=dhcp.dhcp, is_container='container', yang_name="dhcp", rest_name="dhcp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Dynamic Host Configuration Protocol (DHCP).', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-dhcp', defining_module='brocade-dhcp', yang_type='container', is_config=True)

  dhcp = __builtin__.property(_get_dhcp, _set_dhcp)


  _pyangbind_elements = {'dhcp': dhcp, }


