import sys
from os.path import dirname, abspath
if __name__ == "__main__":
    sys.path.append(dirname(dirname(abspath(__file__))))
from card_counter.Players import Dealer

NUMBER_PLAYERS = 2

def start_game(n):
    dealer = Dealer(n)
    dealer.deck.shuffle()
    dealer.play()

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 1:
        numplayers = sys.argv[-1]
    else:
        numplayers = NUMBER_PLAYERS
    start_game(numplayers)
