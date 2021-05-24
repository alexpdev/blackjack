#! /usr/bin/python3
# -*- coding: utf-8 -*-

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
LIMIT=(.5 * DECKS * 52)


class Config:
    def __init__(self):
        window = Window(parent=None)
        args = {
            "pos" : 0,
            "limit" : LIMIT ,
            "window" : window,
            "deck_count" : DECKS,
            "num_players" : PLAYERS,
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
