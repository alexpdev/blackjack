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

from blackJack.MenuBar import MenuBar
from blackJack.PlayerBox import PlayerBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QHBoxLayout,
                            QLabel,
                            QMainWindow,
                            QPushButton,
                            QTextBrowser,
                            QVBoxLayout,
                            QWidget)


class Window(QMainWindow):
    """
    Window MainWindow for Blackjack UI.

    Args:
        QMainWindow (Qt Widget Window): MainWindow
    """

    ssheet = """ QMainWindow {margin: 8px; padding: 6px; background-color: #e9e9e9}"""

    def __init__(self, parent=None, players=None, decks=None, app=None):
        """
        __init__ Constructor for MainWindow

        Args:
            parent (QWidget, optional): parent widget. Defaults to None.
            players (list, optional): list of players. Defaults to None.
            decks (number of decks to use, optional): this number * 52 Cards. Defaults to None.
            app (QApplication, optional): Main Application. Defaults to None.
        """
        super().__init__(parent=parent)
        self.players = []
        self.players_count = players
        self.deck_count = decks
        self.app = app
        self.setStyleSheet(self.ssheet)
        self.setWindowTitle("BlackJack")
        self.setObjectName("MainWindow")
        icon = QIcon(os.path.join(os.environ["IMG_DIR"], "blackjackicon.png"))
        self.setWindowIcon(icon)
        self.setupUi()

    def setupUi(self):
        """
        setupUi Constructs the internal layout and
                widget contents for the Window
        """
        #central widget
        self.central = QWidget(parent=self)
        self.centLayout = QVBoxLayout()
        self.central.setLayout(self.centLayout)
        self.setCentralWidget(self.central)

        #layouts
        self.horiztop = QHBoxLayout()
        self.horiz1 = QHBoxLayout()
        self.horiz2 = QHBoxLayout()

        # buttons and textbox
        self.button1 = HitButton(window=self, parent=self)
        self.button2 = StandButton(window=self, parent=self)
        self.button3 = NewGameButton(window=self, parent=self)
        self.textBrowser = QTextBrowser(self)

        # information labels
        self.ncards_label = QLabel("Cards in Deck: ")
        self.ncards_val = QLabel(str(self.deck_count * 52))
        self.ndecks_label = QLabel("Number of Decks: ")
        self.ndecks_val = QLabel("0")
        self.nplayers_label = QLabel("Number of Players: ")
        self.nplayers_val = QLabel("0")

        for label, val in [
            (self.ncards_label, self.ncards_val),
            (self.ndecks_label, self.ndecks_val),
            (self.nplayers_label, self.nplayers_val),
        ]:

            for widg in [label, val]:
                self.horiztop.addWidget(widg)
                widg.setStyleSheet("""QLabel {font-weight: bold; color: black;}""")
            label.setAlignment(Qt.AlignmentFlag.AlignRight)
            val.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # layout configuration for window
        self.horiz2.addWidget(self.button3)
        self.horiz2.addWidget(self.button1)
        self.horiz2.addWidget(self.button2)
        self.centLayout.addLayout(self.horiztop)
        self.centLayout.addLayout(self.horiz1)
        self.centLayout.addLayout(self.horiz2)
        self.centLayout.addWidget(self.textBrowser)

        # adding a MenuBar
        self.mainMenuBar = MenuBar(parent=self, window=self)
        self.setMenuBar(self.mainMenuBar)
        self.mainMenuBar.setNativeMenuBar(False)

        # list of groupboxes. one for each player
        self.boxes = []

    def addPlayer(self, player):
        """
        addPlayer construct groupbox for each player

        Args:
            player (Player Object): One of the Dealers challengers
        """
        self.players.append(player)
        groupbox = PlayerBox(player.title, parent=self, player=player)
        self.horiz1.addWidget(groupbox)
        self.boxes.append(groupbox)

    def setDealer(self, dealer):
        """
        setDealer Assign a dealer to the window

        Args:
            dealer (Dealer Object): subtype of Player with more power
            - responsible for dealing cards and shuffling.
        """
        self.dealer = dealer
        for button in [self.button1, self.button2, self.button3]:
            button.dealer = self.dealer
        self.addPlayer(dealer)

    def clearPlayers(self):
        """
        clearPlayers Clear out old players groupbox for new players
        """
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
    """
    HitButton Click button if player wants to
    be dealt another card

    Args:
        QPushButton (ButtonWidget): Ask dealer for one more card.
    """
    ssheet = """QPushButton{ background-color: #1259ff;
                font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None, window=None):
        """
        __init__ constructor for HitButton

        Args:
            parent (Window, optional): mainwindow. Defaults to None.
            window (Window, optional): mainwindow. Defaults to None.
        """
        super().__init__(parent=parent)
        self.window = window
        self.dealer = None
        self.setText("Hit")
        self.setStyleSheet(self.ssheet)
        self.pressed.connect(self.hit)

    def hit(self):
        """
        hit ask dealer for another card
        """
        for player in self.window.players:
            if player.isturn():
                self.dealer.player_hit(player)


class StandButton(QPushButton):
    """
    StandButton Click button if player does not want another
    card and is ready to hand turn to next player

    Args:
        QPushButton (ButtonWidget): Tell dealer no more cards and
        allow next player to take turn
    """

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None, window=None):
        """
        __init__ constructor for StayButton

        Args:
            parent (Window, optional): mainwindow. Defaults to None.
            window (Window, optional): mainwindow. Defaults to None.
        """
        super().__init__(parent=parent)
        self.window = window
        self.dealer = None
        self.setText("Stand")
        self.setStyleSheet(self.stylesheet)
        self.pressed.connect(self.stay)

    def stay(self):
        """
        stay Tell Dealer you do not want any more cards
        and next player can take turn.
        """
        for player in self.window.players:
            if player.isturn():
                player.turn()
                break
        self.dealer.next_player()


class NewGameButton(QPushButton):
    """
    NewGameButton Click button when all players including the
    dealer have taken turn and ready to start next round of dealing.

    Args:
        QPushButton (ButtonWidget): NextRound of dealing
    """

    stylesheet = """QPushButton{ background-color: #1259ff;
                    font: bold 20pt black; padding: px; margin: 2px;}"""

    def __init__(self, parent=None, window=None):
        """
        __init__ constructor for NewGameButton

        Args:
            parent (Window, optional): mainwindow. Defaults to None.
            window (Window, optional): mainwindow. Defaults to None.
        """
        super().__init__(parent=parent)
        self.window = window
        self.dealer = None
        self.setText("New Game")
        self.pressed.connect(self.start_new_game)
        self.setStyleSheet(self.stylesheet)

    def start_new_game(self):
        """
        start_new_game remove cards from playerbox, remove cards in hand,
        set score to zero, and start next round of dealing for each player.
        """
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
