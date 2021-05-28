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
import random


class InvalidType(Exception):
    def __init__(self,other):
        print(type(other))

class DeckEmpty(Exception):
    pass

class Deck(list):
    suits = ("clubs", "spade", "hearts", "diamonds")
    values = {"2":2, "3":3, "4":4,
            "5":5, "6":6, "7":7,
            "8":8, "9":9, "10":10,
            "jack":10, "queen":10, "king":10,
            "ace":11}

    def __init__(cls,*args,**kwargs):
        if not args and not kwargs:
            cards = []
            for suit in cls.suits:
                for name,value in cls.values.items():
                    card = Card(suit,name,value)
                    cards.append(card)
            super().__init__(cards)
        else:
            super().__init__(*args,**kwargs)

    @classmethod
    def times(cls,num):
        deck = []
        for _ in range(num):
            for card in Deck():
                deck.append(card)
        new_deck = cls(deck)
        new_deck.shuffle()
        return new_deck

    def pop(self,x=0):
        try:
            return super().pop(x)
        except IndexError:
            raise DeckEmpty

    def swap(self, i1, i2):
        val = self[i1]
        self[i1] = self[i2]
        self[i2] = val

    def shuffle(self,t=8):
        for _ in range(len(self) * t):
            i1 = random.choice(range(len(self)))
            i2 = random.choice(range(len(self)))
            self.swap(i1,i2)

class Card:

    def __init__(self,suit,name,value):
        self.suit = suit
        self.name = name
        self.value = value
        self.path = self.getPath()

    def getPath(self):
        faces = {"ace": 1,"jack": 11,"queen": 12,"king": 13}
        img_dir = os.environ.get("IMG_DIR")
        val = str(self.value) if self.name not in faces  else str(faces.get(self.name))
        filename = ''.join([self.suit, "_", val, ".png"])
        return os.path.join(img_dir, filename)

    def __str__(self):
        return "<" + self.name.title() + ":" + self.suit.title() + ">"

    def __repr__(self):
        return str(self)

    def __lt__(self,other):
        if self.value < other.value:
            return True
        return False

    def __ne__(self,other):
        if self.__eq__(other):
            return False
        return True

    def __gt__(self,other):
        if isinstance(other,type(self)):
            other = other.value
        if self.value > other:
            return True
        return False

    def __eq__(self,other):
        if isinstance(other,type(self)):
            return self.value == other.value
        if isinstance(other,str):
            return self.suit == other
        if isinstance(other,int):
            return self.value == other
        return False

    def __le__(self,other):
        if self.__eq__(other) or self.__lt__(other):
            return True
        return False

    def __ge__(self,other):
        if self.__eq__(other) or self.__gt__(other):
            return True
        return False

    def ismatch(self,other):
        if self.suit == other.suit:
            return True
        return False

    def __typecheck__(self,other):
        if not isinstance(other,type(self)):
            raise InvalidType(other)
