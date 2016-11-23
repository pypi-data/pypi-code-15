"""passlib.tests -- unittests for passlib.crypto.des"""
#=============================================================================
# imports
#=============================================================================
from __future__ import with_statement, division
# core
from functools import partial
# site
# pkg
# module
from passlib.utils import getrandbytes
from passlib.tests.utils import TestCase

#=============================================================================
# test DES routines
#=============================================================================
class DesTest(TestCase):
    descriptionPrefix = "passlib.crypto.des"

    # test vectors taken from http://www.skepticfiles.org/faq/testdes.htm
    des_test_vectors = [
        # key, plaintext, ciphertext
        (0x0000000000000000, 0x0000000000000000, 0x8CA64DE9C1B123A7),
        (0xFFFFFFFFFFFFFFFF, 0xFFFFFFFFFFFFFFFF, 0x7359B2163E4EDC58),
        (0x3000000000000000, 0x1000000000000001, 0x958E6E627A05557B),
        (0x1111111111111111, 0x1111111111111111, 0xF40379AB9E0EC533),
        (0x0123456789ABCDEF, 0x1111111111111111, 0x17668DFC7292532D),
        (0x1111111111111111, 0x0123456789ABCDEF, 0x8A5AE1F81AB8F2DD),
        (0x0000000000000000, 0x0000000000000000, 0x8CA64DE9C1B123A7),
        (0xFEDCBA9876543210, 0x0123456789ABCDEF, 0xED39D950FA74BCC4),
        (0x7CA110454A1A6E57, 0x01A1D6D039776742, 0x690F5B0D9A26939B),
        (0x0131D9619DC1376E, 0x5CD54CA83DEF57DA, 0x7A389D10354BD271),
        (0x07A1133E4A0B2686, 0x0248D43806F67172, 0x868EBB51CAB4599A),
        (0x3849674C2602319E, 0x51454B582DDF440A, 0x7178876E01F19B2A),
        (0x04B915BA43FEB5B6, 0x42FD443059577FA2, 0xAF37FB421F8C4095),
        (0x0113B970FD34F2CE, 0x059B5E0851CF143A, 0x86A560F10EC6D85B),
        (0x0170F175468FB5E6, 0x0756D8E0774761D2, 0x0CD3DA020021DC09),
        (0x43297FAD38E373FE, 0x762514B829BF486A, 0xEA676B2CB7DB2B7A),
        (0x07A7137045DA2A16, 0x3BDD119049372802, 0xDFD64A815CAF1A0F),
        (0x04689104C2FD3B2F, 0x26955F6835AF609A, 0x5C513C9C4886C088),
        (0x37D06BB516CB7546, 0x164D5E404F275232, 0x0A2AEEAE3FF4AB77),
        (0x1F08260D1AC2465E, 0x6B056E18759F5CCA, 0xEF1BF03E5DFA575A),
        (0x584023641ABA6176, 0x004BD6EF09176062, 0x88BF0DB6D70DEE56),
        (0x025816164629B007, 0x480D39006EE762F2, 0xA1F9915541020B56),
        (0x49793EBC79B3258F, 0x437540C8698F3CFA, 0x6FBF1CAFCFFD0556),
        (0x4FB05E1515AB73A7, 0x072D43A077075292, 0x2F22E49BAB7CA1AC),
        (0x49E95D6D4CA229BF, 0x02FE55778117F12A, 0x5A6B612CC26CCE4A),
        (0x018310DC409B26D6, 0x1D9D5C5018F728C2, 0x5F4C038ED12B2E41),
        (0x1C587F1C13924FEF, 0x305532286D6F295A, 0x63FAC0D034D9F793),
        (0x0101010101010101, 0x0123456789ABCDEF, 0x617B3A0CE8F07100),
        (0x1F1F1F1F0E0E0E0E, 0x0123456789ABCDEF, 0xDB958605F8C8C606),
        (0xE0FEE0FEF1FEF1FE, 0x0123456789ABCDEF, 0xEDBFD1C66C29CCC7),
        (0x0000000000000000, 0xFFFFFFFFFFFFFFFF, 0x355550B2150E2451),
        (0xFFFFFFFFFFFFFFFF, 0x0000000000000000, 0xCAAAAF4DEAF1DBAE),
        (0x0123456789ABCDEF, 0x0000000000000000, 0xD5D44FF720683D0D),
        (0xFEDCBA9876543210, 0xFFFFFFFFFFFFFFFF, 0x2A2BB008DF97C2F2),
    ]

    def test_01_expand(self):
        """expand_des_key()"""
        from passlib.crypto.des import expand_des_key, shrink_des_key, \
                                             _KDATA_MASK, INT_56_MASK

        # make sure test vectors are preserved (sans parity bits)
        # uses ints, bytes are tested under # 02
        for key1, _, _ in self.des_test_vectors:
            key2 = shrink_des_key(key1)
            key3 = expand_des_key(key2)
            # NOTE: this assumes expand_des_key() sets parity bits to 0
            self.assertEqual(key3, key1 & _KDATA_MASK)

        # type checks
        self.assertRaises(TypeError, expand_des_key, 1.0)

        # too large
        self.assertRaises(ValueError, expand_des_key, INT_56_MASK+1)
        self.assertRaises(ValueError, expand_des_key, b"\x00"*8)

        # too small
        self.assertRaises(ValueError, expand_des_key, -1)
        self.assertRaises(ValueError, expand_des_key, b"\x00"*6)

    def test_02_shrink(self):
        """shrink_des_key()"""
        from passlib.crypto.des import expand_des_key, shrink_des_key, INT_64_MASK
        rng = self.getRandom()

        # make sure reverse works for some random keys
        # uses bytes, ints are tested under # 01
        for i in range(20):
            key1 = getrandbytes(rng, 7)
            key2 = expand_des_key(key1)
            key3 = shrink_des_key(key2)
            self.assertEqual(key3, key1)

        # type checks
        self.assertRaises(TypeError, shrink_des_key, 1.0)

        # too large
        self.assertRaises(ValueError, shrink_des_key, INT_64_MASK+1)
        self.assertRaises(ValueError, shrink_des_key, b"\x00"*9)

        # too small
        self.assertRaises(ValueError, shrink_des_key, -1)
        self.assertRaises(ValueError, shrink_des_key, b"\x00"*7)

    def _random_parity(self, key):
        """randomize parity bits"""
        from passlib.crypto.des import _KDATA_MASK, _KPARITY_MASK, INT_64_MASK
        rng = self.getRandom()
        return (key & _KDATA_MASK) | (rng.randint(0,INT_64_MASK) & _KPARITY_MASK)

    def test_03_encrypt_bytes(self):
        """des_encrypt_block()"""
        from passlib.crypto.des import (des_encrypt_block, shrink_des_key,
                                              _pack64, _unpack64)

        # run through test vectors
        for key, plaintext, correct in self.des_test_vectors:
            # convert to bytes
            key = _pack64(key)
            plaintext = _pack64(plaintext)
            correct = _pack64(correct)

            # test 64-bit key
            result = des_encrypt_block(key, plaintext)
            self.assertEqual(result, correct, "key=%r plaintext=%r:" %
                                              (key, plaintext))

            # test 56-bit version
            key2 = shrink_des_key(key)
            result = des_encrypt_block(key2, plaintext)
            self.assertEqual(result, correct, "key=%r shrink(key)=%r plaintext=%r:" %
                                              (key, key2, plaintext))

            # test with random parity bits
            for _ in range(20):
                key3 = _pack64(self._random_parity(_unpack64(key)))
                result = des_encrypt_block(key3, plaintext)
                self.assertEqual(result, correct, "key=%r rndparity(key)=%r plaintext=%r:" %
                                                  (key, key3, plaintext))

        # check invalid keys
        stub = b'\x00' * 8
        self.assertRaises(TypeError, des_encrypt_block, 0, stub)
        self.assertRaises(ValueError, des_encrypt_block, b'\x00'*6, stub)

        # check invalid input
        self.assertRaises(TypeError, des_encrypt_block, stub, 0)
        self.assertRaises(ValueError, des_encrypt_block, stub, b'\x00'*7)

        # check invalid salts
        self.assertRaises(ValueError, des_encrypt_block, stub, stub, salt=-1)
        self.assertRaises(ValueError, des_encrypt_block, stub, stub, salt=1<<24)

        # check invalid rounds
        self.assertRaises(ValueError, des_encrypt_block, stub, stub, 0, rounds=0)

    def test_04_encrypt_ints(self):
        """des_encrypt_int_block()"""
        from passlib.crypto.des import des_encrypt_int_block

        # run through test vectors
        for key, plaintext, correct in self.des_test_vectors:
            # test 64-bit key
            result = des_encrypt_int_block(key, plaintext)
            self.assertEqual(result, correct, "key=%r plaintext=%r:" %
                                              (key, plaintext))

            # test with random parity bits
            for _ in range(20):
                key3 = self._random_parity(key)
                result = des_encrypt_int_block(key3, plaintext)
                self.assertEqual(result, correct, "key=%r rndparity(key)=%r plaintext=%r:" %
                                                  (key, key3, plaintext))

        # check invalid keys
        self.assertRaises(TypeError, des_encrypt_int_block, b'\x00', 0)
        self.assertRaises(ValueError, des_encrypt_int_block, -1, 0)

        # check invalid input
        self.assertRaises(TypeError, des_encrypt_int_block, 0, b'\x00')
        self.assertRaises(ValueError, des_encrypt_int_block, 0, -1)

        # check invalid salts
        self.assertRaises(ValueError, des_encrypt_int_block, 0, 0, salt=-1)
        self.assertRaises(ValueError, des_encrypt_int_block, 0, 0, salt=1<<24)

        # check invalid rounds
        self.assertRaises(ValueError, des_encrypt_int_block, 0, 0, 0, rounds=0)

#=============================================================================
# eof
#=============================================================================
