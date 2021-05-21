from Players import Dealer

class Stats:

    counts = {
        2: 4, 3: 4,
        4: 4, 5: 4,
        6: 4, 7: 4,
        8: 4, 9: 4,
        10: 16, 11: 4
        }

    refresh = lambda: [counts.__setitem__(k,4) for k in counts]

    @classmethod
    def probability(cls,val):
        total = sum(cls.counts.values())
        p = cls.counts[val]
        return p/total



def start_game(n):
    dealer = Dealer(n)
    dealer.deck.shuffle()
    dealer.play()


if __name__ == "__main__":
    number_of_players = 2
    start_game(number_of_players)
