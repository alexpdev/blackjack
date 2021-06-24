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

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QHBoxLayout, QMainWindow, QMessageBox,
                             QPushButton, QVBoxLayout, QWidget)

from blackJack.MenuBar import MenuBar
from blackJack.statsFrame import StatsFrame
from blackJack.PlayerBox import PlayerBox


class Window(QMainWindow):
    """QMainWindow subclass.

    Main window widget for the program. Holds general layout details
    for other widgets.
    """

    ssheet = """
        QMainWindow {
            margin: 8px;
            padding: 6px;
            background-color: #151a1e;
            color: #d3dae3;}
        """

    def __init__(self, parent=None, app=None, driver=None):
        """Window Constructor.

        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
            app (QApplication, optional): Main Application. Defaults to None.
            driver (Driver, optional):
        """
        super().__init__(parent=parent)
        self.app = app
        self.dealer = None
        self.driver = driver
        self.setStyleSheet(self.ssheet)
        self.setWindowTitle("BlackJack")
        self.setObjectName("MainWindow")
        icon = QIcon(os.path.join(os.environ["IMG_DIR"], "blackjackicon.png"))
        # icon.setObjectName("WindowIcon")
        self.setWindowIcon(icon)
        self._setupUi()

    def _setupUi(self):
        """Construct the general layout of Window."""
        self.central = QWidget(parent=self)
        self.central.setObjectName("CentralWidget")
        self.centLayout = QVBoxLayout()
        self.centLayout.setObjectName("CentralLayout")
        self.central.setLayout(self.centLayout)
        self.setCentralWidget(self.central)

        # layouts
        self.horiztop = QHBoxLayout()
        self.horiztop.setObjectName("TopLayout")
        self.horiz1 = QHBoxLayout()
        self.horiz1.setObjectName("HorizontalLayout1")
        self.horiz2 = QHBoxLayout()
        self.horiz2.setObjectName("HorizontalLayout2")

        # buttons and textbox
        self.button1 = HitButton(window=self, parent=self.central)
        self.button1.setObjectName("HitButton")
        self.button2 = StandButton(window=self, parent=self.central)
        self.button2.setObjectName("StandButton")
        self.button3 = NewGameButton(window=self, parent=self.central)
        self.button3.setObjectName("NewGameButton")
        self.statsFrame = StatsFrame(window=self,parent=self.central)
        self.statsFrame.setObjectName("StatsFrame")

        # layout configuration for window
        self.horiz2.addWidget(self.button3)
        self.horiz2.addWidget(self.button1)
        self.horiz2.addWidget(self.button2)
        self.centLayout.addLayout(self.horiztop)
        self.centLayout.addLayout(self.horiz1)
        self.centLayout.addLayout(self.horiz2)
        self.centLayout.addWidget(self.statsFrame)

        # adding a MenuBar
        self.mainMenuBar = MenuBar(parent=self, window=self)
        self.mainMenuBar.setObjectName("MainMenuBar")
        self.setMenuBar(self.mainMenuBar)

        # list of groupboxes. one for each player
        self.boxes = []

    @property
    def players(self):
        if self.dealer:
            return self.dealer.players
        return []

    def addPlayer(self, player):
        """Add Player construct groupbox for each player.

        Args:
            Player (Player): One of the Dealers challengers.
        """
        groupbox = PlayerBox(player.title, parent=self, player=player)
        groupbox.setObjectName(player.title + "Box")
        self.horiz1.addWidget(groupbox)
        self.boxes.append(groupbox)

    def setDealer(self, dealer):
        """Set Dealer Assign a dealer to the window.

        Args:
            dealer (Dealer): Subclass of Player with more responsibility.
                performs all dealing cards and shuffling.
        """
        self.dealer = dealer
        for button in [self.button1, self.button2, self.button3]:
            button.dealer = self.dealer
        self.addPlayer(dealer)

    def clearPlayers(self):
        """Clear Players Clear out old players groupbox for new players."""
        for player in self.players:
            # self.horiz1.removeWidget(player.box)
            player.box.reset()
            # player.box.destroy()
            # player.box.setVisible(False)
            # player.box.hide()
            # del player.box
            # self.players.remove(player)
            # self.dealer.players.remove(player)
            # del player
            self.update()
            self.repaint()
        # self.players = self.players[:1]

    def playerBroke(self, player, score):
        """
        Show and alert box to user when they break 21.

        Args:
            player (Player): The player who broke 21
            score (int): The score. Will be over 21
        """
        self.brokeDialog = BrokeDialog(parent=self, player=player, score=score)
        self.brokeDialog.exec()


class HitButton(QPushButton):
    """Hit Button triggered by player wants to be dealt another card.

    Args:
        QPushButton (ButtonWidget): Ask dealer for one more card.
    """

    ssheet = """QPushButton{
                    background-color: #1259ff;
                    font: bold 20pt black;
                    padding: px;
                    margin: 2px;
                    border: 1px solid #050a0e;
                    border-radius: 5px;}
                    """

    def __init__(self, parent=None, window=None):
        """Construct HitButton Object.

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
        """Ask dealer for another card."""
        for player in self.window.players:
            if player.isturn():
                return self.dealer.player_hit(player)


class StandButton(QPushButton):
    """Stand Button is for players who want their turn to be over.

    Args:
        QPushButton (ButtonWidget)
        Tell dealer no more cards and allow next player to take turn.
    """

    ssheet = """QPushButton{
                    background-color: #1259ff;
                    font: bold 20pt black;
                    padding: px;
                    margin: 2px;
                    border: 1px solid #050a0e;
                    border-radius: 5px;}
                    """

    def __init__(self, parent=None, window=None):
        """Construct Stay Button.

        Args:
            parent (Window, optional): mainwindow. Defaults to None.
            window (Window, optional): mainwindow. Defaults to None.
        """
        super().__init__(parent=parent)
        self.window = window
        self.dealer = None
        self.setText("Stand")
        self.setStyleSheet(self.ssheet)
        self.pressed.connect(self.stay)

    def stay(self):
        """Stay function."""
        for player in self.window.players:
            if player.isturn():
                player.turn()
                break
        self.dealer.next_player()


class NewGameButton(QPushButton):
    """New Game Button."""

    ssheet = """QPushButton{
                    background-color: #1259ff;
                    font: bold 20pt black;
                    padding: px;
                    margin: 2px;
                    border: 1px solid #050a0e;
                    border-radius: 5px;}"""

    def __init__(self, parent=None, window=None):
        """Construct for NewGameButton.

        Args:
            parent (Window, optional): mainwindow. Defaults to None.
            window (Window, optional): mainwindow. Defaults to None.
        """
        super().__init__(parent=parent)
        self.window = window
        self.dealer = None
        self.setText("New Game")
        self.pressed.connect(self.start_new_game)
        self.setStyleSheet(self.ssheet)

    def start_new_game(self):
        """Start new game function.

        Sets score to zero, and starts a new game.
        """
        for player in self.window.players:
            player.reset()
        self.window.adjustSize()
        self.window.dealer.new_game()


class BrokeDialog(QMessageBox):
    """
    BrokeDialog box to show player if their score is over 21.

    Args:
        QMessageBox (Window): Alerts the user they lost.
    """

    def __init__(self, parent=None, player=None, score=None):
        """
        Construct for the Alert box.

        Args:
            parent (Widget, optional): parent window. Defaults to None.
            player (player, optional): players title. Defaults to None.
            score (int, optional): players score. Defaults to None.
        """
        super().__init__(parent=parent)
        self.setText("Broke")
        self.setInformativeText(f"Sorry, {player} lost. \n Score: {score}.")
        self.button = QPushButton("OK")
        self.setDefaultButton(self.button)
