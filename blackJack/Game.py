import math

from blackJack.Players import Dealer
from blackJack.Window import Window


class Driver:
    """
    Responsible for putting pieces together and driving them forward.

    Starts the application, creates the window, creates the dealer and allows
    dealer to perform the rest of game setup. Calculates probabilities
    and statistics for the active game.
    """

    def __init__(self, app, players=2, decks=2):
        """
        Construct the Driver class for the new game.

        Args:
            app (QApp): Application base for program.
            players (int, optional): Number of players. Defaults to None
            decks (int, optional): Number of decks. Defaults tp None.
        """
        self.app = app
        self.drawn = []
        self.window = Window(parent=None, app=self.app)
        # Dealer instance has most power and constrol over gameplay.
        self.dealer = Dealer(
            window=self.window,
            decks=decks,
            players=players,
            pos=0,
            driver=self,
        )
        self.window.setDealer(self.dealer)
        self.window.show()

    def play(self):
        self.dealer.add_players()
        self.dealer.new_game()


    def output(self, s):
        """
        Output textual information to TextBrowser GUI Widget.

        Args:
            s (str): text to be written to TextBrowser Widget.
        """
        self.dealer.output(s)

    def chances_of_blackjack(self):
        """Calculate the odds of being dealt a blackJack."""
        tens = self.total_tens()
        aces = sum([1 for i in self.dealer.deck if i.name == "ace"])
        combinations = math.comb(self.decksize, 2)
        percentage = (tens * aces) / combinations
        s = f"{percentage}% chance of blackjack"
        self.output(s)

    def chances_of_x(self, x):
        """
        Calculate the odds of breaking if player hits.

        Args:
            x (int): 21 minus the current players score.
        """
        count = sum([1 for i in self.dealer.deck if i.value <= x])
        busting = (count / self.decksize) * 100
        s = f"{str(busting)}% chance of not breaking 21"
        self.output(s)

    def total_tens(self):
        """
        Count number of cards left in the Deck with a value of 10.

        Returns:
            int: Total number of cards with the value of 10
        """
        return sum([1 for i in self.dealer.deck if i.value == 10])

    @property
    def decksize(self):
        """
        Get total cards in the deck.

        Returns:
            int: total count of cards left in deck.
        """
        return self.dealer.decksize

    @property
    def players(self):
        """Get count of players actively playing."""
        return self.dealer.player_count

    @property
    def decks(self):
        """Get number of decks used to make current deck."""
        return self.dealer.deck_count

    def draw(self, card):
        """
        Collect cards that have already been drawn and discarded.

        Args:
            card (obj): the card most recently pulled from the deck.
        """
        self.update_count()
        self.drawn.append(card)

    def update_count(self):
        """Update the GUI label with current deck size."""
        self.window.cards_val.setText(str(self.decksize))
