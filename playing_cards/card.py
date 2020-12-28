class Card:
    """
    Represent a single playing card
    """

    def __init__(self, rank, suit, hidden=True):
        self.rank = rank
        self.suit = suit
        self.hidden = hidden

    def flip(self):
        self.hidden = (not self.hidden)

    def __str__(self):
        if self.hidden:
            return 'Unknown'
        else:
            return '%s of %s' % (str(self.rank), str(self.suit))

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return (self.suit, self.rank) == (other.suit, other.rank)

    def __ne__(self, other):
        if self.__class__ is other.__class__:
            return (self.suit, self.rank) != (other.suit, other.rank)

    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return ((self.suit, self.rank) < (other.suit, other.rank))
        return NotImplemented
