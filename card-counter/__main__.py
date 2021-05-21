import sys
from os.path import dirname, abspath
from .Players import Dealer


src_dir = dirname(abspath(__file__))
project_dir = dirname(src_dir)
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
