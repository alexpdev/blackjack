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
from card_counter.Deck import Deck
from card_counter.Window import CardWidget

class Player:

    def __init__(self,pos=None,window=None,**kwargs):
        self.pos = pos
        self.hand = []
        self.window = window
        self._turn = False
        self.cards = []
        self.box = None
        self.title = "Player " + str(pos)

    @property
    def score(self):
        return sum(card.value for card in self.hand)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def isturn(self):
        return self._turn

    def turn(self):
        self._turn = not self._turn
        self.box.turn()

    def output(self,line):
        self.window.textBrowser.append(line)

    def add_card(self,card):
        self.hand.append(card)
        for widg in self.cards:
            if widg.cover == True:
                widg.setCard(card)
                return self.show_hand()
        widget = CardWidget(cover=False,card=card,path=card.path)
        self.box.hbox.addWidget(widget)
        self.cards.append(widget)
        return self.show_hand()

    def show_score(self):
        self.box.scorebox.display(self.score)

    def show_hand(self):
        self.show_score()
        output = str(self) + " "  + str(self.hand) + " " + str(self.score) + "\n"
        print(self,self.hand,self.score)
        self.output(output)

class Dealer(Player):
    """
        Dealer Object. Controls game.
    """

    def __init__(self,deck_count=1,players=[],**kwargs):
        super().__init__(**kwargs)
        self.title = "Dealer"
        self.deck_count = deck_count
        self.players = players
        self.current = 0
        self.deck = Deck.times(deck_count)
        self.limit = len(self.deck)//2

    def start_deal(self):
        for _ in range(2):
            for player in self.players:
                self.deal_card(player)
            self.deal_card(self)

    def deal_card(self,player):
        card = self.deck.pop()
        player.add_card(card)
        self.window.update()

    def round(self):
        player = self.players[self.current]
        print("round",player)
        player.turn()
        player.show_hand()

    def dealer_round(self):
        self.turn()
        while self.score < 16:
            self.deal_card(self)
            self.show_hand()
        if self.score > 21:
            self.output("Dealer Busts")

    def player_hit(self,player):
        self.deal_card(player)
        player.show_hand()
        if player.score > 21:
            self.output(player.title + " Broke")
            player.turn()
            return False
        return True

    def next_player(self):
        self.current += 1
        if self.current < len(self.players):
            self.round()
        else:
            self.current = 0
            self.dealer_round()

    def next_round(self):
        for player in self.players:
            player.cards = []
            player.hand = []
            player.box.reset()
            for _ in range(2):
                card = CardWidget(parent=self.central)
                player.box.layout().addWidget(card)
                player.cards.append(card)

    def new_game(self):
        self.deck.shuffle()
        self.start_deal()
        self.current = 0
        self.round()
