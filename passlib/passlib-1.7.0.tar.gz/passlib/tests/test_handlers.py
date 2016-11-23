"""passlib.tests.test_handlers - tests for passlib hash algorithms"""
#=============================================================================
# imports
#=============================================================================
from __future__ import with_statement
# core
import logging; log = logging.getLogger(__name__)
import os
import sys
import warnings
# site
# pkg
from passlib import hash
from passlib.utils import repeat_string
from passlib.utils.compat import irange, PY3, u, get_method_function
from passlib.tests.utils import TestCase, HandlerCase, skipUnless, \
        TEST_MODE, UserHandlerMixin, EncodingHandlerMixin
# module

#=============================================================================
# constants & support
#=============================================================================

# some common unicode passwords which used as test cases
UPASS_WAV = u('\u0399\u03c9\u03b1\u03bd\u03bd\u03b7\u03c2')
UPASS_USD = u("\u20AC\u00A5$")
UPASS_TABLE = u("t\u00e1\u0411\u2113\u0259")

PASS_TABLE_UTF8 = b't\xc3\xa1\xd0\x91\xe2\x84\x93\xc9\x99' # utf-8

# handlers which support multiple backends, but don't have multi-backend tests.
_omitted_backend_tests = ["django_bcrypt", "django_bcrypt_sha256", "django_argon2"]

def get_handler_case(scheme):
    """return HandlerCase instance for scheme, used by other tests"""
    from passlib.registry import get_crypt_handler
    handler = get_crypt_handler(scheme)
    if hasattr(handler, "backends") and scheme not in _omitted_backend_tests:
        # NOTE: will throw MissingBackendError if none are installed.
        backend = handler.get_backend()
        name = "%s_%s_test" % (scheme, backend)
    else:
        name = "%s_test" % scheme
    for module in ("test_handlers", "test_handlers_argon2", "test_handlers_bcrypt",
                   "test_handlers_django", "test_handlers_pbkdf2", "test_handlers_scrypt"):
        modname = "passlib.tests." + module
        __import__(modname)
        mod = sys.modules[modname]
        try:
            return getattr(mod, name)
        except AttributeError:
            pass
    raise KeyError("test case %r not found" % name)

#: hashes which there may not be a backend available for,
#: and get_handler_case() may (correctly) throw a MissingBackendError
conditionally_available_hashes = ["argon2", "bcrypt", "bcrypt_sha256"]

#=============================================================================
# apr md5 crypt
#=============================================================================
class apr_md5_crypt_test(HandlerCase):
    handler = hash.apr_md5_crypt

    known_correct_hashes = [
        #
        # http://httpd.apache.org/docs/2.2/misc/password_encryptions.html
        #
        ('myPassword', '$apr1$r31.....$HqJZimcKQFAMYayBlzkrA/'),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '$apr1$bzYrOHUx$a1FcpXuQDJV3vPY20CS6N1'),
        ]

    known_malformed_hashes = [
        # bad char in otherwise correct hash ----\/
            '$apr1$r31.....$HqJZimcKQFAMYayBlzkrA!'
        ]

#=============================================================================
# bigcrypt
#=============================================================================
class bigcrypt_test(HandlerCase):
    handler = hash.bigcrypt

    # TODO: find an authoritative source of test vectors
    known_correct_hashes = [

        #
        # various docs & messages on the web.
        #
        ("passphrase",               "qiyh4XPJGsOZ2MEAyLkfWqeQ"),
        ("This is very long passwd", "f8.SVpL2fvwjkAnxn8/rgTkwvrif6bjYB5c"),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_TABLE, 'SEChBAyMbMNhgGLyP7kD1HZU'),
    ]

    known_unidentified_hashes = [
        # one char short (10 % 11)
        "qiyh4XPJGsOZ2MEAyLkfWqe"

        # one char too many (1 % 11)
        "f8.SVpL2fvwjkAnxn8/rgTkwvrif6bjYB5cd"
    ]

    # omit des_crypt from known_other since it's a valid bigcrypt hash too.
    known_other_hashes = [row for row in HandlerCase.known_other_hashes
                          if row[0] != "des_crypt"]

    def test_90_internal(self):
        # check that _norm_checksum() also validates checksum size.
        # (current code uses regex in parser)
        self.assertRaises(ValueError, hash.bigcrypt, use_defaults=True,
                          checksum=u('yh4XPJGsOZ'))

#=============================================================================
# bsdi crypt
#=============================================================================
class _bsdi_crypt_test(HandlerCase):
    """test BSDiCrypt algorithm"""
    handler = hash.bsdi_crypt

    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ('U*U*U*U*', '_J9..CCCCXBrJUJV154M'),
        ('U*U***U', '_J9..CCCCXUhOBTXzaiE'),
        ('U*U***U*', '_J9..CCCC4gQ.mB/PffM'),
        ('*U*U*U*U', '_J9..XXXXvlzQGqpPPdk'),
        ('*U*U*U*U*', '_J9..XXXXsqM/YSSP..Y'),
        ('*U*U*U*U*U*U*U*U', '_J9..XXXXVL7qJCnku0I'),
        ('*U*U*U*U*U*U*U*U*', '_J9..XXXXAj8cFbP5scI'),
        ('ab1234567', '_J9..SDizh.vll5VED9g'),
        ('cr1234567', '_J9..SDizRjWQ/zePPHc'),
        ('zxyDPWgydbQjgq', '_J9..SDizxmRI1GjnQuE'),
        ('726 even', '_K9..SaltNrQgIYUAeoY'),
        ('', '_J9..SDSD5YGyRCr4W4c'),

        #
        # custom
        #
        (" ", "_K1..crsmZxOLzfJH8iw"),
        ("my", '_KR/.crsmykRplHbAvwA'), # <-- to detect old 12-bit rounds bug
        ("my socra", "_K1..crsmf/9NzZr1fLM"),
        ("my socrates", '_K1..crsmOv1rbde9A9o'),
        ("my socrates note", "_K1..crsm/2qeAhdISMA"),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '_7C/.ABw0WIKy0ILVqo2'),
    ]
    known_unidentified_hashes = [
        # bad char in otherwise correctly formatted hash
        #    \/
        "_K1.!crsmZxOLzfJH8iw"
    ]

    platform_crypt_support = [
        ("freebsd|openbsd|netbsd|darwin", True),
        ("linux|solaris", False),
    ]

    def test_77_fuzz_input(self, **kwds):
        # we want to generate even rounds to verify it's correct, but want to ignore warnings
        warnings.filterwarnings("ignore", "bsdi_crypt rounds should be odd.*")
        super(_bsdi_crypt_test, self).test_77_fuzz_input(**kwds)

    def test_needs_update_w_even_rounds(self):
        """needs_update() should flag even rounds"""
        handler = self.handler
        even_hash = '_Y/../cG0zkJa6LY6k4c'
        odd_hash = '_Z/..TgFg0/ptQtpAgws'
        secret = 'test'

        # don't issue warning
        self.assertTrue(handler.verify(secret, even_hash))
        self.assertTrue(handler.verify(secret, odd_hash))

        # *do* signal as needing updates
        self.assertTrue(handler.needs_update(even_hash))
        self.assertFalse(handler.needs_update(odd_hash))

        # new hashes shouldn't have even rounds
        new_hash = handler.hash("stub")
        self.assertFalse(handler.needs_update(new_hash))

# create test cases for specific backends
bsdi_crypt_os_crypt_test = _bsdi_crypt_test.create_backend_case("os_crypt")
bsdi_crypt_builtin_test = _bsdi_crypt_test.create_backend_case("builtin")

#=============================================================================
# cisco pix
#=============================================================================
class cisco_pix_test(UserHandlerMixin, HandlerCase):
    handler = hash.cisco_pix
    requires_user = False

    known_correct_hashes = [
        #
        # http://www.perlmonks.org/index.pl?node_id=797623
        #
        ("cisco", "2KFQnbNIdI.2KYOU"),

        #
        # http://www.hsc.fr/ressources/breves/pix_crack.html.en
        #
        ("hsc", "YtT8/k6Np8F1yz2c"),

        #
        # www.freerainbowtables.com/phpBB3/viewtopic.php?f=2&t=1441
        #
        ("", "8Ry2YjIyt7RRXU24"),
        (("cisco", "john"), "hN7LzeyYjw12FSIU"),
        (("cisco", "jack"), "7DrfeZ7cyOj/PslD"),

        #
        # http://comments.gmane.org/gmane.comp.security.openwall.john.user/2529
        #
        (("ripper", "alex"), "h3mJrcH0901pqX/m"),
        (("cisco", "cisco"), "3USUcOPFUiMCO4Jk"),
        (("cisco", "cisco1"), "3USUcOPFUiMCO4Jk"),
        (("CscFw-ITC!", "admcom"), "lZt7HSIXw3.QP7.R"),
        ("cangetin", "TynyB./ftknE77QP"),
        (("cangetin", "rramsey"), "jgBZqYtsWfGcUKDi"),

        #
        # http://openwall.info/wiki/john/sample-hashes
        #
        (("phonehome", "rharris"), "zyIIMSYjiPm0L7a6"),

        #
        # from JTR 1.7.9
        #
        ("test1", "TRPEas6f/aa6JSPL"),
        ("test2", "OMT6mXmAvGyzrCtp"),
        ("test3", "gTC7RIy1XJzagmLm"),
        ("test4", "oWC1WRwqlBlbpf/O"),
        ("password", "NuLKvvWGg.x9HEKO"),
        ("0123456789abcdef", ".7nfVBEIEu4KbF/1"),

        #
        # custom
        #
        (("cisco1", "cisco1"), "jmINXNH6p1BxUppp"),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, 'CaiIvkLMu2TOHXGT'),
        ]

def _get_secret(value):
    """extract secret from secret or (secret, user) tuple"""
    if isinstance(value, tuple):
        return value[0]
    else:
        return value

class cisco_asa_test(UserHandlerMixin, HandlerCase):
    handler = hash.cisco_asa
    requires_user = False

    known_correct_hashes = [
        # format: ((secret, user), hash)

        #
        # passlib test vectors
        # TODO: these have not been confirmed by an outside source,
        #       nor tested against an official implementation.
        #       for now, these only confirm we haven't had a regression.
        #

        # 8 char password -- should be same as pix
        (('01234567', ''), '0T52THgnYdV1tlOF'),
        (('01234567', '36'), 'oY0Dh6RVC9KFlopL'),
        (('01234567', 'user'), 'PNZ4ycbbZ0jp1.j1'),
        (('01234567', 'user1234'), 'PNZ4ycbbZ0jp1.j1'),

        # 12 char password -- should be same as pix
        (('0123456789ab', ''), 'S31BxZOGlAigndcJ'),
        (('0123456789ab', '36'), 'JqCXavOaaaTn9B5y'),
        (('0123456789ab', 'user'), 'f.T4BKdzdNkjxQl7'),
        (('0123456789ab', 'user1234'), 'f.T4BKdzdNkjxQl7'),

        # 13 char password -- ASA should switch to larger padding
        (('0123456789abc', ''), 'XGUn8JhVAnJsaJ69'),  # e.g: cisco_pix is 'eacOpB7vE7ZDukSF'
        (('0123456789abc', '36'), 'feNbQYEDXynZXMJH'),
        (('0123456789abc', 'user'), '8Q/FZeam5ai1A47p'),
        (('0123456789abc', 'user1234'), '8Q/FZeam5ai1A47p'),

        # 16 char password -- verify fencepost
        (('0123456789abcdef', ''), 'YO.dC.tE77bB35aH'),
        (('0123456789abcdef', '36'), 'ekOxFx1Mqt8hL3vJ'),
        (('0123456789abcdef', 'user'), 'IneB.wc9sfRzLPoh'),
        (('0123456789abcdef', 'user1234'), 'IneB.wc9sfRzLPoh'),

        # 27 char password -- ASA should still append user
        (('0123456789abcdefqwertyuiopa', ''), '4wp19zS3OCe.2jt5'),
        (('0123456789abcdefqwertyuiopa', '36'), 'GlGggqfEc19br12c'),
        (('0123456789abcdefqwertyuiopa', 'user'), 'zynfWw3UtszxLMgL'),
        (('0123456789abcdefqwertyuiopa', 'user1234'), 'zynfWw3UtszxLMgL'),

        # 28 char password -- ASA shouldn't append user anymore
        (('0123456789abcdefqwertyuiopas', ''), 'W6nbOddI0SutTK7m'),
        (('0123456789abcdefqwertyuiopas', '36'), 'W6nbOddI0SutTK7m'),
        (('0123456789abcdefqwertyuiopas', 'user'), 'W6nbOddI0SutTK7m'),
        (('0123456789abcdefqwertyuiopas', 'user1234'), 'W6nbOddI0SutTK7m'),

        # 32 char password -- verify fencepost
        (('0123456789abcdefqwertyuiopasdfgh', ''), '5hPT/iC6DnoBxo6a'),
        (('0123456789abcdefqwertyuiopasdfgh', '36'), '5hPT/iC6DnoBxo6a'),
        (('0123456789abcdefqwertyuiopasdfgh', 'user'), '5hPT/iC6DnoBxo6a'),
        (('0123456789abcdefqwertyuiopasdfgh', 'user1234'), '5hPT/iC6DnoBxo6a'),

        # 33 char password -- ASA should truncate to 32 (should be same as above)
        (('0123456789abcdefqwertyuiopasdfghj', ''), '5hPT/iC6DnoBxo6a'),
        (('0123456789abcdefqwertyuiopasdfghj', '36'), '5hPT/iC6DnoBxo6a'),
        (('0123456789abcdefqwertyuiopasdfghj', 'user'), '5hPT/iC6DnoBxo6a'),
        (('0123456789abcdefqwertyuiopasdfghj', 'user1234'), '5hPT/iC6DnoBxo6a'),

        # unicode password -- assumes cisco will use utf-8 encoding
        ((u('t\xe1ble'), ''), 'xQXX755BKYRl0ZpQ'),
        ((u('t\xe1ble'), '36'), 'Q/43xXKmIaKLycSj'),
        ((u('t\xe1ble'), 'user'), 'Og8fB4NyF0m5Ed9c'),
        ((u('t\xe1ble'), 'user1234'), 'Og8fB4NyF0m5Ed9c'),
    ]

    # append all the cisco_pix hashes w/ password < 13 chars ... those should be the same.
    known_correct_hashes.extend(row for row in cisco_pix_test.known_correct_hashes
                                if len(_get_secret(row[0])) < 13)

#=============================================================================
# cisco type 7
#=============================================================================
class cisco_type7_test(HandlerCase):
    handler = hash.cisco_type7
    salt_bits = 4
    salt_type = int

    known_correct_hashes = [
        #
        # http://mccltd.net/blog/?p=1034
        #
        ("secure ", "04480E051A33490E"),

        #
        # http://insecure.org/sploits/cisco.passwords.html
        #
        ("Its time to go to lunch!",
         "153B1F1F443E22292D73212D5300194315591954465A0D0B59"),

        #
        # http://blog.ioshints.info/2007/11/type-7-decryption-in-cisco-ios.html
        #
        ("t35t:pa55w0rd", "08351F1B1D431516475E1B54382F"),

        #
        # http://www.m00nie.com/2011/09/cisco-type-7-password-decryption-and-encryption-with-perl/
        #
        ("hiImTesting:)", "020E0D7206320A325847071E5F5E"),

        #
        # http://packetlife.net/forums/thread/54/
        #
        ("cisco123", "060506324F41584B56"),
        ("cisco123", "1511021F07257A767B"),

        #
        # source ?
        #
        ('Supe&8ZUbeRp4SS', "06351A3149085123301517391C501918"),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '0958EDC8A9F495F6F8A5FD'),
    ]

    known_unidentified_hashes = [
        # salt with hex value
        "0A480E051A33490E",

        # salt value > 52. this may in fact be valid, but we reject it for now
        # (see docs for more).
        '99400E4812',
    ]

    def test_90_decode(self):
        """test cisco_type7.decode()"""
        from passlib.utils import to_unicode, to_bytes

        handler = self.handler
        for secret, hash in self.known_correct_hashes:
            usecret = to_unicode(secret)
            bsecret = to_bytes(secret)
            self.assertEqual(handler.decode(hash), usecret)
            self.assertEqual(handler.decode(hash, None), bsecret)

        self.assertRaises(UnicodeDecodeError, handler.decode,
                          '0958EDC8A9F495F6F8A5FD', 'ascii')

    def test_91_salt(self):
        """test salt value border cases"""
        handler = self.handler
        self.assertRaises(TypeError, handler, salt=None)
        handler(salt=None, use_defaults=True)
        self.assertRaises(TypeError, handler, salt='abc')
        self.assertRaises(ValueError, handler, salt=-10)
        self.assertRaises(ValueError, handler, salt=100)

        self.assertRaises(TypeError, handler.using, salt='abc')
        self.assertRaises(ValueError, handler.using, salt=-10)
        self.assertRaises(ValueError, handler.using, salt=100)
        with self.assertWarningList("salt/offset must be.*"):
            subcls = handler.using(salt=100, relaxed=True)
        self.assertEqual(subcls(use_defaults=True).salt, 52)

#=============================================================================
# crypt16
#=============================================================================
class crypt16_test(HandlerCase):
    handler = hash.crypt16

    # TODO: find an authortative source of test vectors
    known_correct_hashes = [
        #
        # from messages around the web, including
        # http://seclists.org/bugtraq/1999/Mar/76
        #
        ("passphrase",  "qi8H8R7OM4xMUNMPuRAZxlY."),
        ("printf",      "aaCjFz4Sh8Eg2QSqAReePlq6"),
        ("printf",      "AA/xje2RyeiSU0iBY3PDwjYo"),
        ("LOLOAQICI82QB4IP", "/.FcK3mad6JwYt8LVmDqz9Lc"),
        ("LOLOAQICI",   "/.FcK3mad6JwYSaRHJoTPzY2"),
        ("LOLOAQIC",    "/.FcK3mad6JwYelhbtlysKy6"),
        ("L",           "/.CIu/PzYCkl6elhbtlysKy6"),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_TABLE, 'YeDc9tKkkmDvwP7buzpwhoqQ'),
        ]

#=============================================================================
# des crypt
#=============================================================================
class _des_crypt_test(HandlerCase):
    """test des-crypt algorithm"""
    handler = hash.des_crypt

    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ('U*U*U*U*', 'CCNf8Sbh3HDfQ'),
        ('U*U***U', 'CCX.K.MFy4Ois'),
        ('U*U***U*', 'CC4rMpbg9AMZ.'),
        ('*U*U*U*U', 'XXxzOu6maQKqQ'),
        ('', 'SDbsugeBiC58A'),

        #
        # custom
        #
        ('', 'OgAwTx2l6NADI'),
        (' ', '/Hk.VPuwQTXbc'),
        ('test', 'N1tQbOFcM5fpg'),
        ('Compl3X AlphaNu3meric', 'um.Wguz3eVCx2'),
        ('4lpHa N|_|M3r1K W/ Cur5Es: #$%(*)(*%#', 'sNYqfOyauIyic'),
        ('AlOtBsOl', 'cEpWz5IUCShqM'),

        # ensures utf-8 used for unicode
        (u('hell\u00D6'), 'saykDgk3BPZ9E'),
        ]
    known_unidentified_hashes = [
        # bad char in otherwise correctly formatted hash
        #\/
        '!gAwTx2l6NADI',

        # wrong size
        'OgAwTx2l6NAD',
        'OgAwTx2l6NADIj',
        ]

    platform_crypt_support = [
        ("freebsd|openbsd|netbsd|linux|solaris|darwin", True),
    ]

# create test cases for specific backends
des_crypt_os_crypt_test = _des_crypt_test.create_backend_case("os_crypt")
des_crypt_builtin_test = _des_crypt_test.create_backend_case("builtin")

#=============================================================================
# fshp
#=============================================================================
class fshp_test(HandlerCase):
    """test fshp algorithm"""
    handler = hash.fshp

    known_correct_hashes = [
        #
        # test vectors from FSHP reference implementation
        # https://github.com/bdd/fshp-is-not-secure-anymore/blob/master/python/test.py
        #
        ('test', '{FSHP0|0|1}qUqP5cyxm6YcTAhz05Hph5gvu9M='),

        ('test',
            '{FSHP1|8|4096}MTIzNDU2NzjTdHcmoXwNc0f'
            'f9+ArUHoN0CvlbPZpxFi1C6RDM/MHSA=='
            ),

        ('OrpheanBeholderScryDoubt',
            '{FSHP1|8|4096}GVSUFDAjdh0vBosn1GUhz'
            'GLHP7BmkbCZVH/3TQqGIjADXpc+6NCg3g=='
            ),
        ('ExecuteOrder66',
            '{FSHP3|16|8192}0aY7rZQ+/PR+Rd5/I9ss'
            'RM7cjguyT8ibypNaSp/U1uziNO3BVlg5qPU'
            'ng+zHUDQC3ao/JbzOnIBUtAeWHEy7a2vZeZ'
            '7jAwyJJa2EqOsq4Io='
            ),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '{FSHP1|16|16384}9v6/l3Lu/d9by5nznpOS'
         'cqQo8eKu/b/CKli3RCkgYg4nRTgZu5y659YV8cCZ68UL'),
        ]

    known_unidentified_hashes = [
        # incorrect header
        '{FSHX0|0|1}qUqP5cyxm6YcTAhz05Hph5gvu9M=',
        'FSHP0|0|1}qUqP5cyxm6YcTAhz05Hph5gvu9M=',
        ]

    known_malformed_hashes = [
        # bad base64 padding
        '{FSHP0|0|1}qUqP5cyxm6YcTAhz05Hph5gvu9M',

        # wrong salt size
        '{FSHP0|1|1}qUqP5cyxm6YcTAhz05Hph5gvu9M=',

        # bad rounds
        '{FSHP0|0|A}qUqP5cyxm6YcTAhz05Hph5gvu9M=',
    ]

    def test_90_variant(self):
        """test variant keyword"""
        handler = self.handler
        kwds = dict(salt=b'a', rounds=1)

        # accepts ints
        handler(variant=1, **kwds)

        # accepts bytes or unicode
        handler(variant=u('1'), **kwds)
        handler(variant=b'1', **kwds)

        # aliases
        handler(variant=u('sha256'), **kwds)
        handler(variant=b'sha256', **kwds)

        # rejects None
        self.assertRaises(TypeError, handler, variant=None, **kwds)

        # rejects other types
        self.assertRaises(TypeError, handler, variant=complex(1,1), **kwds)

        # invalid variant
        self.assertRaises(ValueError, handler, variant='9', **kwds)
        self.assertRaises(ValueError, handler, variant=9, **kwds)

#=============================================================================
# hex digests
#=============================================================================
class hex_md4_test(HandlerCase):
    handler = hash.hex_md4
    known_correct_hashes = [
        ("password", '8a9d093f14f8701df17732b2bb182c74'),
        (UPASS_TABLE, '876078368c47817ce5f9115f3a42cf74'),
    ]

class hex_md5_test(HandlerCase):
    handler = hash.hex_md5
    known_correct_hashes = [
        ("password", '5f4dcc3b5aa765d61d8327deb882cf99'),
        (UPASS_TABLE, '05473f8a19f66815e737b33264a0d0b0'),
    ]

class hex_sha1_test(HandlerCase):
    handler = hash.hex_sha1
    known_correct_hashes = [
        ("password", '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'),
        (UPASS_TABLE, 'e059b2628e3a3e2de095679de9822c1d1466e0f0'),
    ]

class hex_sha256_test(HandlerCase):
    handler = hash.hex_sha256
    known_correct_hashes = [
        ("password", '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'),
        (UPASS_TABLE, '6ed729e19bf24d3d20f564375820819932029df05547116cfc2cc868a27b4493'),
    ]

class hex_sha512_test(HandlerCase):
    handler = hash.hex_sha512
    known_correct_hashes = [
        ("password", 'b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c'
         '706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cac'
         'bc86'),
        (UPASS_TABLE, 'd91bb0a23d66dca07a1781fd63ae6a05f6919ee5fc368049f350c9f'
         '293b078a18165d66097cf0d89fdfbeed1ad6e7dba2344e57348cd6d51308c843a06f'
         '29caf'),
    ]

#=============================================================================
# htdigest hash
#=============================================================================
class htdigest_test(UserHandlerMixin, HandlerCase):
    handler = hash.htdigest

    known_correct_hashes = [
        # secret, user, realm

        # from RFC 2617
        (("Circle Of Life", "Mufasa", "testrealm@host.com"),
            '939e7578ed9e3c518a452acee763bce9'),

        # custom
        ((UPASS_TABLE, UPASS_USD, UPASS_WAV),
            '4dabed2727d583178777fab468dd1f17'),
    ]

    known_unidentified_hashes = [
        # bad char \/ - currently rejecting upper hex chars, may change
        '939e7578edAe3c518a452acee763bce9',

        # bad char \/
        '939e7578edxe3c518a452acee763bce9',
    ]

    def test_80_user(self):
        raise self.skipTest("test case doesn't support 'realm' keyword")

    def populate_context(self, secret, kwds):
        """insert username into kwds"""
        if isinstance(secret, tuple):
            secret, user, realm = secret
        else:
            user, realm = "user", "realm"
        kwds.setdefault("user", user)
        kwds.setdefault("realm", realm)
        return secret

#=============================================================================
# ldap hashes
#=============================================================================
class ldap_md5_test(HandlerCase):
    handler = hash.ldap_md5
    known_correct_hashes = [
        ("helloworld", '{MD5}/F4DjTilcDIIVEHn/nAQsA=='),
        (UPASS_TABLE, '{MD5}BUc/ihn2aBXnN7MyZKDQsA=='),
    ]

class ldap_sha1_test(HandlerCase):
    handler = hash.ldap_sha1
    known_correct_hashes = [
        ("helloworld", '{SHA}at+xg6SiyUovktq1redipHiJpaE='),
        (UPASS_TABLE, '{SHA}4FmyYo46Pi3glWed6YIsHRRm4PA='),
    ]

class ldap_salted_md5_test(HandlerCase):
    handler = hash.ldap_salted_md5
    known_correct_hashes = [
        ("testing1234", '{SMD5}UjFY34os/pnZQ3oQOzjqGu4yeXE='),
        (UPASS_TABLE, '{SMD5}Z0ioJ58LlzUeRxm3K6JPGAvBGIM='),

        # alternate salt sizes (8, 15, 16)
        ('test', '{SMD5}LnuZPJhiaY95/4lmVFpg548xBsD4P4cw'),
        ('test', '{SMD5}XRlncfRzvGi0FDzgR98tUgBg7B3jXOs9p9S615qTkg=='),
        ('test', '{SMD5}FbAkzOMOxRbMp6Nn4hnZuel9j9Gas7a2lvI+x5hT6j0='),
    ]

    known_malformed_hashes = [
        # salt too small (3)
        '{SMD5}IGVhwK+anvspmfDt2t0vgGjt/Q==',

        # incorrect base64 encoding
        '{SMD5}LnuZPJhiaY95/4lmVFpg548xBsD4P4c',
        '{SMD5}LnuZPJhiaY95/4lmVFpg548xBsD4P4cw'
        '{SMD5}LnuZPJhiaY95/4lmVFpg548xBsD4P4cw=',
        '{SMD5}LnuZPJhiaY95/4lmV=pg548xBsD4P4cw',
        '{SMD5}LnuZPJhiaY95/4lmVFpg548xBsD4P===',
    ]

class ldap_salted_sha1_test(HandlerCase):
    handler = hash.ldap_salted_sha1
    known_correct_hashes = [
        ("testing123", '{SSHA}0c0blFTXXNuAMHECS4uxrj3ZieMoWImr'),
        ("secret", "{SSHA}0H+zTv8o4MR4H43n03eCsvw1luG8LdB7"),
        (UPASS_TABLE, '{SSHA}3yCSD1nLZXznra4N8XzZgAL+s1sQYsx5'),

        # alternate salt sizes (8, 15, 16)
        ('test', '{SSHA}P90+qijSp8MJ1tN25j5o1PflUvlqjXHOGeOckw=='),
        ('test', '{SSHA}/ZMF5KymNM+uEOjW+9STKlfCFj51bg3BmBNCiPHeW2ttbU0='),
        ('test', '{SSHA}Pfx6Vf48AT9x3FVv8znbo8WQkEVSipHSWovxXmvNWUvp/d/7'),
    ]

    known_malformed_hashes = [
        # salt too small (3)
        '{SSHA}ZQK3Yvtvl6wtIRoISgMGPkcWU7Nfq5U=',

        # incorrect base64 encoding
        '{SSHA}P90+qijSp8MJ1tN25j5o1PflUvlqjXHOGeOck',
        '{SSHA}P90+qijSp8MJ1tN25j5o1PflUvlqjXHOGeOckw=',
        '{SSHA}P90+qijSp8MJ1tN25j5o1Pf=UvlqjXHOGeOckw==',
        '{SSHA}P90+qijSp8MJ1tN25j5o1PflUvlqjXHOGeOck===',
    ]

class ldap_plaintext_test(HandlerCase):
    # TODO: integrate EncodingHandlerMixin
    handler = hash.ldap_plaintext
    known_correct_hashes = [
        ("password", 'password'),
        (UPASS_TABLE, UPASS_TABLE if PY3 else PASS_TABLE_UTF8),
        (PASS_TABLE_UTF8, UPASS_TABLE if PY3 else PASS_TABLE_UTF8),
    ]
    known_unidentified_hashes = [
        "{FOO}bar",

        # NOTE: this hash currently rejects the empty string.
        "",
    ]

    known_other_hashes = [
        ("ldap_md5", "{MD5}/F4DjTilcDIIVEHn/nAQsA==")
    ]

    class FuzzHashGenerator(HandlerCase.FuzzHashGenerator):

        def random_password(self):
            # NOTE: this hash currently rejects the empty string.
            while True:
                pwd = super(ldap_plaintext_test.FuzzHashGenerator, self).random_password()
                if pwd:
                    return pwd

class _ldap_md5_crypt_test(HandlerCase):
    # NOTE: since the ldap_{crypt} handlers are all wrappers, don't need
    #       separate test; this is just to test the codebase end-to-end
    handler = hash.ldap_md5_crypt

    known_correct_hashes = [
        #
        # custom
        #
        ('', '{CRYPT}$1$dOHYPKoP$tnxS1T8Q6VVn3kpV8cN6o.'),
        (' ', '{CRYPT}$1$m/5ee7ol$bZn0kIBFipq39e.KDXX8I0'),
        ('test', '{CRYPT}$1$ec6XvcoW$ghEtNK2U1MC5l.Dwgi3020'),
        ('Compl3X AlphaNu3meric', '{CRYPT}$1$nX1e7EeI$ljQn72ZUgt6Wxd9hfvHdV0'),
        ('4lpHa N|_|M3r1K W/ Cur5Es: #$%(*)(*%#', '{CRYPT}$1$jQS7o98J$V6iTcr71CGgwW2laf17pi1'),
        ('test', '{CRYPT}$1$SuMrG47N$ymvzYjr7QcEQjaK5m1PGx1'),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '{CRYPT}$1$d6/Ky1lU$/xpf8m7ftmWLF.TjHCqel0'),
        ]

    known_malformed_hashes = [
        # bad char in otherwise correct hash
        '{CRYPT}$1$dOHYPKoP$tnxS1T8Q6VVn3kpV8cN6o!',
        ]

# create test cases for specific backends
ldap_md5_crypt_os_crypt_test =_ldap_md5_crypt_test.create_backend_case("os_crypt")
ldap_md5_crypt_builtin_test =_ldap_md5_crypt_test.create_backend_case("builtin")

class _ldap_sha1_crypt_test(HandlerCase):
    # NOTE: this isn't for testing the hash (see ldap_md5_crypt note)
    # but as a self-test of the os_crypt patching code in HandlerCase.
    handler = hash.ldap_sha1_crypt

    known_correct_hashes = [
        ('password', '{CRYPT}$sha1$10$c.mcTzCw$gF8UeYst9yXX7WNZKc5Fjkq0.au7'),
        (UPASS_TABLE, '{CRYPT}$sha1$10$rnqXlOsF$aGJf.cdRPewJAXo1Rn1BkbaYh0fP'),
    ]

    def populate_settings(self, kwds):
        kwds.setdefault("rounds", 10)
        super(_ldap_sha1_crypt_test, self).populate_settings(kwds)

    def test_77_fuzz_input(self):
        raise self.skipTest("unneeded")

# create test cases for specific backends
ldap_sha1_crypt_os_crypt_test = _ldap_sha1_crypt_test.create_backend_case("os_crypt")

#=============================================================================
# lanman
#=============================================================================
class lmhash_test(EncodingHandlerMixin, HandlerCase):
    handler = hash.lmhash
    secret_case_insensitive = True

    known_correct_hashes = [
        #
        # http://msdn.microsoft.com/en-us/library/cc245828(v=prot.10).aspx
        #
        ("OLDPASSWORD", "c9b81d939d6fd80cd408e6b105741864"),
        ("NEWPASSWORD", '09eeab5aa415d6e4d408e6b105741864'),
        ("welcome", "c23413a8a1e7665faad3b435b51404ee"),

        #
        # custom
        #
        ('', 'aad3b435b51404eeaad3b435b51404ee'),
        ('zzZZZzz', 'a5e6066de61c3e35aad3b435b51404ee'),
        ('passphrase', '855c3697d9979e78ac404c4ba2c66533'),
        ('Yokohama', '5ecd9236d21095ce7584248b8d2c9f9e'),

        # ensures cp437 used for unicode
        (u('ENCYCLOP\xC6DIA'), 'fed6416bffc9750d48462b9d7aaac065'),
        (u('encyclop\xE6dia'), 'fed6416bffc9750d48462b9d7aaac065'),

        # test various encoding values
        ((u("\xC6"), None), '25d8ab4a0659c97aaad3b435b51404ee'),
        ((u("\xC6"), "cp437"), '25d8ab4a0659c97aaad3b435b51404ee'),
        ((u("\xC6"), "latin-1"), '184eecbbe9991b44aad3b435b51404ee'),
        ((u("\xC6"), "utf-8"), '00dd240fcfab20b8aad3b435b51404ee'),
    ]

    known_unidentified_hashes = [
        # bad char in otherwise correct hash
        '855c3697d9979e78ac404c4ba2c6653X',
    ]

    def test_90_raw(self):
        """test lmhash.raw() method"""
        from binascii import unhexlify
        from passlib.utils.compat import str_to_bascii
        lmhash = self.handler
        for secret, hash in self.known_correct_hashes:
            kwds = {}
            secret = self.populate_context(secret, kwds)
            data = unhexlify(str_to_bascii(hash))
            self.assertEqual(lmhash.raw(secret, **kwds), data)
        self.assertRaises(TypeError, lmhash.raw, 1)

#=============================================================================
# md5 crypt
#=============================================================================
class _md5_crypt_test(HandlerCase):
    handler = hash.md5_crypt

    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ('U*U*U*U*', '$1$dXc3I7Rw$ctlgjDdWJLMT.qwHsWhXR1'),
        ('U*U***U', '$1$dXc3I7Rw$94JPyQc/eAgQ3MFMCoMF.0'),
        ('U*U***U*', '$1$dXc3I7Rw$is1mVIAEtAhIzSdfn5JOO0'),
        ('*U*U*U*U', '$1$eQT9Hwbt$XtuElNJD.eW5MN5UCWyTQ0'),
        ('', '$1$Eu.GHtia$CFkL/nE1BYTlEPiVx1VWX0'),

        #
        # custom
        #

        # NOTE: would need to patch HandlerCase to coerce hashes
        # to native str for this first one to work under py3.
##        ('', b('$1$dOHYPKoP$tnxS1T8Q6VVn3kpV8cN6o.')),
        ('', '$1$dOHYPKoP$tnxS1T8Q6VVn3kpV8cN6o.'),
        (' ', '$1$m/5ee7ol$bZn0kIBFipq39e.KDXX8I0'),
        ('test', '$1$ec6XvcoW$ghEtNK2U1MC5l.Dwgi3020'),
        ('Compl3X AlphaNu3meric', '$1$nX1e7EeI$ljQn72ZUgt6Wxd9hfvHdV0'),
        ('4lpHa N|_|M3r1K W/ Cur5Es: #$%(*)(*%#', '$1$jQS7o98J$V6iTcr71CGgwW2laf17pi1'),
        ('test', '$1$SuMrG47N$ymvzYjr7QcEQjaK5m1PGx1'),
        (b'test', '$1$SuMrG47N$ymvzYjr7QcEQjaK5m1PGx1'),
        (u('s'), '$1$ssssssss$YgmLTApYTv12qgTwBoj8i/'),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '$1$d6/Ky1lU$/xpf8m7ftmWLF.TjHCqel0'),
        ]

    known_malformed_hashes = [
        # bad char in otherwise correct hash \/
           '$1$dOHYPKoP$tnxS1T8Q6VVn3kpV8cN6o!',

        # too many fields
        '$1$dOHYPKoP$tnxS1T8Q6VVn3kpV8cN6o.$',
        ]

    platform_crypt_support = [
        ("freebsd|openbsd|netbsd|linux|solaris", True),
        ("darwin", False),
    ]

# create test cases for specific backends
md5_crypt_os_crypt_test = _md5_crypt_test.create_backend_case("os_crypt")
md5_crypt_builtin_test = _md5_crypt_test.create_backend_case("builtin")

#=============================================================================
# msdcc 1 & 2
#=============================================================================
class msdcc_test(UserHandlerMixin, HandlerCase):
    handler = hash.msdcc
    user_case_insensitive = True

    known_correct_hashes = [

        #
        # http://www.jedge.com/wordpress/windows-password-cache/
        #
        (("Asdf999", "sevans"), "b1176c2587478785ec1037e5abc916d0"),

        #
        # http://infosecisland.com/blogview/12156-Cachedump-for-Meterpreter-in-Action.html
        #
        (("ASDqwe123", "jdoe"), "592cdfbc3f1ef77ae95c75f851e37166"),

        #
        # http://comments.gmane.org/gmane.comp.security.openwall.john.user/1917
        #
        (("test1", "test1"), "64cd29e36a8431a2b111378564a10631"),
        (("test2", "test2"), "ab60bdb4493822b175486810ac2abe63"),
        (("test3", "test3"), "14dd041848e12fc48c0aa7a416a4a00c"),
        (("test4", "test4"), "b945d24866af4b01a6d89b9d932a153c"),

        #
        # http://ciscoit.wordpress.com/2011/04/13/metasploit-hashdump-vs-cachedump/
        #
        (("1234qwer!@#$", "Administrator"), "7b69d06ef494621e3f47b9802fe7776d"),

        #
        # http://www.securiteam.com/tools/5JP0I2KFPA.html
        #
        (("password", "user"), "2d9f0b052932ad18b87f315641921cda"),

        #
        # from JTR 1.7.9
        #
        (("", "root"), "176a4c2bd45ac73687676c2f09045353"),
        (("test1", "TEST1"), "64cd29e36a8431a2b111378564a10631"),
        (("okolada", "nineteen_characters"), "290efa10307e36a79b3eebf2a6b29455"),
        ((u("\u00FC"), u("\u00FC")), "48f84e6f73d6d5305f6558a33fa2c9bb"),
        ((u("\u00FC\u00FC"), u("\u00FC\u00FC")), "593246a8335cf0261799bda2a2a9c623"),
        ((u("\u20AC\u20AC"), "user"), "9121790702dda0fa5d353014c334c2ce"),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        ((UPASS_TABLE, 'bob'), 'fcb82eb4212865c7ac3503156ca3f349'),
    ]

    known_alternate_hashes = [
        # check uppercase accepted.
        ("B1176C2587478785EC1037E5ABC916D0", ("Asdf999", "sevans"),
            "b1176c2587478785ec1037e5abc916d0"),
    ]

class msdcc2_test(UserHandlerMixin, HandlerCase):
    handler = hash.msdcc2
    user_case_insensitive = True

    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        (("test1", "test1"), "607bbe89611e37446e736f7856515bf8"),
        (("qerwt", "Joe"), "e09b38f84ab0be586b730baf61781e30"),
        (("12345", "Joe"), "6432f517a900b3fc34ffe57f0f346e16"),
        (("", "bin"), "c0cbe0313a861062e29f92ede58f9b36"),
        (("w00t", "nineteen_characters"), "87136ae0a18b2dafe4a41d555425b2ed"),
        (("w00t", "eighteencharacters"), "fc5df74eca97afd7cd5abb0032496223"),
        (("longpassword", "twentyXXX_characters"), "cfc6a1e33eb36c3d4f84e4c2606623d2"),
        (("longpassword", "twentyoneX_characters"), "99ff74cea552799da8769d30b2684bee"),
        (("longpassword", "twentytwoXX_characters"), "0a721bdc92f27d7fb23b87a445ec562f"),
        (("test2", "TEST2"), "c6758e5be7fc943d00b97972a8a97620"),
        (("test3", "test3"), "360e51304a2d383ea33467ab0b639cc4"),
        (("test4", "test4"), "6f79ee93518306f071c47185998566ae"),
        ((u("\u00FC"), "joe"), "bdb80f2c4656a8b8591bd27d39064a54"),
        ((u("\u20AC\u20AC"), "joe"), "1e1e20f482ff748038e47d801d0d1bda"),
        ((u("\u00FC\u00FC"), "admin"), "0839e4a07c00f18a8c65cf5b985b9e73"),

        #
        # custom
        #

        # custom unicode test
        ((UPASS_TABLE, 'bob'), 'cad511dc9edefcf69201da72efb6bb55'),
    ]

#=============================================================================
# mssql 2000 & 2005
#=============================================================================
class mssql2000_test(HandlerCase):
    handler = hash.mssql2000
    secret_case_insensitive = "verify-only"
    # FIXME: fix UT framework - this hash is sensitive to password case, but verify() is not

    known_correct_hashes = [
        #
        # http://hkashfi.blogspot.com/2007/08/breaking-sql-server-2005-hashes.html
        #
        ('Test', '0x010034767D5C0CFA5FDCA28C4A56085E65E882E71CB0ED2503412FD54D6119FFF04129A1D72E7C3194F7284A7F3A'),
        ('TEST', '0x010034767D5C2FD54D6119FFF04129A1D72E7C3194F7284A7F3A2FD54D6119FFF04129A1D72E7C3194F7284A7F3A'),

        #
        # http://www.sqlmag.com/forums/aft/68438
        #
        ('x', '0x010086489146C46DD7318D2514D1AC706457CBF6CD3DF8407F071DB4BBC213939D484BF7A766E974F03C96524794'),

        #
        # http://stackoverflow.com/questions/173329/how-to-decrypt-a-password-from-sql-server
        #
        ('AAAA', '0x0100CF465B7B12625EF019E157120D58DD46569AC7BF4118455D12625EF019E157120D58DD46569AC7BF4118455D'),

        #
        # http://msmvps.com/blogs/gladchenko/archive/2005/04/06/41083.aspx
        #
        ('123', '0x01002D60BA07FE612C8DE537DF3BFCFA49CD9968324481C1A8A8FE612C8DE537DF3BFCFA49CD9968324481C1A8A8'),

        #
        # http://www.simple-talk.com/sql/t-sql-programming/temporarily-changing-an-unknown-password-of-the-sa-account-/
        #
        ('12345', '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3'),

        #
        # XXX: sample is incomplete, password unknown
        # https://anthonystechblog.wordpress.com/2011/04/20/password-encryption-in-sql-server-how-to-tell-if-a-user-is-using-a-weak-password/
        # (????, '0x0100813F782D66EF15E40B1A3FDF7AB88B322F51401A87D8D3E3A8483C4351A3D96FC38499E6CDD2B6F?????????'),
        #

        #
        # from JTR 1.7.9
        #
        ('foo', '0x0100A607BA7C54A24D17B565C59F1743776A10250F581D482DA8B6D6261460D3F53B279CC6913CE747006A2E3254'),
        ('bar', '0x01000508513EADDF6DB7DDD270CCA288BF097F2FF69CC2DB74FBB9644D6901764F999BAB9ECB80DE578D92E3F80D'),
        ('canard', '0x01008408C523CF06DCB237835D701C165E68F9460580132E28ED8BC558D22CEDF8801F4503468A80F9C52A12C0A3'),
        ('lapin', '0x0100BF088517935FC9183FE39FDEC77539FD5CB52BA5F5761881E5B9638641A79DBF0F1501647EC941F3355440A2'),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_USD,   '0x0100624C0961B28E39FEE13FD0C35F57B4523F0DA1861C11D5A5B28E39FEE13FD0C35F57B4523F0DA1861C11D5A5'),
        (UPASS_TABLE, '0x010083104228FAD559BE52477F2131E538BE9734E5C4B0ADEFD7F6D784B03C98585DC634FE2B8CA3A6DFFEC729B4'),

    ]

    known_alternate_hashes = [
        # lower case hex
        ('0x01005b20054332752e1bc2e7c5df0f9ebfe486e9bee063e8d3b332752e1bc2e7c5df0f9ebfe486e9bee063e8d3b3',
         '12345', '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3'),
    ]

    known_unidentified_hashes = [
        # malformed start
        '0X01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3',

        # wrong magic value
        '0x02005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3',

        # wrong size
        '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3',
        '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3AF',

        # mssql2005
        '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3',
    ]

    known_malformed_hashes = [
        # non-hex char -----\/
        b'0x01005B200543327G2E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3',
        u('0x01005B200543327G2E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3'),
    ]

class mssql2005_test(HandlerCase):
    handler = hash.mssql2005

    known_correct_hashes = [
        #
        # http://hkashfi.blogspot.com/2007/08/breaking-sql-server-2005-hashes.html
        #
        ('TEST', '0x010034767D5C2FD54D6119FFF04129A1D72E7C3194F7284A7F3A'),

        #
        # http://www.openwall.com/lists/john-users/2009/07/14/2
        #
        ('toto', '0x01004086CEB6BF932BC4151A1AF1F13CD17301D70816A8886908'),

        #
        # http://msmvps.com/blogs/gladchenko/archive/2005/04/06/41083.aspx
        #
        ('123', '0x01004A335DCEDB366D99F564D460B1965B146D6184E4E1025195'),
        ('123', '0x0100E11D573F359629B344990DCD3D53DE82CF8AD6BBA7B638B6'),

        #
        # XXX: password unknown
        # http://www.simple-talk.com/sql/t-sql-programming/temporarily-changing-an-unknown-password-of-the-sa-account-/
        # (???, '0x01004086CEB6301EEC0A994E49E30DA235880057410264030797'),
        #

        #
        # http://therelentlessfrontend.com/2010/03/26/encrypting-and-decrypting-passwords-in-sql-server/
        #
        ('AAAA', '0x010036D726AE86834E97F20B198ACD219D60B446AC5E48C54F30'),

        #
        # from JTR 1.7.9
        #
        ("toto", "0x01004086CEB6BF932BC4151A1AF1F13CD17301D70816A8886908"),
        ("titi", "0x01004086CEB60ED526885801C23B366965586A43D3DEAC6DD3FD"),
        ("foo", "0x0100A607BA7C54A24D17B565C59F1743776A10250F581D482DA8"),
        ("bar", "0x01000508513EADDF6DB7DDD270CCA288BF097F2FF69CC2DB74FB"),
        ("canard", "0x01008408C523CF06DCB237835D701C165E68F9460580132E28ED"),
        ("lapin", "0x0100BF088517935FC9183FE39FDEC77539FD5CB52BA5F5761881"),

        #
        # adapted from mssql2000.known_correct_hashes (above)
        #
        ('Test',  '0x010034767D5C0CFA5FDCA28C4A56085E65E882E71CB0ED250341'),
        ('Test',  '0x0100993BF2315F36CC441485B35C4D84687DC02C78B0E680411F'),
        ('x',     '0x010086489146C46DD7318D2514D1AC706457CBF6CD3DF8407F07'),
        ('AAAA',  '0x0100CF465B7B12625EF019E157120D58DD46569AC7BF4118455D'),
        ('123',   '0x01002D60BA07FE612C8DE537DF3BFCFA49CD9968324481C1A8A8'),
        ('12345', '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3'),

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_USD,   '0x0100624C0961B28E39FEE13FD0C35F57B4523F0DA1861C11D5A5'),
        (UPASS_TABLE, '0x010083104228FAD559BE52477F2131E538BE9734E5C4B0ADEFD7'),
    ]

    known_alternate_hashes = [
        # lower case hex
        ('0x01005b20054332752e1bc2e7c5df0f9ebfe486e9bee063e8d3b3',
         '12345', '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3'),
    ]

    known_unidentified_hashes = [
        # malformed start
        '0X010036D726AE86834E97F20B198ACD219D60B446AC5E48C54F30',

        # wrong magic value
        '0x020036D726AE86834E97F20B198ACD219D60B446AC5E48C54F30',

        # wrong size
        '0x010036D726AE86834E97F20B198ACD219D60B446AC5E48C54F',
        '0x010036D726AE86834E97F20B198ACD219D60B446AC5E48C54F3012',

        # mssql2000
        '0x01005B20054332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B332752E1BC2E7C5DF0F9EBFE486E9BEE063E8D3B3',
    ]

    known_malformed_hashes = [
        # non-hex char --\/
        '0x010036D726AE86G34E97F20B198ACD219D60B446AC5E48C54F30',
    ]

#=============================================================================
# mysql 323 & 41
#=============================================================================
class mysql323_test(HandlerCase):
    handler = hash.mysql323

    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ('drew', '697a7de87c5390b2'),
        ('password', "5d2e19393cc5ef67"),

        #
        # custom
        #
        ('mypass', '6f8c114b58f2ce9e'),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '4ef327ca5491c8d7'),
    ]

    known_unidentified_hashes = [
        # bad char in otherwise correct hash
        '6z8c114b58f2ce9e',
    ]

    def test_90_whitespace(self):
        """check whitespace is ignored per spec"""
        h = self.do_encrypt("mypass")
        h2 = self.do_encrypt("my pass")
        self.assertEqual(h, h2)

    class FuzzHashGenerator(HandlerCase.FuzzHashGenerator):

        def accept_password_pair(self, secret, other):
            # override to handle whitespace
            return secret.replace(" ","") != other.replace(" ","")

class mysql41_test(HandlerCase):
    handler = hash.mysql41
    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ('verysecretpassword', '*2C905879F74F28F8570989947D06A8429FB943E6'),
        ('12345678123456781234567812345678', '*F9F1470004E888963FB466A5452C9CBD9DF6239C'),
        ("' OR 1 /*'", '*97CF7A3ACBE0CA58D5391AC8377B5D9AC11D46D9'),

        #
        # custom
        #
        ('mypass', '*6C8989366EAF75BB670AD8EA7A7FC1176A95CEF4'),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '*E7AFE21A9CFA2FC9D15D942AE8FB5C240FE5837B'),
    ]
    known_unidentified_hashes = [
        # bad char in otherwise correct hash
        '*6Z8989366EAF75BB670AD8EA7A7FC1176A95CEF4',
    ]

#=============================================================================
# NTHASH
#=============================================================================
class nthash_test(HandlerCase):
    handler = hash.nthash

    known_correct_hashes = [
        #
        # http://msdn.microsoft.com/en-us/library/cc245828(v=prot.10).aspx
        #
        ("OLDPASSWORD", u("6677b2c394311355b54f25eec5bfacf5")),
        ("NEWPASSWORD", u("256781a62031289d3c2c98c14f1efc8c")),

        #
        # from JTR 1.7.9
        #

        # ascii
        ('', '31d6cfe0d16ae931b73c59d7e0c089c0'),
        ('tigger', 'b7e0ea9fbffcf6dd83086e905089effd'),

        # utf-8
        (b'\xC3\xBC', '8bd6e4fb88e01009818749c5443ea712'),
        (b'\xC3\xBC\xC3\xBC', 'cc1260adb6985ca749f150c7e0b22063'),
        (b'\xE2\x82\xAC', '030926b781938db4365d46adc7cfbcb8'),
        (b'\xE2\x82\xAC\xE2\x82\xAC','682467b963bb4e61943e170a04f7db46'),

        #
        # custom
        #
        ('passphrase', '7f8fe03093cc84b267b109625f6bbf4b'),
    ]

    known_unidentified_hashes = [
        # bad char in otherwise correct hash
        '7f8fe03093cc84b267b109625f6bbfxb',
    ]

class bsd_nthash_test(HandlerCase):
    handler = hash.bsd_nthash

    known_correct_hashes = [
        ('passphrase', '$3$$7f8fe03093cc84b267b109625f6bbf4b'),
        (b'\xC3\xBC', '$3$$8bd6e4fb88e01009818749c5443ea712'),
    ]

    known_unidentified_hashes = [
        # bad char in otherwise correct hash --\/
            '$3$$7f8fe03093cc84b267b109625f6bbfxb',
    ]

#=============================================================================
# oracle 10 & 11
#=============================================================================
class oracle10_test(UserHandlerMixin, HandlerCase):
    handler = hash.oracle10
    secret_case_insensitive = True
    user_case_insensitive = True

    # TODO: get more test vectors (especially ones which properly test unicode)
    known_correct_hashes = [
        # ((secret,user),hash)

        #
        # http://www.petefinnigan.com/default/default_password_list.htm
        #
        (('tiger', 'scott'), 'F894844C34402B67'),
        ((u('ttTiGGeR'), u('ScO')), '7AA1A84E31ED7771'),
        (("d_syspw", "SYSTEM"), '1B9F1F9A5CB9EB31'),
        (("strat_passwd", "strat_user"), 'AEBEDBB4EFB5225B'),

        #
        # http://openwall.info/wiki/john/sample-hashes
        #
        (('#95LWEIGHTS', 'USER'), '000EA4D72A142E29'),
        (('CIAO2010', 'ALFREDO'), 'EB026A76F0650F7B'),

        #
        # from JTR 1.7.9
        #
        (('GLOUGlou', 'Bob'), 'CDC6B483874B875B'),
        (('GLOUGLOUTER', 'bOB'), 'EF1F9139DB2D5279'),
        (('LONG_MOT_DE_PASSE_OUI', 'BOB'), 'EC8147ABB3373D53'),

        #
        # custom
        #
        ((UPASS_TABLE, 'System'), 'B915A853F297B281'),
    ]

    known_unidentified_hashes = [
        # bad char in hash --\
             'F894844C34402B6Z',
    ]

class oracle11_test(HandlerCase):
    handler = hash.oracle11
    # TODO: find more test vectors (especially ones which properly test unicode)
    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ("abc123", "S:5FDAB69F543563582BA57894FE1C1361FB8ED57B903603F2C52ED1B4D642"),
        ("SyStEm123!@#", "S:450F957ECBE075D2FA009BA822A9E28709FBC3DA82B44D284DDABEC14C42"),
        ("oracle", "S:3437FF72BD69E3FB4D10C750B92B8FB90B155E26227B9AB62D94F54E5951"),
        ("11g", "S:61CE616647A4F7980AFD7C7245261AF25E0AFE9C9763FCF0D54DA667D4E6"),
        ("11g", "S:B9E7556F53500C8C78A58F50F24439D79962DE68117654B6700CE7CC71CF"),

        #
        # source?
        #
        ("SHAlala", "S:2BFCFDF5895014EE9BB2B9BA067B01E0389BB5711B7B5F82B7235E9E182C"),

        #
        # custom
        #
        (UPASS_TABLE, 'S:51586343E429A6DF024B8F242F2E9F8507B1096FACD422E29142AA4974B0'),
    ]

#=============================================================================
# PHPass Portable Crypt
#=============================================================================
class phpass_test(HandlerCase):
    handler = hash.phpass

    known_correct_hashes = [
        #
        # from official 0.3 implementation
        # http://www.openwall.com/phpass/
        #
        ('test12345', '$P$9IQRaTwmfeRo7ud9Fh4E2PdI0S3r.L0'), # from the source

        #
        # from JTR 1.7.9
        #
        ('test1', '$H$9aaaaaSXBjgypwqm.JsMssPLiS8YQ00'),
        ('123456', '$H$9PE8jEklgZhgLmZl5.HYJAzfGCQtzi1'),
        ('123456', '$H$9pdx7dbOW3Nnt32sikrjAxYFjX8XoK1'),
        ('thisisalongertestPW', '$P$912345678LIjjb6PhecupozNBmDndU0'),
        ('JohnRipper', '$P$612345678si5M0DDyPpmRCmcltU/YW/'),
        ('JohnRipper', '$H$712345678WhEyvy1YWzT4647jzeOmo0'),
        ('JohnRipper', '$P$B12345678L6Lpt4BxNotVIMILOa9u81'),

        #
        # custom
        #
        ('', '$P$7JaFQsPzJSuenezefD/3jHgt5hVfNH0'),
        ('compL3X!', '$P$FiS0N5L672xzQx1rt1vgdJQRYKnQM9/'),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '$P$7SMy8VxnfsIy2Sxm7fJxDSdil.h7TW.'),
        ]

    known_malformed_hashes = [
        # bad char in otherwise correct hash
        #                            ---\/
        '$P$9IQRaTwmfeRo7ud9Fh4E2PdI0S3r!L0',
        ]

#=============================================================================
# plaintext
#=============================================================================
class plaintext_test(HandlerCase):
    # TODO: integrate EncodingHandlerMixin
    handler = hash.plaintext
    accepts_all_hashes = True

    known_correct_hashes = [
        ('',''),
        ('password', 'password'),

        # ensure unicode uses utf-8
        (UPASS_TABLE, UPASS_TABLE if PY3 else PASS_TABLE_UTF8),
        (PASS_TABLE_UTF8, UPASS_TABLE if PY3 else PASS_TABLE_UTF8),
    ]

#=============================================================================
# postgres_md5
#=============================================================================
class postgres_md5_test(UserHandlerMixin, HandlerCase):
    handler = hash.postgres_md5
    known_correct_hashes = [
        # ((secret,user),hash)

        #
        # generated using postgres 8.1
        #
        (('mypass', 'postgres'), 'md55fba2ea04fd36069d2574ea71c8efe9d'),
        (('mypass', 'root'), 'md540c31989b20437833f697e485811254b'),
        (("testpassword",'testuser'), 'md5d4fc5129cc2c25465a5370113ae9835f'),

        #
        # custom
        #

        # verify unicode->utf8
        ((UPASS_TABLE, 'postgres'), 'md5cb9f11283265811ce076db86d18a22d2'),
    ]
    known_unidentified_hashes = [
        # bad 'z' char in otherwise correct hash
        'md54zc31989b20437833f697e485811254b',
    ]

#=============================================================================
# (netbsd's) sha1 crypt
#=============================================================================
class _sha1_crypt_test(HandlerCase):
    handler = hash.sha1_crypt

    known_correct_hashes = [
        #
        # custom
        #
        ("password", "$sha1$19703$iVdJqfSE$v4qYKl1zqYThwpjJAoKX6UvlHq/a"),
        ("password", "$sha1$21773$uV7PTeux$I9oHnvwPZHMO0Nq6/WgyGV/tDJIH"),
        (UPASS_TABLE, '$sha1$40000$uJ3Sp7LE$.VEmLO5xntyRFYihC7ggd3297T/D'),
    ]

    known_malformed_hashes = [
        # bad char in otherwise correct hash
        '$sha1$21773$u!7PTeux$I9oHnvwPZHMO0Nq6/WgyGV/tDJIH',

        # zero padded rounds
        '$sha1$01773$uV7PTeux$I9oHnvwPZHMO0Nq6/WgyGV/tDJIH',

        # too many fields
        '$sha1$21773$uV7PTeux$I9oHnvwPZHMO0Nq6/WgyGV/tDJIH$',

        # empty rounds field
        '$sha1$$uV7PTeux$I9oHnvwPZHMO0Nq6/WgyGV/tDJIH$',
    ]

    platform_crypt_support = [
        ("netbsd", True),
        ("freebsd|openbsd|linux|solaris|darwin", False),
    ]

# create test cases for specific backends
sha1_crypt_os_crypt_test = _sha1_crypt_test.create_backend_case("os_crypt")
sha1_crypt_builtin_test = _sha1_crypt_test.create_backend_case("builtin")

#=============================================================================
# roundup
#=============================================================================

# NOTE: all roundup hashes use PrefixWrapper,
#       so there's nothing natively to test.
#       so we just have a few quick cases...

class RoundupTest(TestCase):

    def _test_pair(self, h, secret, hash):
        self.assertTrue(h.verify(secret, hash))
        self.assertFalse(h.verify('x'+secret, hash))

    def test_pairs(self):
        self._test_pair(
            hash.ldap_hex_sha1,
            "sekrit",
            '{SHA}8d42e738c7adee551324955458b5e2c0b49ee655')

        self._test_pair(
            hash.ldap_hex_md5,
            "sekrit",
            '{MD5}ccbc53f4464604e714f69dd11138d8b5')

        self._test_pair(
            hash.ldap_des_crypt,
            "sekrit",
            '{CRYPT}nFia0rj2TT59A')

        self._test_pair(
            hash.roundup_plaintext,
            "sekrit",
            '{plaintext}sekrit')

        self._test_pair(
            hash.ldap_pbkdf2_sha1,
            "sekrit",
            '{PBKDF2}5000$7BvbBq.EZzz/O0HuwX3iP.nAG3s$g3oPnFFaga2BJaX5PoPRljl4XIE')

#=============================================================================
# sha256-crypt
#=============================================================================
class _sha256_crypt_test(HandlerCase):
    handler = hash.sha256_crypt

    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ('U*U*U*U*', '$5$LKO/Ute40T3FNF95$U0prpBQd4PloSGU0pnpM4z9wKn4vZ1.jsrzQfPqxph9'),
        ('U*U***U', '$5$LKO/Ute40T3FNF95$fdgfoJEBoMajNxCv3Ru9LyQ0xZgv0OBMQoq80LQ/Qd.'),
        ('U*U***U*', '$5$LKO/Ute40T3FNF95$8Ry82xGnnPI/6HtFYnvPBTYgOL23sdMXn8C29aO.x/A'),
        ('*U*U*U*U', '$5$9mx1HkCz7G1xho50$O7V7YgleJKLUhcfk9pgzdh3RapEaWqMtEp9UUBAKIPA'),
        ('', '$5$kc7lRD1fpYg0g.IP$d7CMTcEqJyTXyeq8hTdu/jB/I6DGkoo62NXbHIR7S43'),

        #
        # custom tests
        #
        ('', '$5$rounds=10428$uy/jIAhCetNCTtb0$YWvUOXbkqlqhyoPMpN8BMe.ZGsGx2aBvxTvDFI613c3'),
        (' ', '$5$rounds=10376$I5lNtXtRmf.OoMd8$Ko3AI1VvTANdyKhBPavaRjJzNpSatKU6QVN9uwS9MH.'),
        ('test', '$5$rounds=11858$WH1ABM5sKhxbkgCK$aTQsjPkz0rBsH3lQlJxw9HDTDXPKBxC0LlVeV69P.t1'),
        ('Compl3X AlphaNu3meric', '$5$rounds=10350$o.pwkySLCzwTdmQX$nCMVsnF3TXWcBPOympBUUSQi6LGGloZoOsVJMGJ09UB'),
        ('4lpHa N|_|M3r1K W/ Cur5Es: #$%(*)(*%#', '$5$rounds=11944$9dhlu07dQMRWvTId$LyUI5VWkGFwASlzntk1RLurxX54LUhgAcJZIt0pYGT7'),
        (u('with unic\u00D6de'), '$5$rounds=1000$IbG0EuGQXw5EkMdP$LQ5AfPf13KufFsKtmazqnzSGZ4pxtUNw3woQ.ELRDF4'),
        ]

    if TEST_MODE("full"):
        # builtin alg was changed in 1.6, and had possibility of fencepost
        # errors near rounds that are multiples of 42. these hashes test rounds
        # 1004..1012 (42*24=1008 +/- 4) to ensure no mistakes were made.
        # (also relying on fuzz testing against os_crypt backend).
        known_correct_hashes.extend([
        ("secret", '$5$rounds=1004$nacl$oiWPbm.kQ7.jTCZoOtdv7/tO5mWv/vxw5yTqlBagVR7'),
        ("secret", '$5$rounds=1005$nacl$6Mo/TmGDrXxg.bMK9isRzyWH3a..6HnSVVsJMEX7ud/'),
        ("secret", '$5$rounds=1006$nacl$I46VwuAiUBwmVkfPFakCtjVxYYaOJscsuIeuZLbfKID'),
        ("secret", '$5$rounds=1007$nacl$9fY4j1AV3N/dV/YMUn1enRHKH.7nEL4xf1wWB6wfDD4'),
        ("secret", '$5$rounds=1008$nacl$CiFWCfn8ODmWs0I1xAdXFo09tM8jr075CyP64bu3by9'),
        ("secret", '$5$rounds=1009$nacl$QtpFX.CJHgVQ9oAjVYStxAeiU38OmFILWm684c6FyED'),
        ("secret", '$5$rounds=1010$nacl$ktAwXuT5WbjBW/0ZU1eNMpqIWY1Sm4twfRE1zbZyo.B'),
        ("secret", '$5$rounds=1011$nacl$QJWLBEhO9qQHyMx4IJojSN9sS41P1Yuz9REddxdO721'),
        ("secret", '$5$rounds=1012$nacl$mmf/k2PkbBF4VCtERgky3bEVavmLZKFwAcvxD1p3kV2'),
        ])

    known_malformed_hashes = [
        # bad char in otherwise correct hash
        '$5$rounds=10428$uy/:jIAhCetNCTtb0$YWvUOXbkqlqhyoPMpN8BMeZGsGx2aBvxTvDFI613c3',

        # zero-padded rounds
       '$5$rounds=010428$uy/jIAhCetNCTtb0$YWvUOXbkqlqhyoPMpN8BMe.ZGsGx2aBvxTvDFI613c3',

        # extra "$"
       '$5$rounds=10428$uy/jIAhCetNCTtb0$YWvUOXbkqlqhyoPMpN8BMe.ZGsGx2aBvxTvDFI613c3$',
    ]

    known_correct_configs = [
        # config, secret, result

        #
        # taken from official specification at http://www.akkadia.org/drepper/SHA-crypt.txt
        #
        ( "$5$saltstring", "Hello world!",
          "$5$saltstring$5B8vYYiY.CVt1RlTTf8KbXBH3hsxY/GNooZaBBGWEc5" ),
        ( "$5$rounds=10000$saltstringsaltstring", "Hello world!",
          "$5$rounds=10000$saltstringsaltst$3xv.VbSHBb41AL9AvLeujZkZRBAwqFMz2."
          "opqey6IcA" ),
        ( "$5$rounds=5000$toolongsaltstring", "This is just a test",
          "$5$rounds=5000$toolongsaltstrin$Un/5jzAHMgOGZ5.mWJpuVolil07guHPvOW8"
          "mGRcvxa5" ),
        ( "$5$rounds=1400$anotherlongsaltstring",
          "a very much longer text to encrypt.  This one even stretches over more"
          "than one line.",
          "$5$rounds=1400$anotherlongsalts$Rx.j8H.h8HjEDGomFU8bDkXm3XIUnzyxf12"
          "oP84Bnq1" ),
        ( "$5$rounds=77777$short",
          "we have a short salt string but not a short password",
          "$5$rounds=77777$short$JiO1O3ZpDAxGJeaDIuqCoEFysAe1mZNJRs3pw0KQRd/" ),
        ( "$5$rounds=123456$asaltof16chars..", "a short string",
          "$5$rounds=123456$asaltof16chars..$gP3VQ/6X7UUEW3HkBn2w1/Ptq2jxPyzV/"
          "cZKmF/wJvD" ),
        ( "$5$rounds=10$roundstoolow", "the minimum number is still observed",
          "$5$rounds=1000$roundstoolow$yfvwcWrQ8l/K0DAWyuPMDNHpIVlTQebY9l/gL97"
          "2bIC" ),
    ]

    filter_config_warnings = True # rounds too low, salt too small

    platform_crypt_support = [
        ("freebsd(9|1\d)|linux", True),
        ("freebsd8", None), # added in freebsd 8.3
        ("freebsd|openbsd|netbsd|darwin", False),
        # solaris - depends on policy
    ]

# create test cases for specific backends
sha256_crypt_os_crypt_test = _sha256_crypt_test.create_backend_case("os_crypt")
sha256_crypt_builtin_test = _sha256_crypt_test.create_backend_case("builtin")

#=============================================================================
# test sha512-crypt
#=============================================================================
class _sha512_crypt_test(HandlerCase):
    handler = hash.sha512_crypt

    known_correct_hashes = [
        #
        # from JTR 1.7.9
        #
        ('U*U*U*U*', "$6$LKO/Ute40T3FNF95$6S/6T2YuOIHY0N3XpLKABJ3soYcXD9mB7uVbtEZDj/LNscVhZoZ9DEH.sBciDrMsHOWOoASbNLTypH/5X26gN0"),
        ('U*U***U', "$6$LKO/Ute40T3FNF95$wK80cNqkiAUzFuVGxW6eFe8J.fSVI65MD5yEm8EjYMaJuDrhwe5XXpHDJpwF/kY.afsUs1LlgQAaOapVNbggZ1"),
        ('U*U***U*', "$6$LKO/Ute40T3FNF95$YS81pp1uhOHTgKLhSMtQCr2cDiUiN03Ud3gyD4ameviK1Zqz.w3oXsMgO6LrqmIEcG3hiqaUqHi/WEE2zrZqa/"),
        ('*U*U*U*U', "$6$OmBOuxFYBZCYAadG$WCckkSZok9xhp4U1shIZEV7CCVwQUwMVea7L3A77th6SaE9jOPupEMJB.z0vIWCDiN9WLh2m9Oszrj5G.gt330"),
        ('', "$6$ojWH1AiTee9x1peC$QVEnTvRVlPRhcLQCk/HnHaZmlGAAjCfrAN0FtOsOnUk5K5Bn/9eLHHiRzrTzaIKjW9NTLNIBUCtNVOowWS2mN."),

        #
        # custom tests
        #
        ('', '$6$rounds=11021$KsvQipYPWpr93wWP$v7xjI4X6vyVptJjB1Y02vZC5SaSijBkGmq1uJhPr3cvqvvkd42Xvo48yLVPFt8dvhCsnlUgpX.//Cxn91H4qy1'),
        (' ', '$6$rounds=11104$ED9SA4qGmd57Fq2m$q/.PqACDM/JpAHKmr86nkPzzuR5.YpYa8ZJJvI8Zd89ZPUYTJExsFEIuTYbM7gAGcQtTkCEhBKmp1S1QZwaXx0'),
        ('test', '$6$rounds=11531$G/gkPn17kHYo0gTF$Kq.uZBHlSBXyzsOJXtxJruOOH4yc0Is13uY7yK0PvAvXxbvc1w8DO1RzREMhKsc82K/Jh8OquV8FZUlreYPJk1'),
        ('Compl3X AlphaNu3meric', '$6$rounds=10787$wakX8nGKEzgJ4Scy$X78uqaX1wYXcSCtS4BVYw2trWkvpa8p7lkAtS9O/6045fK4UB2/Jia0Uy/KzCpODlfVxVNZzCCoV9s2hoLfDs/'),
        ('4lpHa N|_|M3r1K W/ Cur5Es: #$%(*)(*%#', '$6$rounds=11065$5KXQoE1bztkY5IZr$Jf6krQSUKKOlKca4hSW07MSerFFzVIZt/N3rOTsUgKqp7cUdHrwV8MoIVNCk9q9WL3ZRMsdbwNXpVk0gVxKtz1'),

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '$6$rounds=40000$PEZTJDiyzV28M3.m$GTlnzfzGB44DGd1XqlmC4erAJKCP.rhvLvrYxiT38htrNzVGBnplFOHjejUGVrCfusGWxLQCc3pFO0A/1jYYr0'),
        ]

    known_malformed_hashes = [
        # zero-padded rounds
        '$6$rounds=011021$KsvQipYPWpr93wWP$v7xjI4X6vyVptJjB1Y02vZC5SaSijBkGmq1uJhPr3cvqvvkd42Xvo48yLVPFt8dvhCsnlUgpX.//Cxn91H4qy1',
        # bad char in otherwise correct hash
        '$6$rounds=11021$KsvQipYPWpr9:wWP$v7xjI4X6vyVptJjB1Y02vZC5SaSijBkGmq1uJhPr3cvqvvkd42Xvo48yLVPFt8dvhCsnlUgpX.//Cxn91H4qy1',
    ]

    known_correct_configs = [
        # config, secret, result

        #
        # taken from official specification at http://www.akkadia.org/drepper/SHA-crypt.txt
        #
        ("$6$saltstring", "Hello world!",
        "$6$saltstring$svn8UoSVapNtMuq1ukKS4tPQd8iKwSMHWjl/O817G3uBnIFNjnQJu"
        "esI68u4OTLiBFdcbYEdFCoEOfaS35inz1" ),

      ( "$6$rounds=10000$saltstringsaltstring", "Hello world!",
        "$6$rounds=10000$saltstringsaltst$OW1/O6BYHV6BcXZu8QVeXbDWra3Oeqh0sb"
        "HbbMCVNSnCM/UrjmM0Dp8vOuZeHBy/YTBmSK6H9qs/y3RnOaw5v." ),

      ( "$6$rounds=5000$toolongsaltstring", "This is just a test",
        "$6$rounds=5000$toolongsaltstrin$lQ8jolhgVRVhY4b5pZKaysCLi0QBxGoNeKQ"
        "zQ3glMhwllF7oGDZxUhx1yxdYcz/e1JSbq3y6JMxxl8audkUEm0" ),

      ( "$6$rounds=1400$anotherlongsaltstring",
        "a very much longer text to encrypt.  This one even stretches over more"
        "than one line.",
        "$6$rounds=1400$anotherlongsalts$POfYwTEok97VWcjxIiSOjiykti.o/pQs.wP"
        "vMxQ6Fm7I6IoYN3CmLs66x9t0oSwbtEW7o7UmJEiDwGqd8p4ur1" ),

      ( "$6$rounds=77777$short",
        "we have a short salt string but not a short password",
        "$6$rounds=77777$short$WuQyW2YR.hBNpjjRhpYD/ifIw05xdfeEyQoMxIXbkvr0g"
        "ge1a1x3yRULJ5CCaUeOxFmtlcGZelFl5CxtgfiAc0" ),

      ( "$6$rounds=123456$asaltof16chars..", "a short string",
        "$6$rounds=123456$asaltof16chars..$BtCwjqMJGx5hrJhZywWvt0RLE8uZ4oPwc"
        "elCjmw2kSYu.Ec6ycULevoBK25fs2xXgMNrCzIMVcgEJAstJeonj1" ),

      ( "$6$rounds=10$roundstoolow", "the minimum number is still observed",
        "$6$rounds=1000$roundstoolow$kUMsbe306n21p9R.FRkW3IGn.S9NPN0x50YhH1x"
        "hLsPuWGsUSklZt58jaTfF4ZEQpyUNGc0dqbpBYYBaHHrsX." ),
    ]

    filter_config_warnings = True # rounds too low, salt too small

    platform_crypt_support = _sha256_crypt_test.platform_crypt_support

# create test cases for specific backends
sha512_crypt_os_crypt_test = _sha512_crypt_test.create_backend_case("os_crypt")
sha512_crypt_builtin_test = _sha512_crypt_test.create_backend_case("builtin")

#=============================================================================
# sun md5 crypt
#=============================================================================
class sun_md5_crypt_test(HandlerCase):
    handler = hash.sun_md5_crypt

    # TODO: this scheme needs some real test vectors, especially due to
    # the "bare salt" issue which plagued the official parser.
    known_correct_hashes = [
        #
        # http://forums.halcyoninc.com/showthread.php?t=258
        #
        ("Gpcs3_adm", "$md5$zrdhpMlZ$$wBvMOEqbSjU.hu5T2VEP01"),

        #
        # http://www.c0t0d0s0.org/archives/4453-Less-known-Solaris-features-On-passwords-Part-2-Using-stronger-password-hashing.html
        #
        ("aa12345678", "$md5$vyy8.OVF$$FY4TWzuauRl4.VQNobqMY."),

        #
        # http://www.cuddletech.com/blog/pivot/entry.php?id=778
        #
        ("this", "$md5$3UqYqndY$$6P.aaWOoucxxq.l00SS9k0"),

        #
        # http://compgroups.net/comp.unix.solaris/password-file-in-linux-and-solaris-8-9
        #
        ("passwd", "$md5$RPgLF6IJ$WTvAlUJ7MqH5xak2FMEwS/"),

        #
        # source: http://solaris-training.com/301_HTML/docs/deepdiv.pdf page 27
        # FIXME: password unknown
        # "$md5,rounds=8000$kS9FT1JC$$mnUrRO618lLah5iazwJ9m1"

        #
        # source: http://www.visualexams.com/310-303.htm
        # XXX: this has 9 salt chars unlike all other hashes. is that valid?
        # FIXME: password unknown
        # "$md5,rounds=2006$2amXesSj5$$kCF48vfPsHDjlKNXeEw7V."
        #

        #
        # custom
        #

        # ensures utf-8 used for unicode
        (UPASS_TABLE, '$md5,rounds=5000$10VYDzAA$$1arAVtMA3trgE1qJ2V0Ez1'),
        ]

    known_correct_configs = [
        # (config, secret, hash)

        #---------------------------
        # test salt string handling
        #
        # these tests attempt to verify that passlib is handling
        # the "bare salt" issue (see sun md5 crypt docs)
        # in a sane manner
        #---------------------------

        # config with "$" suffix, hash strings with "$$" suffix,
        # should all be treated the same, with one "$" added to salt digest.
        ("$md5$3UqYqndY$",
            "this", "$md5$3UqYqndY$$6P.aaWOoucxxq.l00SS9k0"),
        ("$md5$3UqYqndY$$.................DUMMY",
            "this", "$md5$3UqYqndY$$6P.aaWOoucxxq.l00SS9k0"),

        # config with no suffix, hash strings with "$" suffix,
        # should all be treated the same, and no suffix added to salt digest.
        # NOTE: this is just a guess re: config w/ no suffix,
        #       but otherwise there's no sane way to encode bare_salt=False
        #       within config string.
        ("$md5$3UqYqndY",
            "this", "$md5$3UqYqndY$HIZVnfJNGCPbDZ9nIRSgP1"),
        ("$md5$3UqYqndY$.................DUMMY",
            "this", "$md5$3UqYqndY$HIZVnfJNGCPbDZ9nIRSgP1"),
    ]

    known_malformed_hashes = [
        # unexpected end of hash
        "$md5,rounds=5000",

        # bad rounds
        "$md5,rounds=500A$xxxx",
        "$md5,rounds=0500$xxxx",
        "$md5,rounds=0$xxxx",

        # bad char in otherwise correct hash
        "$md5$RPgL!6IJ$WTvAlUJ7MqH5xak2FMEwS/",

        # digest too short
        "$md5$RPgLa6IJ$WTvAlUJ7MqH5xak2FMEwS",

        # digest too long
        "$md5$RPgLa6IJ$WTvAlUJ7MqH5xak2FMEwS/.",

        # 2+ "$" at end of salt in config
        # NOTE: not sure what correct behavior is, so forbidding format for now.
        "$md5$3UqYqndY$$",

        # 3+ "$" at end of salt in hash
        # NOTE: not sure what correct behavior is, so forbidding format for now.
        "$md5$RPgLa6IJ$$$WTvAlUJ7MqH5xak2FMEwS/",

        ]

    platform_crypt_support = [
        ("solaris", True),
        ("freebsd|openbsd|netbsd|linux|darwin", False),
    ]
    def do_verify(self, secret, hash):
        # Override to fake error for "$..." hash string listed in known_correct_configs (above)
        # These have to be hash strings, in order to test bare salt issue.
        if isinstance(hash, str) and hash.endswith("$.................DUMMY"):
            raise ValueError("pretending '$...' stub hash is config string")
        return self.handler.verify(secret, hash)

#=============================================================================
# unix disabled / fallback
#=============================================================================
class unix_disabled_test(HandlerCase):
    handler = hash.unix_disabled
#    accepts_all_hashes = True # TODO: turn this off.

    known_correct_hashes = [
        # everything should hash to "!" (or "*" on BSD),
        # and nothing should verify against either string
        ("password", "!"),
        (UPASS_TABLE, "*"),
    ]

    known_unidentified_hashes = [
        # should never identify anything crypt() could return...
        "$1$xxx",
        "abc",
        "./az",
        "{SHA}xxx",
    ]

    def test_76_hash_border(self):
        # so empty strings pass
        self.accepts_all_hashes = True
        super(unix_disabled_test, self).test_76_hash_border()

    def test_90_special(self):
        """test marker option & special behavior"""
        warnings.filterwarnings("ignore", "passing settings to .*.hash\(\) is deprecated")
        handler = self.handler

        # preserve hash if provided
        self.assertEqual(handler.genhash("stub", "!asd"), "!asd")

        # use marker if no hash
        self.assertEqual(handler.genhash("stub", ""), handler.default_marker)
        self.assertEqual(handler.hash("stub"), handler.default_marker)
        self.assertEqual(handler.using().default_marker, handler.default_marker)

        # custom marker
        self.assertEqual(handler.genhash("stub", "", marker="*xxx"), "*xxx")
        self.assertEqual(handler.hash("stub", marker="*xxx"), "*xxx")
        self.assertEqual(handler.using(marker="*xxx").hash("stub"), "*xxx")

        # reject invalid marker
        self.assertRaises(ValueError, handler.genhash, 'stub', "", marker='abc')
        self.assertRaises(ValueError, handler.hash, 'stub', marker='abc')
        self.assertRaises(ValueError, handler.using, marker='abc')

class unix_fallback_test(HandlerCase):
    handler = hash.unix_fallback
    accepts_all_hashes = True

    known_correct_hashes = [
        # *everything* should hash to "!", and nothing should verify
        ("password", "!"),
        (UPASS_TABLE, "!"),
    ]

    # silence annoying deprecation warning
    def setUp(self):
        super(unix_fallback_test, self).setUp()
        warnings.filterwarnings("ignore", "'unix_fallback' is deprecated")

    def test_90_wildcard(self):
        """test enable_wildcard flag"""
        h = self.handler
        self.assertTrue(h.verify('password','', enable_wildcard=True))
        self.assertFalse(h.verify('password',''))
        for c in "!*x":
            self.assertFalse(h.verify('password',c, enable_wildcard=True))
            self.assertFalse(h.verify('password',c))

    def test_91_preserves_existing(self):
        """test preserves existing disabled hash"""
        handler = self.handler

        # use marker if no hash
        self.assertEqual(handler.genhash("stub", ""), "!")
        self.assertEqual(handler.hash("stub"), "!")

        # use hash if provided and valid
        self.assertEqual(handler.genhash("stub", "!asd"), "!asd")

#=============================================================================
# eof
#=============================================================================
