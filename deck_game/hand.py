from deck_game.deck import Deck

class Hand(Deck):
    """
    Represents a hand of cards
    """
    def __init__(self, player):
        self.cards = []
        self.player = player

    def __str__(self):
        return 'Hand of %s: \n' % (self.player) + super(Hand, self).__str__()
        