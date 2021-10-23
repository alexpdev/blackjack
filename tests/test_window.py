#! /env/Scripts/python
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


from tests.context import app, driver
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class TestWindow:

    decks = 1
    players = 2
    app = app
    driver = driver
    window = driver.window()

    def test_window(self):
        assert self.window is not None
        assert isinstance(self.window, QMainWindow)

    def test_window_app(self):
        assert self.window.app is not None
        assert isinstance(self.window.app, QApplication)

    def test_window_driver(self):
        assert self.window.driver == self.driver

    def test_window_stylesheet(self):
        assert self.window.styleSheet() == self.window.ssheet

    def test_window_objectName(self):
        assert self.window.objectName() == "BlackJack"

    def test_window_centralWidget(self):
        assert type(self.window.central) == QWidget
