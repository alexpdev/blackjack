from players import Player,Dealer
from game import Card,Deck


def start_game():
    dealer = Dealer(2)
    dealer.deck.shuffle()
    dealer.play()
    print([player.hand for player in dealer.players])

start_game()
