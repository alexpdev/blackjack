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

from card_counter.Players import Dealer, Player
from card_counter.Window import Window

PLAYERS=2
DECKS=1


class Config:
    def __init__(self):
        window = Window(parent=None)
        args = {
            "window" : window,
            "deck_count" : DECKS,
        }
        dealer = Dealer(**args)
        window.setDealer(dealer)
        for num in range(1, PLAYERS+1):
            args["pos"] = num
            player = Player(**args)
            window.addPlayer(player)
            dealer.players.append(player)
        window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Config()
    sys.exit(app.exec())
