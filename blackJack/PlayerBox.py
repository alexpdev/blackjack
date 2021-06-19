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

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QGridLayout, QGroupBox, QHBoxLayout, QLabel,
                             QSizePolicy, QSpacerItem, QVBoxLayout)


class PlayerBox(QGroupBox):
    """PlayerBox Subclass of QGroupBox.

    Returns GroupBoxWidget data and cards for each player.
    """

    offsheet = """QGroupBox {
        font-size: 14pt;
        padding: 4px;
        margin: 5px;
        color: #efeefe;
        border: 9px solid #dfa;} """

    onsheet = """QGroupBox {
        color: red;
        padding: 4px;
        margin: 5px;
        border: 5px solid red;
        border-radius: 2px;}"""

    labelsheet = """QLabel {
        color: #efeefe;
        margin-bottom: 8px;
        font-weight: bold;
        font-size: 14pt;
        font-style: italic;}"""

    scoresheet = """QLabel {
        border: 1px solid #efeefe;
        padding: 3px;
        margin-bottom: 8px;
        color: #efeefe;
        font-weight: bold;
        font-size: 16pt;
        font-style: italic;}"""

    def __init__(self, title, parent=None, player=None):
        """Construct a PlayerBox Widget.

        Args:
            parent (QWidget, optional) Parent widget object. Defaults to None.
            player (Player) The player this box will be assigned to.
        """
        super().__init__(title, parent=parent)
        self.player = player
        self._turn = False
        self.player.box = self
        self.setStyleSheet(self.offsheet)
        self._setupUi()

    def _setupLabels(self):
        """Set up window labels."""
        expolicy = QSizePolicy.Policy.MinimumExpanding
        minpolicy = QSizePolicy.Policy.Minimum
        self.label = QLabel("Score: ")
        self.label.setStyleSheet(self.labelsheet)
        self.hbox.addWidget(self.label)
        self.hbox.addSpacerItem(QSpacerItem(10, 0, minpolicy, minpolicy))
        self.scorelabel = QLabel("0")
        self.scorelabel.setStyleSheet(self.scoresheet)
        self.hbox.addWidget(self.scorelabel)
        self.hbox.addSpacerItem(QSpacerItem(50, 0, expolicy, minpolicy))

    def _setupCards(self):
        """Create card covers."""
        card = CardWidget(parent=self)
        self.addCard(card)
        self.grid.addWidget(card, 0, 0, -1, -1)
        card2 = CardWidget(parent=self)
        self.addCard(card2)
        self.grid.addWidget(card2, 0, 1, -1, -1)

    def _setupUi(self):
        """Create UI elements."""
        self.vbox = QVBoxLayout()
        self.grid = QGridLayout()
        self.hbox = QHBoxLayout()
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.grid)
        self.setLayout(self.vbox)
        self._setupLabels()
        self._setupCards()

    @property
    def cardCount(self):
        """Count cards in players hand.

        Returns:
            int: Total number of cards in players hand.
        """
        return len(self.player.cards)

    @property
    def cards(self):
        """Shortcut method accessing players cards property.

        Returns:
            list: A list of cards stored in players hand.
        """
        return self.player.cards

    def addCard(self, card):
        """Shortcut for adding card widget to players list of cards."""
        self.player.cards.append(card)

    def deleteCard(self):
        """Remove card from Players list of cards property."""
        self.player.cards = self.player.cards[1:]

    def reset(self):
        """Clear PlayerBox of all widgets.

        Called when current round ends and new deal begins.
        """
        while len(self.cards) > 0:
            card = self.cards[0]
            card.destroy(True, True)
            self.grid.removeWidget(card)
            self.deleteCard()
            del card

    def addWidget(self, card):
        """Add another card to Window."""
        pos = self.cardCount
        widget = CardWidget(cover=False, card=card, path=card.path)
        if pos:
            self.grid.addWidget(widget, 0, pos, -1, -1)
        else:
            self.grid.addWidget(widget, 0, 0, -1, -1)
        self.addCard(widget)

    def isTurn(self):
        """Return True if currently players turn.

        Returns:
            bool: True if it's players turn else false.
        """
        return self._turn

    def turn(self):
        """Flip `self.turn` property False or True.

        Changes the style of PlayerBox to indicate if it
        is or isn't currently players turn.
        """
        if self.isTurn():
            self._turn = False
            self.setStyleSheet(self.offsheet)
        else:
            self._turn = True
            self.setStyleSheet(self.onsheet)


CARDBACK = os.path.join(os.environ["IMG_DIR"], "card_cover.png")


class CardWidget(QLabel):
    """Store the image of the card it represents for GUI display.

    QLabel (QPixmap) Either a specific card or back of card if it is facedown.
    """

    stylesheet = """QLabel {
                        margin: 0px;
                        padding: 0px;}"""

    def __init__(self, parent=None, card=None, cover=True, path=None):
        """Construct new CardWidget instance.

        parent (QWidget, optional): parent widget for CardWidget.
        card (Card, optional): Card object. Defaults to None.
        cover (bool, optional): If True use Cardcoverpath else use give path.
        path (str, optional): path to Pixmap Image. Defaults to CARDCOVER.
        """
        super().__init__(parent=parent)
        self.setStyleSheet(self.stylesheet)
        self.cover = cover
        self.path = path
        self.card = card
        self.setImage()

    def faceDown(self):
        """Call to hide value of dealers facedown card."""
        pixmap = QPixmap(CARDBACK)
        self.setPixmap(pixmap)

    def faceUp(self):
        """Flip a facedown card to up position."""
        self.setImage()

    def setCard(self, card):
        """Assign Card objrct to a CardWidget.

        Args: card (Card object)
        """
        self.cover = False
        self.card = card
        self.path = card.path
        self.setImage()

    def setImage(self):
        """Assign image path as pixmap."""
        if not self.path:
            self.path = CARDBACK
        pixmap = QPixmap(self.path)
        self.setPixmap(pixmap)
