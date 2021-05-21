import sys
from os.path import join, dirname, abspath
from utils import start_game

__version__ = "0.2.1"

src_dir = dirname(abspath(__file__))
project_dir = dirname(src_dir)
NUMBER_PLAYERS = 2

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 1:
        numplayers = sys.argv[-1]
    else:
        numplayers = NUMBER_PLAYERS
    start_game(numplayers)
