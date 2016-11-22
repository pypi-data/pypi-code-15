u"""
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
from __future__ import absolute_import
import os
import time
import urwid
from threading import Thread
from toktokkie.utils.metadata.MetaDataManager import MetaDataManager
from toktokkie.utils.renaming.TVSeriesRenamer import TVSeriesRenamer
from toktokkie.utils.renaming.schemes.SchemeManager import SchemeManager


class TVSeriesRenamerUrwidTui(object):
    u"""
    Urwid TUI for the TV Series Renamer functionality
    """

    def __init__(self):
        u"""
        Initializes the TUI's various widgets
        """

        self.renamer = None
        self.confirmation = None

        self.parsing = False
        self.renaming = False

        self.list_walker = None
        self.upper_body, self.middle_body, self.lower_body = [[], [], []]
        self.top = None
        self.loop = None

        self.title = urwid.Text(u"TV Episode Renamer")

        self.naming_scheme_text = urwid.Text(u"Naming Scheme:")
        self.renaming_schemes = []

        for scheme in SchemeManager.get_scheme_names():
            urwid.RadioButton(group=self.renaming_schemes, label=scheme)

        self.dir_entry = urwid.Edit(caption=u"Directory: ")
        self.dir_entry.set_edit_text(os.getcwdu())
        self.recursive_check = urwid.CheckBox(u"Recursive?")
        self.start_search_button = urwid.Button(u"Start Search")
        urwid.connect_signal(self.start_search_button, u'click', self.search)

        self.episodes_text = urwid.Text(u"Episodes: (Old -> New)")

        self.remove_selection_button = urwid.Button(u"Remove Selection")
        urwid.connect_signal(self.remove_selection_button, u'click', self.remove_selection)

        self.confirm_button = urwid.Button(u"Confirm")
        urwid.connect_signal(self.confirm_button, u'click', self.confirm)

        self.lay_out()

    def lay_out(self):
        u"""
        Handles the layout of the TUI elements

        :return: None
        """
        div = urwid.Divider()

        confirm_button = urwid.AttrMap(self.confirm_button, None, focus_map=u'reversed')
        start_search_button = urwid.AttrMap(self.start_search_button, None, focus_map=u'reversed')
        remove_selection_button = urwid.AttrMap(self.remove_selection_button, None, focus_map=u'reversed')

        dir_entry = urwid.AttrMap(self.dir_entry, None, focus_map=u'reversed')

        self.upper_body = [self.title, div, self.naming_scheme_text] + self.renaming_schemes + [div]
        self.upper_body += [dir_entry, self.recursive_check, start_search_button, div, self.episodes_text, div]
        self.lower_body = [div, remove_selection_button, div, confirm_button]

        self.list_walker = urwid.SimpleFocusListWalker(self.upper_body + self.middle_body + self.lower_body)
        self.top = urwid.Overlay(urwid.Padding(urwid.ListBox(self.list_walker), left=2, right=2),
                                 urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                                 align=u'center', width=(u'relative', 80),
                                 valign=u'middle', height=(u'relative', 70),
                                 min_width=20, min_height=10)

    def start(self):  # pragma: no cover
        u"""
        Starts the TUI

        :return: None
        """
        self.loop = urwid.MainLoop(self.top, palette=[(u'reversed', u'standout', u'')])
        self.loop.run()

    # noinspection PyUnusedLocal
    def confirm(self, button):
        u"""
        Starts the renaming process

        :param button: The Confirm Button
        :return:       None
        """
        if self.renaming:
            return

        self.renaming = True
        self.start_spinner(u"rename")

        def rename():

            if self.confirmation is not None and self.renamer is not None:

                for item in self.confirmation:
                    item.confirm()

                self.renamer.confirm(self.confirmation)
                self.renamer.start_rename()

                self.renamer = None
                self.confirmation = None

                self.refresh()

                self.renaming = False
                # noinspection PyTypeChecker
                self.search(None)

        Thread(target=rename).start()

    # noinspection PyUnusedLocal
    def search(self, directory_entry, parameters = None):
        u"""
        Fills the episode list from the provided directory with the current recursive option

        :param directory_entry: The widget that caused the method to be called
        :param parameters:      Parameters passed by the widget, but not used
        :return:                None
        """
        if self.parsing or self.renaming:
            return

        self.parsing = True
        self.start_spinner(u"parse")

        def parse():

            self.renamer = None
            self.confirmation = None

            directory = self.dir_entry.get_edit_text()
            while directory.endswith(os.path.sep):
                directory = directory.rsplit(os.path.sep, 1)[0]

            if os.path.isdir(directory) and \
                    (MetaDataManager.is_media_directory(directory, media_type=u"tv_series")
                     or self.recursive_check.get_state()):

                recursive = self.recursive_check.get_state()
                scheme = u""
                for radio_button in self.renaming_schemes:
                    if radio_button.get_state():  # pragma: no cover
                        scheme = radio_button.get_label()

                self.renamer = TVSeriesRenamer(directory, SchemeManager.get_scheme_from_scheme_name(scheme), recursive)
                self.confirmation = self.renamer.request_confirmation()

                if len(self.confirmation) == 0:
                    self.renamer = None
                    self.confirmation = None

            self.refresh()
            self.parsing = False

        Thread(target=parse).start()

    # noinspection PyUnusedLocal
    def remove_selection(self, button):
        u"""
        Removes all currently selected elements from the renaming queue

        :param button: The button that called this method
        :return:       None
        """
        pop_indices = []

        for index, item in enumerate(self.middle_body):
            if item.get_state():
                pop_indices.append(index)

        for index in reversed(sorted(pop_indices)):
            self.confirmation.pop(index)

        if len(self.confirmation) == 0:
            self.renamer = None
            self.confirmation = None

        self.refresh()

    def refresh(self):
        u"""
        Refreshes the Window with the currently active widgets

        :return: None
        """
        self.middle_body = []

        if self.confirmation is not None:

            old_name_max = max(len(x.get_names()[0]) for x in self.confirmation) + 1

            for episode in self.confirmation:
                episode_checkbox = urwid.CheckBox(
                    episode.get_names()[0].ljust(old_name_max) + u" --->  " + episode.get_names()[1])
                episode_checkbox.set_state(False)
                self.middle_body.append(episode_checkbox)

        self.list_walker[:] = self.upper_body + self.middle_body + self.lower_body
        self.loop.draw_screen()

    def start_spinner(self, mode):
        u"""
        Starts a small animation while something is loading, parsing etc.

        :param mode:  The mode determines which UI element is going to be 'spun'
        :return:      None
        """
        renaming = mode == u"rename"
        parsing = mode == u"parse"

        def spin():

            while (renaming and self.renaming) or (parsing and self.parsing):

                if renaming and self.renaming:
                    new_text = u"Renaming" + (self.confirm_button.get_label().count(u".") % 3 + 1) * u"."
                    self.confirm_button.set_label(new_text)

                if parsing and self.parsing:
                    new_text = u"Reloading" + (self.start_search_button.get_label().count(u".") % 3 + 1) * u"."
                    self.start_search_button.set_label(new_text)

                self.loop.draw_screen()
                time.sleep(0.3)

            if renaming and not self.renaming:
                self.confirm_button.set_label(u"Confirm")
            if parsing and not self.parsing:
                self.start_search_button.set_label(u"Start Search")
            self.loop.draw_screen()

        Thread(target=spin).start()

    def quit(self):
        u"""
        Cleans up any variables that may cause thread to continue executing after the TUI ends

        :return: None
        """
        self.renaming = False
        self.parsing = False
