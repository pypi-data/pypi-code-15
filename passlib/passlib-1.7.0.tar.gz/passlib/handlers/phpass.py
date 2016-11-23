"""passlib.handlers.phpass - PHPass Portable Crypt

phppass located - http://www.openwall.com/phpass/
algorithm described - http://www.openwall.com/articles/PHP-Users-Passwords

phpass context - blowfish, bsdi_crypt, phpass
"""
#=============================================================================
# imports
#=============================================================================
# core
from hashlib import md5
import logging; log = logging.getLogger(__name__)
# site
# pkg
from passlib.utils.binary import h64
from passlib.utils.compat import u, uascii_to_str, unicode
import passlib.utils.handlers as uh
# local
__all__ = [
    "phpass",
]

#=============================================================================
# phpass
#=============================================================================
class phpass(uh.HasManyIdents, uh.HasRounds, uh.HasSalt, uh.GenericHandler):
    """This class implements the PHPass Portable Hash, and follows the :ref:`password-hash-api`.

    It supports a fixed-length salt, and a variable number of rounds.

    The :meth:`~passlib.ifc.PasswordHash.using` method accepts the following optional keywords:

    :type salt: str
    :param salt:
        Optional salt string.
        If not specified, one will be autogenerated (this is recommended).
        If specified, it must be 8 characters, drawn from the regexp range ``[./0-9A-Za-z]``.

    :type rounds: int
    :param rounds:
        Optional number of rounds to use.
        Defaults to 19, must be between 7 and 30, inclusive.
        This value is logarithmic, the actual number of iterations used will be :samp:`2**{rounds}`.

    :type ident: str
    :param ident:
        phpBB3 uses ``H`` instead of ``P`` for its identifier,
        this may be set to ``H`` in order to generate phpBB3 compatible hashes.
        it defaults to ``P``.

    :type relaxed: bool
    :param relaxed:
        By default, providing an invalid value for one of the other
        keywords will result in a :exc:`ValueError`. If ``relaxed=True``,
        and the error can be corrected, a :exc:`~passlib.exc.PasslibHashWarning`
        will be issued instead. Correctable errors include ``rounds``
        that are too small or too large, and ``salt`` strings that are too long.

        .. versionadded:: 1.6
    """

    #===================================================================
    # class attrs
    #===================================================================
    #--GenericHandler--
    name = "phpass"
    setting_kwds = ("salt", "rounds", "ident")
    checksum_chars = uh.HASH64_CHARS

    #--HasSalt--
    min_salt_size = max_salt_size = 8
    salt_chars = uh.HASH64_CHARS

    #--HasRounds--
    default_rounds = 19
    min_rounds = 7
    max_rounds = 30
    rounds_cost = "log2"

    #--HasManyIdents--
    default_ident = u("$P$")
    ident_values = (u("$P$"), u("$H$"))
    ident_aliases = {u("P"):u("$P$"), u("H"):u("$H$")}

    #===================================================================
    # formatting
    #===================================================================

    #$P$9IQRaTwmfeRo7ud9Fh4E2PdI0S3r.L0
    # $P$
    # 9
    # IQRaTwmf
    # eRo7ud9Fh4E2PdI0S3r.L0

    @classmethod
    def from_string(cls, hash):
        ident, data = cls._parse_ident(hash)
        rounds, salt, chk = data[0], data[1:9], data[9:]
        return cls(
            ident=ident,
            rounds=h64.decode_int6(rounds.encode("ascii")),
            salt=salt,
            checksum=chk or None,
        )

    def to_string(self):
        hash = u("%s%s%s%s") % (self.ident,
                              h64.encode_int6(self.rounds).decode("ascii"),
                              self.salt,
                              self.checksum or u(''))
        return uascii_to_str(hash)

    #===================================================================
    # backend
    #===================================================================
    def _calc_checksum(self, secret):
        # FIXME: can't find definitive policy on how phpass handles non-ascii.
        if isinstance(secret, unicode):
            secret = secret.encode("utf-8")
        real_rounds = 1<<self.rounds
        result = md5(self.salt.encode("ascii") + secret).digest()
        r = 0
        while r < real_rounds:
            result = md5(result + secret).digest()
            r += 1
        return h64.encode_bytes(result).decode("ascii")

    #===================================================================
    # eoc
    #===================================================================

#=============================================================================
# eof
#=============================================================================
