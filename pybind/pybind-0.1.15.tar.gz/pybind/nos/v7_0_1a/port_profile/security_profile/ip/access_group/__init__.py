
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class access_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/security-profile/ip/access-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This provides the grouping of configuration
elements of IP access list.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv4_access_group_name','__ipv4_in',)

  _yang_name = 'access-group'
  _rest_name = 'access-group'

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
    self.__ipv4_access_group_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ipv4-access-group-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access list name (Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)
    self.__ipv4_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv4-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ingress direction', u'cli-suppress-show-conf-path': None, u'alt-name': u'in', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='empty', is_config=True)

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
      return [u'port-profile', u'security-profile', u'ip', u'access-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'security-profile', u'ip', u'access-group']

  def _get_ipv4_access_group_name(self):
    """
    Getter method for ipv4_access_group_name, mapped from YANG variable /port_profile/security_profile/ip/access_group/ipv4_access_group_name (ip-access-list:l3-acl-policy-name)

    YANG Description: This specifies the Access list name which is 
already configured at the global level. This
access list contains access rules.
    """
    return self.__ipv4_access_group_name
      
  def _set_ipv4_access_group_name(self, v, load=False):
    """
    Setter method for ipv4_access_group_name, mapped from YANG variable /port_profile/security_profile/ip/access_group/ipv4_access_group_name (ip-access-list:l3-acl-policy-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_access_group_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_access_group_name() directly.

    YANG Description: This specifies the Access list name which is 
already configured at the global level. This
access list contains access rules.
    """
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ipv4-access-group-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access list name (Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_access_group_name must be of a type compatible with ip-access-list:l3-acl-policy-name""",
          'defined-type': "ip-access-list:l3-acl-policy-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ipv4-access-group-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access list name (Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)""",
        })

    self.__ipv4_access_group_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_access_group_name(self):
    self.__ipv4_access_group_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z0-9]{1}([-a-zA-Z0-9_]{0,62})', 'length': [u'1..63']}), is_leaf=True, yang_name="ipv4-access-group-name", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Access list name (Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='ip-access-list:l3-acl-policy-name', is_config=True)


  def _get_ipv4_in(self):
    """
    Getter method for ipv4_in, mapped from YANG variable /port_profile/security_profile/ip/access_group/ipv4_in (empty)

    YANG Description: This specifies if the direction is ingress or
not.
The presence of this leaf indicates Ingress 
direction.
    """
    return self.__ipv4_in
      
  def _set_ipv4_in(self, v, load=False):
    """
    Setter method for ipv4_in, mapped from YANG variable /port_profile/security_profile/ip/access_group/ipv4_in (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_in() directly.

    YANG Description: This specifies if the direction is ingress or
not.
The presence of this leaf indicates Ingress 
direction.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv4-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ingress direction', u'cli-suppress-show-conf-path': None, u'alt-name': u'in', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_in must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv4-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ingress direction', u'cli-suppress-show-conf-path': None, u'alt-name': u'in', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='empty', is_config=True)""",
        })

    self.__ipv4_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_in(self):
    self.__ipv4_in = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv4-in", rest_name="in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ingress direction', u'cli-suppress-show-conf-path': None, u'alt-name': u'in', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='empty', is_config=True)

  ipv4_access_group_name = __builtin__.property(_get_ipv4_access_group_name, _set_ipv4_access_group_name)
  ipv4_in = __builtin__.property(_get_ipv4_in, _set_ipv4_in)


  _pyangbind_elements = {'ipv4_access_group_name': ipv4_access_group_name, 'ipv4_in': ipv4_in, }


