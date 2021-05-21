from Players import Dealer

def start_game():
    dealer = Dealer(2)
    dealer.deck.shuffle()
    dealer.play()


if __name__ == "__main__":
    number_of_players = 2
    start_game(number_of_players)
