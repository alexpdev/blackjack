#! /env/Scripts/python
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
from PyQt6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class PlayerBox(QGroupBox):
    """PlayerBox Subclass of QGroupBox.

    Returns GroupBoxWidget data and cards for each player.
    """

    offsheet = """QGroupBox {
        font-size: 14pt;
        padding: 4px;
        margin: 5px;
        color: #efeefe;
        border: 9px solid #dfa;}"""

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
        self.player.set_box(self)
        self.setStyleSheet(self.offsheet)
        self._setupUi()

    def _setupUi(self):
        """Create UI elements."""
        self.vbox = QVBoxLayout()
        self.vbox.setObjectName(self.player.title + "BoxVertLayout")
        self.grid = QGridLayout()
        self.grid.setObjectName(self.player.title + "BoxCardPicsLayout")
        self.hbox = QHBoxLayout()
        self.hbox.setObjectName(self.player.title + "BoxHorizLayout")
        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.grid)
        self.setLayout(self.vbox)
        self._setupLabels()
        self._setupCards()

    def _setupLabels(self):
        """Set up window labels."""
        expolicy = QSizePolicy.Policy.MinimumExpanding
        minpolicy = QSizePolicy.Policy.Minimum
        self.label = QLabel("Score: ")
        self.label.setObjectName("ScoreLabel")
        self.label.setStyleSheet(self.labelsheet)
        self.hbox.addWidget(self.label)
        self.hbox.addSpacerItem(QSpacerItem(10, 0, minpolicy, minpolicy))
        self.scorelabel = QLabel("0")
        self.scorelabel.setObjectName("ScoreValue")
        self.scorelabel.setStyleSheet(self.scoresheet)
        self.hbox.addWidget(self.scorelabel)
        self.hbox.addSpacerItem(QSpacerItem(50, 0, expolicy, minpolicy))

    def _setupCards(self):
        """Create card covers."""
        card = CardWidget(parent=self)
        card.setObjectName("Card1")
        self.addCard(card)
        self.grid.addWidget(card, 0, 0, -1, -1)
        card2 = CardWidget(parent=self)
        card2.setObjectName(self.player.title + "Card2")
        self.addCard(card2)
        self.grid.addWidget(card2, 0, 1, -1, -1)

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
            list: List of card widgets.
        """
        return self.player.cards

    def addCard(self, card):
        """Shortcut for adding card widget to players list of cards.

        Args:
            card (obj): CardWidget object.
        """
        self.player.cards.append(card)

    def deleteCard(self, card):
        """Remove card from Players list of cards property."""
        if card in self.player.cards:
            self.player.cards.remove(card)

    def reset(self):
        """Clear PlayerBox of all widgets.

        Called when current round ends and new deal begins.
        """
        while len(self.cards) > 0:
            card = self.cards[0]
            self.grid.removeWidget(card)
            card.setVisible(False)
            card.hide()
            card.destroy(True, True)
            self.deleteCard(card)
            del card
            self.repaint()
            self.update()

    def addWidget(self, card):
        """Add another card to Window.

        Args:
            card (obj): Card object from deck.

        Returns:
            bool: True if successful else None
        """
        if self.cardCount <= 2:
            for widget in self.cards:
                if not widget.has_card():
                    return widget.setCard(card)
        widget = CardWidget(card=card)
        widget.setObjectName("Card" + str(self.cardCount))
        self.grid.addWidget(widget, 0, self.cardCount, -1, -1)
        return self.addCard(widget)

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

    def __init__(self, parent=None, card=None):
        """Construct new CardWidget instance.

        parent (QWidget, optional): parent widget for CardWidget.
        card (Card, optional): Card object. Defaults to None.
        """
        super().__init__(parent=parent)
        self.setStyleSheet(self.stylesheet)
        self.card = card
        self._down = False
        self.setImage()

    def isdown(self):
        return self._down

    def faceDown(self):
        pixmap = QPixmap(CARDBACK)
        self.setPixmap(pixmap)
        self._down = True
        return True

    def faceUp(self):
        self._down = False
        self.setImage()

    def path(self):
        """Path to card image.

        Returns:
            str: filesystem path to image of card.
        """
        if self.has_card():
            return self.card.path
        else:
            return CARDBACK

    def has_card(self):
        """Ask if Widget have a card set.

        Returns:
            bool: if self.card is None
        """
        if self.card is None:
            return False
        return True

    def setCard(self, card):
        """Assign Card objrct to a CardWidget.

        Args:
            card (Card object): Card dealt from deck by dealer.

        Returns:
            bool: True if succeeded
        """
        self.card = card
        self.setImage()
        return True

    def setImage(self):
        """Assign image path as pixmap.

        Returns:
            bool: True if succeeded
        """
        pixmap = QPixmap(self.path())
        self.setPixmap(pixmap)
        return True
