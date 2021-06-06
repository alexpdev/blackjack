import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import QApplication
from blackJack.Players import Dealer
from blackJack.Window import Window



class Driver:

    default_players = 2
    default_decks = 2

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Window(parent=None,
                            players=self.default_players,
                            app=self.app)
        self.dealer = Dealer(window=self.window,
                            decks=self.default_decks,
                            players=self.default_players,
                            pos=0,
                            driver=self)
        self.window.setDealer(self.dealer)
        self.window.show()

    @property
    def decksize(self):
        return self.dealer.decksize

    def update_count(self):
        self.window.ncards_val.setText(str(self.decksize))
