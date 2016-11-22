
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rev_metric_common_attributes
class interface_reverse_metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/intf-isis/interface-isis/interface-reverse-metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rev_metric_common_attributes',)

  _yang_name = 'interface-reverse-metric'
  _rest_name = 'reverse-metric'

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
    self.__rev_metric_common_attributes = YANGDynClass(base=rev_metric_common_attributes.rev_metric_common_attributes, is_container='container', yang_name="rev-metric-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'intf-isis', u'interface-isis', u'interface-reverse-metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'isis', u'reverse-metric']

  def _get_rev_metric_common_attributes(self):
    """
    Getter method for rev_metric_common_attributes, mapped from YANG variable /routing_system/interface/ve/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes (container)
    """
    return self.__rev_metric_common_attributes
      
  def _set_rev_metric_common_attributes(self, v, load=False):
    """
    Setter method for rev_metric_common_attributes, mapped from YANG variable /routing_system/interface/ve/intf_isis/interface_isis/interface_reverse_metric/rev_metric_common_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rev_metric_common_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rev_metric_common_attributes() directly.
    """
    try:
      t = YANGDynClass(v,base=rev_metric_common_attributes.rev_metric_common_attributes, is_container='container', yang_name="rev-metric-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rev_metric_common_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rev_metric_common_attributes.rev_metric_common_attributes, is_container='container', yang_name="rev-metric-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__rev_metric_common_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rev_metric_common_attributes(self):
    self.__rev_metric_common_attributes = YANGDynClass(base=rev_metric_common_attributes.rev_metric_common_attributes, is_container='container', yang_name="rev-metric-common-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-sequence-commands': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

  rev_metric_common_attributes = __builtin__.property(_get_rev_metric_common_attributes, _set_rev_metric_common_attributes)


  _pyangbind_elements = {'rev_metric_common_attributes': rev_metric_common_attributes, }


