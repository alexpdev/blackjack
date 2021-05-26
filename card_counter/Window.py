#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

CARDCOVER = os.path.join(os.environ["IMG_DIR"],"card_cover.png")

class Window(QMainWindow):
    def __init__(self,parent=None,**kwargs):
        super().__init__(parent=parent)
        self.players = []
        self.setWindowTitle("BlackJack")
        self.setupUi()

    def setupUi(self):
        self.central = QWidget(parent=self)
        self.centLayout = QVBoxLayout()
        self.central.setLayout(self.centLayout)
        self.setCentralWidget(self.central)
        self.horiz1 = QHBoxLayout()
        self.horiz2 = QHBoxLayout()
        kwargs = {"window":self, "parent": self}
        self.button1 = HitButton(**kwargs)
        self.button2 = StandButton(**kwargs)
        self.button3 = NewGameButton(**kwargs)
        self.textBrowser = QTextBrowser(self)
        self.horiz2.addWidget(self.button3)
        self.horiz2.addWidget(self.button1)
        self.horiz2.addWidget(self.button2)
        self.centLayout.addLayout(self.horiz1)
        self.centLayout.addLayout(self.horiz2)
        self.centLayout.addWidget(self.textBrowser)
        self.boxes = []

    def addPlayer(self,player):
        self.players.append(player)
        groupbox = PlayerBox(player.title,parent=self,player=player)
        self.horiz1.addWidget(groupbox)
        self.boxes.append(groupbox)

    def setDealer(self,dealer):
        self.dealer = dealer
        for button in [self.button1,self.button2,self.button3]:
            button.dealer = self.dealer
        self.addPlayer(dealer)


class PlayerBox(QGroupBox):
    offsheet = """QGroupBox {
        padding: 4px;
        margin: 2px;
        color: black;
        border: 2px solid grey;} """
    onsheet = """QGroupBox {
            color: red;
            padding: 6px;
            margin: 3px;
            border: 3px solid red;
            border-radius: 3px;}"""

    def __init__(self,title,parent=None,player=None):
        super().__init__(title,parent=parent)
        self.player = player
        self.setStyleSheet(self.offsheet)
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.setLayout(self.vbox)
        self.scorebox = QLCDNumber(parent=self)
        self.vbox.addWidget(self.scorebox)
        self.vbox.addLayout(self.hbox)
        self._turn = False
        for _ in range(2):
            card = CardWidget(parent=self)
            self.hbox.addWidget(card)
            self.addCard(card)
        self.player.box = self

    @property
    def cards(self):
        return self.player.cards

    def addCard(self,card):
        self.player.cards.append(card)

    def deleteCard(self):
        self.player.cards = self.player.cards[1:]

    def reset(self):
        while len(self.cards):
            card = self.cards[0]
            card.destroy(True,True)
            self.hbox.removeWidget(card)
            self.deleteCard()
            del card

    def isTurn(self):
        return self._turn

    def turn(self):
        if self.isTurn():
            self._turn = False
            self.setStyleSheet(self.offsheet)
        else:
            self._turn = True
            self.setStyleSheet(self.onsheet)

class CardWidget(QLabel):
    stylesheet = """QLabel {
        margin: 3px;
        padding: 3px;}"""

    def __init__(self, parent=None,card=None,cover=True,path=CARDCOVER):
        super().__init__(parent=parent)
        self.setStyleSheet(self.stylesheet)
        self.cover = cover
        self.path = path
        self.card = card
        self.setImage()

    def setCard(self,card):
        self.cover = False
        self.card = card
        self.path = card.path
        self.setImage()

    def setImage(self):
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)

class HitButton(QPushButton):

    ssheet = """QPushButton{ background-color: #1259ff;
                font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None,**kwargs):
        super().__init__(parent=parent)
        self.window = parent
        self.dealer = None
        self.setText("Hit")
        self.setStyleSheet(self.ssheet)
        self.pressed.connect(self.hit)

    def hit(self):
        for player in self.window.players:
            if not player.isturn(): continue
            if not self.dealer.player_hit(player):
                self.dealer.next_player()

class StandButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None,**kwargs):
        super().__init__(parent=parent)
        self.window = parent
        self.dealer = None
        self.setText("Stand")
        self.setStyleSheet(self.stylesheet)
        self.pressed.connect(self.stay)

    def stay(self):
        for player in self.window.players:
            if player.isturn():
                player.turn()
                break
        self.dealer.next_player()

class NewGameButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None, **kwargs):
        super().__init__(parent=parent)
        self.window = parent
        self.dealer = None
        self.setText("New Game")
        self.pressed.connect(self.start_new_game)
        self.setStyleSheet(self.stylesheet)

    def start_new_game(self):
        for player in self.window.players:
            if player.isturn():
                player.turn()
            player.box.reset()
            player.hand = []
            player.cards = []
        self.window.dealer.new_game()
