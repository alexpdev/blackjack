#! /usr/bin/python3
# -*- coding: utf-8 -*-

#######################################################################
# BlackJack Card Counting
# Copyright (C) 2021  alexpdev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses
#########################################################################

import sys
from PyQt6.QtGui import QAction, QFont
from PyQt6.QtCore import QRect, Qt
from PyQt6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QMenu,
    QMenuBar,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QDialogButtonBox,
    QSizePolicy
)


class MenuBar(QMenuBar):
    """QMenuBar instance for main window menubar.

    Assigns object instance to as QMainWindow Menubar and creates
    File and Settings submenu.
    """

    def __init__(self, parent=None, window=None):
        """Construct MenuBar instance and create submenus."""
        super().__init__(parent=parent)
        self.setObjectName("MainMenuBar")
        self.setVisible(True)
        self.setNativeMenuBar(False)
        self.window = window
        self.window.setMenuBar(self)
        self.filemenu = QMenu("File", parent=self)
        self.settings = QMenu("Preferences", parent=self)
        self.help = QMenu("Help",parent=self)
        self.settingsdialog = Settings(parent=self, window=self.window)
        self.aboutdialog = About(parent=self,window=self.window)
        self.addMenu(self.filemenu)
        self.addMenu(self.settings)
        self.addMenu(self.help)
        self.exitaction = QAction("&Exit")
        self.settingsaction = QAction("&Settings")
        self.newGameAction = QAction("&New Game")
        self.minimize = QAction("&Minimize")
        self.maximize = QAction("&Maximize")
        self.aboutQt = QAction("&About Qt")
        self.aboutSelf = QAction("&About")
        self.help.addAction(self.aboutQt)
        self.help.addAction(self.aboutSelf)
        self.filemenu.addAction(self.minimize)
        self.filemenu.addAction(self.maximize)
        self.filemenu.addAction(self.exitaction)
        self.settings.addAction(self.settingsaction)
        self.filemenu.addAction(self.newGameAction)
        self.aboutQt.triggered.connect(self.aboutQtMenu)
        self.minimize.triggered.connect(self.minimizeWindow)
        self.maximize.triggered.connect(self.maxamizeWindow)
        self.exitaction.triggered.connect(self.exit_app)
        self.settingsaction.triggered.connect(self.open_settings)
        self.newGameAction.triggered.connect(self.newGame)
        self.aboutSelf.triggered.connect(self.about)

    def aboutQtMenu(self):
        self.aboutQt()

    def about(self):
        self.modal = self.aboutDialog()
        self.modal.show()

    def maxamizeWindow(self):
        width = self.window.maximumWidth()
        height = self.window.maximumHeight()
        self.window.resize(width,height)
        return

    def minimizeWindow(self):
        width = self.window.minimumWidth()
        height = self.window.minimumHeight()
        self.window.resize(width,height)
        return

    def newGame(self):
        """Start New Game Action for File Submenu.

        Same as pressing NewGameButton.
        """
        self.window.dealer.setPreferences()

    def open_settings(self):
        """Create a QDialog with editable options related to gameplay.

        Options include: Number of players, Number of Decks.
        """
        self.settingsdialog.open()

    def exit_app(self):
        """Quit program."""
        sys.exit()


class About(QDialogButtonBox):
    def __init__(self, parent=None,window=None):
        super().__init__(parent=parent)
        self.window = window
        self.resize(365, 229)
        self.setObjectName(u"buttonBox")
        self.setGeometry(QRect(180, 190, 171, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setOrientation(Qt.Orientation.Horizontal)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 30, 49, 16))
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 211, 16))
        font = QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 160, 201, 20))
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 120, 341, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_5.setFont(font1)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 161, 51))
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 110, 121, 16))
        self.label_6.setFont(font)
        self.accepted.connect(self.accept)
        self.rejected.connect(self.reject)
        self.setWindowTitle("About")
        self.label_2.setText("v 0.3")
        self.label_3.setText("Copyright 2021 AlexPdev Inc.")
        self.label_4.setText("https://fsf.org/>")
        self.label_5.setText("License GNU LESSER GENERAL PUBLIC LICENSE")
        self.label.setText("BlackJack")
        self.label_6.setText("Creator AlexPdev")
    # retranslateUi

    def accept(self):
        pass
    def reject(self):
        pass





class Settings(QDialog):
    """Open new window with editable options that effect gameplay."""

    def __init__(self, parent=None, window=None):
        """Construct Settings Dialog."""
        super().__init__(parent=parent)
        self.setObjectName("Preferences")
        self.window = window
        self.setSizeGripEnabled(False)
        self.setObjectName("Settings")
        self.setWindowTitle("Preferences")
        self.setModal(True)
        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)
        self.playersLabel = QLabel("Number of Players", parent=self)
        self.decksLabel = QLabel("Number of Decks", parent=self)
        self.playersSpin = QSpinBox(parent=self)
        self.decksSpin = QSpinBox(parent=self)
        self.hLayout1 = QHBoxLayout()
        self.hLayout2 = QHBoxLayout()
        self.hLayout1.addWidget(self.playersLabel)
        self.hLayout1.addWidget(self.playersSpin)
        self.hLayout2.addWidget(self.decksLabel)
        self.hLayout2.addWidget(self.decksSpin)
        self.vlayout.addLayout(self.hLayout1)
        self.vlayout.addLayout(self.hLayout2)
        self.hLayout3 = QHBoxLayout()
        self.okayButton = QPushButton("Submit", parent=self)
        self.cancelButton = QPushButton("Cancel", parent=self)
        self.hLayout3.addWidget(self.okayButton)
        self.hLayout3.addWidget(self.cancelButton)
        self.vlayout.addLayout(self.hLayout3)
        self.okayButton.pressed.connect(self.accept)
        self.cancelButton.pressed.connect(self.reject)
        self.finished.connect(self.finishedSignal)

    def accept(self):
        dealer = self.window.dealer
        dealer.setPreferences(self.decksSpin.value(), self.playersSpin.value())
        super().accept()


    def finishedSignal(self):
        """When Settings Window returns accept or reject signals."""
        self.window.dealer.deck_count = self.decksSpin.value()
        self.window.dealer.player_count = self.playersSpin.value()
