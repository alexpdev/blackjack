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

import pytest
from pathlib import Path
from tests.context import app
from blackJack.Deck import Deck, Card, DeckEmpty, InvalidType

App = app

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
        for i in range(51):
            l = len(deck)
            c = deck.pop()
            assert type(c) == Card
            assert len(deck) == l - 1



class TestCards:

    suits = ("clubs", "spade", "hearts", "diamonds")
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "jack": 10,
        "queen": 10,
        "king": 10,
        "ace": 11,
    }

    def test_card_setup(self):
        for suit in self.suits:
            print(self.values)
            for k in self.values:
                v = self.values.get(k)
                card = Card(suit, k, v)
                assert card.value == v
                assert card.name == k
                assert card.suit == suit
                assert card.path is not None

    def test_card_paths(self):
        cards = []
        for suit in self.suits:
            for k in self.values:
                v = self.values.get(k)
                card = Card(suit, k, v)
                cards.append(card)
        assert len(cards) == 52
        for card in cards:
            p = Path(card.path)
            assert p.exists()
            assert p.is_file()
            assert p.suffix in [".jpg", ".png", ".bmp", ".tiff"]

    def test_operator_funcs(self):
        cards = []
        for suit in self.suits:
            for k in self.values:
                v = self.values.get(k)
                card = Card(suit, k, v)
                cards.append(card)
        for i, card in enumerate(cards[1: ]):
            other = cards[i - 1]
            assert card == card
            if other.value != card.value:
                assert other != card
                if card.value > other.value:
                    assert card > other
                else:
                    assert card < other
                if card.value >= other.value:
                    assert card >= other
                else:
                    assert card <= other
            if card.suit == other.suit:
                assert card.ismatch(other)
            else:
                assert card.ismatch(other) is False
            assert card.__typecheck__(other)
            assert pytest.raises(InvalidType,lambda : card.__typecheck__("some string"))
