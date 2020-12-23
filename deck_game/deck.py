from deck_game.card import Card

import random
import itertools

class Deck():
    """
    Represents a deck of cards
    """
    cards_suits = []
    cards_ranks = []

    def __init__(self):
        self.cards = []
        self.refresh()

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return  '\n'.join(res)
    
    def refresh(self):
        self.cards = [Card(rank,suit) for rank in range(1, len(self.card_ranks)) for suit in range(len(self.card_suits))]

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