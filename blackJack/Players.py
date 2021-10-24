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

from time import sleep

from blackjack.Deck import Deck


class Player:
    """Object representing a player playing against the dealer.

    Player(pos=None: int, window=None: widget, **kwargs)
    """

    def __init__(self, pos=None, window=None, **kwargs):
        """Player Constructor Function.

        Args:
            pos (int): players position at table.
            window (Window): The program's main window.
            **kwargs: arbitrary keyword arguements.
        """
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
        """Total points from sum of card values in hand.

        Returns:
            int: sum of the cards in players hand.
        """
        return sum(card.value for card in self.hand)

    def __str__(self):
        """Player Title.

        Returns:
            str: Players title attribute.
        """
        return self.title

    def reset(self):
        """Reset player for new game."""
        self.box.reset()
        self.cards = []
        self.hand = []

    def __repr__(self):
        """Return players title.

        Returns:
            str: players title
        """
        return self.title

    def isturn(self):
        """Return True if it is player's turn else False

        Returns:
            bool: true if it is players turn else false.
        """
        return self._turn

    def turn(self):
        """Call at the beginning and end of players turn."""
        self._turn = not self._turn
        self.box.turn()

    def add_card(self, card):
        """Add a Card object to Players hand.

        Takes a card just poped off Deck by dealer and includes it in hand.

        Args:
            card (Card): Card object popped off deck
        """
        self.hand.append(card)
        self.box.addWidget(card)
        self.window.repaint()
        self.window.update()

    def set_box(self, box):
        """Set box to PlayerBox widget.

        Args:
            box (PlayerBox): QGroupBox containing each players cards.
        """
        self.box = box

    def show_score(self, score):
        """Write players score to the QTextBrowser Widgit.

        Args:
            score (int): self.score
        """
        self.box.scorelabel.setText(str(score))


class Dealer(Player):
    """Dealer Object. Controls most aspects of the game.

    Subclass of Player but requires a few extra keyword args
    """

    def __init__(self, decks=2, players=2, driver=None, **kwargs):
        """Dealer constructor.

        Args:
            decks (int, optional): Number of decks to use.
            players (int, optional): Total players in game.
        """
        super().__init__(**kwargs)
        self.title = "Dealer"
        self.deck_count = decks
        self.player_count = players
        self.deck = Deck.times(self.deck_count)
        self.current = 0
        self.players = []
        self.driver = driver

    def set_prefs(self, players, decks):
        """Set game preferences.

        Args:
            players (int): number of players
            decks (int): number of decks
        """
        self.deck_count = decks
        if self.player_count < players:
            for _ in range(players - self.player_count):
                pos = len(self.players) + 1
                player = Player(pos=pos, window=self.window)
                self.window.add_player(player)
                self.players.append(player)
        self.player_count = players
        self.resetDeck()
        self.driver.update_prefs()

    def resetDeck(self):
        """Delete deck and Shuffle new deck."""
        del self.deck
        self.deck = Deck.times(self.deck_count)

    @property
    def limit(self):
        """Return the size of the deck needed before deck is reset.

        Returns:
            int: minimum deck size before reset.
        """
        if self.deck_count == 1:
            return 20
        return 50

    @property
    def score(self):
        """Overloaded method from Player Class.

        Returns:
            int: Dealers score
        """
        down = False
        for card in self.cards:
            if card.isdown():
                down = True
                break
        if down:
            score = super().score - self.hand[0].value
            return score
        return super().score

    def add_card(self, card):
        """Overload method from player class.

        Args:
            card (Card): adds card just pooped from deck to hand.
        """
        super().add_card(card)
        if len(self.cards) == 2:
            self.cards[0].faceDown()

    def start_initial_deal(self):
        """Initialize deal sequence of 2 cards to each player.

        Returns:
            bool: True upon completion.
        """
        for _ in range(2):
            for player in self.players:
                self.deal_card(player)
            self.deal_card(self)
        return True

    def deal_card(self, player):
        """Retreive card from top of deck and deals to player.

        Args:
            player (Player): instance of Player in game
        """
        card = self.deck.pop()
        player.add_card(card)
        player.show_score(player.score)
        self.driver.update_decksize()
        self.window.update()
        self.window.repaint()

    def dealer_round(self):
        """Call when all other players have had their turn betting."""
        self.turn()
        for card in self.cards:
            card.faceUp()
            self.show_score(self.score)
            sleep(0.3)
        while self.score < 16:
            self.deal_card(self)
            sleep(0.3)
        self.turn()

    def player_hit(self, player):
        """Call when Player asks dealer to "hit".

        Args:
            Player (Player) the player whos turn it is.
        """
        self.deal_card(player)
        self.driver.chances_of_exactly(player)
        self.driver.chances_of_breaking(player)
        self.driver.chances_of_under(player)
        if player.score > 21:
            for card in player.hand:
                if card.name == "ace":
                    card.value = 1
                    self.driver.chances_of_exactly(player)
                    self.driver.chances_of_breaking(player)
                    self.driver.chances_of_under(player)
                    return player.show_score(player.score)
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

    def round(self):
        """Begin new players turn for betting, hitting or staying."""
        player = self.players[self.current]
        self.driver.chances_of_exactly(player)
        self.driver.chances_of_breaking(player)
        self.driver.chances_of_under(player)
        player.turn()

    def new_game(self):
        """Call after dealer has played their turn."""
        if len(self.deck) <= self.limit:
            self.resetDeck()
        self.start_initial_deal()
        self.current = 0
        self.round()

    def add_players(self):
        """Part of the constructor.

        Initializes a new players according to num_players attribute
        and creates their GUI representation.
        """
        for num in range(1, self.player_count + 1):
            kwargs = {"pos": num, "window": self.window}
            player = Player(**kwargs)
            self.window.addPlayer(player)
            self.players.append(player)
