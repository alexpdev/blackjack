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
from pathlib import Path

from PyQt6.QtWidgets import QApplication

__version__ = "0.3.1"

sys.path.insert(0, str(Path(__file__).parent.parent))
os.environ["IMG_DIR"] = os.path.join(sys.path[0], "img")

PLAYERS = 2
DECKS = 1

from blackJack.Players import Dealer
from blackJack.Window import Window


def main():
    """Initialize function to invoke game.

    Args: app (QApplication): GUI Application
    """
    app = QApplication(sys.argv)
    window = Window(parent=None, players=PLAYERS, decks=DECKS, app=app)

    args = {
        "window": window,
        "deck_count": DECKS,
        "player_count": PLAYERS ,
        "pos": 0,
    }

    window.show()
    dealer = Dealer(**args)
    window.setDealer(dealer)
    dealer.add_players()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
