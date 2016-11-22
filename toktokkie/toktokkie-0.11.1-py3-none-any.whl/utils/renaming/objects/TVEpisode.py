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
import os
import shutil
from toktokkie.utils.renaming.schemes.GenericScheme import GenericScheme


class TVEpisode(object):
    """
    TV Episode Object, containing important episode info used for renaming an episode file
    """

    def __init__(self, episode_file: str, episode_number: int, season_number: int, show_name: str,
                 naming_scheme: GenericScheme) -> None:
        """
        Constructor for the TVEpisode class, getting information about the Episode
        via the method parameters and generating the new episode name using a provided
        naming scheme

        :param episode_file:   the current episode file path
        :param episode_number: the episode number
        :param season_number:  the season number
        :param show_name: the  show name
        :param naming_scheme:  the naming scheme with which the new episode name is generated
        """

        # Store data about the episode in class variables
        self.episode_file = episode_file
        self.episode_number = episode_number
        self.season_number = season_number
        self.show_name = show_name
        self.old_name = os.path.basename(episode_file).rsplit(".", 1)[0]

        # noinspection PyCallingNonCallable
        renamer = naming_scheme(self.show_name, self.season_number, self.episode_number)
        self.new_name = renamer.generate_episode_name()

    def rename(self) -> None:
        """
        Renames the original file to the new name generated with help of the naming scheme

        :raise IOError, OSError:  if the episode file does not exist, which of course should not happen
                                  under normal circumstances
        :return:                  None
        """
        if not self.new_name == self.old_name:

            original_file_name = os.path.basename(self.episode_file)
            extension = os.path.splitext(original_file_name)[1]
            new_file = os.path.join(os.path.dirname(self.episode_file), self.new_name + extension)

            shutil.move(self.episode_file, new_file)

            self.episode_file = new_file

    def get_old_name(self) -> str:
        """
        :return: The old episode name
        """
        return self.old_name

    def get_new_name(self) -> str:
        """
        :return: The new episode name
        """
        return self.new_name
