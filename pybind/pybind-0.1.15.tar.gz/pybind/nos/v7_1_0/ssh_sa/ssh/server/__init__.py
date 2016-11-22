
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import standby
import key
import ssh_vrf_cont
class server(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sec-services - based on the path /ssh-sa/ssh/server. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__shutdown','__key_exchange','__rekey_interval','__cipher','__mac','__max_sessions','__standby','__key','__ssh_vrf_cont',)

  _yang_name = 'server'
  _rest_name = 'server'

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
    self.__key_exchange = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Key Exchange algorithm(s))', u'cli-full-command': None, u'callpoint': u'ssh_server_list_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    self.__key = YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH host keys', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    self.__standby = YANGDynClass(base=standby.standby, is_container='container', yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Standby SSH'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    self.__ssh_vrf_cont = YANGDynClass(base=ssh_vrf_cont.ssh_vrf_cont, is_container='container', yang_name="ssh-vrf-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    self.__max_sessions = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="max-sessions", rest_name="max-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max number of multiplexed sessions permitted per network connection', u'cli-full-command': None, u'callpoint': u'ssh_server_session_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC algorithm(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_mac_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    self.__cipher = YANGDynClass(base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Cipher(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_cipher_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown SSH Server', u'cli-full-command': None, u'callpoint': u'ssh_server_disable_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='empty', is_config=True)
    self.__rekey_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'900..3600']}), is_leaf=True, yang_name="rekey-interval", rest_name="rekey-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval for session rekeying', u'cli-full-command': None, u'callpoint': u'ssh_server_rekey_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)

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
      return [u'ssh-sa', u'ssh', u'server']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ssh', u'server']

  def _get_shutdown(self):
    """
    Getter method for shutdown, mapped from YANG variable /ssh_sa/ssh/server/shutdown (empty)
    """
    return self.__shutdown
      
  def _set_shutdown(self, v, load=False):
    """
    Setter method for shutdown, mapped from YANG variable /ssh_sa/ssh/server/shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown SSH Server', u'cli-full-command': None, u'callpoint': u'ssh_server_disable_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown SSH Server', u'cli-full-command': None, u'callpoint': u'ssh_server_disable_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='empty', is_config=True)""",
        })

    self.__shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown(self):
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shutdown SSH Server', u'cli-full-command': None, u'callpoint': u'ssh_server_disable_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='empty', is_config=True)


  def _get_key_exchange(self):
    """
    Getter method for key_exchange, mapped from YANG variable /ssh_sa/ssh/server/key_exchange (string)
    """
    return self.__key_exchange
      
  def _set_key_exchange(self, v, load=False):
    """
    Setter method for key_exchange, mapped from YANG variable /ssh_sa/ssh/server/key_exchange (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key_exchange is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key_exchange() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Key Exchange algorithm(s))', u'cli-full-command': None, u'callpoint': u'ssh_server_list_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key_exchange must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Key Exchange algorithm(s))', u'cli-full-command': None, u'callpoint': u'ssh_server_list_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)""",
        })

    self.__key_exchange = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key_exchange(self):
    self.__key_exchange = YANGDynClass(base=unicode, is_leaf=True, yang_name="key-exchange", rest_name="key-exchange", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Key Exchange algorithm(s))', u'cli-full-command': None, u'callpoint': u'ssh_server_list_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)


  def _get_rekey_interval(self):
    """
    Getter method for rekey_interval, mapped from YANG variable /ssh_sa/ssh/server/rekey_interval (uint32)
    """
    return self.__rekey_interval
      
  def _set_rekey_interval(self, v, load=False):
    """
    Setter method for rekey_interval, mapped from YANG variable /ssh_sa/ssh/server/rekey_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rekey_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rekey_interval() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'900..3600']}), is_leaf=True, yang_name="rekey-interval", rest_name="rekey-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval for session rekeying', u'cli-full-command': None, u'callpoint': u'ssh_server_rekey_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rekey_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'900..3600']}), is_leaf=True, yang_name="rekey-interval", rest_name="rekey-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval for session rekeying', u'cli-full-command': None, u'callpoint': u'ssh_server_rekey_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)""",
        })

    self.__rekey_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rekey_interval(self):
    self.__rekey_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'900..3600']}), is_leaf=True, yang_name="rekey-interval", rest_name="rekey-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Time interval for session rekeying', u'cli-full-command': None, u'callpoint': u'ssh_server_rekey_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)


  def _get_cipher(self):
    """
    Getter method for cipher, mapped from YANG variable /ssh_sa/ssh/server/cipher (string)
    """
    return self.__cipher
      
  def _set_cipher(self, v, load=False):
    """
    Setter method for cipher, mapped from YANG variable /ssh_sa/ssh/server/cipher (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cipher is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cipher() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Cipher(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_cipher_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cipher must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Cipher(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_cipher_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)""",
        })

    self.__cipher = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cipher(self):
    self.__cipher = YANGDynClass(base=unicode, is_leaf=True, yang_name="cipher", rest_name="cipher", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Cipher(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_cipher_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)


  def _get_mac(self):
    """
    Getter method for mac, mapped from YANG variable /ssh_sa/ssh/server/mac (string)
    """
    return self.__mac
      
  def _set_mac(self, v, load=False):
    """
    Setter method for mac, mapped from YANG variable /ssh_sa/ssh/server/mac (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac() directly.
    """
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC algorithm(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_mac_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC algorithm(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_mac_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)""",
        })

    self.__mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac(self):
    self.__mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="mac", rest_name="mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure MAC algorithm(s)', u'cli-full-command': None, u'callpoint': u'ssh_server_mac_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='string', is_config=True)


  def _get_max_sessions(self):
    """
    Getter method for max_sessions, mapped from YANG variable /ssh_sa/ssh/server/max_sessions (uint32)
    """
    return self.__max_sessions
      
  def _set_max_sessions(self, v, load=False):
    """
    Setter method for max_sessions, mapped from YANG variable /ssh_sa/ssh/server/max_sessions (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_sessions() directly.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="max-sessions", rest_name="max-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max number of multiplexed sessions permitted per network connection', u'cli-full-command': None, u'callpoint': u'ssh_server_session_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_sessions must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="max-sessions", rest_name="max-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max number of multiplexed sessions permitted per network connection', u'cli-full-command': None, u'callpoint': u'ssh_server_session_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)""",
        })

    self.__max_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_sessions(self):
    self.__max_sessions = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="max-sessions", rest_name="max-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Max number of multiplexed sessions permitted per network connection', u'cli-full-command': None, u'callpoint': u'ssh_server_session_cp'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='uint32', is_config=True)


  def _get_standby(self):
    """
    Getter method for standby, mapped from YANG variable /ssh_sa/ssh/server/standby (container)
    """
    return self.__standby
      
  def _set_standby(self, v, load=False):
    """
    Setter method for standby, mapped from YANG variable /ssh_sa/ssh/server/standby (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_standby is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_standby() directly.
    """
    try:
      t = YANGDynClass(v,base=standby.standby, is_container='container', yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Standby SSH'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """standby must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=standby.standby, is_container='container', yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Standby SSH'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)""",
        })

    self.__standby = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_standby(self):
    self.__standby = YANGDynClass(base=standby.standby, is_container='container', yang_name="standby", rest_name="standby", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Standby SSH'}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)


  def _get_key(self):
    """
    Getter method for key, mapped from YANG variable /ssh_sa/ssh/server/key (container)
    """
    return self.__key
      
  def _set_key(self, v, load=False):
    """
    Setter method for key, mapped from YANG variable /ssh_sa/ssh/server/key (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key() directly.
    """
    try:
      t = YANGDynClass(v,base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH host keys', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH host keys', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)""",
        })

    self.__key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key(self):
    self.__key = YANGDynClass(base=key.key, is_container='container', yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure SSH host keys', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)


  def _get_ssh_vrf_cont(self):
    """
    Getter method for ssh_vrf_cont, mapped from YANG variable /ssh_sa/ssh/server/ssh_vrf_cont (container)
    """
    return self.__ssh_vrf_cont
      
  def _set_ssh_vrf_cont(self, v, load=False):
    """
    Setter method for ssh_vrf_cont, mapped from YANG variable /ssh_sa/ssh/server/ssh_vrf_cont (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ssh_vrf_cont is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ssh_vrf_cont() directly.
    """
    try:
      t = YANGDynClass(v,base=ssh_vrf_cont.ssh_vrf_cont, is_container='container', yang_name="ssh-vrf-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ssh_vrf_cont must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ssh_vrf_cont.ssh_vrf_cont, is_container='container', yang_name="ssh-vrf-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)""",
        })

    self.__ssh_vrf_cont = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ssh_vrf_cont(self):
    self.__ssh_vrf_cont = YANGDynClass(base=ssh_vrf_cont.ssh_vrf_cont, is_container='container', yang_name="ssh-vrf-cont", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-sec-services', defining_module='brocade-sec-services', yang_type='container', is_config=True)

  shutdown = __builtin__.property(_get_shutdown, _set_shutdown)
  key_exchange = __builtin__.property(_get_key_exchange, _set_key_exchange)
  rekey_interval = __builtin__.property(_get_rekey_interval, _set_rekey_interval)
  cipher = __builtin__.property(_get_cipher, _set_cipher)
  mac = __builtin__.property(_get_mac, _set_mac)
  max_sessions = __builtin__.property(_get_max_sessions, _set_max_sessions)
  standby = __builtin__.property(_get_standby, _set_standby)
  key = __builtin__.property(_get_key, _set_key)
  ssh_vrf_cont = __builtin__.property(_get_ssh_vrf_cont, _set_ssh_vrf_cont)


  _pyangbind_elements = {'shutdown': shutdown, 'key_exchange': key_exchange, 'rekey_interval': rekey_interval, 'cipher': cipher, 'mac': mac, 'max_sessions': max_sessions, 'standby': standby, 'key': key, 'ssh_vrf_cont': ssh_vrf_cont, }


