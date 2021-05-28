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

from blackJack.utils import (QGroupBox, QHBoxLayout, QLabel, QPixmap,
                             QSpacerItem, QVBoxLayout)

IMG_DIR = os.environ.get("IMG_DIR")
CARDCOVER = os.path.join(IMG_DIR,"card_cover.png")

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
        self.hbox2 = QHBoxLayout()
        self.label = QLabel("Score: ")
        self.label.setStyleSheet("""QLabel {
                                    color: black;
                                    font-weight: bold;
                                    font-size: 14pt;
                                    font-style: italic;}""")
        self.scorelabel = QLabel("0")
        self.scorelabel.setStyleSheet("""QLabel {
                                        border: 1px solid black;
                                        padding: 3px;
                                        color: black;
                                        font-weight: bold;
                                        font-size: 16pt;
                                        font-style: italic;}""")
        self.hbox2.addWidget(self.label)
        self.hbox2.addWidget(self.scorelabel)
        self.hbox2.addSpacerItem(QSpacerItem(80,0))
        self.setLayout(self.vbox)
        self.vbox.addLayout(self.hbox2)
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
        while len(self.cards) > 0:
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
        margin: 4px;
        padding: 5px;}"""

    def __init__(self, parent=None,card=None,cover=True,path=CARDCOVER):
        super().__init__(parent=parent)
        self.setStyleSheet(self.stylesheet)
        self.cover = cover
        self.path = path
        self.card = card
        self.setImage()

    def faceDown(self):
        pixmap = QPixmap(CARDCOVER)
        self.setPixmap(pixmap)

    def faceUp(self):
        self.setImage()

    def setCard(self,card):
        self.cover = False
        self.card = card
        self.path = card.path
        self.setImage()

    def setImage(self):
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)
