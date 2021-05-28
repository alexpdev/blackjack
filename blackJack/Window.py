#! /usr/bin/python3
# -*- coding: utf-8 -*-

#######################################################################
# BlackJack Card Counting
# Copyright (C) 2021  alexpdev
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses
#########################################################################

import os

from card_counter.MenuBar import MenuBar
from card_counter.PlayerBox import PlayerBox
from card_counter.utils import (QMainWindow,
                                QHBoxLayout,
                                QVBoxLayout,
                                QPushButton,
                                QLabel,
                                Qt,
                                QIcon,
                                QWidget,
                                QTextBrowser)



class Window(QMainWindow):
    ssheet = """ QMainWindow {margin: 8px; padding: 6px; background-color: #e9e9e9}"""
    def __init__(self,parent=None,**kwargs):
        super().__init__(parent=parent)
        self.players = []
        self.setStyleSheet(self.ssheet)
        self.setWindowTitle("BlackJack")
        self.setObjectName("MainWindow")
        icon = QIcon(os.path.join(os.environ["IMG_DIR"],"blackjackicon.png"))
        self.setWindowIcon(icon)
        self.setupUi()

    def setupUi(self):
        self.central = QWidget(parent=self)
        self.centLayout = QVBoxLayout()
        self.central.setLayout(self.centLayout)
        self.setCentralWidget(self.central)
        self.horiztop = QHBoxLayout()
        self.ncards_label = QLabel("Cards in Deck: ")
        self.ncards_val = QLabel("0")
        self.ndecks_label = QLabel("Number of Decks: ")
        self.ndecks_val = QLabel("0")
        self.nplayers_label = QLabel("Number of Players: ")
        self.nplayers_val = QLabel("0")
        for label,val in [
            (self.ncards_label,self.ncards_val),
            (self.ndecks_label,self.ndecks_val),
            (self.nplayers_label,self.nplayers_val)
            ]:
            for widg in [label,val]:
                self.horiztop.addWidget(widg)
                widg.setStyleSheet("""QLabel {font-weight: bold; color: black;}""")
            label.setAlignment(Qt.AlignmentFlag.AlignRight)
            val.setAlignment(Qt.AlignmentFlag.AlignLeft)
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
        self.centLayout.addLayout(self.horiztop)
        self.centLayout.addLayout(self.horiz1)
        self.centLayout.addLayout(self.horiz2)
        self.centLayout.addWidget(self.textBrowser)
        self.mainMenuBar = MenuBar(parent=self,window=self)
        self.setMenuBar(self.mainMenuBar)
        self.mainMenuBar.setNativeMenuBar(False)
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

    def clearPlayers(self):
        for player in self.players[1:]:
            self.horiz1.removeWidget(player.box)
            player.box.reset()
            player.box.destroy()
            player.box.setVisible(False)
            player.box.hide()
            del player.box
            self.players.remove(player)
            self.dealer.players.remove(player)
            del player
            self.update()
            self.repaint()
        self.players = self.players[:1]

class HitButton(QPushButton):

    ssheet = """QPushButton{ background-color: #1259ff;
                font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None,**kwargs):
        super().__init__(parent=parent)
        self.window = window
        self.dealer = None
        self.setText("Hit")
        self.setStyleSheet(self.ssheet)
        self.pressed.connect(self.hit)

    def hit(self):
        for player in self.window.players:
            if player.isturn():
                if self.dealer.player_hit(player): return
                return self.dealer.next_player()

class StandButton(QPushButton):

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None,window=None,**kwargs):
        super().__init__(parent=parent)
        self.window = window
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
        self.window = window
        self.dealer = None
        self.setText("New Game")
        self.pressed.connect(self.start_new_game)
        self.setStyleSheet(self.stylesheet)

    def start_new_game(self):
        if len(self.window.players) < self.dealer.player_count + 1:
            self.window.clearPlayers()
            self.dealer.add_players()
        else:
            for player in self.window.players:
                if player.isturn():
                    player.turn()
                player.box.reset()
                player.hand = []
                player.cards = []
            self.window.dealer.new_game()
