import os
import sys
from os.path import dirname, abspath, join

PROJ_DIR = dirname(dirname(abspath(__file__)))
IMG_DIR = join(PROJ_DIR,"img")

sys.path.append(PROJ_DIR)
os.environ["IMG_DIR"] = IMG_DIR


from card_counter.Players import Dealer,Player
from card_counter.Window import Window
from PyQt6.QtWidgets import QApplication


class Game:
    def __init__(self,window, dealer, num_players=5):
        self.window = window
        self.dealer = dealer
        self.players = []
        self.window.setDealer(dealer,self)
        for n in range(1, num_players+1):
            p = Player(self.window, n)
            self.players.append(p)
            self.window.addPlayer(p)

    def new_game(self):
        self.dealer.new_game(self.players)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    dealer = Dealer(window)
    game = Game(window, dealer)
    sys.exit(app.exec())
