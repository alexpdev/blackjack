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
from os.path import abspath, dirname, join
import pytest
proj_dir = dirname(dirname(abspath(__file__)))
IMG_DIR = join(proj_dir,"img")
sys.path.append(proj_dir)
os.environ["IMG_DIR"] = IMG_DIR
from blackJack.Deck import Deck

class TestDeck:

    def test_deck_setup(self):
        for i in range(1,6):
            deck = Deck.times(i)
            assert len(deck) == i * 52
            for card in deck:
                assert card.suit in deck.suits
