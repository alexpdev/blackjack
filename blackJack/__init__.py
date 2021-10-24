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
"""Imports for the package."""

import os
from pathlib import Path

PKG = (Path(__file__).resolve()).parent
os.environ["IMG_DIR"] = os.path.join(PKG, "assets")

from blackjack.Driver import Driver, main, testMain
from blackjack.Window import Window
from blackjack.Players import Dealer, Player

__version__ = "0.3.2"

__all__ = ["Driver", "Window", "Dealer", "Player", "main", "testMain"]
