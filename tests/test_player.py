import os
import sys
import pytest
from os.path import abspath, dirname, join
from PyQt6.QtWidgets import QMainWindow
proj_dir = dirname(dirname(abspath(__file__)))
IMG_DIR = join(proj_dir,"img")
sys.path.append(proj_dir)
os.environ["IMG_DIR"] = IMG_DIR
from card_counter.Players import Player, Dealer

class TestPlayer:
    window = QMainWindow()

    def test_player_setup(self):
        for num in range(100):
            player = Player(num, self.window)
            assert player is not None
            assert player.pos == num
            assert player.title == "Player " + str(num)
            assert not player.isturn()
            assert player.window == self.window

    def test_dealer_setup(self):
        for num in range(3,50):
            decks = num % 3 if num % 3 > 0 else 1
            args = {"deck_count": decks, "window":self.window}
            dealer = Dealer(**args)
            assert dealer is not None
            assert dealer.window == self.window
            assert len(dealer.deck) == ((num % 3) + 1)*52
            assert dealer.limit == len(dealer.deck)//2
            assert len(dealer.deck) >= 52
            assert dealer.title == "Dealer"
            assert dealer.pos == 0
