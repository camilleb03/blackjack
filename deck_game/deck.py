from deck_game.card import Card
import random

class Deck():
    """
    Represents a deck of cards
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return  '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self, order=False):
        self.cards.sort(reverse=order)

    def remove_card(self, card):
        # TODO: Check if there are cards left in the deck
        self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)
    
    def deal_cards(self, hand, number):
        # TODO: Check if there are enough cards in deck to deal
        for i in range(number):
            hand.add_card(self.cards.pop())