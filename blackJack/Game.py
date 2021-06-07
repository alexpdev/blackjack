import sys
import math
from PyQt6.QtWidgets import QApplication
from blackJack.Players import Dealer
from blackJack.Window import Window



class Driver:

    default_players = 2
    default_decks = 2

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.window = Window(parent=None,
                            players=self.default_players,
                            app=self.app)
        self.dealer = Dealer(window=self.window,
                            decks=self.default_decks,
                            players=self.default_players,
                            pos=0,
                            driver=self)
        self.window.setDealer(self.dealer)
        self.window.show()
        self.drawn = []
        self.counts = {
            "ace": 0,
            "king": 0,
            "queen": 0,
            "jack": 0,
            "10": 0,
            "9": 0,
            "8":0,
            "7":0,
            "6":0,
            "5":0,
            "4":0,
            "3":0,
            "2":0,
        }

    def output(self,s):
        self.dealer.output(s)

    def chances_of_blackjack(self):
        tens_aces = self.total_tens() * self.counts["ace"]
        print(tens_aces)
        alls = math.comb(self.decksize,2)
        print(alls)
        percentage = (tens_aces / alls )
        print(percentage)
        # p = round(percentage,2)
        s = f"{percentage}% chance of blackjack"
        self.output(s)

    def chances_of_x(self,x):
        count, num = 0, x
        if num >= 10: count, num = self.total_tens(), 9
        while 1 > num < 10:
            count += self.counts[str(x)]
            num -= 1
        busting = (count / self.decksize) * 100
        print(busting)
        s = f"{str(busting)}% chance of not breaking 21"
        self.output(s)

    def total_tens(self):
        total = 0
        for name in ["queen","10","jack","king"]:
            total += self.counts[name]
        return total

    @property
    def decksize(self):
        return self.dealer.decksize

    @property
    def players(self):
        return self.dealer.player_count

    @property
    def decks(self):
        return self.dealer.deck_count

    def draw(self,card):
        self.window.cards_val.setText(str(self.decksize))
        self.drawn.append(card)
        self.counts[card.name] -= 1

    def update_count(self):
        # self.window.ndecks_val.setText(str(self.decks))
        # self.window.nplayers_val.setText(str(self.players))
        self.window.cards_val.setText(str(self.decksize))
