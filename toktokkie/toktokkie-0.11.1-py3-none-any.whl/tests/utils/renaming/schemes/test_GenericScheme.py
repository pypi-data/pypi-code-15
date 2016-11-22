"""
LICENSE:
Copyright 2015,2016 Hermann Krumrey

This file is part of toktokkie.

    toktokkie is a program that allows convenient managing of various
    local media collections, mostly focused on video.

    toktokkie is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    toktokkie is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with toktokkie.  If not, see <http://www.gnu.org/licenses/>.
LICENSE
"""

# imports
import unittest
from toktokkie.utils.renaming.schemes.GenericScheme import GenericScheme


class GenericSchemeUnitTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_tvdb_episode_name(self):
        self.assertEqual(GenericScheme.get_tvdb_episode_name("Game of Thrones", 1, 1), "Winter Is Coming")
        self.assertEqual(GenericScheme.get_tvdb_episode_name("Game of Thrones", 1, 11), "Episode 11")
        self.assertEqual(GenericScheme.get_tvdb_episode_name("Show does not exist", 1, 1), "Episode 1")
        self.assertEqual(GenericScheme.get_tvdb_episode_name("Game of Thrones", -1, 1), "Episode 1")
        self.assertEqual(GenericScheme.get_tvdb_episode_name("Game of Thrones", 1, -1), "Episode -1")

    def abstract_method(self):
        try:
            GenericScheme("", 0, 0).apply_scheme()
            self.assertTrue(False)
        except NotImplementedError:
            pass

        try:
            GenericScheme("", 0, 0).generate_episode_name()
            self.assertTrue(False)
        except NotImplementedError:
            pass
