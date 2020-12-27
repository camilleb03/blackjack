import copy
import itertools

from .card import Card
from .deck import Deck


class FrenchDeck(Deck):
    """
    Defines french deck of cards
    """
    card_suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    card_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, nb_decks=1):
        super().__init__(nb_decks)
        self.build()

    def build(self):
        self.cards = []
        # Generate content of one deck
        for i in itertools.product(self.card_suits, self.card_ranks):
            self.cards.append(Card(i[1], i[0]))
        # Multiply content as many as the number of decks
        self.cards = [copy.deepcopy(card) for card in self.nb_decks * self.cards]

    def sort(self, order=False):
        self.cards.sort(reverse=order)
