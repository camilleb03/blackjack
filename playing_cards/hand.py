from .deck import Deck

class Hand(Deck):
    """
    Represents a hand of cards
    """
    def __init__(self, player_name):
        self.cards = []
        self.player_name = player_name

    def __str__(self):
        return 'Hand of %s: \n' % (self.player_name) + super(Hand, self).__str__()
        