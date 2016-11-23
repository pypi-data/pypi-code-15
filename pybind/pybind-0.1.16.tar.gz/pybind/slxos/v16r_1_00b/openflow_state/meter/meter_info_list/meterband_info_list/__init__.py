
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class meterband_info_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/meter/meter-info-list/meterband-info-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Meterband details
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__band_type','__rate','__burst_size','__in_packet_band_count','__in_byte_band_count',)

  _yang_name = 'meterband-info-list'
  _rest_name = 'meterband-info-list'

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
    self.__band_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="band-type", rest_name="band-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rate", rest_name="rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__burst_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__in_packet_band_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-band-count", rest_name="in-packet-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__in_byte_band_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-band-count", rest_name="in-byte-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

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
      return [u'openflow-state', u'meter', u'meter-info-list', u'meterband-info-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'meter', u'meter-info-list', u'meterband-info-list']

  def _get_band_type(self):
    """
    Getter method for band_type, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/band_type (uint32)

    YANG Description: Band Type
    """
    return self.__band_type
      
  def _set_band_type(self, v, load=False):
    """
    Setter method for band_type, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/band_type (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_band_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_band_type() directly.

    YANG Description: Band Type
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="band-type", rest_name="band-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """band_type must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="band-type", rest_name="band-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__band_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_band_type(self):
    self.__band_type = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="band-type", rest_name="band-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_rate(self):
    """
    Getter method for rate, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/rate (uint32)

    YANG Description: Rate
    """
    return self.__rate
      
  def _set_rate(self, v, load=False):
    """
    Setter method for rate, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/rate (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rate() directly.

    YANG Description: Rate
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rate", rest_name="rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rate must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rate", rest_name="rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__rate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rate(self):
    self.__rate = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rate", rest_name="rate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_burst_size(self):
    """
    Getter method for burst_size, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/burst_size (uint32)

    YANG Description: Burst size
    """
    return self.__burst_size
      
  def _set_burst_size(self, v, load=False):
    """
    Setter method for burst_size, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/burst_size (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_burst_size is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_burst_size() directly.

    YANG Description: Burst size
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """burst_size must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__burst_size = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_burst_size(self):
    self.__burst_size = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="burst-size", rest_name="burst-size", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_in_packet_band_count(self):
    """
    Getter method for in_packet_band_count, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/in_packet_band_count (uint32)

    YANG Description: In packet band count
    """
    return self.__in_packet_band_count
      
  def _set_in_packet_band_count(self, v, load=False):
    """
    Setter method for in_packet_band_count, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/in_packet_band_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_packet_band_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_packet_band_count() directly.

    YANG Description: In packet band count
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-band-count", rest_name="in-packet-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_packet_band_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-band-count", rest_name="in-packet-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__in_packet_band_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_packet_band_count(self):
    self.__in_packet_band_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-packet-band-count", rest_name="in-packet-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_in_byte_band_count(self):
    """
    Getter method for in_byte_band_count, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/in_byte_band_count (uint32)

    YANG Description: In byte band count
    """
    return self.__in_byte_band_count
      
  def _set_in_byte_band_count(self, v, load=False):
    """
    Setter method for in_byte_band_count, mapped from YANG variable /openflow_state/meter/meter_info_list/meterband_info_list/in_byte_band_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_in_byte_band_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_in_byte_band_count() directly.

    YANG Description: In byte band count
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-band-count", rest_name="in-byte-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """in_byte_band_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-band-count", rest_name="in-byte-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__in_byte_band_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_in_byte_band_count(self):
    self.__in_byte_band_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="in-byte-band-count", rest_name="in-byte-band-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)

  band_type = __builtin__.property(_get_band_type)
  rate = __builtin__.property(_get_rate)
  burst_size = __builtin__.property(_get_burst_size)
  in_packet_band_count = __builtin__.property(_get_in_packet_band_count)
  in_byte_band_count = __builtin__.property(_get_in_byte_band_count)


  _pyangbind_elements = {'band_type': band_type, 'rate': rate, 'burst_size': burst_size, 'in_packet_band_count': in_packet_band_count, 'in_byte_band_count': in_byte_band_count, }


