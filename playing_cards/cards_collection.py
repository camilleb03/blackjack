import random
from playing_cards import Card


class CardsCollection:
    """
    Represents a collection of cards (Deck, Hand, DiscardPile, etc.)
    """

    def __init__(self):
        self.cards = []

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def get_nb_cards(self):
        return len(self.cards)

    def check_enough_cards(self, nb_to_remove=1):
        return self.get_nb_cards() >= nb_to_remove

    # List starts at 0
    def add_card(self, card: Card, index=None):
        if index is None:
            self.cards.append(card)
        elif 0 <= index <= self.get_nb_cards():
            self.cards.insert(index, card)
        else:
            print("Cannot add card")

    def remove_card_by_value(self, card: Card):
        if self.check_enough_cards() and card in self.cards:
            self.cards.remove(card)
            return card
        else:
            print("Cannot remove card by value")

    def remove_card_by_index(self, index=None):
        if self.check_enough_cards():
            if index is None:
                return self.cards.pop()
            elif index < self.get_nb_cards():
                return self.cards.pop(index)
            else:
                print("Cannot remove card by index")

    @staticmethod
    def merge_collections_cards(cards_from_c1: list, cards_from_c2: list):
        return cards_from_c1 + cards_from_c2
