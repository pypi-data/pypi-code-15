
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import raslog
import syslog_server
import auditlog
import syslog_facility
import syslog_client
class logging(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ras - based on the path /logging. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__raslog','__syslog_server','__auditlog','__syslog_facility','__syslog_client',)

  _yang_name = 'logging'
  _rest_name = 'logging'

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
    self.__syslog_client = YANGDynClass(base=syslog_client.syslog_client, is_container='container', yang_name="syslog-client", rest_name="syslog-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog Client configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__syslog_facility = YANGDynClass(base=syslog_facility.syslog_facility, is_container='container', yang_name="syslog-facility", rest_name="syslog-facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog facility configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__syslog_server = YANGDynClass(base=YANGListType("syslogip use_vrf",syslog_server.syslog_server, yang_name="syslog-server", rest_name="syslog-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='syslogip use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}), is_container='list', yang_name="syslog-server", rest_name="syslog-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='list', is_config=True)
    self.__raslog = YANGDynClass(base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message/module configurations'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    self.__auditlog = YANGDynClass(base=auditlog.auditlog, is_container='container', yang_name="auditlog", rest_name="auditlog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Audit log configurations', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)

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
      return [u'logging']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'logging']

  def _get_raslog(self):
    """
    Getter method for raslog, mapped from YANG variable /logging/raslog (container)
    """
    return self.__raslog
      
  def _set_raslog(self, v, load=False):
    """
    Setter method for raslog, mapped from YANG variable /logging/raslog (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_raslog is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_raslog() directly.
    """
    try:
      t = YANGDynClass(v,base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message/module configurations'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """raslog must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message/module configurations'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__raslog = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_raslog(self):
    self.__raslog = YANGDynClass(base=raslog.raslog, is_container='container', yang_name="raslog", rest_name="raslog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'RASLOG message/module configurations'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_syslog_server(self):
    """
    Getter method for syslog_server, mapped from YANG variable /logging/syslog_server (list)
    """
    return self.__syslog_server
      
  def _set_syslog_server(self, v, load=False):
    """
    Setter method for syslog_server, mapped from YANG variable /logging/syslog_server (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_syslog_server is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_syslog_server() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("syslogip use_vrf",syslog_server.syslog_server, yang_name="syslog-server", rest_name="syslog-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='syslogip use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}), is_container='list', yang_name="syslog-server", rest_name="syslog-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """syslog_server must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("syslogip use_vrf",syslog_server.syslog_server, yang_name="syslog-server", rest_name="syslog-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='syslogip use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}), is_container='list', yang_name="syslog-server", rest_name="syslog-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='list', is_config=True)""",
        })

    self.__syslog_server = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_syslog_server(self):
    self.__syslog_server = YANGDynClass(base=YANGListType("syslogip use_vrf",syslog_server.syslog_server, yang_name="syslog-server", rest_name="syslog-server", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='syslogip use-vrf', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}), is_container='list', yang_name="syslog-server", rest_name="syslog-server", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'callpoint': u'RASSingleCallPoint', u'info': u'Configure upto 4 syslog-server address.'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='list', is_config=True)


  def _get_auditlog(self):
    """
    Getter method for auditlog, mapped from YANG variable /logging/auditlog (container)
    """
    return self.__auditlog
      
  def _set_auditlog(self, v, load=False):
    """
    Setter method for auditlog, mapped from YANG variable /logging/auditlog (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auditlog is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auditlog() directly.
    """
    try:
      t = YANGDynClass(v,base=auditlog.auditlog, is_container='container', yang_name="auditlog", rest_name="auditlog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Audit log configurations', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auditlog must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auditlog.auditlog, is_container='container', yang_name="auditlog", rest_name="auditlog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Audit log configurations', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__auditlog = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auditlog(self):
    self.__auditlog = YANGDynClass(base=auditlog.auditlog, is_container='container', yang_name="auditlog", rest_name="auditlog", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Audit log configurations', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_syslog_facility(self):
    """
    Getter method for syslog_facility, mapped from YANG variable /logging/syslog_facility (container)
    """
    return self.__syslog_facility
      
  def _set_syslog_facility(self, v, load=False):
    """
    Setter method for syslog_facility, mapped from YANG variable /logging/syslog_facility (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_syslog_facility is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_syslog_facility() directly.
    """
    try:
      t = YANGDynClass(v,base=syslog_facility.syslog_facility, is_container='container', yang_name="syslog-facility", rest_name="syslog-facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog facility configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """syslog_facility must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=syslog_facility.syslog_facility, is_container='container', yang_name="syslog-facility", rest_name="syslog-facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog facility configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__syslog_facility = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_syslog_facility(self):
    self.__syslog_facility = YANGDynClass(base=syslog_facility.syslog_facility, is_container='container', yang_name="syslog-facility", rest_name="syslog-facility", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog facility configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)


  def _get_syslog_client(self):
    """
    Getter method for syslog_client, mapped from YANG variable /logging/syslog_client (container)
    """
    return self.__syslog_client
      
  def _set_syslog_client(self, v, load=False):
    """
    Setter method for syslog_client, mapped from YANG variable /logging/syslog_client (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_syslog_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_syslog_client() directly.
    """
    try:
      t = YANGDynClass(v,base=syslog_client.syslog_client, is_container='container', yang_name="syslog-client", rest_name="syslog-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog Client configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """syslog_client must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=syslog_client.syslog_client, is_container='container', yang_name="syslog-client", rest_name="syslog-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog Client configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)""",
        })

    self.__syslog_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_syslog_client(self):
    self.__syslog_client = YANGDynClass(base=syslog_client.syslog_client, is_container='container', yang_name="syslog-client", rest_name="syslog-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Syslog Client configurations', u'callpoint': u'RASSysFcCallPoint'}}, namespace='urn:brocade.com:mgmt:brocade-ras', defining_module='brocade-ras', yang_type='container', is_config=True)

  raslog = __builtin__.property(_get_raslog, _set_raslog)
  syslog_server = __builtin__.property(_get_syslog_server, _set_syslog_server)
  auditlog = __builtin__.property(_get_auditlog, _set_auditlog)
  syslog_facility = __builtin__.property(_get_syslog_facility, _set_syslog_facility)
  syslog_client = __builtin__.property(_get_syslog_client, _set_syslog_client)


  _pyangbind_elements = {'raslog': raslog, 'syslog_server': syslog_server, 'auditlog': auditlog, 'syslog_facility': syslog_facility, 'syslog_client': syslog_client, }


