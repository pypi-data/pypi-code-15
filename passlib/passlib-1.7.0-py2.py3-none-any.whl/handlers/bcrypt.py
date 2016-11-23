"""passlib.bcrypt -- implementation of OpenBSD's BCrypt algorithm.

TODO:

* support 2x and altered-2a hashes?
  http://www.openwall.com/lists/oss-security/2011/06/27/9

* deal with lack of PY3-compatibile c-ext implementation
"""
#=============================================================================
# imports
#=============================================================================
from __future__ import with_statement, absolute_import
# core
from base64 import b64encode
from hashlib import sha256
import os
import re
import logging; log = logging.getLogger(__name__)
from warnings import warn
# site
_bcrypt = None # dynamically imported by _load_backend_bcrypt()
_pybcrypt = None # dynamically imported by _load_backend_pybcrypt()
_bcryptor = None # dynamically imported by _load_backend_bcryptor()
# pkg
_builtin_bcrypt = None  # dynamically imported by _load_backend_builtin()
from passlib.exc import PasslibHashWarning, PasslibSecurityWarning, PasslibSecurityError
from passlib.utils import safe_crypt, repeat_string, to_bytes, parse_version, \
                          rng, getrandstr, test_crypt, to_unicode
from passlib.utils.binary import bcrypt64
from passlib.utils.compat import u, uascii_to_str, unicode, str_to_uascii
import passlib.utils.handlers as uh

# local
__all__ = [
    "bcrypt",
]

#=============================================================================
# support funcs & constants
#=============================================================================
IDENT_2 = u("$2$")
IDENT_2A = u("$2a$")
IDENT_2X = u("$2x$")
IDENT_2Y = u("$2y$")
IDENT_2B = u("$2b$")
_BNULL = b'\x00'

# reference hash of "test", used in various self-checks
TEST_HASH_2A = b"$2a$04$5BJqKfqMQvV7nS.yUguNcueVirQqDBGaLXSqj.rs.pZPlNR0UX/HK"

def _detect_pybcrypt():
    """
    internal helper which tries to distinguish pybcrypt vs bcrypt.

    :returns:
        True if cext-based py-bcrypt,
        False if ffi-based bcrypt,
        None if 'bcrypt' module not found.

    .. versionchanged:: 1.6.3

        Now assuming bcrypt installed, unless py-bcrypt explicitly detected.
        Previous releases assumed py-bcrypt by default.

        Making this change since py-bcrypt is (apparently) unmaintained and static,
        whereas bcrypt is being actively maintained, and it's internal structure may shift.
    """
    # NOTE: this is also used by the unittests.

    # check for module.
    try:
        import bcrypt
    except ImportError:
        return None

    # py-bcrypt has a "._bcrypt.__version__" attribute (confirmed for v0.1 - 0.4),
    # which bcrypt lacks (confirmed for v1.0 - 2.0)
    # "._bcrypt" alone isn't sufficient, since bcrypt 2.0 now has that attribute.
    try:
        from bcrypt._bcrypt import __version__
    except ImportError:
        return False
    return True

#=============================================================================
# backend mixins
#=============================================================================
class _BcryptCommon(uh.SubclassBackendMixin, uh.TruncateMixin, uh.HasManyIdents,
                    uh.HasRounds, uh.HasSalt, uh.GenericHandler):
    """
    Base class which implements brunt of BCrypt code.
    This is then subclassed by the various backends,
    to override w/ backend-specific methods.

    When a backend is loaded, the bases of the 'bcrypt' class proper
    are modified to prepend the correct backend-specific subclass.
    """
    #===================================================================
    # class attrs
    #===================================================================

    #--------------------
    # PasswordHash
    #--------------------
    name = "bcrypt"
    setting_kwds = ("salt", "rounds", "ident", "truncate_error")

    #--------------------
    # GenericHandler
    #--------------------
    checksum_size = 31
    checksum_chars = bcrypt64.charmap

    #--------------------
    # HasManyIdents
    #--------------------
    default_ident = IDENT_2B
    ident_values = (IDENT_2, IDENT_2A, IDENT_2X, IDENT_2Y, IDENT_2B)
    ident_aliases = {u("2"): IDENT_2, u("2a"): IDENT_2A,  u("2y"): IDENT_2Y,
                     u("2b"): IDENT_2B}

    #--------------------
    # HasSalt
    #--------------------
    min_salt_size = max_salt_size = 22
    salt_chars = bcrypt64.charmap
        # NOTE: 22nd salt char must be in bcrypt64._padinfo2[1], not full charmap

    #--------------------
    # HasRounds
    #--------------------
    default_rounds = 12 # current passlib default
    min_rounds = 4 # minimum from bcrypt specification
    max_rounds = 31 # 32-bit integer limit (since real_rounds=1<<rounds)
    rounds_cost = "log2"

    #--------------------
    # TruncateMixin
    #--------------------
    truncate_size = 72

    #--------------------
    # custom
    #--------------------

    # backend workaround detection flags
    # NOTE: these are only set on the backend mixin classes
    _workrounds_initialized = False
    _has_2a_wraparound_bug = False
    _lacks_20_support = False
    _lacks_2y_support = False
    _lacks_2b_support = False
    _fallback_ident = IDENT_2A

    #===================================================================
    # formatting
    #===================================================================

    @classmethod
    def from_string(cls, hash):
        ident, tail = cls._parse_ident(hash)
        if ident == IDENT_2X:
            raise ValueError("crypt_blowfish's buggy '2x' hashes are not "
                             "currently supported")
        rounds_str, data = tail.split(u("$"))
        rounds = int(rounds_str)
        if rounds_str != u('%02d') % (rounds,):
            raise uh.exc.MalformedHashError(cls, "malformed cost field")
        salt, chk = data[:22], data[22:]
        return cls(
            rounds=rounds,
            salt=salt,
            checksum=chk or None,
            ident=ident,
        )

    def to_string(self):
        hash = u("%s%02d$%s%s") % (self.ident, self.rounds, self.salt, self.checksum)
        return uascii_to_str(hash)

    # NOTE: this should be kept separate from to_string()
    #       so that bcrypt_sha256() can still use it, while overriding to_string()
    def _get_config(self, ident):
        """internal helper to prepare config string for backends"""
        config = u("%s%02d$%s") % (ident, self.rounds, self.salt)
        return uascii_to_str(config)

    #===================================================================
    # migration
    #===================================================================

    @classmethod
    def needs_update(cls, hash, **kwds):
        # check for incorrect padding bits (passlib issue 25)
        if isinstance(hash, bytes):
            hash = hash.decode("ascii")
        if hash.startswith(IDENT_2A) and hash[28] not in bcrypt64._padinfo2[1]:
            return True

        # TODO: try to detect incorrect 8bit/wraparound hashes using kwds.get("secret")

        # hand off to base implementation, so HasRounds can check rounds value.
        return super(_BcryptCommon, cls).needs_update(hash, **kwds)

    #===================================================================
    # specialized salt generation - fixes passlib issue 25
    #===================================================================

    @classmethod
    def normhash(cls, hash):
        """helper to normalize hash, correcting any bcrypt padding bits"""
        if cls.identify(hash):
            return cls.from_string(hash).to_string()
        else:
            return hash

    @classmethod
    def _generate_salt(cls):
        # generate random salt as normal,
        # but repair last char so the padding bits always decode to zero.
        salt = super(_BcryptCommon, cls)._generate_salt()
        return bcrypt64.repair_unused(salt)

    @classmethod
    def _norm_salt(cls, salt, **kwds):
        salt = super(_BcryptCommon, cls)._norm_salt(salt, **kwds)
        assert salt is not None, "HasSalt didn't generate new salt!"
        changed, salt = bcrypt64.check_repair_unused(salt)
        if changed:
            # FIXME: if salt was provided by user, this message won't be
            # correct. not sure if we want to throw error, or use different warning.
            warn(
                "encountered a bcrypt salt with incorrectly set padding bits; "
                "you may want to use bcrypt.normhash() "
                "to fix this; this will be an error under Passlib 2.0",
                PasslibHashWarning)
        return salt

    def _norm_checksum(self, checksum, relaxed=False):
        checksum = super(_BcryptCommon, self)._norm_checksum(checksum, relaxed=relaxed)
        changed, checksum = bcrypt64.check_repair_unused(checksum)
        if changed:
            warn(
                "encountered a bcrypt hash with incorrectly set padding bits; "
                "you may want to use bcrypt.normhash() "
                "to fix this; this will be an error under Passlib 2.0",
                PasslibHashWarning)
        return checksum

    #===================================================================
    # backend configuration
    # NOTE: backends are defined in terms of mixin classes,
    #       which are dynamically inserted into the bases of the 'bcrypt' class
    #       via the machinery in 'SubclassBackendMixin'.
    #       this lets us load in a backend-specific implementation
    #       of _calc_checksum() and similar methods.
    #===================================================================

    # NOTE: backend config is located down in <bcrypt> class

    # NOTE: set_backend() will execute the ._load_backend_mixin()
    #       of the matching mixin class, which will handle backend detection

    # appended to HasManyBackends' "no backends available" error message
    _no_backend_suggestion = " -- recommend you install one (e.g. 'pip install bcrypt')"

    @classmethod
    def _finalize_backend_mixin(mixin_cls, backend, dryrun):
        """
        helper called by from backend mixin classes' _load_backend_mixin() --
        invoked after backend imports have been loaded, and performs
        feature detection & testing common to all backends.
        """
        #----------------------------------------------------------------
        # setup helpers
        #----------------------------------------------------------------
        assert mixin_cls is bcrypt._backend_mixin_map[backend], \
            "_configure_workarounds() invoked from wrong class"

        if mixin_cls._workrounds_initialized:
            return True

        verify = mixin_cls.verify

        err_types = (ValueError,)
        if _bcryptor:
            err_types += (_bcryptor.engine.SaltError,)

        def safe_verify(secret, hash):
            """verify() wrapper which traps 'unknown identifier' errors"""
            try:
                return verify(secret, hash)
            except err_types:
                # backends without support for given ident will throw various
                # errors about unrecognized version:
                #   pybcrypt, bcrypt -- raises ValueError
                #   bcryptor -- raises bcryptor.engine.SaltError
                return NotImplemented
            except AssertionError as err:
                # _calc_checksum() code may also throw AssertionError
                # if correct hash isn't returned (e.g. 2y hash converted to 2b,
                # such as happens with bcrypt 3.0.0)
                log.debug("trapped unexpected response from %r backend: verify(%r, %r):",
                          backend, secret, hash, exc_info=True)
                return NotImplemented

        def assert_lacks_8bit_bug(ident):
            """
            helper to check for cryptblowfish 8bit bug (fixed in 2y/2b);
            even though it's not known to be present in any of passlib's backends.
            this is treated as FATAL, because it can easily result in seriously malformed hashes,
            and we can't correct for it ourselves.

            test cases from <http://cvsweb.openwall.com/cgi/cvsweb.cgi/Owl/packages/glibc/crypt_blowfish/wrapper.c.diff?r1=1.9;r2=1.10>
            reference hash is the incorrectly generated $2x$ hash taken from above url
            """
            secret = b"\xA3"
            bug_hash = ident.encode("ascii") + b"05$/OK.fbVrR/bpIqNJ5ianF.CE5elHaaO4EbggVDjb8P19RukzXSM3e"
            if verify(secret, bug_hash):
                # NOTE: this only EVER be observed in 2a hashes,
                #       2y/2b hashes should have fixed the bug.
                #       (but we check w/ them anyways).
                raise PasslibSecurityError(
                    "passlib.hash.bcrypt: Your installation of the %r backend is vulnerable to "
                    "the crypt_blowfish 8-bit bug (CVE-2011-2483), "
                    "and should be upgraded or replaced with another backend." % backend)

            # if it doesn't have wraparound bug, make sure it *does* handle things
            # correctly -- or we're in some weird third case.
            correct_hash = ident.encode("ascii") + b"05$/OK.fbVrR/bpIqNJ5ianF.Sa7shbm4.OzKpvFnX1pQLmQW96oUlCq"
            if not verify(secret, correct_hash):
                raise RuntimeError("%s backend failed to verify %s 8bit hash" % (backend, ident))

        def detect_wrap_bug(ident):
            """
            check for bsd wraparound bug (fixed in 2b)
            this is treated as a warning, because it's rare in the field,
            and pybcrypt (as of 2015-7-21) is unpatched, but some people may be stuck with it.

            test cases from <http://www.openwall.com/lists/oss-security/2012/01/02/4>

            NOTE: reference hash is of password "0"*72

            NOTE: if in future we need to deliberately create hashes which have this bug,
                  can use something like 'hashpw(repeat_string(secret[:((1+secret) % 256) or 1]), 72)'
            """
            # check if it exhibits wraparound bug
            secret = (b"0123456789"*26)[:255]
            bug_hash = ident.encode("ascii") + b"04$R1lJ2gkNaoPGdafE.H.16.nVyh2niHsGJhayOHLMiXlI45o8/DU.6"
            if verify(secret, bug_hash):
                return True

            # if it doesn't have wraparound bug, make sure it *does* handle things
            # correctly -- or we're in some weird third case.
            correct_hash = ident.encode("ascii") + b"04$R1lJ2gkNaoPGdafE.H.16.1MKHPvmKwryeulRe225LKProWYwt9Oi"
            if not verify(secret, correct_hash):
                raise RuntimeError("%s backend failed to verify %s wraparound hash" % (backend, ident))

            return False

        def assert_lacks_wrap_bug(ident):
            if not detect_wrap_bug(ident):
                return
            # should only see in 2a, later idents should NEVER exhibit this bug:
            # * 2y implementations should have been free of it
            # * 2b was what (supposedly) fixed it
            raise RuntimeError("%s backend unexpectedly has wraparound bug for %s" % (backend, ident))

        #----------------------------------------------------------------
        # check for old 20 support
        #----------------------------------------------------------------
        test_hash_20 = b"$2$04$5BJqKfqMQvV7nS.yUguNcuRfMMOXK0xPWavM7pOzjEi5ze5T1k8/S"
        result = safe_verify("test", test_hash_20)
        if not result:
            raise RuntimeError("%s incorrectly rejected $2$ hash" % backend)
        elif result is NotImplemented:
            mixin_cls._lacks_20_support = True
            log.debug("%r backend lacks $2$ support, enabling workaround", backend)

        #----------------------------------------------------------------
        # check for 2a support
        #----------------------------------------------------------------
        result = safe_verify("test", TEST_HASH_2A)
        if not result:
            raise RuntimeError("%s incorrectly rejected $2a$ hash" % backend)
        elif result is NotImplemented:
            # 2a support is required, and should always be present
            raise RuntimeError("%s lacks support for $2a$ hashes" % backend)
        else:
            assert_lacks_8bit_bug(IDENT_2A)
            if detect_wrap_bug(IDENT_2A):
                warn("passlib.hash.bcrypt: Your installation of the %r backend is vulnerable to "
                     "the bsd wraparound bug, "
                     "and should be upgraded or replaced with another backend "
                     "(enabling workaround for now)." % backend,
                     uh.exc.PasslibSecurityWarning)
                mixin_cls._has_2a_wraparound_bug = True

        #----------------------------------------------------------------
        # check for 2y support
        #----------------------------------------------------------------
        test_hash_2y = TEST_HASH_2A.replace(b"2a", b"2y")
        result = safe_verify("test", test_hash_2y)
        if not result:
            raise RuntimeError("%s incorrectly rejected $2y$ hash" % backend)
        elif result is NotImplemented:
            mixin_cls._lacks_2y_support = True
            log.debug("%r backend lacks $2y$ support, enabling workaround", backend)
        else:
            # NOTE: Not using this as fallback candidate,
            #       lacks wide enough support across implementations.
            assert_lacks_8bit_bug(IDENT_2Y)
            assert_lacks_wrap_bug(IDENT_2Y)

        #----------------------------------------------------------------
        # TODO: check for 2x support
        #----------------------------------------------------------------

        #----------------------------------------------------------------
        # check for 2b support
        #----------------------------------------------------------------
        test_hash_2b = TEST_HASH_2A.replace(b"2a", b"2b")
        result = safe_verify("test", test_hash_2b)
        if not result:
            raise RuntimeError("%s incorrectly rejected $2b$ hash" % backend)
        elif result is NotImplemented:
            mixin_cls._lacks_2b_support = True
            log.debug("%r backend lacks $2b$ support, enabling workaround", backend)
        else:
            mixin_cls._fallback_ident = IDENT_2B
            assert_lacks_8bit_bug(IDENT_2B)
            assert_lacks_wrap_bug(IDENT_2B)

        # set flag so we don't have to run this again
        mixin_cls._workrounds_initialized = True
        return True

    #===================================================================
    # digest calculation
    #===================================================================

    # _calc_checksum() defined by backends

    def _prepare_digest_args(self, secret):
        """
        common helper for backends to implement _calc_checksum().
        takes in secret, returns (secret, ident) pair,
        """
        return self._norm_digest_args(secret, self.ident, new=self.use_defaults)

    @classmethod
    def _norm_digest_args(cls, secret, ident, new=False):
        # make sure secret is unicode
        if isinstance(secret, unicode):
            secret = secret.encode("utf-8")

        # check max secret size
        uh.validate_secret(secret)

        # check for truncation (during .hash() calls only)
        if new:
            cls._check_truncate_policy(secret)

        # NOTE: especially important to forbid NULLs for bcrypt, since many
        # backends (bcryptor, bcrypt) happily accept them, and then
        # silently truncate the password at first NULL they encounter!
        if _BNULL in secret:
            raise uh.exc.NullPasswordError(cls)

        # TODO: figure out way to skip these tests when not needed...

        # protect from wraparound bug by truncating secret before handing it to the backend.
        # bcrypt only uses first 72 bytes anyways.
        # NOTE: not needed for 2y/2b, but might use 2a as fallback for them.
        if cls._has_2a_wraparound_bug and len(secret) >= 255:
            secret = secret[:72]

        # special case handling for variants (ordered most common first)
        if ident == IDENT_2A:
            # nothing needs to be done.
            pass

        elif ident == IDENT_2B:
            if cls._lacks_2b_support:
                # handle $2b$ hash format even if backend is too old.
                # have it generate a 2A/2Y digest, then return it as a 2B hash.
                # 2a-only backend could potentially exhibit wraparound bug --
                # but we work around that issue above.
                ident = cls._fallback_ident

        elif ident == IDENT_2Y:
            if cls._lacks_2y_support:
                # handle $2y$ hash format (not supported by BSDs, being phased out on others)
                # have it generate a 2A/2B digest, then return it as a 2Y hash.
                ident = cls._fallback_ident

        elif ident == IDENT_2:
            if cls._lacks_20_support:
                # handle legacy $2$ format (not supported by most backends except BSD os_crypt)
                # we can fake $2$ behavior using the 2A/2Y/2B algorithm
                # by repeating the password until it's at least 72 chars in length.
                if secret:
                    secret = repeat_string(secret, 72)
                ident = cls._fallback_ident

        elif ident == IDENT_2X:

            # NOTE: shouldn't get here.
            # XXX: could check if backend does actually offer 'support'
            raise RuntimeError("$2x$ hashes not currently supported by passlib")

        else:
            raise AssertionError("unexpected ident value: %r" % ident)

        return secret, ident

#-----------------------------------------------------------------------
# stub backend
#-----------------------------------------------------------------------
class _NoBackend(_BcryptCommon):
    """
    mixin used before any backend has been loaded.
    contains stubs that force loading of one of the available backends.
    """
    #===================================================================
    # digest calculation
    #===================================================================
    def _calc_checksum(self, secret):
        self._stub_requires_backend()
        # NOTE: have to use super() here so that we don't recursively
        #       call subclass's wrapped _calc_checksum, e.g. bcrypt_sha256._calc_checksum
        return super(bcrypt, self)._calc_checksum(secret)

    #===================================================================
    # eoc
    #===================================================================

#-----------------------------------------------------------------------
# bcrypt backend
#-----------------------------------------------------------------------
class _BcryptBackend(_BcryptCommon):
    """
    backend which uses 'bcrypt' package
    """

    @classmethod
    def _load_backend_mixin(mixin_cls, name, dryrun):
        # try to import bcrypt
        global _bcrypt
        if _detect_pybcrypt():
            # pybcrypt was installed instead
            return False
        try:
            import bcrypt as _bcrypt
        except ImportError: # pragma: no cover
            return False
        try:
            version = _bcrypt.__about__.__version__
        except:
            log.warning("(trapped) error reading bcrypt version", exc_info=True)
            version = '<unknown>'

        log.debug("detected 'bcrypt' backend, version %r", version)
        return mixin_cls._finalize_backend_mixin(name, dryrun)

    # # TODO: would like to implementing verify() directly,
    # #       to skip need for parsing hash strings.
    # #       below method has a few edge cases where it chokes though.
    # @classmethod
    # def verify(cls, secret, hash):
    #     if isinstance(hash, unicode):
    #         hash = hash.encode("ascii")
    #     ident = hash[:hash.index(b"$", 1)+1].decode("ascii")
    #     if ident not in cls.ident_values:
    #         raise uh.exc.InvalidHashError(cls)
    #     secret, eff_ident = cls._norm_digest_args(secret, ident)
    #     if eff_ident != ident:
    #         # lacks support for original ident, replace w/ new one.
    #         hash = eff_ident.encode("ascii") + hash[len(ident):]
    #     result = _bcrypt.hashpw(secret, hash)
    #     assert result.startswith(eff_ident)
    #     return consteq(result, hash)

    def _calc_checksum(self, secret):
        # bcrypt behavior:
        #   secret must be bytes
        #   config must be ascii bytes
        #   returns ascii bytes
        secret, ident = self._prepare_digest_args(secret)
        config = self._get_config(ident)
        if isinstance(config, unicode):
            config = config.encode("ascii")
        hash = _bcrypt.hashpw(secret, config)
        assert hash.startswith(config) and len(hash) == len(config)+31, \
            "config mismatch: %r => %r" % (config, hash)
        assert isinstance(hash, bytes)
        return hash[-31:].decode("ascii")

#-----------------------------------------------------------------------
# bcryptor backend
#-----------------------------------------------------------------------
class _BcryptorBackend(_BcryptCommon):
    """
    backend which uses 'bcryptor' package
    """

    @classmethod
    def _load_backend_mixin(mixin_cls, name, dryrun):
        # try to import bcryptor
        global _bcryptor
        try:
            import bcryptor as _bcryptor
        except ImportError: # pragma: no cover
            return False
        return mixin_cls._finalize_backend_mixin(name, dryrun)

    def _calc_checksum(self, secret):
        # bcryptor behavior:
        #   py2: unicode secret/hash encoded as ascii bytes before use,
        #        bytes taken as-is; returns ascii bytes.
        #   py3: not supported
        secret, ident = self._prepare_digest_args(secret)
        config = self._get_config(ident)
        hash = _bcryptor.engine.Engine(False).hash_key(secret, config)
        assert hash.startswith(config) and len(hash) == len(config)+31
        return str_to_uascii(hash[-31:])

#-----------------------------------------------------------------------
# pybcrypt backend
#-----------------------------------------------------------------------
class _PyBcryptBackend(_BcryptCommon):
    """
    backend which uses 'pybcrypt' package
    """

    #: classwide thread lock used for pybcrypt < 0.3
    _calc_lock = None

    @classmethod
    def _load_backend_mixin(mixin_cls, name, dryrun):
        # try to import pybcrypt
        global _pybcrypt
        if not _detect_pybcrypt():
            # not installed, or bcrypt installed instead
            return False
        try:
            import bcrypt as _pybcrypt
        except ImportError: # pragma: no cover
            return False

        # determine pybcrypt version
        try:
            version = _pybcrypt._bcrypt.__version__
        except:
            log.warning("(trapped) error reading pybcrypt version", exc_info=True)
            version = "<unknown>"
        log.debug("detected 'pybcrypt' backend, version %r", version)

        # return calc function based on version
        vinfo = parse_version(version) or (0, 0)
        if vinfo < (0, 3):
            warn("py-bcrypt %s has a major security vulnerability, "
                 "you should upgrade to py-bcrypt 0.3 immediately."
                 % version, uh.exc.PasslibSecurityWarning)
            if mixin_cls._calc_lock is None:
                import threading
                mixin_cls._calc_lock = threading.Lock()
            mixin_cls._calc_checksum = mixin_cls._calc_checksum_threadsafe.__func__

        return mixin_cls._finalize_backend_mixin(name, dryrun)

    def _calc_checksum_threadsafe(self, secret):
        # as workaround for pybcrypt < 0.3's concurrency issue,
        # we wrap everything in a thread lock. as long as bcrypt is only
        # used through passlib, this should be safe.
        with self._calc_lock:
            return self._calc_checksum_raw(secret)

    def _calc_checksum_raw(self, secret):
        # py-bcrypt behavior:
        #   py2: unicode secret/hash encoded as ascii bytes before use,
        #        bytes taken as-is; returns ascii bytes.
        #   py3: unicode secret encoded as utf-8 bytes,
        #        hash encoded as ascii bytes, returns ascii unicode.
        secret, ident = self._prepare_digest_args(secret)
        config = self._get_config(ident)
        hash = _pybcrypt.hashpw(secret, config)
        assert hash.startswith(config) and len(hash) == len(config)+31
        return str_to_uascii(hash[-31:])

    _calc_checksum = _calc_checksum_raw

#-----------------------------------------------------------------------
# os crypt backend
#-----------------------------------------------------------------------
class _OsCryptBackend(_BcryptCommon):
    """
    backend which uses :func:`crypt.crypt`
    """

    @classmethod
    def _load_backend_mixin(mixin_cls, name, dryrun):
        if not test_crypt("test", TEST_HASH_2A):
            return False
        return mixin_cls._finalize_backend_mixin(name, dryrun)

    def _calc_checksum(self, secret):
        secret, ident = self._prepare_digest_args(secret)
        config = self._get_config(ident)
        hash = safe_crypt(secret, config)
        if hash:
            assert hash.startswith(config) and len(hash) == len(config)+31
            return hash[-31:]
        else:
            # NOTE: Have to raise this error because python3's crypt.crypt() only accepts unicode.
            #       This means it can't handle any passwords that aren't either unicode
            #       or utf-8 encoded bytes.  However, hashing a password with an alternate
            #       encoding should be a pretty rare edge case; if user needs it, they can just
            #       install bcrypt backend.
            # XXX: is this the right error type to raise?
            #      maybe have safe_crypt() not swallow UnicodeDecodeError, and have handlers
            #      like sha256_crypt trap it if they have alternate method of handling them?
            raise uh.exc.MissingBackendError(
                "non-utf8 encoded passwords can't be handled by crypt.crypt() under python3, "
                "recommend running `pip install bcrypt`.",
                )

#-----------------------------------------------------------------------
# builtin backend
#-----------------------------------------------------------------------
class _BuiltinBackend(_BcryptCommon):
    """
    backend which uses passlib's pure-python implementation
    """
    @classmethod
    def _load_backend_mixin(mixin_cls, name, dryrun):
        from passlib.utils import as_bool
        if not as_bool(os.environ.get("PASSLIB_BUILTIN_BCRYPT")):
            log.debug("bcrypt 'builtin' backend not enabled via $PASSLIB_BUILTIN_BCRYPT")
            return False
        global _builtin_bcrypt
        from passlib.crypto._blowfish import raw_bcrypt as _builtin_bcrypt
        return mixin_cls._finalize_backend_mixin(name, dryrun)

    def _calc_checksum(self, secret):
        secret, ident = self._prepare_digest_args(secret)
        chk = _builtin_bcrypt(secret, ident[1:-1],
                              self.salt.encode("ascii"), self.rounds)
        return chk.decode("ascii")

#=============================================================================
# handler
#=============================================================================
class bcrypt(_NoBackend, _BcryptCommon):
    """This class implements the BCrypt password hash, and follows the :ref:`password-hash-api`.

    It supports a fixed-length salt, and a variable number of rounds.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: str
    :param salt:
        Optional salt string.
        If not specified, one will be autogenerated (this is recommended).
        If specified, it must be 22 characters, drawn from the regexp range ``[./0-9A-Za-z]``.

    :type rounds: int
    :param rounds:
        Optional number of rounds to use.
        Defaults to 12, must be between 4 and 31, inclusive.
        This value is logarithmic, the actual number of iterations used will be :samp:`2**{rounds}`
        -- increasing the rounds by +1 will double the amount of time taken.

    :type ident: str
    :param ident:
        Specifies which version of the BCrypt algorithm will be used when creating a new hash.
        Typically this option is not needed, as the default (``"2a"``) is usually the correct choice.
        If specified, it must be one of the following:

        * ``"2"`` - the first revision of BCrypt, which suffers from a minor security flaw and is generally not used anymore.
        * ``"2a"`` - some implementations suffered from rare security flaws, replaced by 2b.
        * ``"2y"`` - format specific to the *crypt_blowfish* BCrypt implementation,
          identical to ``"2a"`` in all but name.
        * ``"2b"`` - latest revision of the official BCrypt algorithm, current default.

    :param bool truncate_error:
        By default, BCrypt will silently truncate passwords larger than 72 bytes.
        Setting ``truncate_error=True`` will cause :meth:`~passlib.ifc.PasswordHash.hash`
        to raise a :exc:`~passlib.exc.PasswordTruncateError` instead.

        .. versionadded:: 1.7

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include ``rounds``
        that are too small or too large, and ``salt`` strings that are too long.

        .. versionadded:: 1.6

    .. versionchanged:: 1.6
        This class now supports ``"2y"`` hashes, and recognizes
        (but does not support) the broken ``"2x"`` hashes.
        (see the :ref:`crypt_blowfish bug <crypt-blowfish-bug>`
        for details).

    .. versionchanged:: 1.6
        Added a pure-python backend.

    .. versionchanged:: 1.6.3

        Added support for ``"2b"`` variant.

    .. versionchanged:: 1.7

        Now defaults to ``"2b"`` variant.
    """
    #=============================================================================
    # backend
    #=============================================================================

    # NOTE: the brunt of the bcrypt class is implemented in _BcryptCommon.
    #       there are then subclass for each backend (e.g. _PyBcryptBackend),
    #       these are dynamically prepended to this class's bases
    #       in order to load the appropriate backend.

    #: list of potential backends
    backends = ("bcrypt", "pybcrypt", "bcryptor", "os_crypt", "builtin")

    #: flag that this class's bases should be modified by SubclassBackendMixin
    _backend_mixin_target = True

    #: map of backend -> mixin class, used by _get_backend_loader()
    _backend_mixin_map = {
        None: _NoBackend,
        "bcrypt": _BcryptBackend,
        "pybcrypt": _PyBcryptBackend,
        "bcryptor": _BcryptorBackend,
        "os_crypt": _OsCryptBackend,
        "builtin": _BuiltinBackend,
    }

    #=============================================================================
    # eoc
    #=============================================================================

#=============================================================================
# variants
#=============================================================================
_UDOLLAR = u("$")

# XXX: it might be better to have all the bcrypt variants share a common base class,
#      and have the (django_)bcrypt_sha256 wrappers just proxy bcrypt instead of subclassing it.
class _wrapped_bcrypt(bcrypt):
    """
    abstracts out some bits bcrypt_sha256 & django_bcrypt_sha256 share.
    - bypass backend-loading wrappers for hash() etc
    - disable truncation support, sha256 wrappers don't need it.
    """
    setting_kwds = tuple(elem for elem in bcrypt.setting_kwds if elem not in ["truncate_error"])
    truncate_size = None

    # XXX: these will be needed if any bcrypt backends directly implement this...
    # @classmethod
    # def hash(cls, secret, **kwds):
    #     # bypass bcrypt backend overriding this method
    #     # XXX: would wrapping bcrypt make this easier than subclassing it?
    #     return super(_BcryptCommon, cls).hash(secret, **kwds)
    #
    # @classmethod
    # def verify(cls, secret, hash):
    #     # bypass bcrypt backend overriding this method
    #     return super(_BcryptCommon, cls).verify(secret, hash)
    #
    # @classmethod
    # def genhash(cls, secret, hash):
    #     # bypass bcrypt backend overriding this method
    #     return super(_BcryptCommon, cls).genhash(secret, hash)

    @classmethod
    def _check_truncate_policy(cls, secret):
        # disable check performed by bcrypt(), since this doesn't truncate passwords.
        pass

#=============================================================================
# bcrypt sha256 wrapper
#=============================================================================

class bcrypt_sha256(_wrapped_bcrypt):
    """This class implements a composition of BCrypt+SHA256, and follows the :ref:`password-hash-api`.

    It supports a fixed-length salt, and a variable number of rounds.

    The :meth:`~passlib.ifc.PasswordHash.hash` and :meth:`~passlib.ifc.PasswordHash.genconfig` methods accept
    all the same optional keywords as the base :class:`bcrypt` hash.

    .. versionadded:: 1.6.2

    .. versionchanged:: 1.7

        Now defaults to ``"2b"`` variant.
    """
    #===================================================================
    # class attrs
    #===================================================================

    #--------------------
    # PasswordHash
    #--------------------
    name = "bcrypt_sha256"

    #--------------------
    # GenericHandler
    #--------------------
    # this is locked at 2a/2b for now.
    ident_values = (IDENT_2A, IDENT_2B)

    # clone bcrypt's ident aliases so they can be used here as well...
    ident_aliases = (lambda ident_values: dict(item for item in bcrypt.ident_aliases.items()
                                               if item[1] in ident_values))(ident_values)
    default_ident = IDENT_2B

    #===================================================================
    # formatting
    #===================================================================

    # sample hash:
    # $bcrypt-sha256$2a,6$/3OeRpbOf8/l6nPPRdZPp.$nRiyYqPobEZGdNRBWihQhiFDh1ws1tu
    # $bcrypt-sha256$           -- prefix/identifier
    # 2a                        -- bcrypt variant
    # ,                         -- field separator
    # 6                         -- bcrypt work factor
    # $                         -- section separator
    # /3OeRpbOf8/l6nPPRdZPp.    -- salt
    # $                         -- section separator
    # nRiyYqPobEZGdNRBWihQhiFDh1ws1tu  -- digest

    # XXX: we can't use .ident attr due to bcrypt code using it.
    #      working around that via prefix.
    prefix = u('$bcrypt-sha256$')

    _hash_re = re.compile(r"""
        ^
        [$]bcrypt-sha256
        [$](?P<variant>2[ab])
        ,(?P<rounds>\d{1,2})
        [$](?P<salt>[^$]{22})
        (?:[$](?P<digest>.{31}))?
        $
        """, re.X)

    @classmethod
    def identify(cls, hash):
        hash = uh.to_unicode_for_identify(hash)
        if not hash:
            return False
        return hash.startswith(cls.prefix)

    @classmethod
    def from_string(cls, hash):
        hash = to_unicode(hash, "ascii", "hash")
        if not hash.startswith(cls.prefix):
            raise uh.exc.InvalidHashError(cls)
        m = cls._hash_re.match(hash)
        if not m:
            raise uh.exc.MalformedHashError(cls)
        rounds = m.group("rounds")
        if rounds.startswith(uh._UZERO) and rounds != uh._UZERO:
            raise uh.exc.ZeroPaddedRoundsError(cls)
        return cls(ident=m.group("variant"),
                   rounds=int(rounds),
                   salt=m.group("salt"),
                   checksum=m.group("digest"),
                   )

    _template = u("$bcrypt-sha256$%s,%d$%s$%s")

    def to_string(self):
        hash = self._template % (self.ident.strip(_UDOLLAR),
                                 self.rounds, self.salt, self.checksum)
        return uascii_to_str(hash)

    #===================================================================
    # checksum
    #===================================================================
    def _calc_checksum(self, secret):
        # NOTE: can't use digest directly, since bcrypt stops at first NULL.
        # NOTE: bcrypt doesn't fully mix entropy for bytes 55-72 of password
        #       (XXX: citation needed), so we don't want key to be > 55 bytes.
        #       thus, have to use base64 (44 bytes) rather than hex (64 bytes).
        # XXX: it's later come out that 55-72 may be ok, so later revision of bcrypt_sha256
        #      may switch to hex encoding, since it's simpler to implement elsewhere.
        if isinstance(secret, unicode):
            secret = secret.encode("utf-8")

        # NOTE: output of b64encode() uses "+/" altchars, "=" padding chars,
        #       and no leading/trailing whitespace.
        key = b64encode(sha256(secret).digest())

        # hand result off to normal bcrypt algorithm
        return super(bcrypt_sha256, self)._calc_checksum(key)

    #===================================================================
    # other
    #===================================================================

    # XXX: have _needs_update() mark the $2a$ ones for upgrading?
    #      maybe do that after we switch to hex encoding?

    #===================================================================
    # eoc
    #===================================================================

#=============================================================================
# eof
#=============================================================================
