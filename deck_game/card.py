from deck_game.constants import SUITS, RANKS

class Card:
    """
    Represent a single playing card
    """
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return '%s of %s' % (RANKS[self.rank],SUITS[self.suit])

    def __eq__(self, other):
        return ((self.suit, self.rank) == (other.suit, other.rank))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.suit, self.rank) < (other.suit, other.rank))
