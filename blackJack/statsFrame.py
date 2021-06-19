from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt

class StatsFrame(QWidget):
    """Calculate statistics for each turn of the players."""

    def __init__(self,parent=None,window=None):
        super().__init__(parent=parent)
        self.window = window
        self.hlayout = QHBoxLayout()
        self.setLayout(self.hlayout)
        self.vbox1 = QVBoxLayout()
        self.vbox2 = QVBoxLayout()
        self.cardCount = HLabels("Cards in Deck: ","0")
        self.deckCount = HLabels("Number of Decks: ","0")
        self.playerCount = HLabels("Number of Players: ","0")
        self.breaking21 = HLabels("Breaking 21: ","0")
        self.exactly = HLabels("Exactly 21: ","0")
        self.under21 = HLabels("Under 21: ", "0")
        self.blackjack = HLabels("BlackJack","0")
        self.probabilities = QLabel("Probabilities",parent=self)
        self.vbox2.addLayout(self.cardCount)
        self.vbox2.addLayout(self.deckCount)
        self.vbox2.addLayout(self.playerCount)
        self.vbox1.addWidget(self.probabilities)
        self.vbox1.addLayout(self.breaking21)
        self.vbox1.addLayout(self.exactly)
        self.vbox1.addLayout(self.blackjack)
        self.vbox1.addLayout(self.under21)
        self.hlayout.addLayout(self.vbox1)
        self.hlayout.addLayout(self.vbox2)
        self.probabilities.setStyleSheet("""QLabel {font-size: 13pt;
                                                    font-weight: bold;
                                                    padding-right: 5px;
                                                    color: #fca018;
                                                    alignment: center;}""")
        self.labels = {
            "cards" : self.cardCount,
            "decks" : self.deckCount,
            "players": self.playerCount,
            "breaking": self.breaking21,
            "exactly": self.exactly,
            "blackjack": self.blackjack,
            "under": self.under21
        }
        self.window.driver.hook(self.labels)

class HLabels(QHBoxLayout):
    labelSheet = """QLabel {
                        font-size: 12pt;
                        font-weight: bold;
                        padding-right: 5px;
                        color: #9eeeee;}"""

    valSheet = """QLabel {
                        font-size: 12pt;
                        font-weight: bold;
                        color: #eece9e;}"""

    def __init__(self,label1=None,label2=None):
        super().__init__()
        self.label = QLabel(label1)
        self.label.setStyleSheet(self.labelSheet)
        self.value = QLabel(label2)
        self.value.setStyleSheet(self.valSheet)
        self.addWidget(self.label)
        self.addWidget(self.value)
        self.label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.value.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def update_value(self,text):
        self.value.setText(str(text))

    def update_percent(self,var):
        text = str(round(var * 100, 4))
        self.value.setText(text + "%")
