from .card import Card
import random

class Deck():
    """
    Represents a deck of cards
    """

    def __init__(self, nb_decks=1):
        self.cards = []
        self.nb_decks = nb_decks

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return  '\n'.join(res)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove_card(self, card):
        if self.check_enough_cards_in_deck(1):
            self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)

    def deal_cards(self, hand, nb_to_deal):
        if self.check_enough_cards_in_deck(nb_to_deal):
            for i in range(nb_to_deal):
                # Adds card to the end of hand
                nb_cards_in_hand = hand.get_nb_cards()
                hand.add_card(card=self.cards.pop(), index=nb_cards_in_hand)
    
    def check_enough_cards_in_deck(self, nb_to_remove):
        return len(self.cards) >= nb_to_remove
    
    def build(self):
        raise NotImplementedError("A deck needs cards in it")