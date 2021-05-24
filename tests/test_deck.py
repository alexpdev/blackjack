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

    def test_deck_setup(self,capsys):
        lst = [1,2,3,4,5,6]
        a = Deck(lst)
        print(a)
        capsys.readouterr()
        assert a and True