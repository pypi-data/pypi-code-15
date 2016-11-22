
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class agtconfig(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-snmp - based on the path /snmp-server/agtconfig. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__contact','__location','__sys_descr',)

  _yang_name = 'agtconfig'
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
    self.__sys_descr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="sys-descr", rest_name="sys-descr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-description', is_config=True)
    self.__contact = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="contact", rest_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Contact information for the system(switch).'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-contact', is_config=True)
    self.__location = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="location", rest_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Location of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-location', is_config=True)

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
      return [u'snmp-server', u'agtconfig']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'snmp-server']

  def _get_contact(self):
    """
    Getter method for contact, mapped from YANG variable /snmp_server/agtconfig/contact (system-contact)
    """
    return self.__contact
      
  def _set_contact(self, v, load=False):
    """
    Setter method for contact, mapped from YANG variable /snmp_server/agtconfig/contact (system-contact)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_contact is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_contact() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="contact", rest_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Contact information for the system(switch).'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-contact', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """contact must be of a type compatible with system-contact""",
          'defined-type': "brocade-snmp:system-contact",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="contact", rest_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Contact information for the system(switch).'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-contact', is_config=True)""",
        })

    self.__contact = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_contact(self):
    self.__contact = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="contact", rest_name="contact", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Contact information for the system(switch).'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-contact', is_config=True)


  def _get_location(self):
    """
    Getter method for location, mapped from YANG variable /snmp_server/agtconfig/location (system-location)
    """
    return self.__location
      
  def _set_location(self, v, load=False):
    """
    Setter method for location, mapped from YANG variable /snmp_server/agtconfig/location (system-location)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_location is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_location() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="location", rest_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Location of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-location', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """location must be of a type compatible with system-location""",
          'defined-type': "brocade-snmp:system-location",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="location", rest_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Location of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-location', is_config=True)""",
        })

    self.__location = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_location(self):
    self.__location = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="location", rest_name="location", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Location of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-location', is_config=True)


  def _get_sys_descr(self):
    """
    Getter method for sys_descr, mapped from YANG variable /snmp_server/agtconfig/sys_descr (system-description)
    """
    return self.__sys_descr
      
  def _set_sys_descr(self, v, load=False):
    """
    Setter method for sys_descr, mapped from YANG variable /snmp_server/agtconfig/sys_descr (system-description)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sys_descr is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sys_descr() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="sys-descr", rest_name="sys-descr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-description', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sys_descr must be of a type compatible with system-description""",
          'defined-type': "brocade-snmp:system-description",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="sys-descr", rest_name="sys-descr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-description', is_config=True)""",
        })

    self.__sys_descr = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sys_descr(self):
    self.__sys_descr = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'4 .. 256']}), is_leaf=True, yang_name="sys-descr", rest_name="sys-descr", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Description of the system.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='system-description', is_config=True)

  contact = __builtin__.property(_get_contact, _set_contact)
  location = __builtin__.property(_get_location, _set_location)
  sys_descr = __builtin__.property(_get_sys_descr, _set_sys_descr)


  _pyangbind_elements = {'contact': contact, 'location': location, 'sys_descr': sys_descr, }


