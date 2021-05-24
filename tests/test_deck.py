import os
import sys
from os.path import abspath, dirname, join
import pytest
proj_dir = dirname(dirname(abspath(__file__)))
IMG_DIR = join(proj_dir,"img")
sys.path.append(proj_dir)
os.environ["IMG_DIR"] = IMG_DIR
from card_counter.Deck import Deck

class TestDeck:

    def test_deck_setup(self):
        for i in range(1,6):
            deck = Deck.times(i)
            assert len(deck) == i * 52
            for card in deck:
                assert card.suit in deck.suits


TestDeck().test_deck_setup()