from deck_game.card import Card
from deck_game.constants import SUITS, RANKS

import random

class Deck():
    """
    Represents a deck of cards
    """
    def __init__(self):
        self.cards = []
        self.cards = [Card(rank,suit) for rank in range(1, len(RANKS)) for suit in range(len(SUITS))]

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
        self.cards.remove(card)
    
    def add_card(self,card):
        self.cards.append(card)
    
    def deal_cards(self,hand,number):
        for i in range(number):
            hand.add_card(self.cards.pop())