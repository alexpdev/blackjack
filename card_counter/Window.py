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
        kwargs = {"window":self, "parent": self.central}
        self.button1 = HitButton(**kwargs)
        self.button2 = StandButton(**kwargs)
        self.button3 = NewGameButton(**kwargs)
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
        groupbox = PlayerBox(player.title,**{"parent": self.central,"player": player})
        groupbox.setLayout(hlayout)
        self.horiz1.addWidget(groupbox)
        self.boxes.append(groupbox)
        player.set_widgets(**{"cards" : cards, "box" : groupbox})


    def setDealer(self,dealer):
        self.dealer = dealer
        self.addPlayer(dealer)


class PlayerBox(QGroupBox):
    stylesheet = """QGroupBox {
        padding: 4px;
        margin: 2px;
        color: black;
        border: 2px solid grey;} """

    def __init__(self,title,parent=None,player=None):
        super().__init__(title,parent=parent)
        self.player = player
        self.setStyleSheet(self.stylesheet)

    def reset(self):
        for card in self.player.cards:
            self.layout().removeWidget(card)
            del card
        self.update()
        self.repaint()



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
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)

    def reset(self,path):
        if self.path is CARDCOVER:
            pixmap = QPixmap(path)
            self.setPixmap(pixmap)
            self.path = path
            self.cover = False

    def setCard(self,card):
        self.card = card


class HitButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None,**kwargs):
        super().__init__(parent=parent)
        self.window = window
        self.setText("Hit")
        self.setStyleSheet(self.stylesheet)
        self.pressed.connect(self.hit)

    def hit(self):
        for player in self.window.players:
            if player.isturn():
                print(player.score)
                if player.score > 21:
                    stylesheet = """QGroupBox { padding: 4px; margin: 2px;
                                    color: black; border: 2px solid grey;}"""
                    player.box.setStyleSheet(stylesheet)
                    self.window.dealer.next_player()
                else:
                    self.window.dealer.player_hit(player)

class StandButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None,**kwargs):
        super().__init__(parent=parent)
        self.window = window
        self.setText("Stand")
        self.setStyleSheet(self.stylesheet)
        self.pressed.connect(self.stay)

    def stay(self):
        for player in self.window.players:
            if player.isturn():
                player.show_hand()
                player.turn()
                stylesheet = """QGroupBox { padding: 4px; margin: 2px;
                                color: black; border: 2px solid grey;}"""
                player.box.setStyleSheet(stylesheet)
                break
        self.window.dealer.next_player()

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
        for player in self.window.players:
            player.box.reset()
            player.hand = []
            player.cards = []
        self.window.dealer.new_game()
