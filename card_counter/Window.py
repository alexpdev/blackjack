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
        self.boxes = []

    def addPlayer(self,player):
        self.players.append(player)
        hlayout = QHBoxLayout()
        cards = []
        for _ in range(2):
            card = CardWidget(parent=self.central)
            hlayout.addWidget(card)
            cards.append(card)
        groupbox = PlayerBox(player.title,**{
            "parent": self.central,
            "player": player
        })
        groupbox.setLayout(hlayout)
        self.horiz1.addWidget(groupbox)
        self.boxes.append(groupbox)
        player.set_widgets(**{
            "cards" : cards,
            "box" : groupbox,
        })


    def setDealer(self,dealer):
        self.dealer = dealer
        self.addPlayer(dealer)


class PlayerBox(QGroupBox):

    def __init__(self,title,parent=None,player=None):
        super().__init__(title,parent=parent)
        self.player = player

class CardWidget(QLabel):

    def __init__(self, parent=None,cover=True,path=CARDCOVER):
        super().__init__(parent=parent)
        self.cover = cover
        self.path = path
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)

    def reset(self,path):
        if self.path is CARDCOVER:
            pixmap = QPixmap(path)
            self.setPixmap(pixmap)
            self.path = path
            self.cover = False

class HitButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None,dealer=None,**kwargs):
        super().__init__(parent=parent)
        self.window = window
        self.dealer = dealer
        self.setText("Hit")
        self.setStyleSheet(self.stylesheet)
        self.pressed.connect(self.hit)

    def hit(self):
        for player in self.window.players:
            if player.isturn():
                self.dealer.deal_card(player)

class StandButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,**kwargs):
        super().__init__(parent=parent)
        self.setText("Stand")
        self.setStyleSheet(self.stylesheet)

class NewGameButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None, **kwargs):
        super().__init__(parent=parent)
        self.window = window
        self.parent = parent
        self.setText("New Game")
        self.pressed.connect(self.start_new_game)
        self.setStyleSheet(self.stylesheet)

    def start_new_game(self):
        self.window.dealer.new_game()
