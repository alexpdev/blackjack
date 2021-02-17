from players import Player,Dealer
from game import Card,Deck


def start_game():
    p1 = Player(1)
    p2 = Player(2)
    dealer = Dealer()
    deck = Deck.create()
    dealer.players.append(p1)
    dealer.players.append(p2)
    dealer.deck = deck
    dealer.deck.shuffle()
    dealer.deal()
    print([player.hand for player in dealer.players])

start_game()
