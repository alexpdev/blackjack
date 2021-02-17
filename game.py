# utf-8
import random

class InvalidType(Exception):

    def __init__(self,arg):
        print('Object must be of type "Card"')
        print(self,arg)


class Deck(list):
    suits = ("clubs","spades","hearts","diamonds")
    values = {"two":2,"three":3,"four":4,
        "five":5,"six":6,"seven":7,"eight":8,
        "nine":9,"ten":10,"jack":10,"queen":10,
        "king":10,"ace":11}

    def __init__(cls,*args,**kwargs):
        if not args and not kwargs:
            cards = []
            for suit in cls.suits:
                for name,value in cls.values.items():
                    card = Card(suit,name,value)
                    cards.append(card)
            return super().__init__(cards)
        return super().__init__(cls,*args,**kwargs)
    
    def pop(self): return super().pop(0)

    def __setitem__(self,*args,**kwargs): raise Exception

    def shuffle(self,t=4):
        randcard = lambda: random.randint(0,len(self)-1)
        for _ in range(len(self) * t):
            r1,r2 = randcard(),randcard()
            card1,card2 = self[r1],self[r2]
            super().__setitem__(r1,card2)
            super().__setitem__(r2,card1)
        
class Card:

    def __init__(self,suit,name,value):
        self._suit = suit
        self._value = value
        self._name = name

    def __repr__(self):
        pass

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value
    
    @property
    def name(self):
        return self._name

    def __str__(self):
        return "<Card(obj): " + self.name.title() + "`" + self.suit.title() + ">"
    
    def __repr__(self):
        return f"<Card({self.suit},{self.name},{self.value})>"
    
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
    
