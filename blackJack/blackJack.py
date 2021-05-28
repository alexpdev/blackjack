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

import os
import sys
from os.path import dirname, abspath, join
from PyQt6.QtWidgets import QApplication

PROJ_DIR = dirname(dirname(abspath(__file__)))
sys.path.append(PROJ_DIR)

IMG_DIR = join(PROJ_DIR,"img")
os.environ["IMG_DIR"] = IMG_DIR

PLAYERS=2
DECKS=1

from card_counter.Players import Dealer
from card_counter.Window import Window

class Config:
    def __init__(self,app):
        window = Window(parent=None,players=PLAYERS,decks=DECKS,app=app)
        window.show()
        args = { "window" : window, "deck_count" : DECKS, "player_count" : PLAYERS , "pos" : 0}
        dealer = Dealer(**args)
        window.setDealer(dealer)
        dealer.add_players()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Config(app)
    sys.exit(app.exec())
