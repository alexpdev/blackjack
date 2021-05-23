import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

CARDCOVER = os.path.join(os.environ["IMG_DIR"],"card_cover.png")

class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.dealer = None
        self.game = None
        self.setWindowTitle("BlackJack")
        self.setupUi()

    def setupUi(self):
        self.central = QWidget(parent=self)
        self.centLayout = QVBoxLayout()
        self.central.setLayout(self.centLayout)
        self.setCentralWidget(self.central)
        self.horiz1 = QHBoxLayout()
        self.horiz2 = QHBoxLayout()
        self.button1 = HitButton(self.central)
        self.button2 = StandButton(self.central)
        self.button3 = NewGameButton(self.central)
        self.textBrowser = QTextBrowser(self.central)
        self.horiz2.addWidget(self.button3)
        self.horiz2.addWidget(self.button1)
        self.horiz2.addWidget(self.button2)
        self.centLayout.addLayout(self.horiz1)
        self.centLayout.addLayout(self.horiz2)
        self.centLayout.addWidget(self.textBrowser)
        self.player_widgets = {}

    def addPlayer(self,player):
        groupbox = QGroupBox(self.central)
        self.horiz1.addWidget(groupbox)
        groupbox.setTitle(player.title)
        hlayout = QHBoxLayout()
        card1 = CardWidget(self)
        card2 = CardWidget(self)
        hlayout.addWidget(card1)
        hlayout.addWidget(card2)
        widgets = { "cards":[card1,card2], "box":groupbox, "layout":hlayout }
        self.player_widgets[str(player)] = widgets
        player.setWidgets(widgets)
        groupbox.setLayout(hlayout)

    def setDealer(self,dealer,game):
        self.game = game
        self.dealer = dealer
        self.addPlayer(dealer)

class CardWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.path = CARDCOVER
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)

    def setImg(self,path):
        self.path = path
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)


class HitButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setText("Hit")

class StandButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setText("Stand")

class NewGameButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.parent = parent
        self.setText("New Game")
        self.pressed.connect(self.start_new_game)

    def start_new_game(self):
        window = self.parent.parent()
        window.game.new_game()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())