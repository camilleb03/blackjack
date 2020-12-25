from .deck import Deck, Card
import itertools

class FrenchDeck(Deck):
    """
    Defines french deck of cards
    """
    card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    card_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        Deck.__init__(self)
        self.build()

    def build(self):
        for i in itertools.product(self.card_suits, self.card_ranks):
            self.cards.append(Card(i[1], i[0]))