from Deck import Deck, DeckEmpty

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

    def __repr__(self):
        return str(self)

    @property
    def score(self):
        return sum(card.value for card in self.hand)

    def add_card(self,card):
        self.hand.append(card)

    @property
    def hit(self):
        return True

    @property
    def stay(self):
        return False

    def show_hand(self):
        print(self,self.hand,self.score)

    def hit_stay(self,faceup):
        print("Faceup:" + str(faceup))
        self.show_hand()
        if self.score <= 21:
            if int(input("Hit[1] or Stay[2]?\n")) == 1:
                return self.hit
            return self.stay
        print(self, " Broke: ", self.score)

class Dealer(Player):

    def __init__(self,num_players=1):
        super().__init__(0)
        self.deck = Deck()
        self.players = None
        self.faceup = []
        self.active = False
        for i in range(num_players):
            player = Player(i+1)
            self.add_player(player)

    def shuffle(self):
        self.deck.shuffle()

    def play(self):
        try:
            while len(self.deck) > 0:
                self.new_deal()
                self.start_round()
                self.end_round()
        except DeckEmpty:
            print("New Deck")
            self.deck = Deck()
            self.play()

    def new_deal(self):
        self.active = True
        for player in self.players:
            self.deal_card(player)
        self.deal_self()
        for player in self.players:
            self.deal_card(player)
        self.deal_self(True)

    def deal_self(self,faceup=False):
        card = self.deck.pop()
        if faceup:
            self.faceup.append(card)
        self.add_card(card)

    def deal_card(self,player):
        card = self.deck.pop()
        player.add_card(card)

    def add_player(self,player):
        if not self.players:
            self.players = (player,)
            return self.players
        players = list(self.players)
        players.append(player)
        self.players = tuple(players)

    def start_round(self):
        for player in self.players:
            while player.hit_stay(self.faceup):
                self.deal_card(player)
        while self.score < 16:
            self.show_hand()
            self.deal_self(True)
        self.show_hand()
        if self.score > 21:
            print("Dealer Broke", self.score)

    def end_round(self):
        self.faceup = []
        self.active = False
        for player in self.players:
            player.show_hand()
            if player.score <= 21:
                if player.score > self.score:
                    print(player, "Winner")
                elif player.score < self.score:
                    print(player, "Lost")
                else:
                    print(player, "Tie")
                player.hand = []
