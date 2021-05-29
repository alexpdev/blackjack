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
import os
from tests.context import app
from blackJack.utils import QLabel
from blackJack.Window import Window

class TestWindow:

    decks = 1
    players = 2
    app = app
    window = Window(parent=None, players=players, decks=decks, app=app)

    def test_window_params(self):
        assert self.window.players_count == self.players
        assert self.window.deck_count == self.decks
        assert self.app == self.window.app

    def test_window_layouts(self):
        assert self.window.ncards_val.text() == str(self.window.deck_count * 52)
        assert self.window.objectName() == "MainWindow"
        assert self.window.windowTitle() == "BlackJack"
        assert self.window.central is not None
        assert self.window.centLayout is not None
        assert self.window.horiztop  is not None
        assert self.window.button1 is not None
        assert self.window.textBrowser is not None

    def test_window_labels(self):
        assert self.window.ncards_label is not None
        assert type(self.window.ncards_label) == QLabel
        assert self.window.ncards_label.text() == "Cards in Deck: "
        assert type(self.window.ncards_val) == QLabel
        assert self.window.ndecks_label.text() == "Number of Decks: "
        assert self.window.ndecks_val.text() == "0"
        assert type(self.window.ndecks_val) == QLabel
        assert self.window.nplayers_label.text() == "Number of Players: "
        assert type(self.window.nplayers_label) == QLabel
        assert self.window.nplayers_val.text() == "0"
        assert type(self.window.nplayers_val) == QLabel