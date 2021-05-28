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

from blackJack.utils import (QAction, QDialog, QHBoxLayout, QLabel, QMenu,
                             QMenuBar, QPushButton, QSpinBox, QVBoxLayout)


class MenuBar(QMenuBar):
    def __init__(self,parent=None,window=None):
        super().__init__(parent=parent)
        self.window = window
        self.setNativeMenuBar(False)
        self.window.setMenuBar(self)
        self.filemenu = QMenu("File",parent=self)
        self.addMenu(self.filemenu)
        self.settings = QMenu("Preferences", parent=self)
        self.settingsdialog = Settings(parent=self,window=self.window)
        self.addMenu(self.settings)
        self.setVisible(True)
        self.exitaction = QAction("Exit")
        self.filemenu.addAction(self.exitaction)
        self.exitaction.triggered.connect(self.exit_app)
        self.settingsaction = QAction("Settings")
        self.settings.addAction(self.settingsaction)
        self.settingsaction.triggered.connect(self.open_settings)
        self.newGameAction = QAction("New Game")
        self.filemenu.addAction(self.newGameAction)
        self.newGameAction.triggered.connect(self.newGame)

    def newGame(self):
        self.window.button3.start_new_game()

    def open_settings(self):
        self.settingsdialog.open()

    def exit_app(self):
        sys.exit()

class Settings(QDialog):
    def __init__(self,parent=None,window=None):
        super().__init__(parent=parent)
        self.window = window
        self.setSizeGripEnabled(False)
        self.setObjectName("Settings")
        self.setWindowTitle("Settings")
        self.setModal(True)
        self.vlayout = QVBoxLayout()
        self.setLayout(self.vlayout)
        self.playersLabel = QLabel("Number of Players",parent=self)
        self.decksLabel = QLabel("Number of Decks",parent=self)
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
        self.okayButton = QPushButton("Submit",parent=self)
        self.cancelButton = QPushButton("Cancel",parent=self)
        self.hLayout3.addWidget(self.okayButton)
        self.hLayout3.addWidget(self.cancelButton)
        self.vlayout.addLayout(self.hLayout3)
        self.okayButton.pressed.connect(self.accept)
        self.cancelButton.pressed.connect(self.reject)
        self.finished.connect(self.finishedSignal)

    def finishedSignal(self):
        self.window.dealer.deck_count = self.decksSpin.value()
        self.window.dealer.player_count = self.playersSpin.value()
