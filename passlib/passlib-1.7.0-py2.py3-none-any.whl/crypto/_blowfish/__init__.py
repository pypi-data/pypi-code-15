"""passlib.crypto._blowfish - pure-python eks-blowfish implementation for bcrypt

This is a pure-python implementation of the EKS-Blowfish algorithm described by
Provos and Mazieres in `A Future-Adaptable Password Scheme
<http://www.openbsd.org/papers/bcrypt-paper.ps>`_.

This package contains two submodules:

* ``_blowfish/base.py`` contains a class implementing the eks-blowfish algorithm
  using easy-to-examine code.

* ``_blowfish/unrolled.py`` contains a subclass which replaces some methods
  of the original class with sped-up versions, mainly using unrolled loops
  and local variables. this is the class which is actually used by
  Passlib to perform BCrypt in pure python.

  This module is auto-generated by a script, ``_blowfish/_gen_files.py``.

Status
------
This implementation is usable, but is an order of magnitude too slow to be
usable with real security. For "ok" security, BCrypt hashes should have at
least 2**11 rounds (as of 2011). Assuming a desired response time <= 100ms,
this means a BCrypt implementation should get at least 20 rounds/ms in order
to be both usable *and* secure. On a 2 ghz cpu, this implementation gets
roughly 0.09 rounds/ms under CPython (220x too slow), and 1.9 rounds/ms
under PyPy (10x too slow).

History
-------
While subsequently modified considerly for Passlib, this code was originally
based on `jBcrypt 0.2 <http://www.mindrot.org/projects/jBCrypt/>`_, which was
released under the BSD license::

    Copyright (c) 2006 Damien Miller <djm@mindrot.org>

    Permission to use, copy, modify, and distribute this software for any
    purpose with or without fee is hereby granted, provided that the above
    copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
#=============================================================================
# imports
#=============================================================================
# core
from itertools import chain
import struct
# pkg
from passlib.utils import getrandbytes, rng
from passlib.utils.binary import bcrypt64
from passlib.utils.compat import BytesIO, unicode, u, native_string_types
from passlib.crypto._blowfish.unrolled import BlowfishEngine
# local
__all__ = [
    'BlowfishEngine',
    'raw_bcrypt',
]

#=============================================================================
# bcrypt constants
#=============================================================================

# bcrypt constant data "OrpheanBeholderScryDoubt" as 6 integers
BCRYPT_CDATA = [
    0x4f727068, 0x65616e42, 0x65686f6c,
    0x64657253, 0x63727944, 0x6f756274
]

# struct used to encode ciphertext as digest (last output byte discarded)
digest_struct = struct.Struct(">6I")

#=============================================================================
# base bcrypt helper
#
# interface designed only for use by passlib.handlers.bcrypt:BCrypt
# probably not suitable for other purposes
#=============================================================================
BNULL = b'\x00'

def raw_bcrypt(password, ident, salt, log_rounds):
    """perform central password hashing step in bcrypt scheme.

    :param password: the password to hash
    :param ident: identifier w/ minor version (e.g. 2, 2a)
    :param salt: the binary salt to use (encoded in bcrypt-base64)
    :param log_rounds: the log2 of the number of rounds (as int)
    :returns: bcrypt-base64 encoded checksum
    """
    #===================================================================
    # parse inputs
    #===================================================================

    # parse ident
    assert isinstance(ident, native_string_types)
    add_null_padding = True
    if ident == u('2a') or ident == u('2y') or ident == u('2b'):
        pass
    elif ident == u('2'):
        add_null_padding = False
    elif ident == u('2x'):
        raise ValueError("crypt_blowfish's buggy '2x' hashes are not "
                         "currently supported")
    else:
        raise ValueError("unknown ident: %r" % (ident,))

    # decode & validate salt
    assert isinstance(salt, bytes)
    salt = bcrypt64.decode_bytes(salt)
    if len(salt) < 16:
        raise ValueError("Missing salt bytes")
    elif len(salt) > 16:
        salt = salt[:16]

    # prepare password
    assert isinstance(password, bytes)
    if add_null_padding:
        password += BNULL

    # validate rounds
    if log_rounds < 4 or log_rounds > 31:
        raise ValueError("Bad number of rounds")

    #===================================================================
    #
    # run EKS-Blowfish algorithm
    #
    # This uses the "enhanced key schedule" step described by
    # Provos and Mazieres in "A Future-Adaptable Password Scheme"
    # http://www.openbsd.org/papers/bcrypt-paper.ps
    #
    #===================================================================

    engine = BlowfishEngine()

    # convert password & salt into list of 18 32-bit integers (72 bytes total).
    pass_words = engine.key_to_words(password)
    salt_words = engine.key_to_words(salt)

    # truncate salt_words to original 16 byte salt, or loop won't wrap
    # correctly when passed to .eks_salted_expand()
    salt_words16 = salt_words[:4]

    # do EKS key schedule setup
    engine.eks_salted_expand(pass_words, salt_words16)

    # apply password & salt keys to key schedule a bunch more times.
    rounds = 1<<log_rounds
    engine.eks_repeated_expand(pass_words, salt_words, rounds)

    # encipher constant data, and encode to bytes as digest.
    data = list(BCRYPT_CDATA)
    i = 0
    while i < 6:
        data[i], data[i+1] = engine.repeat_encipher(data[i], data[i+1], 64)
        i += 2
    raw = digest_struct.pack(*data)[:-1]
    return bcrypt64.encode_bytes(raw)

#=============================================================================
# eof
#=============================================================================
