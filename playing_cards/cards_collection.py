import random
from playing_cards import Card

class CardsCollection:
    """
    Represents a collection of cards
    """

    def __init__(self):
        self.cards = []
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return  '\n'.join(res)
    
    def get_nb_cards(self):
        return len(self.cards)

    def check_enough_cards(self, nb_to_remove=1):
        return get_nb_cards() >= nb_to_remove

    # List starts at 0
    def add_card(self, card: Card, index=None):
        if index is None:
            self.cards.append(card)
        elif 0 <= index and index <= self.get_nb_cards():
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
    def merge_collections_cards(self, c1: CardsCollection, c2: CardsCollection):
        return c1 + c2

    # TODO: Hand class
    def discard_cards(self, nb_to_discard):
        if self.check_enough_cards(nb_to_discard):
            nb_to_keep = self.get_nb_cards() - nb_to_discard
            # Chooose randomly cards to keep
            cards_to_keep = set(random.sample(self.cards, nb_to_keep))
            # Rebuild collection of cards with chosen cards
            self.cards = [card for card in self.cards if card in cards_to_keep]
            discarded_cards = [card for card in self.cards if card not in cards_to_keep]
            return discarded_cards
        else:
            print("Cannot discards cards")

    # TODO: Deck class
    def deal_cards(self, hand, nb_to_deal):
        if self.check_enough_cards(nb_to_deal):
            for i in range(nb_to_deal):
                # Adds card to the end of hand
                nb_cards_in_hand = hand.get_nb_cards()
                hand.add_card(card=self.cards.pop())
        # TODO: Do something when there is not enough cards to deal
        else:
            print("Cannot deal cards")
            
    # TODO: Deck class
    def build(self):
        raise NotImplementedError("A deck needs cards in it")