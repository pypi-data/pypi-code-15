import time
import unittest
import common

from trezorlib import messages_pb2 as proto
from trezorlib import types_pb2 as proto_types

class TestMsgChangepin(common.TrezorTest):

    def test_set_pin(self):
        self.setup_mnemonic_nopin_nopassphrase()
        features = self.client.call_raw(proto.Initialize())
        self.assertFalse(features.pin_protection)

        # Check that there's no PIN protection
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.Success)

        # Let's set new PIN
        ret = self.client.call_raw(proto.ChangePin())
        self.assertIsInstance(ret, proto.ButtonRequest)

        # Press button
        self.client.debug.press_yes()
        ret = self.client.call_raw(proto.ButtonAck())

        # Send the PIN for first time
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin6)
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Send the PIN for second time
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin6)
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Now we're done
        self.assertIsInstance(ret, proto.Success)

        # Check that there's PIN protection now
        features = self.client.call_raw(proto.Initialize())
        self.assertTrue(features.pin_protection)
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        self.client.call_raw(proto.Cancel())

        # Check that the PIN is correct
        self.assertEqual(self.client.debug.read_pin()[0], self.pin6)

    def test_change_pin(self):
        self.setup_mnemonic_pin_passphrase()
        features = self.client.call_raw(proto.Initialize())
        self.assertTrue(features.pin_protection)

        # Check that there's PIN protection
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        self.client.call_raw(proto.Cancel())

        # Check current PIN value
        self.assertEqual(self.client.debug.read_pin()[0], self.pin4)

        # Let's change PIN
        ret = self.client.call_raw(proto.ChangePin())
        self.assertIsInstance(ret, proto.ButtonRequest)

        # Press button
        self.client.debug.press_yes()
        ret = self.client.call_raw(proto.ButtonAck())

        # Send current PIN
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.read_pin_encoded()
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Send new PIN for first time
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin6)
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Send the PIN for second time
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin6)
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Now we're done
        self.assertIsInstance(ret, proto.Success)

        # Check that there's still PIN protection now
        features = self.client.call_raw(proto.Initialize())
        self.assertTrue(features.pin_protection)
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        self.client.call_raw(proto.Cancel())

        # Check that the PIN is correct
        self.assertEqual(self.client.debug.read_pin()[0], self.pin6)

    def test_remove_pin(self):
        self.setup_mnemonic_pin_passphrase()
        features = self.client.call_raw(proto.Initialize())
        self.assertTrue(features.pin_protection)

        # Check that there's PIN protection
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        self.client.call_raw(proto.Cancel())

        # Let's remove PIN
        ret = self.client.call_raw(proto.ChangePin(remove=True))
        self.assertIsInstance(ret, proto.ButtonRequest)

        # Press button
        self.client.debug.press_yes()
        ret = self.client.call_raw(proto.ButtonAck())

        # Send current PIN
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.read_pin_encoded()
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Now we're done
        self.assertIsInstance(ret, proto.Success)

        # Check that there's no PIN protection now
        features = self.client.call_raw(proto.Initialize())
        self.assertFalse(features.pin_protection)
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.Success)

    def test_set_failed(self):
        self.setup_mnemonic_nopin_nopassphrase()
        features = self.client.call_raw(proto.Initialize())
        self.assertFalse(features.pin_protection)

        # Check that there's no PIN protection
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.Success)

        # Let's set new PIN
        ret = self.client.call_raw(proto.ChangePin())
        self.assertIsInstance(ret, proto.ButtonRequest)

        # Press button
        self.client.debug.press_yes()
        ret = self.client.call_raw(proto.ButtonAck())

        # Send the PIN for first time
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin6)
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Send the PIN for second time, but with typo
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin4)
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Now it should fail, because pins are different
        self.assertIsInstance(ret, proto.Failure)

        # Check that there's still no PIN protection now
        features = self.client.call_raw(proto.Initialize())
        self.assertFalse(features.pin_protection)
        ret = self.client.call_raw(proto.Ping(pin_protection=True))
        self.assertIsInstance(ret, proto.Success)

    def test_set_failed_2(self):
        self.setup_mnemonic_pin_passphrase()
        features = self.client.call_raw(proto.Initialize())
        self.assertTrue(features.pin_protection)

        # Let's set new PIN
        ret = self.client.call_raw(proto.ChangePin())
        self.assertIsInstance(ret, proto.ButtonRequest)

        # Press button
        self.client.debug.press_yes()
        ret = self.client.call_raw(proto.ButtonAck())

        # Send current PIN
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.read_pin_encoded()
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Send the PIN for first time
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin6)
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Send the PIN for second time, but with typo
        self.assertIsInstance(ret, proto.PinMatrixRequest)
        pin_encoded = self.client.debug.encode_pin(self.pin6 + '3')
        ret = self.client.call_raw(proto.PinMatrixAck(pin=pin_encoded))

        # Now it should fail, because pins are different
        self.assertIsInstance(ret, proto.Failure)

        # Check that there's still old PIN protection
        features = self.client.call_raw(proto.Initialize())
        self.assertTrue(features.pin_protection)
        self.assertEqual(self.client.debug.read_pin()[0], self.pin4)

if __name__ == '__main__':
    unittest.main()
