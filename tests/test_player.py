import os
import sys
from os.path import abspath, dirname, join
import pytest
proj_dir = dirname(dirname(abspath(__file__)))
IMG_DIR = join(proj_dir,"img")
sys.path.append(proj_dir)
os.environ["IMG_DIR"] = IMG_DIR
from card_counter.Players import Player, Dealer

class TestPlayer:

    def test_player_setup(self):
        p = Player()
        assert p is not None
        g = Dealer()
        assert g is not None

    def test_with_kwargs(self):
        kws = {"pos":8,  "random": 67, "word":"blue"}
        p2 = Player(**kws)
        d2 = Dealer(**kws)
        assert p2 is not None
        assert p2.pos == 8
        assert p2.window == None
        assert p2.title == "Player 8"
        assert d2.title == "Dealer"
