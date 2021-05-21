# utf-8
import random

class InvalidType(Exception):
    pass

class DeckEmpty(Exception):
    pass

class Deck(list):
    suits = ("clubs","spades","hearts","diamonds")
    counts = {2: 4, 3: 4, 4: 4, 5: 4, 6: 4,
              7: 4, 8: 4, 9: 4, 10: 16, 11: 4}
    values = {"two":2, "three":3, "four":4,
            "five":5, "six":6, "seven":7,
            "eight":8, "nine":9, "ten":10,
            "jack":10, "queen":10, "king":10,
            "ace":11}

    def __init__(cls,*args,**kwargs):
        if not args and not kwargs:
            cards = []
            for suit in cls.suits:
                for name,value in cls.values.items():
                    card = Card(suit,name,value)
                    cards.append(card)
            return super().__init__(cards)
        return super().__init__(cls,*args,**kwargs)

    def pop(self,x=0):
        if not len(self):
            raise DeckEmpty
        return super().pop(x)

    def swap(self, i1, i2):
        val = self[i1]
        self[i1] = self[i2]
        self[i2] = val

    def shuffle(self,t=4):
        slen = len(self)
        d = dict.fromkeys(list(range(slen)), 0)
        for _ in range(slen * t):
            i1 = random.choice(range(slen))
            i2 = random.choice(range(slen))
            self.swap(i1,i2)
            d[i1], d[i2] = d[i1] + 1, d[i2] + 1
        print(self,d,"\n")

class Card:

    def __init__(self,suit,name,value):
        self.suit = suit
        self.value = value
        self.name = name

    def __str__(self):
        return "<" + self.name.title() + ": " + self.suit.title() + ">"

    def __repr__(self):
        return str(self)

    def __lt__(self,other):
        if self.value < other.value:
            return True
        return False

    def __ne__(self,other):
        if self.__eq__(other):
            return False
        return True

    def __gt__(self,other):
        if isinstance(other,type(self)):
            other = other.value
        if self.value > other:
            return True
        return False

    def __eq__(self,other):
        if isinstance(other,type(self)):
            return self.value == other.value
        if isinstance(other,str):
            return self.suit == other
        if isinstance(other,int):
            return self.value == other
        return False

    def __le__(self,other):
        if self.__eq__(other) or self.__lt__(other):
            return True
        return False

    def __ge__(self,other):
        if self.__eq__(other) or self.__gt__(other):
            return True
        return False

    def ismatch(self,other):
        if self.suit == other.suit:
            return True
        return False

    def __typecheck__(self,other):
        if not isinstance(other,type(self)):
            raise Exception
