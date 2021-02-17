import random
from game import Deck

class Player:

    def __init__(self,id):
        self.hand = []
        self.turn = False
        self.id = id
        self.title = "Player " + str(id)

    def __str__(self):
        if self.id == 0:
            return "Dealer"
        return self.title

    def score(self):
        score = sum([i.value for i in self.hand])
        if score > 21 and "ace" in [i.suit for i in self.hand]: 
            score = sum([i.value if i != "ace" else 1 for i in self.hand])
        return score
    
    def add_card(self,card):
        self.hand.append(card)
    
    def hit(self):
        return True
    
    def stay(self):
        return False
    
    def hit_stay(self,faceup):
        print("Your hand " + str([str(i) for i in self.hand]))
        print("Your Score " + str(self.score()))
        print("Dealer's Faceup Card:" + str(faceup))
        if self.score() <= 21:
            i = input("(1)Hit or (2)Stay")
            if i == 1:
                return self.hit()
        return self.stay()


class Dealer(Player):

    def __init__(self):
        super().__init__(0)
        self._deck = Deck()
        self.players = []
        self._faceup = None

    @property
    def faceup(self):
        return self._faceup

    @faceup.setter
    def faceup(self,card):
        self._faceup = card

    @property
    def deck(self):
        return self._deck

    def deal_table(self):
        for player in self.players:
            self.deal_card(player)
        self.deal_self()
        for player in self.players:
            self.deal_card(player)
        self.deal_self()

    def deal_self(self):
        card = self.deck.pop()
        self.add_card(card)
        if not self.faceup:
            self.faceup = card

    def deal_card(self,player):
        card = self.deck.pop()
        player.add_card(card)
        return
    
    def add_player(self,player):
        self.players.append(player)
    
    def ask_table(self):
        stays = 0
        for player in self.players:
            if player.hit_stay(self.faceup):
                card = self.deck.pop()
                player.add_card(card)
            else:
                stays += 1
        if stays == len(self.players):
            self.show_hand()

    def show_hand(self):
        print(str(self.hand))

    def self_ask(self):
        if self.calculate_hand < 16:
            self.deal_self()
        else:
            self.stay()

if __name__ == "__main__":
    num_players = 1
    d = Dealer()
    p = Player(num_players)
    d.add_player(p)
    print("shuffling...")
    d.deck.shuffle()
    print("Table is set. Time to deal cards.")
    d.deal_table()
    d.ask_table()

    



