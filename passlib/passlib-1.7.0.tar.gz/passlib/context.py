"""passlib.context - CryptContext implementation"""
#=============================================================================
# imports
#=============================================================================
from __future__ import with_statement
# core
import re
import logging; log = logging.getLogger(__name__)
import threading
import time
from warnings import warn
# site
# pkg
from passlib.exc import ExpectedStringError, ExpectedTypeError, PasslibConfigWarning
from passlib.registry import get_crypt_handler, _validate_handler_name
from passlib.utils import (handlers as uh, to_bytes,
                           to_unicode, splitcomma,
                           as_bool, timer, rng, getrandstr,
                           )
from passlib.utils.binary import BASE64_CHARS
from passlib.utils.compat import (iteritems, num_types, irange,
                                  PY2, PY3, unicode, SafeConfigParser,
                                  NativeStringIO, BytesIO,
                                  unicode_or_bytes_types, native_string_types,
                                  )
from passlib.utils.decor import deprecated_method, memoized_property
# local
__all__ = [
    'CryptContext',
    'LazyCryptContext',
    'CryptPolicy',
]

#=============================================================================
# support
#=============================================================================

# private object to detect unset params
_UNSET = object()

def _coerce_vary_rounds(value):
    """parse vary_rounds string to percent as [0,1) float, or integer"""
    if value.endswith("%"):
        # XXX: deprecate this in favor of raw float?
        return float(value.rstrip("%"))*.01
    try:
        return int(value)
    except ValueError:
        return float(value)

# set of options which aren't allowed to be set via policy
_forbidden_scheme_options = set(["salt"])
    # 'salt' - not allowed since a fixed salt would defeat the purpose.

# dict containing funcs used to coerce strings to correct type for scheme option keys.
# NOTE: this isn't really needed any longer, since Handler.using() handles the actual parsing.
#       keeping this around for now, though, since it makes context.to_dict() output cleaner.
_coerce_scheme_options = dict(
    min_rounds=int,
    max_rounds=int,
    default_rounds=int,
    vary_rounds=_coerce_vary_rounds,
    salt_size=int,
)

def _is_handler_registered(handler):
    """detect if handler is registered or a custom handler"""
    return get_crypt_handler(handler.name, None) is handler

@staticmethod
def _always_needs_update(hash, secret=None):
    """
    dummy function patched into handler.needs_update() by _CryptConfig
    when hash alg has been deprecated for context.
    """
    return True

#: list of keys allowed under wildcard "all" scheme w/o a security warning.
_global_settings = set(["truncate_error", "vary_rounds"])

#=============================================================================
# crypt policy
#=============================================================================
_preamble = ("The CryptPolicy class has been deprecated as of "
             "Passlib 1.6, and will be removed in Passlib 1.8. ")

class CryptPolicy(object):
    """
    .. deprecated:: 1.6
        This class has been deprecated, and will be removed in Passlib 1.8.
        All of its functionality has been rolled into :class:`CryptContext`.

    This class previously stored the configuration options for the
    CryptContext class. In the interest of interface simplification,
    all of this class' functionality has been rolled into the CryptContext
    class itself.
    The documentation for this class is now focused on  documenting how to
    migrate to the new api. Additionally, where possible, the deprecation
    warnings issued by the CryptPolicy methods will list the replacement call
    that should be used.

    Constructors
    ============
    CryptPolicy objects can be constructed directly using any of
    the keywords accepted by :class:`CryptContext`. Direct uses of the
    :class:`!CryptPolicy` constructor should either pass the keywords
    directly into the CryptContext constructor, or to :meth:`CryptContext.update`
    if the policy object was being used to update an existing context object.

    In addition to passing in keywords directly,
    CryptPolicy objects can be constructed by the following methods:

    .. automethod:: from_path
    .. automethod:: from_string
    .. automethod:: from_source
    .. automethod:: from_sources
    .. automethod:: replace

    Introspection
    =============
    All of the informational methods provided by this class have been deprecated
    by identical or similar methods in the :class:`CryptContext` class:

    .. automethod:: has_schemes
    .. automethod:: schemes
    .. automethod:: iter_handlers
    .. automethod:: get_handler
    .. automethod:: get_options
    .. automethod:: handler_is_deprecated
    .. automethod:: get_min_verify_time

    Exporting
    =========
    .. automethod:: iter_config
    .. automethod:: to_dict
    .. automethod:: to_file
    .. automethod:: to_string

    .. note::
        CryptPolicy are immutable.
        Use the :meth:`replace` method to mutate existing instances.

    .. deprecated:: 1.6
    """
    #===================================================================
    # class methods
    #===================================================================
    @classmethod
    def from_path(cls, path, section="passlib", encoding="utf-8"):
        """create a CryptPolicy instance from a local file.

        .. deprecated:: 1.6

        Creating a new CryptContext from a file, which was previously done via
        ``CryptContext(policy=CryptPolicy.from_path(path))``, can now be
        done via ``CryptContext.from_path(path)``.
        See :meth:`CryptContext.from_path` for details.

        Updating an existing CryptContext from a file, which was previously done
        ``context.policy = CryptPolicy.from_path(path)``, can now be
        done via ``context.load_path(path)``.
        See :meth:`CryptContext.load_path` for details.
        """
        warn(_preamble +
             "Instead of ``CryptPolicy.from_path(path)``, "
             "use ``CryptContext.from_path(path)`` "
             " or ``context.load_path(path)`` for an existing CryptContext.",
             DeprecationWarning, stacklevel=2)
        return cls(_internal_context=CryptContext.from_path(path, section,
                                                            encoding))

    @classmethod
    def from_string(cls, source, section="passlib", encoding="utf-8"):
        """create a CryptPolicy instance from a string.

        .. deprecated:: 1.6

        Creating a new CryptContext from a string, which was previously done via
        ``CryptContext(policy=CryptPolicy.from_string(data))``, can now be
        done via ``CryptContext.from_string(data)``.
        See :meth:`CryptContext.from_string` for details.

        Updating an existing CryptContext from a string, which was previously done
        ``context.policy = CryptPolicy.from_string(data)``, can now be
        done via ``context.load(data)``.
        See :meth:`CryptContext.load` for details.
        """
        warn(_preamble +
             "Instead of ``CryptPolicy.from_string(source)``, "
             "use ``CryptContext.from_string(source)`` or "
             "``context.load(source)`` for an existing CryptContext.",
             DeprecationWarning, stacklevel=2)
        return cls(_internal_context=CryptContext.from_string(source, section,
                                                              encoding))

    @classmethod
    def from_source(cls, source, _warn=True):
        """create a CryptPolicy instance from some source.

        this method autodetects the source type, and invokes
        the appropriate constructor automatically. it attempts
        to detect whether the source is a configuration string, a filepath,
        a dictionary, or an existing CryptPolicy instance.

        .. deprecated:: 1.6

        Create a new CryptContext, which could previously be done via
        ``CryptContext(policy=CryptPolicy.from_source(source))``, should
        now be done using an explicit method: the :class:`CryptContext`
        constructor itself, :meth:`CryptContext.from_path`,
        or :meth:`CryptContext.from_string`.

        Updating an existing CryptContext, which could previously be done via
        ``context.policy = CryptPolicy.from_source(source)``, should
        now be done using an explicit method: :meth:`CryptContext.update`,
        or :meth:`CryptContext.load`.
        """
        if _warn:
            warn(_preamble +
                 "Instead of ``CryptPolicy.from_source()``, "
                 "use ``CryptContext.from_string(path)`` "
                 " or ``CryptContext.from_path(source)``, as appropriate.",
                 DeprecationWarning, stacklevel=2)
        if isinstance(source, CryptPolicy):
            return source
        elif isinstance(source, dict):
            return cls(_internal_context=CryptContext(**source))
        elif not isinstance(source, (bytes,unicode)):
            raise TypeError("source must be CryptPolicy, dict, config string, "
                            "or file path: %r" % (type(source),))
        elif any(c in source for c in "\n\r\t") or not source.strip(" \t./\;:"):
            return cls(_internal_context=CryptContext.from_string(source))
        else:
            return cls(_internal_context=CryptContext.from_path(source))

    @classmethod
    def from_sources(cls, sources, _warn=True):
        """create a CryptPolicy instance by merging multiple sources.

        each source is interpreted as by :meth:`from_source`,
        and the results are merged together.

        .. deprecated:: 1.6
            Instead of using this method to merge multiple policies together,
            a :class:`CryptContext` instance should be created, and then
            the multiple sources merged together via :meth:`CryptContext.load`.
        """
        if _warn:
            warn(_preamble +
                 "Instead of ``CryptPolicy.from_sources()``, "
                 "use the various CryptContext constructors "
                 " followed by ``context.update()``.",
                 DeprecationWarning, stacklevel=2)
        if len(sources) == 0:
            raise ValueError("no sources specified")
        if len(sources) == 1:
            return cls.from_source(sources[0], _warn=False)
        kwds = {}
        for source in sources:
            kwds.update(cls.from_source(source, _warn=False)._context.to_dict(resolve=True))
        return cls(_internal_context=CryptContext(**kwds))

    def replace(self, *args, **kwds):
        """create a new CryptPolicy, optionally updating parts of the
        existing configuration.

        .. deprecated:: 1.6
            Callers of this method should :meth:`CryptContext.update` or
            :meth:`CryptContext.copy` instead.
        """
        if self._stub_policy:
            warn(_preamble + # pragma: no cover -- deprecated & unused
                 "Instead of ``context.policy.replace()``, "
                 "use ``context.update()`` or ``context.copy()``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().replace()``, "
                 "create a CryptContext instance and "
                 "use ``context.update()`` or ``context.copy()``.",
                 DeprecationWarning, stacklevel=2)
        sources = [ self ]
        if args:
            sources.extend(args)
        if kwds:
            sources.append(kwds)
        return CryptPolicy.from_sources(sources, _warn=False)

    #===================================================================
    # instance attrs
    #===================================================================

    # internal CryptContext we're wrapping to handle everything
    # until this class is removed.
    _context = None

    # flag indicating this is wrapper generated by the CryptContext.policy
    # attribute, rather than one created independantly by the application.
    _stub_policy = False

    #===================================================================
    # init
    #===================================================================
    def __init__(self, *args, **kwds):
        context = kwds.pop("_internal_context", None)
        if context:
            assert isinstance(context, CryptContext)
            self._context = context
            self._stub_policy = kwds.pop("_stub_policy", False)
            assert not (args or kwds), "unexpected args: %r %r" % (args,kwds)
        else:
            if args:
                if len(args) != 1:
                    raise TypeError("only one positional argument accepted")
                if kwds:
                    raise TypeError("cannot specify positional arg and kwds")
                kwds = args[0]
            warn(_preamble +
                 "Instead of constructing a CryptPolicy instance, "
                 "create a CryptContext directly, or use ``context.update()`` "
                 "and ``context.load()`` to reconfigure existing CryptContext "
                 "instances.",
                 DeprecationWarning, stacklevel=2)
            self._context = CryptContext(**kwds)

    #===================================================================
    # public interface for examining options
    #===================================================================
    def has_schemes(self):
        """return True if policy defines *any* schemes for use.

        .. deprecated:: 1.6
            applications should use ``bool(context.schemes())`` instead.
            see :meth:`CryptContext.schemes`.
        """
        if self._stub_policy:
            warn(_preamble + # pragma: no cover -- deprecated & unused
                 "Instead of ``context.policy.has_schemes()``, "
                 "use ``bool(context.schemes())``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().has_schemes()``, "
                 "create a CryptContext instance and "
                 "use ``bool(context.schemes())``.",
                 DeprecationWarning, stacklevel=2)
        return bool(self._context.schemes())

    def iter_handlers(self):
        """return iterator over handlers defined in policy.

        .. deprecated:: 1.6
            applications should use ``context.schemes(resolve=True))`` instead.
            see :meth:`CryptContext.schemes`.
        """
        if self._stub_policy:
            warn(_preamble +
                 "Instead of ``context.policy.iter_handlers()``, "
                 "use ``context.schemes(resolve=True)``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().iter_handlers()``, "
                 "create a CryptContext instance and "
                 "use ``context.schemes(resolve=True)``.",
                 DeprecationWarning, stacklevel=2)
        return self._context.schemes(resolve=True, unconfigured=True)

    def schemes(self, resolve=False):
        """return list of schemes defined in policy.

        .. deprecated:: 1.6
            applications should use :meth:`CryptContext.schemes` instead.
        """
        if self._stub_policy:
            warn(_preamble + # pragma: no cover -- deprecated & unused
                 "Instead of ``context.policy.schemes()``, "
                 "use ``context.schemes()``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().schemes()``, "
                 "create a CryptContext instance and "
                 "use ``context.schemes()``.",
                 DeprecationWarning, stacklevel=2)
        return list(self._context.schemes(resolve=resolve, unconfigured=True))

    def get_handler(self, name=None, category=None, required=False):
        """return handler as specified by name, or default handler.

        .. deprecated:: 1.6
            applications should use :meth:`CryptContext.handler` instead,
            though note that the ``required`` keyword has been removed,
            and the new method will always act as if ``required=True``.
        """
        if self._stub_policy:
            warn(_preamble +
                 "Instead of ``context.policy.get_handler()``, "
                 "use ``context.handler()``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().get_handler()``, "
                 "create a CryptContext instance and "
                 "use ``context.handler()``.",
                 DeprecationWarning, stacklevel=2)
        # CryptContext.handler() doesn't support required=False,
        # so wrapping it in try/except
        try:
            return self._context.handler(name, category, unconfigured=True)
        except KeyError:
            if required:
                raise
            else:
                return None

    def get_min_verify_time(self, category=None):
        """get min_verify_time setting for policy.

        .. deprecated:: 1.6
            min_verify_time option will be removed entirely in passlib 1.8

        .. versionchanged:: 1.7
            this method now always returns the value automatically
            calculated by :meth:`CryptContext.min_verify_time`,
            any value specified by policy is ignored.
        """
        warn("get_min_verify_time() and min_verify_time option is deprecated and ignored, "
             "and will be removed in Passlib 1.8", DeprecationWarning,
             stacklevel=2)
        context = self._context
        if context.harden_verify:
            return context.min_verify_time
        else:
            return 0

    def get_options(self, name, category=None):
        """return dictionary of options specific to a given handler.

        .. deprecated:: 1.6
            this method has no direct replacement in the 1.6 api, as there
            is not a clearly defined use-case. however, examining the output of
            :meth:`CryptContext.to_dict` should serve as the closest alternative.
        """
        # XXX: might make a public replacement, but need more study of the use cases.
        if self._stub_policy:
            warn(_preamble + # pragma: no cover -- deprecated & unused
                 "``context.policy.get_options()`` will no longer be available.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "``CryptPolicy().get_options()`` will no longer be available.",
                 DeprecationWarning, stacklevel=2)
        if hasattr(name, "name"):
            name = name.name
        return self._context._config._get_record_options_with_flag(name, category)[0]

    def handler_is_deprecated(self, name, category=None):
        """check if handler has been deprecated by policy.

        .. deprecated:: 1.6
            this method has no direct replacement in the 1.6 api, as there
            is not a clearly defined use-case. however, examining the output of
            :meth:`CryptContext.to_dict` should serve as the closest alternative.
        """
        # XXX: might make a public replacement, but need more study of the use cases.
        if self._stub_policy:
            warn(_preamble +
                 "``context.policy.handler_is_deprecated()`` will no longer be available.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "``CryptPolicy().handler_is_deprecated()`` will no longer be available.",
                 DeprecationWarning, stacklevel=2)
        if hasattr(name, "name"):
            name = name.name
        return self._context.handler(name, category).deprecated

    #===================================================================
    # serialization
    #===================================================================

    def iter_config(self, ini=False, resolve=False):
        """iterate over key/value pairs representing the policy object.

        .. deprecated:: 1.6
            applications should use :meth:`CryptContext.to_dict` instead.
        """
        if self._stub_policy:
            warn(_preamble + # pragma: no cover -- deprecated & unused
                 "Instead of ``context.policy.iter_config()``, "
                 "use ``context.to_dict().items()``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().iter_config()``, "
                 "create a CryptContext instance and "
                 "use ``context.to_dict().items()``.",
                 DeprecationWarning, stacklevel=2)
        # hacked code that renders keys & values in manner that approximates
        # old behavior. context.to_dict() is much cleaner.
        context = self._context
        if ini:
            def render_key(key):
                return context._render_config_key(key).replace("__", ".")
            def render_value(value):
                if isinstance(value, (list,tuple)):
                    value = ", ".join(value)
                return value
            resolve = False
        else:
            render_key = context._render_config_key
            render_value = lambda value: value
        return (
            (render_key(key), render_value(value))
            for key, value in context._config.iter_config(resolve)
        )

    def to_dict(self, resolve=False):
        """export policy object as dictionary of options.

        .. deprecated:: 1.6
            applications should use :meth:`CryptContext.to_dict` instead.
        """
        if self._stub_policy:
            warn(_preamble +
                 "Instead of ``context.policy.to_dict()``, "
                 "use ``context.to_dict()``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().to_dict()``, "
                 "create a CryptContext instance and "
                 "use ``context.to_dict()``.",
                 DeprecationWarning, stacklevel=2)
        return self._context.to_dict(resolve)

    def to_file(self, stream, section="passlib"): # pragma: no cover -- deprecated & unused
        """export policy to file.

        .. deprecated:: 1.6
            applications should use :meth:`CryptContext.to_string` instead,
            and then write the output to a file as desired.
        """
        if self._stub_policy:
            warn(_preamble +
                 "Instead of ``context.policy.to_file(stream)``, "
                 "use ``stream.write(context.to_string())``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().to_file(stream)``, "
                 "create a CryptContext instance and "
                 "use ``stream.write(context.to_string())``.",
                 DeprecationWarning, stacklevel=2)
        out = self._context.to_string(section=section)
        if PY2:
            out = out.encode("utf-8")
        stream.write(out)

    def to_string(self, section="passlib", encoding=None):
        """export policy to file.

        .. deprecated:: 1.6
            applications should use :meth:`CryptContext.to_string` instead.
        """
        if self._stub_policy:
            warn(_preamble + # pragma: no cover -- deprecated & unused
                 "Instead of ``context.policy.to_string()``, "
                 "use ``context.to_string()``.",
                 DeprecationWarning, stacklevel=2)
        else:
            warn(_preamble +
                 "Instead of ``CryptPolicy().to_string()``, "
                 "create a CryptContext instance and "
                 "use ``context.to_string()``.",
                 DeprecationWarning, stacklevel=2)
        out = self._context.to_string(section=section)
        if encoding:
            out = out.encode(encoding)
        return out

    #===================================================================
    # eoc
    #===================================================================

#=============================================================================
# _CryptConfig helper class
#=============================================================================
class _CryptConfig(object):
    """parses, validates, and stores CryptContext config

    this is a helper used internally by CryptContext to handle
    parsing, validation, and serialization of its config options.
    split out from the main class, but not made public since
    that just complicates interface too much (c.f. CryptPolicy)

    :arg source: config as dict mapping ``(cat,scheme,option) -> value``
    """
    #===================================================================
    # instance attrs
    #===================================================================

    # triple-nested dict which maps scheme -> category -> key -> value,
    # storing all hash-specific options
    _scheme_options = None

    # double-nested dict which maps key -> category -> value
    # storing all CryptContext options
    _context_options = None

    # tuple of handler objects
    handlers = None

    # tuple of scheme objects in same order as handlers
    schemes = None

    # tuple of categories in alphabetical order (not including None)
    categories = None

    # set of all context keywords used by active schemes
    context_kwds = None

    # dict mapping category -> default scheme
    _default_schemes = None

    # dict mapping (scheme, category) -> custom handler
    _records = None

    # dict mapping category -> list of custom handler instances for that category,
    # in order of schemes(). populated on demand by _get_record_list()
    _record_lists = None

    #===================================================================
    # constructor
    #===================================================================
    def __init__(self, source):
        self._init_scheme_list(source.get((None,None,"schemes")))
        self._init_options(source)
        self._init_default_schemes()
        self._init_records()

    def _init_scheme_list(self, data):
        """initialize .handlers and .schemes attributes"""
        handlers  = []
        schemes = []
        if isinstance(data, native_string_types):
            data = splitcomma(data)
        for elem in data or ():
            # resolve elem -> handler & scheme
            if hasattr(elem, "name"):
                handler = elem
                scheme = handler.name
                _validate_handler_name(scheme)
            elif isinstance(elem, native_string_types):
                handler = get_crypt_handler(elem)
                scheme = handler.name
            else:
                raise TypeError("scheme must be name or CryptHandler, "
                                "not %r" % type(elem))

            # check scheme name isn't already in use
            if scheme in schemes:
                raise KeyError("multiple handlers with same name: %r" %
                               (scheme,))

            # add to handler list
            handlers.append(handler)
            schemes.append(scheme)

        self.handlers = tuple(handlers)
        self.schemes = tuple(schemes)

    #===================================================================
    # lowlevel options
    #===================================================================

    #---------------------------------------------------------------
    # init lowlevel option storage
    #---------------------------------------------------------------
    def _init_options(self, source):
        """load config dict into internal representation,
        and init .categories attr
        """
        # prepare dicts & locals
        norm_scheme_option = self._norm_scheme_option
        norm_context_option = self._norm_context_option
        self._scheme_options = scheme_options = {}
        self._context_options = context_options = {}
        categories = set()

        # load source config into internal storage
        for (cat, scheme, key), value in iteritems(source):
            categories.add(cat)
            explicit_scheme = scheme
            if not cat and not scheme and key in _global_settings:
                # going forward, not using "<cat>__all__<key>" format. instead...
                # whitelisting set of keys which should be passed to (all) schemes,
                # rather than passed to the CryptContext itself
                scheme = "all"
            if scheme:
                # normalize scheme option
                key, value = norm_scheme_option(key, value)

                # e.g. things like "min_rounds" should never be set cross-scheme
                # this will be fatal under 2.0.
                if scheme == "all" and key not in _global_settings:
                    warn("The '%s' option should be configured per-algorithm, and not set "
                         "globally in the context; This will be an error in Passlib 2.0" %
                         (key,), PasslibConfigWarning)

                # this scheme is going away in 2.0;
                # but most keys deserve an extra warning since it impacts security.
                if explicit_scheme == "all":
                    warn("The 'all' scheme is deprecated as of Passlib 1.7, "
                         "and will be removed in Passlib 2.0; Please configure "
                         "options on a per-algorithm basis.", DeprecationWarning)

                # store in scheme_options
                # map structure: scheme_options[scheme][category][key] = value
                try:
                    category_map = scheme_options[scheme]
                except KeyError:
                    scheme_options[scheme] = {cat: {key: value}}
                else:
                    try:
                        option_map = category_map[cat]
                    except KeyError:
                        category_map[cat] = {key: value}
                    else:
                        option_map[key] = value
            else:
                # normalize context option
                if cat and key == "schemes":
                    raise KeyError("'schemes' context option is not allowed "
                                   "per category")
                key, value = norm_context_option(cat, key, value)
                if key == "min_verify_time": # ignored in 1.7, to be removed in 1.8
                    continue

                # store in context_options
                # map structure: context_options[key][category] = value
                try:
                    category_map = context_options[key]
                except KeyError:
                    context_options[key] = {cat: value}
                else:
                    category_map[cat] = value

        # store list of configured categories
        categories.discard(None)
        self.categories = tuple(sorted(categories))

    def _norm_scheme_option(self, key, value):
        # check for invalid options
        if key in _forbidden_scheme_options:
            raise KeyError("%r option not allowed in CryptContext "
                           "configuration" % (key,))
        # coerce strings for certain fields (e.g. min_rounds uses ints)
        if isinstance(value, native_string_types):
            func = _coerce_scheme_options.get(key)
            if func:
                value = func(value)
        return key, value

    def _norm_context_option(self, cat, key, value):
        schemes = self.schemes
        if key == "default":
            if hasattr(value, "name"):
                value = value.name
            elif not isinstance(value, native_string_types):
                raise ExpectedTypeError(value, "str", "default")
            if schemes and value not in schemes:
                raise KeyError("default scheme not found in policy")
        elif key == "deprecated":
            if isinstance(value, native_string_types):
                value = splitcomma(value)
            elif not isinstance(value, (list,tuple)):
                raise ExpectedTypeError(value, "str or seq", "deprecated")
            if 'auto' in value:
                # XXX: have any statements been made about when this is default?
                #      should do it in 1.8 at latest.
                if len(value) > 1:
                    raise ValueError("cannot list other schemes if "
                                     "``deprecated=['auto']`` is used")
            elif schemes:
                # make sure list of deprecated schemes is subset of configured schemes
                for scheme in value:
                    if not isinstance(scheme, native_string_types):
                        raise ExpectedTypeError(value, "str", "deprecated element")
                    if scheme not in schemes:
                        raise KeyError("deprecated scheme not found "
                                   "in policy: %r" % (scheme,))
        elif key == "min_verify_time":
            warn("'min_verify_time' was deprecated in Passlib 1.6, is "
                 "ignored in 1.7, and will be removed in 1.8; use 'harden_verify' instead",
                 DeprecationWarning)
        elif key == "harden_verify":
            if cat:
                raise ValueError("'harden_verify' cannot be specified per category")
            value = as_bool(value, param="harden_verify")
        elif key != "schemes":
            raise KeyError("unknown CryptContext keyword: %r" % (key,))
        return key, value

    #---------------------------------------------------------------
    # reading context options
    #---------------------------------------------------------------
    def get_context_optionmap(self, key, _default={}):
        """return dict mapping category->value for specific context option.

        .. warning:: treat return value as readonly!
        """
        return self._context_options.get(key, _default)

    def get_context_option_with_flag(self, category, key):
        """return value of specific option, handling category inheritance.
        also returns flag indicating whether value is category-specific.
        """
        try:
            category_map = self._context_options[key]
        except KeyError:
            return None, False
        value = category_map.get(None)
        if category:
            try:
                alt = category_map[category]
            except KeyError:
                pass
            else:
                if value is None or alt != value:
                    return alt, True
        return value, False

    #---------------------------------------------------------------
    # reading scheme options
    #---------------------------------------------------------------
    def _get_scheme_optionmap(self, scheme, category, default={}):
        """return all options for (scheme,category) combination

        .. warning:: treat return value as readonly!
        """
        try:
            return self._scheme_options[scheme][category]
        except KeyError:
            return default

    def get_base_handler(self, scheme):
        return self.handlers[self.schemes.index(scheme)]

    @staticmethod
    def expand_settings(handler):
        setting_kwds = handler.setting_kwds
        if 'rounds' in handler.setting_kwds:
            # XXX: historically this extras won't be listed in setting_kwds
            setting_kwds += uh.HasRounds.using_rounds_kwds
        return setting_kwds

    # NOTE: this is only used by _get_record_options_with_flag()...
    def get_scheme_options_with_flag(self, scheme, category):
        """return composite dict of all options set for scheme.
        includes options inherited from 'all' and from default category.
        result can be modified.
        returns (kwds, has_cat_specific_options)
        """
        # start out with copy of global options
        get_optionmap = self._get_scheme_optionmap
        kwds = get_optionmap("all", None).copy()
        has_cat_options = False

        # add in category-specific global options
        if category:
            defkwds = kwds.copy() # <-- used to detect category-specific options
            kwds.update(get_optionmap("all", category))

        # filter out global settings not supported by handler
        allowed_settings = self.expand_settings(self.get_base_handler(scheme))
        for key in set(kwds).difference(allowed_settings):
            kwds.pop(key)
        if category:
            for key in set(defkwds).difference(allowed_settings):
                defkwds.pop(key)

        # add in default options for scheme
        other = get_optionmap(scheme, None)
        kwds.update(other)

        # load category-specific options for scheme
        if category:
            defkwds.update(other)
            kwds.update(get_optionmap(scheme, category))

            # compare default category options to see if there's anything
            # category-specific
            if kwds != defkwds:
                has_cat_options = True

        return kwds, has_cat_options

    #===================================================================
    # deprecated & default schemes
    #===================================================================
    def _init_default_schemes(self):
        """initialize maps containing default scheme for each category.

        have to do this after _init_options(), since the default scheme
        is affected by the list of deprecated schemes.
        """
        # init maps & locals
        get_optionmap = self.get_context_optionmap
        default_map = self._default_schemes = get_optionmap("default").copy()
        dep_map = get_optionmap("deprecated")
        schemes = self.schemes
        if not schemes:
            return

        # figure out default scheme
        deps = dep_map.get(None) or ()
        default = default_map.get(None)
        if not default:
            for scheme in schemes:
                if scheme not in deps:
                    default_map[None] = scheme
                    break
            else:
                raise ValueError("must have at least one non-deprecated scheme")
        elif default in deps:
            raise ValueError("default scheme cannot be deprecated")

        # figure out per-category default schemes,
        for cat in self.categories:
            cdeps = dep_map.get(cat, deps)
            cdefault = default_map.get(cat, default)
            if not cdefault:
                for scheme in schemes:
                    if scheme not in cdeps:
                        default_map[cat] = scheme
                        break
                else:
                    raise ValueError("must have at least one non-deprecated "
                                     "scheme for %r category" % cat)
            elif cdefault in cdeps:
                raise ValueError("default scheme for %r category "
                                 "cannot be deprecated" % cat)

    def default_scheme(self, category):
        """return default scheme for specific category"""
        defaults = self._default_schemes
        try:
            return defaults[category]
        except KeyError:
            pass
        if not self.schemes:
            raise KeyError("no hash schemes configured for this "
                           "CryptContext instance")
        return defaults[None]

    def is_deprecated_with_flag(self, scheme, category):
        """is scheme deprecated under particular category?"""
        depmap = self.get_context_optionmap("deprecated")
        def test(cat):
            source = depmap.get(cat, depmap.get(None))
            if source is None:
                return None
            elif 'auto' in source:
                return scheme != self.default_scheme(cat)
            else:
                return scheme in source
        value = test(None) or False
        if category:
            alt = test(category)
            if alt is not None and value != alt:
                return alt, True
        return value, False

    #===================================================================
    # CryptRecord objects
    #===================================================================
    def _init_records(self):
        # NOTE: this step handles final validation of settings,
        #       checking for violations against handler's internal invariants.
        #       this is why we create all the records now,
        #       so CryptContext throws error immediately rather than later.
        self._record_lists = {}
        records = self._records = {}
        all_context_kwds = self.context_kwds = set()
        get_options = self._get_record_options_with_flag
        categories = (None,) + self.categories
        for handler in self.handlers:
            scheme = handler.name
            all_context_kwds.update(handler.context_kwds)
            for cat in categories:
                kwds, has_cat_options = get_options(scheme, cat)
                if cat is None or has_cat_options:
                    records[scheme, cat] = self._create_record(handler, cat, **kwds)
                # NOTE: if handler has no category-specific opts, get_record()
                # will automatically use the default category's record.
        # NOTE: default records for specific category stored under the
        # key (None,category); these are populated on-demand by get_record().

    @staticmethod
    def _create_record(handler, category=None, deprecated=False, **settings):
        # create custom handler if needed.
        try:
            # XXX: relaxed=True is mostly here to retain backwards-compat behavior.
            #      could make this optional flag in future.
            subcls = handler.using(relaxed=True, **settings)
        except TypeError as err:
            m = re.match(r".* unexpected keyword argument '(.*)'$", str(err))
            if m and m.group(1) in settings:
                # translate into KeyError, for backwards compat.
                # XXX: push this down to GenericHandler.using() implementation?
                key = m.group(1)
                raise KeyError("keyword not supported by %s handler: %r" %
                               (handler.name, key))
            raise

        # using private attrs to store some extra metadata in custom handler
        assert subcls is not handler, "expected unique variant of handler"
        ##subcls._Context__category = category
        subcls._Context__orig_handler = handler
        subcls.deprecated = deprecated  # attr reserved for this purpose
        return subcls

    def _get_record_options_with_flag(self, scheme, category):
        """return composite dict of options for given scheme + category.

        this is currently a private method, though some variant
        of its output may eventually be made public.

        given a scheme & category, it returns two things:
        a set of all the keyword options to pass to :meth:`_create_record`,
        and a bool flag indicating whether any of these options
        were specific to the named category. if this flag is false,
        the options are identical to the options for the default category.

        the options dict includes all the scheme-specific settings,
        as well as optional *deprecated* keyword.
        """
        # get scheme options
        kwds, has_cat_options = self.get_scheme_options_with_flag(scheme, category)

        # throw in deprecated flag
        value, not_inherited = self.is_deprecated_with_flag(scheme, category)
        if value:
            kwds['deprecated'] = True
        if not_inherited:
            has_cat_options = True

        return kwds, has_cat_options

    def get_record(self, scheme, category):
        """return record for specific scheme & category (cached)"""
        # NOTE: this is part of the critical path shared by
        #       all of CryptContext's PasswordHash methods,
        #       hence all the caching and error checking.

        # quick lookup in cache
        try:
            return self._records[scheme, category]
        except KeyError:
            pass

        # type check
        if category is not None and not isinstance(category, native_string_types):
            if PY2 and isinstance(category, unicode):
                # for compatibility with unicode-centric py2 apps
                return self.get_record(scheme, category.encode("utf-8"))
            raise ExpectedTypeError(category, "str or None", "category")
        if scheme is not None and not isinstance(scheme, native_string_types):
            raise ExpectedTypeError(scheme, "str or None", "scheme")

        # if scheme=None,
        # use record for category's default scheme, and cache result.
        if not scheme:
            default = self.default_scheme(category)
            assert default
            record = self._records[None, category] = self.get_record(default,
                                                                      category)
            return record

        # if no record for (scheme, category),
        # use record for (scheme, None), and cache result.
        if category:
            try:
                cache = self._records
                record = cache[scheme, category] = cache[scheme, None]
                return record
            except KeyError:
                pass

        # scheme not found in configuration for default category
        raise KeyError("crypt algorithm not found in policy: %r" % (scheme,))

    def _get_record_list(self, category=None):
        """return list of records for category (cached)

        this is an internal helper used only by identify_record()
        """
        # type check of category - handled by _get_record()
        # quick lookup in cache
        try:
            return self._record_lists[category]
        except KeyError:
            pass
        # cache miss - build list from scratch
        value = self._record_lists[category] = [
            self.get_record(scheme, category)
            for scheme in self.schemes
            ]
        return value

    def identify_record(self, hash, category, required=True):
        """internal helper to identify appropriate custom handler for hash"""
        # NOTE: this is part of the critical path shared by
        #       all of CryptContext's PasswordHash methods,
        #       hence all the caching and error checking.
        # FIXME: if multiple hashes could match (e.g. lmhash vs nthash)
        #        this will only return first match. might want to do something
        #        about this in future, but for now only hashes with
        #        unique identifiers will work properly in a CryptContext.
        # XXX: if all handlers have a unique prefix (e.g. all are MCF / LDAP),
        #      could use dict-lookup to speed up this search.
        if not isinstance(hash, unicode_or_bytes_types):
            raise ExpectedStringError(hash, "hash")
        # type check of category - handled by _get_record_list()
        for record in self._get_record_list(category):
            if record.identify(hash):
                return record
        if not required:
            return None
        elif not self.schemes:
            raise KeyError("no crypt algorithms supported")
        else:
            raise ValueError("hash could not be identified")

    @memoized_property
    def disabled_record(self):
        for record in self._get_record_list(None):
            if record.is_disabled:
                return record
        raise RuntimeError("no disabled hasher present "
                           "(perhaps add 'unix_disabled' to list of schemes?)")

    #===================================================================
    # serialization
    #===================================================================
    def iter_config(self, resolve=False):
        """regenerate original config.

        this is an iterator which yields ``(cat,scheme,option),value`` items,
        in the order they generally appear inside an INI file.
        if interpreted as a dictionary, it should match the original
        keywords passed to the CryptContext (aside from any canonization).

        it's mainly used as the internal backend for most of the public
        serialization methods.
        """
        # grab various bits of data
        scheme_options = self._scheme_options
        context_options = self._context_options
        scheme_keys = sorted(scheme_options)
        context_keys = sorted(context_options)

        # write loaded schemes (may differ from 'schemes' local var)
        if 'schemes' in context_keys:
            context_keys.remove("schemes")
        value = self.handlers if resolve else self.schemes
        if value:
            yield (None, None, "schemes"), list(value)

        # then run through config for each user category
        for cat in (None,) + self.categories:

            # write context options
            for key in context_keys:
                try:
                    value = context_options[key][cat]
                except KeyError:
                    pass
                else:
                    if isinstance(value, list):
                        value = list(value)
                    yield (cat, None, key), value

            # write per-scheme options for all schemes.
            for scheme in scheme_keys:
                try:
                    kwds = scheme_options[scheme][cat]
                except KeyError:
                    pass
                else:
                    for key in sorted(kwds):
                        yield (cat, scheme, key), kwds[key]

    #===================================================================
    # eoc
    #===================================================================

#=============================================================================
# main CryptContext class
#=============================================================================
class CryptContext(object):
    """Helper for hashing & verifying passwords using multiple algorithms.

    Instances of this class allow applications to choose a specific
    set of hash algorithms which they wish to support, set limits and defaults
    for the rounds and salt sizes those algorithms should use, flag
    which algorithms should be deprecated, and automatically handle
    migrating users to stronger hashes when they log in.

    Basic usage::

        >>> ctx = CryptContext(schemes=[...])

    See the Passlib online documentation for details and full documentation.
    """
    # FIXME: altering the configuration of this object isn't threadsafe,
    # but is generally only done during application init, so not a major
    # issue (just yet).

    # XXX: would like some way to restrict the categories that are allowed,
    # to restrict what the app OR the config can use.

    # XXX: add wrap/unwrap callback hooks so app can mutate hash format?

    # XXX: add method for detecting and warning user about schemes
    #      which don't have any good distinguishing marks?
    #      or greedy ones (unix_disabled, plaintext) which are not listed at the end?

    #===================================================================
    # instance attrs
    #===================================================================

    # _CryptConfig instance holding current parsed config
    _config = None

    # copy of _config methods, stored in CryptContext instance for speed.
    _get_record = None
    _identify_record = None

    #===================================================================
    # secondary constructors
    #===================================================================
    @classmethod
    def _norm_source(cls, source):
        """internal helper - accepts string, dict, or context"""
        if isinstance(source, dict):
            return cls(**source)
        elif isinstance(source, cls):
            return source
        else:
            self = cls()
            self.load(source)
            return self

    @classmethod
    def from_string(cls, source, section="passlib", encoding="utf-8"):
        """create new CryptContext instance from an INI-formatted string.

        :type source: unicode or bytes
        :arg source:
            string containing INI-formatted content.

        :type section: str
        :param section:
            option name of section to read from, defaults to ``"passlib"``.

        :type encoding: str
        :arg encoding:
            optional encoding used when source is bytes, defaults to ``"utf-8"``.

        :returns:
            new :class:`CryptContext` instance, configured based on the
            parameters in the *source* string.

        Usage example::

            >>> from passlib.context import CryptContext
            >>> context = CryptContext.from_string('''
            ... [passlib]
            ... schemes = sha256_crypt, des_crypt
            ... sha256_crypt__default_rounds = 30000
            ... ''')

        .. versionadded:: 1.6

        .. seealso:: :meth:`to_string`, the inverse of this constructor.
        """
        if not isinstance(source, unicode_or_bytes_types):
            raise ExpectedTypeError(source, "unicode or bytes", "source")
        self = cls(_autoload=False)
        self.load(source, section=section, encoding=encoding)
        return self

    @classmethod
    def from_path(cls, path, section="passlib", encoding="utf-8"):
        """create new CryptContext instance from an INI-formatted file.

        this functions exactly the same as :meth:`from_string`,
        except that it loads from a local file.

        :type path: str
        :arg path:
            path to local file containing INI-formatted config.

        :type section: str
        :param section:
            option name of section to read from, defaults to ``"passlib"``.

        :type encoding: str
        :arg encoding:
            encoding used to load file, defaults to ``"utf-8"``.

        :returns:
            new CryptContext instance, configured based on the parameters
            stored in the file *path*.

        .. versionadded:: 1.6

        .. seealso:: :meth:`from_string` for an equivalent usage example.
        """
        self = cls(_autoload=False)
        self.load_path(path, section=section, encoding=encoding)
        return self

    def copy(self, **kwds):
        """Return copy of existing CryptContext instance.

        This function returns a new CryptContext instance whose configuration
        is exactly the same as the original, with the exception that any keywords
        passed in will take precedence over the original settings.
        As an example::

            >>> from passlib.context import CryptContext

            >>> # given an existing context...
            >>> ctx1 = CryptContext(["sha256_crypt", "md5_crypt"])

            >>> # copy can be used to make a clone, and update
            >>> # some of the settings at the same time...
            >>> ctx2 = custom_app_context.copy(default="md5_crypt")

            >>> # and the original will be unaffected by the change
            >>> ctx1.default_scheme()
            "sha256_crypt"
            >>> ctx2.default_scheme()
            "md5_crypt"

        .. versionadded:: 1.6
            This method was previously named :meth:`!replace`. That alias
            has been deprecated, and will be removed in Passlib 1.8.

        .. seealso:: :meth:`update`
        """
        # XXX: it would be faster to store ref to self._config,
        #      but don't want to share config objects til sure
        #      can rely on them being immutable.
        other = CryptContext(_autoload=False)
        other.load(self)
        if kwds:
            other.load(kwds, update=True)
        return other

    def using(self, **kwds):
        """
        alias for :meth:`copy`, to match PasswordHash.using()
        """
        return self.copy(**kwds)

    def replace(self, **kwds):
        """deprecated alias of :meth:`copy`"""
        warn("CryptContext().replace() has been deprecated in Passlib 1.6, "
             "and will be removed in Passlib 1.8, "
             "it has been renamed to CryptContext().copy()",
             DeprecationWarning, stacklevel=2)
        return self.copy(**kwds)

    #===================================================================
    # init
    #===================================================================
    def __init__(self, schemes=None,
                 # keyword only...
                 policy=_UNSET, # <-- deprecated
                 _autoload=True, **kwds):
        # XXX: add ability to make flag certain contexts as immutable,
        #      e.g. the builtin passlib ones?
        # XXX: add a name or import path for the contexts, to help out repr?
        if schemes is not None:
            kwds['schemes'] = schemes
        if policy is not _UNSET:
            warn("The CryptContext ``policy`` keyword has been deprecated as of Passlib 1.6, "
                 "and will be removed in Passlib 1.8; please use "
                 "``CryptContext.from_string()` or "
                 "``CryptContext.from_path()`` instead.",
                 DeprecationWarning)
            if policy is None:
                self.load(kwds)
            elif isinstance(policy, CryptPolicy):
                self.load(policy._context)
                self.update(kwds)
            else:
                raise TypeError("policy must be a CryptPolicy instance")
        elif _autoload:
            self.load(kwds)
        else:
            assert not kwds, "_autoload=False and kwds are mutually exclusive"

    # XXX: would this be useful?
    ##def __str__(self):
    ##    if PY3:
    ##        return self.to_string()
    ##    else:
    ##        return self.to_string().encode("utf-8")

    def __repr__(self):
        return "<CryptContext at 0x%0x>" % id(self)

    #===================================================================
    # deprecated policy object
    #===================================================================
    def _get_policy(self):
        # The CryptPolicy class has been deprecated, so to support any
        # legacy accesses, we create a stub policy object so .policy attr
        # will continue to work.
        #
        # the code waits until app accesses a specific policy object attribute
        # before issuing deprecation warning, so developer gets method-specific
        # suggestion for how to upgrade.

        # NOTE: making a copy of the context so the policy acts like a snapshot,
        # to retain the pre-1.6 behavior.
        return CryptPolicy(_internal_context=self.copy(), _stub_policy=True)

    def _set_policy(self, policy):
        warn("The CryptPolicy class and the ``context.policy`` attribute have "
             "been deprecated as of Passlib 1.6, and will be removed in "
             "Passlib 1.8; please use the ``context.load()`` and "
             "``context.update()`` methods instead.",
             DeprecationWarning, stacklevel=2)
        if isinstance(policy, CryptPolicy):
            self.load(policy._context)
        else:
            raise TypeError("expected CryptPolicy instance")

    policy = property(_get_policy, _set_policy,
                    doc="[deprecated] returns CryptPolicy instance "
                        "tied to this CryptContext")

    #===================================================================
    # loading / updating configuration
    #===================================================================
    @staticmethod
    def _parse_ini_stream(stream, section, filename):
        """helper read INI from stream, extract passlib section as dict"""
        # NOTE: this expects a unicode stream under py3,
        # and a utf-8 bytes stream under py2,
        # allowing the resulting dict to always use native strings.
        p = SafeConfigParser()
        if PY3:
            # python 3.2 deprecated readfp in favor of read_file
            p.read_file(stream, filename)
        else:
            p.readfp(stream, filename)
        # XXX: could change load() to accept list of items,
        #      and skip intermediate dict creation
        return dict(p.items(section))

    def load_path(self, path, update=False, section="passlib", encoding="utf-8"):
        """Load new configuration into CryptContext from a local file.

        This function is a wrapper for :meth:`load` which
        loads a configuration string from the local file *path*,
        instead of an in-memory source. Its behavior and options
        are otherwise identical to :meth:`!load` when provided with
        an INI-formatted string.

        .. versionadded:: 1.6
        """
        def helper(stream):
            kwds = self._parse_ini_stream(stream, section, path)
            return self.load(kwds, update=update)
        if PY3:
            # decode to unicode, which load() expected under py3
            with open(path, "rt", encoding=encoding) as stream:
                return helper(stream)
        elif encoding in ["utf-8", "ascii"]:
            # keep as utf-8 bytes, which load() expects under py2
            with open(path, "rb") as stream:
                return helper(stream)
        else:
            # transcode to utf-8 bytes
            with open(path, "rb") as fh:
                tmp = fh.read().decode(encoding).encode("utf-8")
                return helper(BytesIO(tmp))

    def load(self, source, update=False, section="passlib", encoding="utf-8"):
        """Load new configuration into CryptContext, replacing existing config.

        :arg source:
            source of new configuration to load.
            this value can be a number of different types:

            * a :class:`!dict` object, or compatible Mapping

                the key/value pairs will be interpreted the same
                keywords for the :class:`CryptContext` class constructor.

            * a :class:`!unicode` or :class:`!bytes` string

                this will be interpreted as an INI-formatted file,
                and appropriate key/value pairs will be loaded from
                the specified *section*.

            * another :class:`!CryptContext` object.

                this will export a snapshot of its configuration
                using :meth:`to_dict`.

        :type update: bool
        :param update:
            By default, :meth:`load` will replace the existing configuration
            entirely. If ``update=True``, it will preserve any existing
            configuration options that are not overridden by the new source,
            much like the :meth:`update` method.

        :type section: str
        :param section:
            When parsing an INI-formatted string, :meth:`load` will look for
            a section named ``"passlib"``. This option allows an alternate
            section name to be used. Ignored when loading from a dictionary.

        :type encoding: str
        :param encoding:
            Encoding to use when decode bytes from string.
            Defaults to ``"utf-8"``. Ignoring when loading from a dictionary.

        :raises TypeError:
            * If the source cannot be identified.
            * If an unknown / malformed keyword is encountered.

        :raises ValueError:
            If an invalid keyword value is encountered.

        .. note::

            If an error occurs during a :meth:`!load` call, the :class:`!CryptContext`
            instance will be restored to the configuration it was in before
            the :meth:`!load` call was made; this is to ensure it is
            *never* left in an inconsistent state due to a load error.

        .. versionadded:: 1.6
        """
        #-----------------------------------------------------------
        # autodetect source type, convert to dict
        #-----------------------------------------------------------
        parse_keys = True
        if isinstance(source, unicode_or_bytes_types):
            if PY3:
                source = to_unicode(source, encoding, param="source")
            else:
                source = to_bytes(source, "utf-8", source_encoding=encoding,
                                  param="source")
            source = self._parse_ini_stream(NativeStringIO(source), section,
                                            "<string passed to CryptContext.load()>")
        elif isinstance(source, CryptContext):
            # extract dict directly from config, so it can be merged later
            source = dict(source._config.iter_config(resolve=True))
            parse_keys = False
        elif not hasattr(source, "items"):
            # mappings are left alone, otherwise throw an error.
            raise ExpectedTypeError(source, "string or dict", "source")

        # XXX: add support for other iterable types, e.g. sequence of pairs?

        #-----------------------------------------------------------
        # parse dict keys into (category, scheme, option) format,
        # and merge with existing configuration if needed.
        #-----------------------------------------------------------
        if parse_keys:
            parse = self._parse_config_key
            source = dict((parse(key), value)
                          for key, value in iteritems(source))
        if update and self._config is not None:
            # if updating, do nothing if source is empty,
            if not source:
                return
            # otherwise overlay source on top of existing config
            tmp = source
            source = dict(self._config.iter_config(resolve=True))
            source.update(tmp)

        #-----------------------------------------------------------
        # compile into _CryptConfig instance, and update state
        #-----------------------------------------------------------
        config = _CryptConfig(source)
        self._config = config
        self.reset_min_verify_time()
        self._get_record = config.get_record
        self._identify_record = config.identify_record
        if config.context_kwds:
            # (re-)enable method for this instance (in case ELSE clause below ran last load).
            self.__dict__.pop("_strip_unused_context_kwds", None)
        else:
            # disable method for this instance, it's not needed.
            self._strip_unused_context_kwds = None

    @staticmethod
    def _parse_config_key(ckey):
        """helper used to parse ``cat__scheme__option`` keys into a tuple"""
        # split string into 1-3 parts
        assert isinstance(ckey, native_string_types)
        parts = ckey.replace(".", "__").split("__")
        count = len(parts)
        if count == 1:
            cat, scheme, key = None, None, parts[0]
        elif count == 2:
            cat = None
            scheme, key = parts
        elif count == 3:
            cat, scheme, key = parts
        else:
            raise TypeError("keys must have less than 3 separators: %r" %
                            (ckey,))
        # validate & normalize the parts
        if cat == "default":
            cat = None
        elif not cat and cat is not None:
            raise TypeError("empty category: %r" % ckey)
        if scheme == "context":
            scheme = None
        elif not scheme and scheme is not None:
            raise TypeError("empty scheme: %r" % ckey)
        if not key:
            raise TypeError("empty option: %r" % ckey)
        return cat, scheme, key

    def update(self, *args, **kwds):
        """Helper for quickly changing configuration.

        This acts much like the :meth:`!dict.update` method:
        it updates the context's configuration,
        replacing the original value(s) for the specified keys,
        and preserving the rest.
        It accepts any :ref:`keyword <context-options>`
        accepted by the :class:`!CryptContext` constructor.

        .. versionadded:: 1.6

        .. seealso:: :meth:`copy`
        """
        if args:
            if len(args) > 1:
                raise TypeError("expected at most one positional argument")
            if kwds:
                raise TypeError("positional arg and keywords mutually exclusive")
            self.load(args[0], update=True)
        elif kwds:
            self.load(kwds, update=True)

    # XXX: make this public? even just as flag to load?
    # FIXME: this function suffered some bitrot in 1.6.1,
    #        will need to be updated before works again.
    ##def _simplify(self):
    ##    "helper to remove redundant/unused options"
    ##    # don't do anything if no schemes are defined
    ##    if not self._schemes:
    ##        return
    ##
    ##    def strip_items(target, filter):
    ##        keys = [key for key,value in iteritems(target)
    ##                if filter(key,value)]
    ##        for key in keys:
    ##            del target[key]
    ##
    ##    # remove redundant default.
    ##    defaults = self._default_schemes
    ##    if defaults.get(None) == self._schemes[0]:
    ##        del defaults[None]
    ##
    ##    # remove options for unused schemes.
    ##    scheme_options = self._scheme_options
    ##    schemes = self._schemes + ("all",)
    ##    strip_items(scheme_options, lambda k,v: k not in schemes)
    ##
    ##    # remove rendundant cat defaults.
    ##    cur = self.default_scheme()
    ##    strip_items(defaults, lambda k,v: k and v==cur)
    ##
    ##    # remove redundant category deprecations.
    ##    # TODO: this should work w/ 'auto', but needs closer inspection
    ##    deprecated = self._deprecated_schemes
    ##    cur = self._deprecated_schemes.get(None)
    ##    strip_items(deprecated, lambda k,v: k and v==cur)
    ##
    ##    # remove redundant category options.
    ##    for scheme, config in iteritems(scheme_options):
    ##        if None in config:
    ##            cur = config[None]
    ##            strip_items(config, lambda k,v: k and v==cur)
    ##
    ##    # XXX: anything else?

    #===================================================================
    # reading configuration
    #===================================================================
    def schemes(self, resolve=False, category=None, unconfigured=False):
        """return schemes loaded into this CryptContext instance.

        :type resolve: bool
        :arg resolve:
            if ``True``, will return a tuple of :class:`~passlib.ifc.PasswordHash`
            objects instead of their names.

        :returns:
            returns tuple of the schemes configured for this context
            via the *schemes* option.

        .. versionadded:: 1.6
            This was previously available as ``CryptContext().policy.schemes()``

        .. seealso:: the :ref:`schemes <context-schemes-option>` option for usage example.
        """
        # XXX: should resolv return records rather than handlers?
        #      or deprecate resolve keyword completely?
        #      offering up a .hashers Mapping in v1.8 would be great.
        # NOTE: supporting 'category' and 'unconfigured' kwds as of 1.7
        #       just to pass through to .handler(), but not documenting them...
        #       may not need to put them to use.
        schemes = self._config.schemes
        if resolve:
            return tuple(self.handler(scheme, category, unconfigured=unconfigured)
                         for scheme in schemes)
        else:
            return schemes

    def default_scheme(self, category=None, resolve=False, unconfigured=False):
        """return name of scheme that :meth:`hash` will use by default.

        :type resolve: bool
        :arg resolve:
            if ``True``, will return a :class:`~passlib.ifc.PasswordHash`
            object instead of the name.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>`.
            If specified, this will return the catgory-specific default scheme instead.

        :returns:
            name of the default scheme.

        .. seealso:: the :ref:`default <context-default-option>` option for usage example.

        .. versionadded:: 1.6

        .. versionchanged:: 1.7

            This now returns a hasher configured with any CryptContext-specific
            options (custom rounds settings, etc).  Previously this returned
            the base hasher from :mod:`passlib.hash`.
        """
        # XXX: deprecate this in favor of .handler() or whatever it's replaced with?
        # NOTE: supporting 'unconfigured' kwds as of 1.7
        #       just to pass through to .handler(), but not documenting them...
        #       may not need to put them to use.
        hasher = self.handler(None, category, unconfigured=unconfigured)
        return hasher if resolve else hasher.name

    # XXX: need to decide if exposing this would be useful in any way
    ##def categories(self):
    ##    """return user-categories with algorithm-specific options in this CryptContext.
    ##
    ##    this will always return a tuple.
    ##    if no categories besides the default category have been configured,
    ##    the tuple will be empty.
    ##    """
    ##    return self._config.categories

    # XXX: need to decide if exposing this would be useful to applications
    # in any meaningful way that isn't already served by to_dict()
    ##def options(self, scheme, category=None):
    ##    kwds, percat = self._config.get_options(scheme, category)
    ##    return kwds

    def handler(self, scheme=None, category=None, unconfigured=False):
        """helper to resolve name of scheme -> :class:`~passlib.ifc.PasswordHash` object used by scheme.

        :arg scheme:
            This should identify the scheme to lookup.
            If omitted or set to ``None``, this will return the handler
            for the default scheme.

        :arg category:
            If a user category is specified, and no scheme is provided,
            it will use the default for that category.
            Otherwise this parameter is ignored.

        :param unconfigured:

            By default, this returns a handler object whose .hash()
            and .needs_update() methods will honor the configured
            provided by CryptContext.   See ``unconfigured=True``
            to get the underlying handler from before any context-specific
            configuration was applied.

        :raises KeyError:
            If the scheme does not exist OR is not being used within this context.

        :returns:
            :class:`~passlib.ifc.PasswordHash` object used to implement
            the named scheme within this context (this will usually
            be one of the objects from :mod:`passlib.hash`)

        .. versionadded:: 1.6
            This was previously available as ``CryptContext().policy.get_handler()``

        .. versionchanged:: 1.7

            This now returns a hasher configured with any CryptContext-specific
            options (custom rounds settings, etc).  Previously this returned
            the base hasher from :mod:`passlib.hash`.
        """
        try:
            hasher = self._get_record(scheme, category)
            if unconfigured:
                return hasher._Context__orig_handler
            else:
                return hasher
        except KeyError:
            pass
        if self._config.handlers:
            raise KeyError("crypt algorithm not found in this "
                           "CryptContext instance: %r" % (scheme,))
        else:
            raise KeyError("no crypt algorithms loaded in this "
                           "CryptContext instance")

    def _get_unregistered_handlers(self):
        """check if any handlers in this context aren't in the global registry"""
        return tuple(handler for handler in self._config.handlers
                     if not _is_handler_registered(handler))

    @property
    def context_kwds(self):
        """
        return :class:`!set` containing union of all :ref:`contextual keywords <context-keywords>`
        supported by the handlers in this context.

        .. versionadded:: 1.6.6
        """
        return self._config.context_kwds

    #===================================================================
    # exporting config
    #===================================================================
    @staticmethod
    def _render_config_key(key):
        """convert 3-part config key to single string"""
        cat, scheme, option = key
        if cat:
            return "%s__%s__%s" % (cat, scheme or "context", option)
        elif scheme:
            return "%s__%s" % (scheme, option)
        else:
            return option

    @staticmethod
    def _render_ini_value(key, value):
        """render value to string suitable for INI file"""
        # convert lists to comma separated lists
        # (mainly 'schemes' & 'deprecated')
        if isinstance(value, (list,tuple)):
            value = ", ".join(value)

        # convert numbers to strings
        elif isinstance(value, num_types):
            if isinstance(value, float) and key[2] == "vary_rounds":
                value = ("%.2f" % value).rstrip("0") if value else "0"
            else:
                value = str(value)

        assert isinstance(value, native_string_types), \
               "expected string for key: %r %r" % (key, value)

        # escape any percent signs.
        return value.replace("%", "%%")

    def to_dict(self, resolve=False):
        """Return current configuration as a dictionary.

        :type resolve: bool
        :arg resolve:
            if ``True``, the ``schemes`` key will contain a list of
            a :class:`~passlib.ifc.PasswordHash` objects instead of just
            their names.

        This method dumps the current configuration of the CryptContext
        instance. The key/value pairs should be in the format accepted
        by the :class:`!CryptContext` class constructor, in fact
        ``CryptContext(**myctx.to_dict())`` will create an exact copy of ``myctx``.
        As an example::

            >>> # you can dump the configuration of any crypt context...
            >>> from passlib.apps import ldap_nocrypt_context
            >>> ldap_nocrypt_context.to_dict()
            {'schemes': ['ldap_salted_sha1',
            'ldap_salted_md5',
            'ldap_sha1',
            'ldap_md5',
            'ldap_plaintext']}

        .. versionadded:: 1.6
            This was previously available as ``CryptContext().policy.to_dict()``

        .. seealso:: the :ref:`context-serialization-example` example in the tutorial.
        """
        # XXX: should resolve default to conditional behavior
        # based on presence of unregistered handlers?
        render_key = self._render_config_key
        return dict((render_key(key), value)
                    for key, value in self._config.iter_config(resolve))

    def _write_to_parser(self, parser, section):
        """helper to write to ConfigParser instance"""
        render_key = self._render_config_key
        render_value = self._render_ini_value
        parser.add_section(section)
        for k,v in self._config.iter_config():
            v = render_value(k, v)
            k = render_key(k)
            parser.set(section, k, v)

    def to_string(self, section="passlib"):
        """serialize to INI format and return as unicode string.

        :param section:
            name of INI section to output, defaults to ``"passlib"``.

        :returns:
            CryptContext configuration, serialized to a INI unicode string.

        This function acts exactly like :meth:`to_dict`, except that it
        serializes all the contents into a single human-readable string,
        which can be hand edited, and/or stored in a file. The
        output of this method is accepted by :meth:`from_string`,
        :meth:`from_path`, and :meth:`load`. As an example::

            >>> # you can dump the configuration of any crypt context...
            >>> from passlib.apps import ldap_nocrypt_context
            >>> print ldap_nocrypt_context.to_string()
            [passlib]
            schemes = ldap_salted_sha1, ldap_salted_md5, ldap_sha1, ldap_md5, ldap_plaintext

        .. versionadded:: 1.6
            This was previously available as ``CryptContext().policy.to_string()``

        .. seealso:: the :ref:`context-serialization-example` example in the tutorial.
        """
        parser = SafeConfigParser()
        self._write_to_parser(parser, section)
        buf = NativeStringIO()
        parser.write(buf)
        unregistered = self._get_unregistered_handlers()
        if unregistered:
            buf.write((
                "# NOTE: the %s handler(s) are not registered with Passlib,\n"
                "# this string may not correctly reproduce the current configuration.\n\n"
                ) % ", ".join(repr(handler.name) for handler in unregistered))
        out = buf.getvalue()
        if not PY3:
            out = out.decode("utf-8")
        return out

    # XXX: is this useful enough to enable?
    ##def write_to_path(self, path, section="passlib", update=False):
    ##    "write to INI file"
    ##    parser = ConfigParser()
    ##    if update and os.path.exists(path):
    ##        if not parser.read([path]):
    ##            raise EnvironmentError("failed to read existing file")
    ##        parser.remove_section(section)
    ##    self._write_to_parser(parser, section)
    ##    fh = file(path, "w")
    ##    parser.write(fh)
    ##    fh.close()

    #===================================================================
    # verify() hardening
    #===================================================================

    # NOTE: the estimation is currently algorithm is a little rough, so
    #       the control values are exposed here to make "poking" at them easier.

    #: maximum samples to take when estimating min_verify_time
    mvt_estimate_max_samples = 10

    #: minimum samples to take when estimating min_verify_time
    mvt_estimate_min_samples = 4

    #: maximum time to spend estimating min_verify_time
    #: (this value is overridden by min_samples)
    mvt_estimate_max_time = 1.2

    #: minimum measurement resolution required by estimate
    mvt_estimate_resolution = 0.05

    # XXX: make writable (once CryptPolicy is removed)?
    @memoized_property
    def harden_verify(self):
        return self._config.get_context_option_with_flag(None, "harden_verify")[0]

    #: global lock used to prevent multiple copies of _calc_min_verify_time()
    #: from running at the same time (whether as part of same context or not);
    #: as this would cause inaccurate measurements
    _mvt_lock = threading.Lock()

    # XXX: how to handle multiple categories? admin cateogry would stand out.
    #      but dont' want multiple levels of min_verify_time, *right*?
    #      maybe want to have CryptContext switch into a "nested" mode
    #      if categories are put in place, and have it act like multiple contexts.

    @memoized_property
    def min_verify_time(self):
        """
        minimum time verify() should take, to mask presence of weak hashes.
        when first accessed, an estimate is performed based on
        how long default hash takes.
        can be overridden by manually writing to this attribute.

        will default to 0 (no estimate performed) unless 'harden_verify = true'
        passed in CryptContext config.
        """
        with self._mvt_lock:
            # check if value was set in another thread
            value = type(self).min_verify_time.peek_cache(self)
            if value is None:
                # value wasn't set, use calc function
                value = self._calc_min_verify_time()
            return value

    def _calc_min_verify_time(self):
        """
        calculate min_verify_time based on system performance.

        .. warning::
            this assumes caller has acquired :attr:`_mvt_lock`

        :return:
            estimated min_verify_time value
        """
        # load config
        log.debug("estimating min_verify_time")
        min_samples = self.mvt_estimate_min_samples
        max_samples = self.mvt_estimate_max_samples
        record = self._get_record(None, None)
        repeat = 1

        # generate random secret to test against,
        # and generate sample hash
        secret = getrandstr(rng, BASE64_CHARS, 16)
        start = timer()
        hash = record.hash(secret)
        samples = [timer() - start]

        # gather samples until condition met
        loop_end = start + self.mvt_estimate_max_time
        while True:
            # gather sample
            start = timer()
            for _ in irange(repeat):
                # XXX: using record.verify() instead of self.verify()
                #      since that would cause recursion errors back to here
                #      (and we can't temporarily set .min_verify_time=0
                #      without temporarily letting other threads through
                #      w/o any delay). presuming there's not a noticeable
                #      overhead for the CryptContext.verify() wrapper.
                record.verify(secret, hash)
            end = timer()
            elapsed = end - start

            # make sure we're far enough above timer's minimum resolution
            if elapsed < self.mvt_estimate_resolution:
                repeat *= 2
                continue
            samples.append(elapsed / repeat)

            # stop as soon as possible if we have plenty of samples
            if len(samples) > max_samples:
                break

            # otherwise stop after max time, as long as we have bare minimum.
            if end > loop_end and len(samples) > min_samples:
                break

        # calc median, to cheaply exclude outliers
        samples.sort()
        result = round(samples[(len(samples)+1)//2], 3)
        log.debug("setting min_verify_time=%f (median of %d samples)",
                  result, len(samples))
        return result

    def reset_min_verify_time(self):
        """
        clear min_verify_time estimate,
        will be recalculated next time :attr:`min_verify_time` is accessed
        (i.e. when :meth:`verify` is called).
        """
        type(self).harden_verify.clear_cache(self)
        type(self).min_verify_time.clear_cache(self)

    def dummy_verify(self, elapsed=0):
        """
        Helper that applications can call when user wasn't found,
        in order to simulate time it would take to hash a password.

        Invokes :func:`time.sleep` for amount of time needed to make
        total elapsed time >= :attr:`min_verify_time`.

        :param elapsed:
            optional amount of time spent hashing so far
            (mainly used internally by :meth:`verify` and :meth:`verify_and_update`).

        See :ref:`harden_verify <context-harden-verify-option>` for details
        about this feature.

        .. versionadded:: 1.7
        """
        assert elapsed >= 0
        remaining = self.min_verify_time - elapsed
        if remaining > 0:
            time.sleep(remaining)

    #===================================================================
    # password hash api
    #===================================================================

    # NOTE: all the following methods do is look up the appropriate
    #       custom handler for a given (scheme,category) combination,
    #       and hand off the real work to the handler itself,
    #       which is optimized for the specific (scheme,category) configuration.
    #
    #       The custom handlers are cached inside the _CryptConfig
    #       instance stored in self._config, and are retrieved
    #       via get_record() and identify_record().
    #
    #       _get_record() and _identify_record() are references
    #       to _config methods of the same name,
    #       stored in CryptContext for speed.

    def _get_or_identify_record(self, hash, scheme=None, category=None):
        """return record based on scheme, or failing that, by identifying hash"""
        if scheme:
            if not isinstance(hash, unicode_or_bytes_types):
                raise ExpectedStringError(hash, "hash")
            return self._get_record(scheme, category)
        else:
            # hash typecheck handled by identify_record()
            return self._identify_record(hash, category)

    def _strip_unused_context_kwds(self, kwds, record):
        """
        helper which removes any context keywords from **kwds**
        that are known to be used by another scheme in this context,
        but are NOT supported by handler specified by **record**.

        .. note::
            as optimization, load() will set this method to None on a per-instance basis
            if there are no context kwds.
        """
        if not kwds:
            return
        unused_kwds = self._config.context_kwds.difference(record.context_kwds)
        for key in unused_kwds:
            kwds.pop(key, None)

    def needs_update(self, hash, scheme=None, category=None, secret=None):
        """Check if hash needs to be replaced for some reason,
        in which case the secret should be re-hashed.

        This function is the core of CryptContext's support for hash migration:
        This function takes in a hash string, and checks the scheme,
        number of rounds, and other properties against the current policy.
        It returns ``True`` if the hash is using a deprecated scheme,
        or is otherwise outside of the bounds specified by the policy
        (e.g. the number of rounds is lower than :ref:`min_rounds <context-min-rounds-option>`
        configuration for that algorithm).
        If so, the password should be re-hashed using :meth:`hash`
        Otherwise, it will return ``False``.

        :type hash: unicode or bytes
        :arg hash:
            The hash string to examine.

        :type scheme: str or None
        :param scheme:

            Optional scheme to use. Scheme must be one of the ones
            configured for this context (see the
            :ref:`schemes <context-schemes-option>` option).
            If no scheme is specified, it will be identified
            based on the value of *hash*.

            .. deprecated:: 1.7

                Support for this keyword is deprecated, and will be removed in Passlib 2.0.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>`.
            If specified, this will cause any category-specific defaults to
            be used when determining if the hash needs to be updated
            (e.g. is below the minimum rounds).

        :type secret: unicode, bytes, or None
        :param secret:
            Optional secret associated with the provided ``hash``.
            This is not required, or even currently used for anything...
            it's for forward-compatibility with any future
            update checks that might need this information.
            If provided, Passlib assumes the secret has already been
            verified successfully against the hash.

            .. versionadded:: 1.6

        :returns: ``True`` if hash should be replaced, otherwise ``False``.

        :raises ValueError:
            If the hash did not match any of the configured :meth:`schemes`.

        .. versionadded:: 1.6
            This method was previously named :meth:`hash_needs_update`.

        .. seealso:: the :ref:`context-migration-example` example in the tutorial.
        """
        if scheme is not None:
            # TODO: offer replacement alternative.
            #       ``context.handler(scheme).needs_update()`` would work,
            #       but may deprecate .handler() in passlib 1.8.
            warn("CryptContext.needs_update(): 'scheme' keyword is deprecated as of "
                 "Passlib 1.7, and will be removed in Passlib 2.0",
                 DeprecationWarning)
        record = self._get_or_identify_record(hash, scheme, category)
        return record.deprecated or record.needs_update(hash, secret=secret)

    @deprecated_method(deprecated="1.6", removed="2.0", replacement="CryptContext.needs_update()")
    def hash_needs_update(self, hash, scheme=None, category=None):
        """Legacy alias for :meth:`needs_update`.

        .. deprecated:: 1.6
            This method was renamed to :meth:`!needs_update` in version 1.6.
            This alias will be removed in version 2.0, and should only
            be used for compatibility with Passlib 1.3 - 1.5.
        """
        return self.needs_update(hash, scheme, category)

    @deprecated_method(deprecated="1.7", removed="2.0")
    def genconfig(self, scheme=None, category=None, **settings):
        """Generate a config string for specified scheme.

        .. deprecated:: 1.7

            This method will be removed in version 2.0, and should only
            be used for compatibility with Passlib 1.3 - 1.6.
        """
        record = self._get_record(scheme, category)
        strip_unused = self._strip_unused_context_kwds
        if strip_unused:
            strip_unused(settings, record)
        return record.genconfig(**settings)

    @deprecated_method(deprecated="1.7", removed="2.0")
    def genhash(self, secret, config, scheme=None, category=None, **kwds):
        """Generate hash for the specified secret using another hash.

        .. deprecated:: 1.7

            This method will be removed in version 2.0, and should only
            be used for compatibility with Passlib 1.3 - 1.6.
        """
        record = self._get_or_identify_record(config, scheme, category)
        strip_unused = self._strip_unused_context_kwds
        if strip_unused:
            strip_unused(kwds, record)
        return record.genhash(secret, config, **kwds)

    def identify(self, hash, category=None, resolve=False, required=False,
                 unconfigured=False):
        """Attempt to identify which algorithm the hash belongs to.

        Note that this will only consider the algorithms
        currently configured for this context
        (see the :ref:`schemes <context-schemes-option>` option).
        All registered algorithms will be checked, from first to last,
        and whichever one positively identifies the hash first will be returned.

        :type hash: unicode or bytes
        :arg hash:
            The hash string to test.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>`.
            Ignored by this function, this parameter
            is provided for symmetry with the other methods.

        :type resolve: bool
        :param resolve:
            If ``True``, returns the hash handler itself,
            instead of the name of the hash.

        :type required: bool
        :param required:
            If ``True``, this will raise a ValueError if the hash
            cannot be identified, instead of returning ``None``.

        :returns:
            The handler which first identifies the hash,
            or ``None`` if none of the algorithms identify the hash.
        """
        record = self._identify_record(hash, category, required)
        if record is None:
            return None
        elif resolve:
            if unconfigured:
                return record._Context__orig_handler
            else:
                return record
        else:
            return record.name

    def hash(self, secret, scheme=None, category=None, **kwds):
        """run secret through selected algorithm, returning resulting hash.

        :type secret: unicode or bytes
        :arg secret:
            the password to hash.

        :type scheme: str or None
        :param scheme:

            Optional scheme to use. Scheme must be one of the ones
            configured for this context (see the
            :ref:`schemes <context-schemes-option>` option).
            If no scheme is specified, the configured default
            will be used.

            .. deprecated:: 1.7

                Support for this keyword is deprecated, and will be removed in Passlib 2.0.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>`.
            If specified, this will cause any category-specific defaults to
            be used when hashing the password (e.g. different default scheme,
            different default rounds values, etc).

        :param \*\*kwds:
            All other keyword options are passed to the selected algorithm's
            :meth:`PasswordHash.hash() <passlib.ifc.PasswordHash.hash>` method.

        :returns:
            The secret as encoded by the specified algorithm and options.
            The return value will always be a :class:`!str`.

        :raises TypeError, ValueError:
            * If any of the arguments have an invalid type or value.
              This includes any keywords passed to the underlying hash's
              :meth:`PasswordHash.hash() <passlib.ifc.PasswordHash.hash>` method.

        .. seealso:: the :ref:`context-basic-example` example in the tutorial
        """
        # XXX: could insert normalization to preferred unicode encoding here
        if scheme is not None:
            # TODO: offer replacement alternative.
            #       ``context.handler(scheme).hash()`` would work,
            #       but may deprecate .handler() in passlib 1.8.
            warn("CryptContext.hash(): 'scheme' keyword is deprecated as of "
                 "Passlib 1.7, and will be removed in Passlib 2.0",
                 DeprecationWarning)
        record = self._get_record(scheme, category)
        strip_unused = self._strip_unused_context_kwds
        if strip_unused:
            strip_unused(kwds, record)
        return record.hash(secret, **kwds)

    @deprecated_method(deprecated="1.7", removed="2.0", replacement="CryptContext.hash()")
    def encrypt(self, *args, **kwds):
        """
        Legacy alias for :meth:`hash`.

        .. deprecated:: 1.7
            This method was renamed to :meth:`!hash` in version 1.7.
            This alias will be removed in version 2.0, and should only
            be used for compatibility with Passlib 1.3 - 1.6.
        """
        return self.hash(*args, **kwds)

    def verify(self, secret, hash, scheme=None, category=None, **kwds):
        """verify secret against an existing hash.

        If no scheme is specified, this will attempt to identify
        the scheme based on the contents of the provided hash
        (limited to the schemes configured for this context).
        It will then check whether the password verifies against the hash.

        :type secret: unicode or bytes
        :arg secret:
            the secret to verify

        :type hash: unicode or bytes
        :arg hash:
            hash string to compare to

            if ``None`` is passed in, this will be treated as "never verifying"

        :type scheme: str
        :param scheme:
            Optionally force context to use specific scheme.
            This is usually not needed, as most hashes can be unambiguously
            identified. Scheme must be one of the ones configured
            for this context
            (see the :ref:`schemes <context-schemes-option>` option).

            .. deprecated:: 1.7

                Support for this keyword is deprecated, and will be removed in Passlib 2.0.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>` string.
            This is mainly used when generating new hashes, it has little
            effect when verifying; this keyword is mainly provided for symmetry.

        :param \*\*kwds:
            All additional keywords are passed to the appropriate handler,
            and should match its :attr:`~passlib.ifc.PasswordHash.context_kwds`.

        :returns:
            ``True`` if the password matched the hash, else ``False``.

        :raises ValueError:
            * if the hash did not match any of the configured :meth:`schemes`.

            * if any of the arguments have an invalid value (this includes
              any keywords passed to the underlying hash's
              :meth:`PasswordHash.verify() <passlib.ifc.PasswordHash.verify>` method).

        :raises TypeError:
            * if any of the arguments have an invalid type (this includes
              any keywords passed to the underlying hash's
              :meth:`PasswordHash.verify() <passlib.ifc.PasswordHash.verify>` method).

        .. seealso:: the :ref:`context-basic-example` example in the tutorial
        """
        # XXX: could insert normalization to preferred unicode encoding here
        # XXX: what about supporting a setter() callback ala django 1.4 ?
        if scheme is not None:
            # TODO: offer replacement alternative.
            #       ``context.handler(scheme).verify()`` would work,
            #       but may deprecate .handler() in passlib 1.8.
            warn("CryptContext.verify(): 'scheme' keyword is deprecated as of "
                 "Passlib 1.7, and will be removed in Passlib 2.0",
                 DeprecationWarning)
        if hash is None:
            # convenience feature -- let apps pass in hash=None when user
            # isn't found / has no hash; mainly to get dummy_verify() benefit.
            if self.harden_verify:
                self.dummy_verify()
            return False
        record = self._get_or_identify_record(hash, scheme, category)
        strip_unused = self._strip_unused_context_kwds
        if strip_unused:
            strip_unused(kwds, record)
        start = timer()
        ok = record.verify(secret, hash, **kwds)
        if not ok and self.harden_verify:
            self.dummy_verify(timer() - start)
        return ok

    def verify_and_update(self, secret, hash, scheme=None, category=None, **kwds):
        """verify password and re-hash the password if needed, all in a single call.

        This is a convenience method which takes care of all the following:
        first it verifies the password (:meth:`~CryptContext.verify`), if this is successfull
        it checks if the hash needs updating (:meth:`~CryptContext.needs_update`), and if so,
        re-hashes the password (:meth:`~CryptContext.hash`), returning the replacement hash.
        This series of steps is a very common task for applications
        which wish to update deprecated hashes, and this call takes
        care of all 3 steps efficiently.

        :type secret: unicode or bytes
        :arg secret:
            the secret to verify

        :type secret: unicode or bytes
        :arg hash:
            hash string to compare to.

            if ``None`` is passed in, this will be treated as "never verifying"

        :type scheme: str
        :param scheme:
            Optionally force context to use specific scheme.
            This is usually not needed, as most hashes can be unambiguously
            identified. Scheme must be one of the ones configured
            for this context
            (see the :ref:`schemes <context-schemes-option>` option).

            .. deprecated:: 1.7

                Support for this keyword is deprecated, and will be removed in Passlib 2.0.

        :type category: str or None
        :param category:
            Optional :ref:`user category <user-categories>`.
            If specified, this will cause any category-specific defaults to
            be used if the password has to be re-hashed.

        :param \*\*kwds:
            all additional keywords are passed to the appropriate handler,
            and should match that hash's
            :attr:`PasswordHash.context_kwds <passlib.ifc.PasswordHash.context_kwds>`.

        :returns:
            This function returns a tuple containing two elements:
            ``(verified, replacement_hash)``. The first is a boolean
            flag indicating whether the password verified,
            and the second an optional replacement hash.
            The tuple will always match one of the following 3 cases:

            * ``(False, None)`` indicates the secret failed to verify.
            * ``(True, None)`` indicates the secret verified correctly,
              and the hash does not need updating.
            * ``(True, str)`` indicates the secret verified correctly,
              but the current hash needs to be updated. The :class:`!str`
              will be the freshly generated hash, to replace the old one.

        :raises TypeError, ValueError:
            For the same reasons as :meth:`verify`.

        .. seealso:: the :ref:`context-migration-example` example in the tutorial.
        """
        # XXX: could insert normalization to preferred unicode encoding here.
        if scheme is not None:
            warn("CryptContext.verify(): 'scheme' keyword is deprecated as of "
                 "Passlib 1.7, and will be removed in Passlib 2.0",
                 DeprecationWarning)
        if hash is None:
            # convenience feature -- let apps pass in hash=None when user
            # isn't found / has no hash; mainly to get dummy_verify() benefit.
            if self.harden_verify:
                self.dummy_verify()
            return False, None
        record = self._get_or_identify_record(hash, scheme, category)
        strip_unused = self._strip_unused_context_kwds
        if strip_unused and kwds:
            clean_kwds = kwds.copy()
            strip_unused(clean_kwds, record)
        else:
            clean_kwds = kwds
        # XXX: if record is default scheme, could extend PasswordHash
        #      api to combine verify & needs_update to single call,
        #      potentially saving some round-trip parsing.
        #      but might make these codepaths more complex...
        start = timer()
        if not record.verify(secret, hash, **clean_kwds):
            if self.harden_verify:
                self.dummy_verify(timer() - start)
            return False, None
        elif record.deprecated or record.needs_update(hash, secret=secret):
            # NOTE: we re-hash with default scheme, not current one.
            return True, self.hash(secret, category=category, **kwds)
        else:
            return True, None

    #===================================================================
    # disabled hash support
    #===================================================================

    def is_enabled(self, hash):
        """
        test if hash represents a usuable password --
        i.e. does not represent an unusuable password such as ``"!"``,
        which is recognized by the :class:`~passlib.hash.unix_disabled` hash.

        :raises ValueError:
            if the hash is not recognized
            (typically solved by adding ``unix_disabled`` to the list of schemes).
        """
        return not self._identify_record(hash, None).is_disabled

    def disable(self, hash=None):
        """
        return a string to disable logins for user,
        usually by returning a non-verifying string such as ``"!"``.

        :param hash:
            Callers can optionally provide the account's existing hash.
            Some disabled handlers (such as :class:`!unix_disabled`)
            will encode this into the returned value,
            so that it can be recovered via :meth:`enable`.

        :raises RuntimeError:
            if this function is called w/o a disabled hasher
            (such as :class:`~passlib.hash.unix_disabled`) included
            in the list of schemes.

        :returns:
            hash string which will be recognized as valid by the context,
            but is guaranteed to not validate against *any* password.
        """
        record = self._config.disabled_record
        assert record.is_disabled
        return record.disable(hash)

    def enable(self, hash):
        """
        inverse of :meth:`disable` --
        attempts to recover original hash which was converted
        by a :meth:`!disable` call into a disabled hash --
        thus restoring the user's original password.

        :raises ValueError:
            if original hash not present, or if the disabled handler doesn't
            support encoding the original hash (e.g. ``django_disabled``)

        :returns:
            the original hash.
        """
        record = self._identify_record(hash, None)
        if record.is_disabled:
            # XXX: should we throw error if result can't be identified by context?
            return record.enable(hash)
        else:
            # hash wasn't a disabled hash, so return unchanged
            return hash

    #===================================================================
    # eoc
    #===================================================================

class LazyCryptContext(CryptContext):
    """CryptContext subclass which doesn't load handlers until needed.

    This is a subclass of CryptContext which takes in a set of arguments
    exactly like CryptContext, but won't import any handlers
    (or even parse its arguments) until
    the first time one of its methods is accessed.

    :arg schemes:
        The first positional argument can be a list of schemes, or omitted,
        just like CryptContext.

    :param onload:

        If a callable is passed in via this keyword,
        it will be invoked at lazy-load time
        with the following signature:
        ``onload(**kwds) -> kwds``;
        where ``kwds`` is all the additional kwds passed to LazyCryptContext.
        It should perform any additional deferred initialization,
        and return the final dict of options to be passed to CryptContext.

        .. versionadded:: 1.6

    :param create_policy:

        .. deprecated:: 1.6
            This option will be removed in Passlib 1.8,
            applications should use ``onload`` instead.

    :param kwds:

        All additional keywords are passed to CryptContext;
        or to the *onload* function (if provided).

    This is mainly used internally by modules such as :mod:`passlib.apps`,
    which define a large number of contexts, but only a few of them will be needed
    at any one time. Use of this class saves the memory needed to import
    the specified handlers until the context instance is actually accessed.
    As well, it allows constructing a context at *module-init* time,
    but using :func:`!onload()` to provide dynamic configuration
    at *application-run* time.

    .. note:: 
        This class is only useful if you're referencing handler objects by name,
        and don't want them imported until runtime. If you want to have the config
        validated before your application runs, or are passing in already-imported
        handler instances, you should use :class:`CryptContext` instead.

    .. versionadded:: 1.4
    """
    _lazy_kwds = None

    # NOTE: the way this class works changed in 1.6.
    #       previously it just called _lazy_init() when ``.policy`` was
    #       first accessed. now that is done whenever any of the public
    #       attributes are accessed, and the class itself is changed
    #       to a regular CryptContext, to remove the overhead once it's unneeded.

    def __init__(self, schemes=None, **kwds):
        if schemes is not None:
            kwds['schemes'] = schemes
        self._lazy_kwds = kwds

    def _lazy_init(self):
        kwds = self._lazy_kwds
        if 'create_policy' in kwds:
            warn("The CryptPolicy class, and LazyCryptContext's "
                 "``create_policy`` keyword have been deprecated as of "
                 "Passlib 1.6, and will be removed in Passlib 1.8; "
                 "please use the ``onload`` keyword instead.",
                 DeprecationWarning)
            create_policy = kwds.pop("create_policy")
            result = create_policy(**kwds)
            policy = CryptPolicy.from_source(result, _warn=False)
            kwds = policy._context.to_dict()
        elif 'onload' in kwds:
            onload = kwds.pop("onload")
            kwds = onload(**kwds)
        del self._lazy_kwds
        super(LazyCryptContext, self).__init__(**kwds)
        self.__class__ = CryptContext

    def __getattribute__(self, attr):
        if (not attr.startswith("_") or attr.startswith("__")) and \
            self._lazy_kwds is not None:
                self._lazy_init()
        return object.__getattribute__(self, attr)

#=============================================================================
# eof
#=============================================================================
