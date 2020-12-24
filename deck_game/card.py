class Card:
    """
    Represent a single playing card
    """
    def __init__(self, rank, suit, hidden=True):
        self.rank = rank
        self.suit = suit
        self.hidden = hidden

    def flip(self):
        self.hidden = not self.hidden
    
    def __str__(self):
        if self.hidden:
            return 'Unknown'
        else:
            return '%s of %s' % (self.rank,self.suit)

    def __eq__(self, other):
        return ((self.suit, self.rank) == (other.suit, other.rank))

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.suit, self.rank) < (other.suit, other.rank))
