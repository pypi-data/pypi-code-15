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
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from toktokkie.ui.qt.pyuic.start_page import Ui_StartPageWindow
from toktokkie.ui.qt.FolderIconizerQtGui import FolderIconizerQtGui
from toktokkie.ui.qt.TVSeriesRenamerQtGui import TVSeriesRenamerQtGui
from toktokkie.ui.qt.XDCCDownloadManagerQtGui import XDCCDownloadManagerQtGui
from toktokkie.ui.qt.XDCCUpdateConfiguratorQtGui import XDCCUpdateConfiguratorQtGui


class StartPageQtGui(QMainWindow, Ui_StartPageWindow):
    u"""
    Class that models th QT GUI for the program's Start Page
    """

    def __init__(self, parent = None):
        u"""
        Sets up the interactive UI elements

        :param parent: the parent window
        """
        super(StartPageQtGui, self).__init__(parent)
        self.setupUi(self)

        # Initialize UI elements
        self.tv_series_renamer.clicked.connect(TVSeriesRenamerQtGui(self).show)
        self.folder_iconizer.clicked.connect(FolderIconizerQtGui(self).show)
        self.xdcc_download_manager.clicked.connect(XDCCDownloadManagerQtGui(self).show)
        self.xdcc_update_configurator.clicked.connect(XDCCUpdateConfiguratorQtGui(self).show)


def start():  # pragma: no cover
    u"""
    Starts the Start Page GUI

    :return: None
    """
    app = QApplication(sys.argv)
    form = StartPageQtGui()
    form.show()
    app.exec_()
