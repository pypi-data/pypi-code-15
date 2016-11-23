
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class udld(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/udld. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Interface specific UDLD configurations.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__udld_enable',)

  _yang_name = 'udld'
  _rest_name = 'udld'

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
    self.__udld_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="udld-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable UDLD protocol on the Interface', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'udld']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'udld']

  def _get_udld_enable(self):
    """
    Getter method for udld_enable, mapped from YANG variable /interface/gigabitethernet/udld/udld_enable (empty)

    YANG Description: When present, indicates that UDLD protocol is
activated on this interface. By default the UDLD
will not be active on any interface. It needs to
be enabled explicitly.
    """
    return self.__udld_enable
      
  def _set_udld_enable(self, v, load=False):
    """
    Setter method for udld_enable, mapped from YANG variable /interface/gigabitethernet/udld/udld_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_udld_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_udld_enable() directly.

    YANG Description: When present, indicates that UDLD protocol is
activated on this interface. By default the UDLD
will not be active on any interface. It needs to
be enabled explicitly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="udld-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable UDLD protocol on the Interface', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """udld_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="udld-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable UDLD protocol on the Interface', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)""",
        })

    self.__udld_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_udld_enable(self):
    self.__udld_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="udld-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable UDLD protocol on the Interface', u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='empty', is_config=True)

  udld_enable = __builtin__.property(_get_udld_enable, _set_udld_enable)


  _pyangbind_elements = {'udld_enable': udld_enable, }


