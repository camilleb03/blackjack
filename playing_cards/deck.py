from .card import Card
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
        if self.check_enough_cards_in_deck(1):
            self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)
    
    def deal_cards(self, hand, number):
        if self.check_enough_cards_in_deck(number):
            for i in range(number):
                hand.add_card(self.cards.pop())
    
    def check_enough_cards_in_deck(self, nb_to_remove):
        return len(self.cards) >= nb_to_remove