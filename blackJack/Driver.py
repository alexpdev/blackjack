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

import math

from blackJack.Players import Dealer
from blackJack.Window import Window


class Driver:
    """
    Responsible for putting pieces together and driving them forward.
    --------------------------------------------------

    Starts the application, creates the window, creates the dealer and allows
    dealer to perform the rest of game setup. Calculates probabilities
    and statistics for the active game.
    """

    def __init__(self, app, players=2, decks=2):
        """
        Construct the Driver class for the new game.

        Args:
            app (QApp): Application base for program.
            players (int, optional): Number of players. Defaults to None
            decks (int, optional): Number of decks. Defaults tp None.
        """
        self.app = app
        self.labels = None
        self.drawn = []
        self.window = Window(parent=None, app=self.app, driver=self)
        # Dealer instance has most power and constrol over gameplay.
        self.dealer = Dealer(
            window=self.window,
            decks=decks,
            players=players,
            pos=0,
            driver=self,
        )
        self.window.setDealer(self.dealer)
        self.window.show()

    def play(self):
        """Start the game."""
        self.dealer.add_players()
        self.dealer.new_game()

    def hook(self, labels):
        """Hook labels to the driver."""
        self.labels = labels

    def chances_of_under(self, player):
        """
        Calculate the odds of breaking if player hits.

        Args:
            player (obj): The player who's turn it currently is
        """
        x = 21 - player.score
        count = sum([1 for i in self.dealer.deck if i.value < x])
        breaking = count / self.decksize
        self.labels["under"].update_percent(breaking)

    def update_prefs(self):
        """Update deck count, player count window labels"""
        self.labels["decks"].update_value(self.decks)
        self.labels["players"].update_value(self.players)
        self.labels["cards"].update_value(self.decksize)

    def update_decksize(self):
        """Update the window with the current card count"""
        self.labels["cards"].update_value(self.decksize)

    def chances_of_exactly(self, player):
        """
        Calculate the odds of breaking if player hits.

        Args:
            player (obj): The player who's turn it currently is
        """
        needed = 21 - player.score
        count = sum([1 for i in self.deck if i.value == needed])
        exactly = count / self.decksize
        self.labels["exactly"].update_percent(exactly)

    def chances_of_blackjack(self):
        """Calculate the odds of being dealt a blackJack."""
        tens = self.total_tens()
        aces = sum([1 for i in self.deck if i.name == "ace"])
        combinations = math.comb(self.decksize, 2)
        percentage = (tens * aces) / combinations
        self.labels["blackjack"].update_percent(percentage)

    def chances_of_breaking(self, player):
        """
        Calculate the odds of breaking if player hits.

        Args:
            player (obj): The player who's turn it currently is
        """
        x = 21 - player.score
        count = sum([1 for i in self.deck if i.value > x])
        breaking = count / self.decksize
        self.labels["breaking"].update_percent(breaking)

    def tens_in_deck(self):
        """
        Count number of cards left in the Deck with a value of 10.

        Returns:
            int: Total number of cards with the value of 10
        """
        return sum([1 for i in self.deck if i.value == 10])

    @property
    def deck(self):
        """Get the dealer's deck.

        Returns:
            obj: The deck actively used by the dealer.
        """
        return self.dealer.deck

    @property
    def decksize(self):
        """
        Get total cards in the deck.

        Returns:
            int: total count of cards left in deck.
        """
        return len(self.dealer.deck)

    @property
    def players(self):
        """Get count of players actively playing.

        Returns:
            int: Number of active players.
        """
        return self.dealer.player_count

    @property
    def decks(self):
        """Get number of decks used to make current deck.

        Returns:
            int: Number of 52 card decks used in game.
        """
        return self.dealer.deck_count
