import copy
import itertools
from enum import Enum
from functools import total_ordering
from .card import Card
from .deck import Deck


class FrenchDeck(Deck):
    """
    Defines a french deck of cards
    """
    
    @total_ordering
    class StandardFrenchDeckValue(Enum):
        A = 1, 'A'
        Deuce = 2, '2'
        Three = 3, '3'
        Four = 4, '4'
        Five = 5, '5'
        Six = 6, '6'
        Seven = 7, '7'
        Eight = 8, '8'
        Nine = 9, '9'
        Ten = 10, '10'
        J = 11, 'J'
        Q = 12, 'Q'
        K = 13, 'K'

        def __new__(cls, value, symbol):
            obj = object.__new__(cls)
            obj._value_ = value
            obj.symbol = symbol
            return obj
        
        def __str__(self):
            return self.symbol

        def __lt__(self, other):
            if self.__class__ is other.__class__:
                return self.value < other.value
            return NotImplemented

    # Alphabetical order
    @total_ordering
    class StandardFrenchDeckSuit(Enum):
        Clubs = 1, "\u2663"
        Hearts = 2, "\u2665"
        Diamonds = 3, "\u2666"
        Spades = 4, "\u2660"

        def __lt__(self, other):
            if self.__class__ is other.__class__:
                return self.value < other.value
            return NotImplemented
        
        def __str__(self):
            return self.symbol
        
        def __new__(cls, value, symbol):
            obj = object.__new__(cls)
            obj._value_ = value
            obj.symbol = symbol
            return obj

    def __init__(self, nb_decks=1):
        super().__init__(nb_decks)
        self.build()

    def build(self):
        self.cards = []
        # Generate content of one deck
        for i in itertools.product(self.StandardFrenchDeckSuit, self.StandardFrenchDeckValue):
            self.cards.append(Card(i[1], i[0]))
        # Multiply content as many as the number of decks
        self.cards = [copy.deepcopy(card) for card in self.nb_decks * self.cards]

    def sort(self, order=False):
        self.cards.sort(reverse=order)
