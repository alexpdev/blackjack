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


import pytest
from PyQt6.QtWidgets import QLabel
from tests.context import app
from blackJack.Window import Window






class TestWindow:

    decks = 1
    players = 2
    app = app
    window = Window(parent=None, app=app)


    def test_window_params(self):
        assert self.app == self.window.app

    def test_window_layouts(self):
        assert self.window.objectName() == "MainWindow"
        assert self.window.windowTitle() == "BlackJack"
        assert self.window.central is not None
        assert self.window.centLayout is not None
        assert self.window.horiztop  is not None
        assert self.window.button1 is not None
        assert self.window.textBrowser is not None
