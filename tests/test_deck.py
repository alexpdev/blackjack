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

import sys
import pytest
from tests.context import app
from blackJack.Deck import Deck, Card, DeckEmpty

class TestDeck:

    def test_deck_setup(self):
        for i in range(1,6):
            deck = Deck.times(i)
            assert len(deck) == i * 52
            for card in deck:
                assert card.suit in deck.suits

    def test_shuffle(self):
        deck = Deck.times(3)
        assert len(deck) > 0
        assert len(deck) == 3*52
        first = deck[1]
        deck.shuffle()
        assert first != deck[1]

    def test_pop(self):
        deck = Deck.times(2)
        deck.shuffle()
        c1 = deck[0]
        card = deck.pop()
        assert c1 == card
        assert type(card) == Card
        for i in range(len(deck)):
            l = len(deck)
            c = deck.pop()
            assert type(c) == Card
            assert len(deck) == l - 1
        assert pytest.raises(DeckEmpty, deck.pop())
