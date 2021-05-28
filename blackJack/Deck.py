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
    """
    `InvalidType`
    - 'Tried comparing Card object with some other
        incompatable datatype'
    """

    def __init__(self, other):
        """
        `__init__` Initialize Exception and print
        incompatible datatype compared.

        Args:
            other (Any): Not Card Object
        """
        print(type(other))


class DeckEmpty(Exception):
    """
    `DeckEmpty`
    - No more cards in deck to deal.
    """
    pass


class Deck(list):
    """
    # `Deck` of cards.

    Args: `list` : subclass of list object
    """
    suits = ("clubs", "spade", "hearts", "diamonds")

    values = {
        "2": 2, "3": 3, "4": 4,
        "5": 5, "6": 6, "7": 7,
        "8": 8, "9": 9, "10": 10,
        "jack": 10, "queen": 10,
        "king": 10, "ace": 11
    }

    def __init__(cls, *args, **kwargs):
        """
        `Deck.__init__` Create Deck Object.
        - list of 52 Card objects based on Deck of cards.
        """
        if not args and not kwargs:
            cards = []
            for suit in cls.suits:
                for name, value in cls.values.items():
                    card = Card(suit, name, value)
                    cards.append(card)
            super().__init__(cards)
        else:
            super().__init__(*args, **kwargs)

    @classmethod
    def times(cls, num):
        """
        ### `Deck.times(num)`
        - Class method constructor for creating num decks
        at once.
        - Args: num (int): Number of decks.
        - Returns: Deck object
        """
        deck = []
        for _ in range(num):
            for card in Deck():
                deck.append(card)

        new_deck = cls(deck)
        new_deck.shuffle()
        return new_deck

    def pop(self, x=0):
        """
        `deck.pop()` remove 1 card from deck at index `x`
        - Args: x (int, optional): index. Defaults to 0.
        - Raises: DeckEmpty: when no cards left
        - Returns: Card object: removed card.
        """
        try:
            return super().pop(x)
        except IndexError:
            raise DeckEmpty

    def swap(self, i1, i2):
        """
        swap utility for shuffling deck

        Args:
            i1 (Card): first card for swapping
            i2 (Card): next card to be swapped with first
        """
        val = self[i1]
        self[i1] = self[i2]
        self[i2] = val

    def shuffle(self, t=8):
        """
        shuffle Shuffle Cards in DeckEmpty

        Args:
            t (int, optional): number of times to shuffle the deck
        """
        for _ in range(len(self) * t):
            i1 = random.choice(range(len(self)))
            i2 = random.choice(range(len(self)))
            self.swap(i1, i2)


class Card:
    """
     Card Object == contents of Deck Object.
    """

    def __init__(self, suit, name, value):
        """
        __init__ Constructor for Card Objects

        Args:
            suit (str): name of suit e.g. Diamonds Hearts
            name (str): name of card e.g. King 7 Ace
            value (int): Point value in blackjackicon
        """
        self.suit = suit
        self.name = name
        self.value = value
        self.path = self.getPath()

    def getPath(self):
        """
        getPath retreive filesystem location for self

        Returns:
            str: absolute path to image file
        """
        faces = {"ace": 1, "jack": 11, "queen": 12, "king": 13}
        img_dir = os.environ.get("IMG_DIR")
        val = str(faces[self.name]) if self.name in faces else str(self.value)
        filename = ''.join([self.suit, "_", val, ".png"])
        return os.path.join(img_dir, filename)

    def __str__(self):
        # string representation of object
        return "<" + self.name.title() + ":" + self.suit.title() + ">"

    def __repr__(self):
        # same as string
        return str(self)

    def __lt__(self, other):
        # less than < other
        if self.value < other.value:
            return True
        return False

    def __ne__(self, other):
        # not equal != other
        if self.__eq__(other):
            return False
        return True

    def __gt__(self, other):
        # greater than > other
        if isinstance(other, type(self)):
            other = other.value
        if self.value > other:
            return True
        return False

    def __eq__(self, other):
        # equal == other

        if isinstance(other, type(self)):
            return self.value == other.value

        if isinstance(other, str):
            return self.suit == other

        if isinstance(other, int):
            return self.value == other
        return False

    def __le__(self, other):
        # less than or equel <= other
        if self.__eq__(other) or self.__lt__(other):
            return True
        return False

    def __ge__(self, other):
        # greater than or equal >= other
        if self.__eq__(other) or self.__gt__(other):
            return True
        return False

    def ismatch(self, other):
        # self.suit == other.suit
        if self.suit == other.suit:
            return True
        return False

    def __typecheck__(self, other):
        # check object type to see if it's a Card
        if not isinstance(other, type(self)):
            raise InvalidType(other)
