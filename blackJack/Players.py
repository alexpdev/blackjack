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

from blackJack.Deck import Deck
from blackJack.PlayerBox import CardWidget


class Player:
    """
        Object representing a player playing against the dealer.

        Player(pos=None: int, window=None: widget, **kwargs)

    """
    def __init__(self, pos=None, window=None, **kwargs):
        self.pos = pos
        self.window = window
        self._turn = False
        self.kwargs = kwargs
        self.hand = []
        self.cards = []
        self.box = None
        self.title = "Player " + str(pos)

    @property
    def score(self):
        # total points from card values in hand
        return sum(card.value for card in self.hand)

    def __str__(self):
        # string representation : returns player's title
        return self.title

    def __repr__(self):
        # same as __str__
        return self.title

    def isturn(self):
        # Returns True when it is the
        # players turn to hit or stay
        return self._turn

    def turn(self):
        # called when players turn begins
        self._turn = not self._turn
        self.box.turn()
        return self.isturn()

    def output(self, line):
        """
        output Logs input to onscreen logging widget

        Args:
            line (str): Content to print to window.
        """
        self.window.textBrowser.append(line)

    def add_card(self, card):
        """
        add_card Takes a card just popped of the deck
        by the dealer and adds it to players hand.

        Args:
            card (Card()): Card object popped off deck
        returns expression;
        """
        self.hand.append(card)
        for widg in self.cards:
            if widg.cover:
                return widg.setCard(card)
        widget = CardWidget(cover=False, card=card, path=card.path)
        self.box.hbox.addWidget(widget)
        return self.cards.append(widget)

    def show_score(self, score):
        """
        show_score logs players total score to Window

        Args:
            score (int): self.score
        """
        self.box.scorelabel.setText(str(score))

    def show_hand(self):
        """
        show_hand logs details about the score and cards in players hand
        """
        score = self.score
        self.show_score(score)
        output = "".join([str(self), " ", str(self.hand), " ", str(score), "\n"])
        self.output(output)


class Dealer(Player):
    """
    Dealer Object. Controls most aspects of the game.
    Subclass of Player but requires a few extra keyword args
    """

    def __init__(self, deck_count=1, player_count=2, **kwargs):
        """
        __init__ Dealer constructor.

        Args:
            deck_count (int, optional): Number of decks to use. Defaults to 1.
            player_count (int, optional): Total players in game. Defaults to 2.
        """
        super().__init__(**kwargs)
        self.title = "Dealer"
        self.deck_count = deck_count
        self.player_count = player_count
        self.current = 0
        self.players = []
        self.deck = Deck.times(deck_count)
        self.limit = len(self.deck) // 2

    def setup_window_labels(self):
        """
        setup_window_labels() : updates card count and
            other details displayed in the main window
        """
        self.window.ncards_val.setText(str(self.deck_count * 52))
        self.window.ndecks_val.setText(str(self.deck_count))
        self.window.nplayers_val.setText(str(self.player_count))

    @property
    def score(self):
        """
        score overloaded function from Player Class

        Returns:
            [str]: Dealers score
        """
        if self.isturn():
            return super().score
        return self.hand[0].value

    def add_card(self, card):
        """
        add_card() : Overloaded from player class
        Args:
            card (Card()): adds card just pooped from deck to hand.
        """
        super().add_card(card)
        if len(self.cards) == 2:
            self.cards[-1].faceDown()

    def start_deal(self):
        """
        start_deal() Initial deal sequence of 2 cards to each player.
        """
        for _ in range(2):
            for player in self.players:
                self.deal_card(player)
            self.deal_card(self)

    def deal_card(self, player):
        """
        deal_card() : retreives 1 card from top of
                    deck and gives it to player

        Args:
            player (Player()): instance of Player in game
        """
        card = self.deck.pop()
        self.window.ncards_val.setText(str(len(self.deck)))
        player.add_card(card)
        player.show_hand()
        self.window.update()
        self.window.repaint()

    def round(self):
        """
        round() begin new players turn for betting,
            hitting or staying
        """
        player = self.players[self.current]
        player.turn()

    def dealer_round(self):
        """
        `dealer_round(self)`
        - Called when all other players have had their turn at hitting.
        """
        self.turn()
        for card in self.cards:
            card.faceUp()
        self.show_hand()
        while self.score < 16:
            self.deal_card(self)
        if self.score > 21:
            self.output("Dealer Busts")
        self.turn()

    def player_hit(self, player):
        """
        `player_hit()` : Called when Player asks dealer to "hit"

        Args:
            player (player object instance)
            - the player whos turn it is;
        """
        self.deal_card(player)
        if player.score > 21:
            self.output(player.title + " Bust")
            player.turn()
            self.next_player()

    def next_player(self):
        """
        `next_player()`
        - Called when previous players turn ended
        """
        self.current += 1
        if self.current < len(self.players):
            self.round()
        else:
            self.current = 0
            self.dealer_round()

    def new_game(self):
        """
        `new_game()`
        Called when all players and dealer
        have had their turn at hitting or staying
        """
        self.setup_window_labels()
        if len(self.deck) <= self.limit:
            del self.deck
            self.deck = Deck.times(self.deck_count)
        self.start_deal()
        self.current = 0
        self.round()

    def add_players(self):
        """
        `add_players()` : Part of the constructor
        initializes a new player for num_players attribute
        and creates their GUI representation.
        """
        for num in range(1, self.player_count + 1):
            args = {"pos": num, "window": self.window}
            player = Player(**args)
            self.window.addPlayer(player)
            self.players.append(player)
