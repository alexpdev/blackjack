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


class Player:
    """Object representing a player playing against the dealer.

    Player(pos=None: int, window=None: widget, **kwargs)
    """

    def __init__(self, pos=None, window=None, **kwargs):
        """Player Constructor Function."""
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
        """Total points from sum of card values in hand."""
        return sum(card.value for card in self.hand)

    def __str__(self):
        """Player Title.

        Returns player's title property.
        """
        return self.title

    def __repr__(self):
        """Return str(self)."""
        return self.title

    def isturn(self):
        """Return True or False.

        Called by dealer and Window Buttons to
        check who's turn it is.
        """
        return self._turn

    def turn(self):
        """Call at the beginning and end of players turn."""
        self._turn = not self._turn
        self.box.turn()
        return self.isturn()

    def output(self, line):
        """Write output to QTextBrowserWidgit.

        Args: line (str): Content to print to window.
        Simple way to keep track of previous hands
        and cards already dealt by dealer.
        """
        self.window.textBrowser.append(line)

    def add_card(self, card):
        """Add a Card object to Players hand.

        Args: card (Card()): Card object popped off deck
        Takes a card just poped off Deck by dealer and includes it in hand.
        """
        self.hand.append(card)
        for widg in self.cards:
            if widg.cover:
                return widg.setCard(card)
        self.box.addWidget(card)
        self.window.repaint()
        self.window.update()


    def show_score(self, score):
        """Write players score to the QTextBrowser Widgit.

        Args: score (int): self.score
        """
        self.box.scorelabel.setText(score)

    def show_hand(self):
        """Wtites logs details about the score and cards in players hand."""
        score = str(self.score)
        self.show_score(score)
        output = "".join([str(self), " ", str(self.hand), " ", score, "\n"])
        self.output(output)


class Dealer(Player):
    """Dealer Object. Controls most aspects of the game.

    Subclass of Player but requires a few extra keyword args
    """

    def __init__(self, decks=1, players=2, driver=None, **kwargs):
        """Dealer constructor.

        Args: deck_count(int, optional): Number of decks to use.
        player_count (int, optional): Total players in game.
        """
        super().__init__(**kwargs)
        self.title = "Dealer"
        self.deck_count = decks
        self.player_count = players
        self.current = 0
        self.players = []
        self.deck = Deck.times(self.deck_count)
        self.limit = 50
        self.driver = driver

    def setPreferences(self,decks=None,players=None):
        del self.deck
        if decks:
            self.deck_count = decks
        if players:
            self.player_count = players
            self.add_players()
        self.deck = Deck.times(self.deck_count)
        self.new_game()

    @property
    def decksize(self):
        return len(self.deck)

    @property
    def score(self):
        """Score overloaded function from Player Class.

        Returns: [str]: Dealers score
        """
        if self.isturn():
            return super().score
        return self.hand[0].value

    def add_card(self, card):
        """Overload method from player class.

        Args: card (Card()): adds card just pooped from deck to hand.
        """
        super().add_card(card)
        if len(self.cards) == 2:
            self.cards[-1].faceDown()

    def start_deal(self):
        """Initialize deal sequence of 2 cards to each player."""
        for _ in range(2):
            for player in self.players:
                self.deal_card(player)
            self.deal_card(self)

    def deal_card(self, player):
        """Retreive card from top of deck and deals to player.

        Args: player (Player()): instance of Player in game
        """
        card = self.deck.pop()
        self.driver.update_count()
        player.add_card(card)
        player.show_hand()
        self.window.update()
        self.window.repaint()

    def round(self):
        """Begin new players turn for betting, hitting or staying."""
        player = self.players[self.current]
        player.turn()

    def dealer_round(self):
        """Call when all other players have had their turn betting."""
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
        """Call when Player asks dealer to "hit".

        Args: Player (player object instance) the player whos turn it is.
        """
        self.deal_card(player)
        if player.score > 21:
            self.output(player.title + " Bust")
            player.turn()
            self.next_player()

    def next_player(self):
        """Call when previous players turn ended."""
        self.current += 1
        if self.current < len(self.players):
            self.round()
        else:
            self.current = 0
            self.dealer_round()

    def new_game(self):
        """Call after dealer has played their turn."""
        if len(self.deck) <= self.limit:
            del self.deck
            self.deck = Deck.times(self.deck_count)
            self.driver.update_count()
        self.start_deal()
        self.current = 0
        self.round()

    def add_players(self):
        """Part of the constructor.

        Initializes a new players according to num_players attribute
        and creates their GUI representation.
        """
        for num in range(1, self.player_count + 1):
            args = {"pos": num, "window": self.window}
            player = Player(**args)
            self.window.addPlayer(player)
            self.players.append(player)
