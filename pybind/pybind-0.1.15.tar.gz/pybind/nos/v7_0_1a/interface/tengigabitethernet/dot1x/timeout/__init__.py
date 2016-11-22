
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class timeout(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/dot1x/timeout. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This provides the grouping of all the timeout
configuration elements.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__re_authperiod','__server_timeout','__supp_timeout','__tx_period',)

  _yang_name = 'timeout'
  _rest_name = 'timeout'

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
    self.__supp_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="supp-timeout", rest_name="supp-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Supplicant response timeout (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-supp-timeout-interval', is_config=True)
    self.__tx_period = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="tx-period", rest_name="tx-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmission period in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-tx-timeout-interval', is_config=True)
    self.__server_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="server-timeout", rest_name="server-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Server timeout in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-server-timeout-interval', is_config=True)
    self.__re_authperiod = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3600), is_leaf=True, yang_name="re-authperiod", rest_name="re-authperiod", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reauthentication interval in seconds \n(default = 3600)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-reauth-timeout-interval', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'dot1x', u'timeout']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'dot1x', u'timeout']

  def _get_re_authperiod(self):
    """
    Getter method for re_authperiod, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/re_authperiod (dot1x-reauth-timeout-interval)

    YANG Description: This specifies the number of seconds
between re-authentication attempts.
    """
    return self.__re_authperiod
      
  def _set_re_authperiod(self, v, load=False):
    """
    Setter method for re_authperiod, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/re_authperiod (dot1x-reauth-timeout-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_re_authperiod is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_re_authperiod() directly.

    YANG Description: This specifies the number of seconds
between re-authentication attempts.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3600), is_leaf=True, yang_name="re-authperiod", rest_name="re-authperiod", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reauthentication interval in seconds \n(default = 3600)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-reauth-timeout-interval', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """re_authperiod must be of a type compatible with dot1x-reauth-timeout-interval""",
          'defined-type': "brocade-dot1x:dot1x-reauth-timeout-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3600), is_leaf=True, yang_name="re-authperiod", rest_name="re-authperiod", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reauthentication interval in seconds \n(default = 3600)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-reauth-timeout-interval', is_config=True)""",
        })

    self.__re_authperiod = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_re_authperiod(self):
    self.__re_authperiod = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(3600), is_leaf=True, yang_name="re-authperiod", rest_name="re-authperiod", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Reauthentication interval in seconds \n(default = 3600)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-reauth-timeout-interval', is_config=True)


  def _get_server_timeout(self):
    """
    Getter method for server_timeout, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/server_timeout (dot1x-server-timeout-interval)

    YANG Description: This specifies the dot1x server timeout
interval. This is the amount of time the switch
waits for a reply before retransmitting the 
response to the server, when relaying the 
response from the client to the authentication
server.
    """
    return self.__server_timeout
      
  def _set_server_timeout(self, v, load=False):
    """
    Setter method for server_timeout, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/server_timeout (dot1x-server-timeout-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server_timeout() directly.

    YANG Description: This specifies the dot1x server timeout
interval. This is the amount of time the switch
waits for a reply before retransmitting the 
response to the server, when relaying the 
response from the client to the authentication
server.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="server-timeout", rest_name="server-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Server timeout in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-server-timeout-interval', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """server_timeout must be of a type compatible with dot1x-server-timeout-interval""",
          'defined-type': "brocade-dot1x:dot1x-server-timeout-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="server-timeout", rest_name="server-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Server timeout in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-server-timeout-interval', is_config=True)""",
        })

    self.__server_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_server_timeout(self):
    self.__server_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="server-timeout", rest_name="server-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Server timeout in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-server-timeout-interval', is_config=True)


  def _get_supp_timeout(self):
    """
    Getter method for supp_timeout, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/supp_timeout (dot1x-supp-timeout-interval)

    YANG Description: This specifies the supplicant response
timeout. This is the amount of time the switch
waits for a response before retransmitting 
the request to the client when relaying a 
request from the authentication server 
to client.
    """
    return self.__supp_timeout
      
  def _set_supp_timeout(self, v, load=False):
    """
    Setter method for supp_timeout, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/supp_timeout (dot1x-supp-timeout-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_supp_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_supp_timeout() directly.

    YANG Description: This specifies the supplicant response
timeout. This is the amount of time the switch
waits for a response before retransmitting 
the request to the client when relaying a 
request from the authentication server 
to client.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="supp-timeout", rest_name="supp-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Supplicant response timeout (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-supp-timeout-interval', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """supp_timeout must be of a type compatible with dot1x-supp-timeout-interval""",
          'defined-type': "brocade-dot1x:dot1x-supp-timeout-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="supp-timeout", rest_name="supp-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Supplicant response timeout (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-supp-timeout-interval', is_config=True)""",
        })

    self.__supp_timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_supp_timeout(self):
    self.__supp_timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="supp-timeout", rest_name="supp-timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Supplicant response timeout (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-supp-timeout-interval', is_config=True)


  def _get_tx_period(self):
    """
    Getter method for tx_period, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/tx_period (dot1x-tx-timeout-interval)

    YANG Description: This specifies the number of seconds the 
switch waits for response to an EAP 
request/identity from client before
retransmitting the request.
    """
    return self.__tx_period
      
  def _set_tx_period(self, v, load=False):
    """
    Setter method for tx_period, mapped from YANG variable /interface/tengigabitethernet/dot1x/timeout/tx_period (dot1x-tx-timeout-interval)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_period is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_period() directly.

    YANG Description: This specifies the number of seconds the 
switch waits for response to an EAP 
request/identity from client before
retransmitting the request.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="tx-period", rest_name="tx-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmission period in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-tx-timeout-interval', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_period must be of a type compatible with dot1x-tx-timeout-interval""",
          'defined-type': "brocade-dot1x:dot1x-tx-timeout-interval",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="tx-period", rest_name="tx-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmission period in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-tx-timeout-interval', is_config=True)""",
        })

    self.__tx_period = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_period(self):
    self.__tx_period = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="tx-period", rest_name="tx-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Transmission period in seconds (default = 30)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='dot1x-tx-timeout-interval', is_config=True)

  re_authperiod = __builtin__.property(_get_re_authperiod, _set_re_authperiod)
  server_timeout = __builtin__.property(_get_server_timeout, _set_server_timeout)
  supp_timeout = __builtin__.property(_get_supp_timeout, _set_supp_timeout)
  tx_period = __builtin__.property(_get_tx_period, _set_tx_period)


  _pyangbind_elements = {'re_authperiod': re_authperiod, 'server_timeout': server_timeout, 'supp_timeout': supp_timeout, 'tx_period': tx_period, }


