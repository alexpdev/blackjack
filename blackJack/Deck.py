#! /env/Scripts/python
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

"""Deck of Cards and Card classes."""

class InvalidType(Exception):
    """Exception Class for Invalid type comparison."""

    def __init__(self, other):
        """Initialize Exception."""
        print(type(other))


class DeckEmpty(Exception):
    """Deck Empty when no more cards in deck to deal."""

    pass


class Deck(list):
    """Deck of cards.

    Subclass of list object representing a deck of cards.
    """

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

    def __init__(cls, *args, **kwargs):
        """Create Deck Object.

        List of 52 Card objects based on deck of playing cards.
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

    @property
    def range(self):
        """Get range of deck.

        Returns:
            iterator: range of deck.
        """
        return range(len(self))

    @classmethod
    def times(cls, num):
        """Class method constructor for creating multiple decks.

        - Arg: num (int): number of decks.
        - Returns: Deck: 52 card deck times the input arguement.
        """
        deck = []
        for _ in range(num):
            for card in Deck():
                deck.append(card)

        new_deck = cls(deck)
        new_deck.shuffle()
        return new_deck

    def pop(self, x=0):
        """Remove 1 card from deck at index `x`.

        - Args: x (int, optional): index. Defaults to 0.
        - Raises: DeckEmpty: when no cards left
        - Returns: Card object: removed card.
        """
        try:
            return super().pop(x)
        except IndexError:
            raise DeckEmpty

    def move(self, position):
        """Move card to another position in the deck.

        - Args: position (int): index location for moving the card.
        """
        count = 0
        while count < len(self):
            card = self.pop(0)
            self.insert(position, card)
            count += 1

    def swap(self, i1, i2):
        """Swap utility for shuffling deck.

        Args:
            - i1 (Card): first card for swapping
            - i2 (Card): next card to be swapped with first
        """
        val = self[i1]
        self[i1] = self[i2]
        self[i2] = val

    def shuffle(self, t=3):
        """Shuffle Cards in deck.

        - Args: t (int, optional): number of times to shuffle the deck
        """
        while t > 0:
            t -= 1
            for _ in self.range:
                i1 = random.choice(self.range)
                i2 = random.choice(self.range)
                self.swap(i1, i2)
                i3 = random.choice(self.range)
                self.move(i3)




def get_image_fd(card):
    """Get the absolute path to the cards image file.

    - Args:
        - card (Card): The card object the image will belong to.

    - Returns:
        - str: Absolute path to image file.
    """
    faces = {"ace": "1", "jack": "11", "queen": "12", "king": "13"}
    val = card.name if card.name not in faces else faces[card.name]
    fd = "".join([card.suit, "_", val, ".png"])
    path = os.path.join(os.environ["IMG_DIR"], fd)
    return path

class Card:
    """Card Object == contents of Deck Object."""

    def __init__(self, suit, name, value):
        """Construct instance of Card Objects.

        - Args:
            - suit (str): name of suit e.g. Diamonds Hearts
            - name (str): name of card e.g. King 7 Ace
            - value (int): Point value in blackjackicon
        """
        self.suit = suit
        self.name = name
        self.value = value
        self.path = self.getPath()

    def getPath(self):
        """Get path retreives filesystem location for card.

        - Returns:
            - str: absolute path to image file
        """
        return get_image_fd(self)

    def __str__(self):
        """Representation of an object as a string."""
        return self.name.title() + "of" + self.suit.title()

    def __repr__(self):
        """Act same as string function."""
        return "<" + self.name.title() + ":" + self.suit.title() + ">"

    def __lt__(self, other):
        """Less than < other."""
        if self.value < other.value:
            return True
        return False

    def __ne__(self, other):
        """Not equal != other."""
        if self.__eq__(other):
            return False
        return True

    def __gt__(self, other):
        """Greater than > other."""
        if isinstance(other, type(self)):
            other = other.value
        if self.value > other:
            return True
        return False

    def __eq__(self, other):
        """Equal == other."""
        if isinstance(other, type(self)):
            return self.value == other.value
        if isinstance(other, str):
            return self.suit == other
        if isinstance(other, int):
            return self.value == other
        return False

    def __le__(self, other):
        """Less than or equel <= other."""
        if self.__eq__(other) or self.__lt__(other):
            return True
        return False

    def __ge__(self, other):
        """Greater than or equal >= other."""
        if self.__eq__(other) or self.__gt__(other):
            return True
        return False

    def ismatch(self, other):
        """Suit matches other suit."""
        if self.suit == other.suit:
            return True
        return False

    def __typecheck__(self, other):
        """Check object type to see if it is a card."""
        if not isinstance(other, type(self)):
            raise InvalidType(other)
        return True
