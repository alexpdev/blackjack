from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Window(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("BlackJack")
        self.setupUi()

    def setupUi(self):
        self.central = QWidget()
        self.centLayout = QVBoxLayout()
        self.central.setLayout(self.centLayout)
        self.button1 = HitButton("Hit",parent=self)
        self.button2 = StandButton("Stay",parent=self)
        self.horiz1 = QHBoxLayout()
        self.horiz1.addWidget(self.button1)
        self.horiz1.addWidget(self.button2)


class HitButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setText("Hit")

class StandButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setText("Stand")
