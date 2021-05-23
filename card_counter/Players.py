#! /usr/bin/python3
# -*- coding: utf-8 -*-
from card_counter.Deck import Deck
from card_counter.Window import CardWidget

class Player:

    def __init__(self,window,id_):
        self.id = id_
        self.window = window
        self.title = "Player " + str(self.id)
        self.hand = []
        self.turn = False
        self.widgets = None

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    @property
    def score(self):
        return sum(card.value for card in self.hand)

    def setWidgets(self, widgets):
        self.widgets = widgets

    def add_card(self,card,img):
        self.hand.append(card)
        self.add_card_image(img)

    def add_card_image(self,img):
        if hlen := len(self.hand) <= 2:
            ncard = self.widgets["cards"][hlen - 1]
            return ncard.setImg(img)
        new_card = CardWidget(self.window)
        new_card.setImg(img)
        self.widgets["cards"].append(new_card)
        self.widgets["layout"].addWidget(new_card)

    def show_hand(self, output):
        output.append(str(self) + " "  + str(self.hand) + " " + str(self.score) + "\n")
        print(self,self.hand,self.score)


class Dealer(Player):
    """
        Dealer Object. Controls game.
    """

    def __init__(self,window,id_=0):
        super().__init__(window,id_=id_)
        self.deck = Deck()
        self.title="Dealer"

    def new_deal(self, players):
        for _ in range(2):
            for player in players:
                self.deal_card(player)
            self.deal_self()

    def deal_self(self):
        self.deal_card(self)

    def add_card(self,card,img):
        if not len(self.hand):
            return self.hand.append(card)
        super().add_card(card,img)

    def deal_card(self,player):
        card = self.deck.pop()
        img = card.getImage()
        player.add_card(card,img)

    def start_round(self,players):
        self.new_deal(players)

    def new_game(self,players):
        self.deck = Deck()
        self.deck.shuffle()
        self.new_deal(players)

    # def start_round(self):
    #     for player in self.players:
    #         if player.score <= 21:
    #             if int(input("Hit[1] or Stay[2]?\t")) == 1:
    #                 return self.hit
    #             return self.stay
    #         print(self, " Broke: ", self.score)
    #         while player.hit_stay(self.faceup):
    #             self.deal_card(player)
    #     while self.score < 16:
    #         self.show_hand(self.output)
    #         self.deal_self(True)
    #     self.show_hand(self.output)
    #     if self.score > 21:
    #         self.output.append(f"Dealer Broke: {self.score}\n")

    # def end_round(self):
    #     self.faceup = None
    #     self.active = False
    #     for player in self.players:
    #         player.show_hand(self.output)
    #         if player.score <= 21:
    #             if player.score > self.score:
    #                 self.output.append(f"{player} Won!\n")
    #             elif player.score < self.score:
    #                 self.output.append(f"{player} Lost!\n")
    #             else:
    #                 self.output.append(f"{player} Tie!\n")
    #         player.hand = []


class Stats:

    counts = {
        2: 4, 3: 4,
        4: 4, 5: 4,
        6: 4, 7: 4,
        8: 4, 9: 4,
        10: 16, 11: 4}

    refresh = lambda: [counts.__setitem__(k,4) for k in counts]

    @classmethod
    def probability(cls,val):
        total = sum(cls.counts.values())
        p = cls.counts[val]
        return p/total