# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toktokkie/ui/qt/qt_designer/start_page.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from __future__ import absolute_import
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartPageWindow(object):
    def setupUi(self, StartPageWindow):
        StartPageWindow.setObjectName(u"StartPageWindow")
        StartPageWindow.resize(352, 178)
        self.centralwidget = QtWidgets.QWidget(StartPageWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tv_series_renamer = QtWidgets.QPushButton(self.centralwidget)
        self.tv_series_renamer.setObjectName(u"tv_series_renamer")
        self.gridLayout.addWidget(self.tv_series_renamer, 1, 0, 1, 1)
        self.folder_iconizer = QtWidgets.QPushButton(self.centralwidget)
        self.folder_iconizer.setObjectName(u"folder_iconizer")
        self.gridLayout.addWidget(self.folder_iconizer, 2, 0, 1, 1)
        self.xdcc_download_manager = QtWidgets.QPushButton(self.centralwidget)
        self.xdcc_download_manager.setObjectName(u"xdcc_download_manager")
        self.gridLayout.addWidget(self.xdcc_download_manager, 3, 0, 1, 1)
        self.xdcc_update_configurator = QtWidgets.QPushButton(self.centralwidget)
        self.xdcc_update_configurator.setObjectName(u"xdcc_update_configurator")
        self.gridLayout.addWidget(self.xdcc_update_configurator, 4, 0, 1, 1)
        StartPageWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StartPageWindow)
        self.statusbar.setObjectName(u"statusbar")
        StartPageWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartPageWindow)
        QtCore.QMetaObject.connectSlotsByName(StartPageWindow)

    def retranslateUi(self, StartPageWindow):
        _translate = QtCore.QCoreApplication.translate
        StartPageWindow.setWindowTitle(_translate(u"StartPageWindow", u"Toktokkie"))
        self.tv_series_renamer.setText(_translate(u"StartPageWindow", u"TV Series Renamer"))
        self.folder_iconizer.setText(_translate(u"StartPageWindow", u"Folder Iconizer"))
        self.xdcc_download_manager.setText(_translate(u"StartPageWindow", u"XDCC Download Manager"))
        self.xdcc_update_configurator.setText(_translate(u"StartPageWindow", u"XDCC Update Configurator"))

