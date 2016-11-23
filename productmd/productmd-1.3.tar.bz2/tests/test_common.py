#!/usr/bin/python
# -*- coding: utf-8 -*-


# Copyright (C) 2015  Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


import unittest

import os
import sys

DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(DIR, ".."))

from productmd.common import is_valid_release_short, is_valid_release_version  # noqa
from productmd.common import split_version  # noqa
from productmd.common import create_release_id  # noqa


class TestRelease(unittest.TestCase):

    def test_valid_short(self):
        self.assertTrue(is_valid_release_short("f"))
        self.assertFalse(is_valid_release_short("F"))

        self.assertTrue(is_valid_release_short("fedora"))
        self.assertFalse(is_valid_release_short("Fedora"))

        self.assertTrue(is_valid_release_short("fedora-server"))
        self.assertTrue(is_valid_release_short("fedora-server-23"))

        self.assertTrue(is_valid_release_short("f23"))
        self.assertFalse(is_valid_release_short("23f"))

        self.assertFalse(is_valid_release_short("-"))
        self.assertFalse(is_valid_release_short("f-"))
        self.assertTrue(is_valid_release_short("f-23"))
        self.assertFalse(is_valid_release_short("f--23"))
        self.assertFalse(is_valid_release_short("f.23"))

    def test_valid_version(self):
        self.assertTrue(is_valid_release_version("0"))
        self.assertTrue(is_valid_release_version("1"))

        self.assertTrue(is_valid_release_version("1.0"))
        self.assertTrue(is_valid_release_version("1.1"))

        self.assertTrue(is_valid_release_version("a"))
        self.assertFalse(is_valid_release_version("1.a"))
        self.assertFalse(is_valid_release_version("1.1a"))

        self.assertFalse(is_valid_release_version(""))

        self.assertFalse(is_valid_release_version("1."))
        self.assertFalse(is_valid_release_version("1.."))
        self.assertFalse(is_valid_release_version("1.1."))
        self.assertFalse(is_valid_release_version("1..1"))

        self.assertTrue(is_valid_release_version("rawhide"))

    def test_split_version(self):
        self.assertEqual(split_version("0"), [0])
        self.assertEqual(split_version("1.0"), [1, 0])

        self.assertEqual(split_version("rawhide"), ["rawhide"])
        self.assertEqual(split_version("rawhide.23"), ["rawhide.23"])

    def test_create_release_id(self):
        self.assertEqual(create_release_id("f", "23", "ga"), "f-23")
        self.assertEqual(create_release_id("f", "23", "updates"), "f-23-updates")
        self.assertRaises(ValueError, create_release_id, "f", "23", None)


if __name__ == "__main__":
    unittest.main()
