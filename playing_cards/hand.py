import random

from .cards_collection import CardsCollection


class Hand(CardsCollection):
    """
    Represents a hand of cards
    """

    def __init__(self, player_name):
        super().__init__()
        self.player_name = player_name

    def discard_cards(self, nb_to_discard):
        if self.check_enough_cards(nb_to_discard):
            nb_to_keep = self.get_nb_cards() - nb_to_discard
            # Choose randomly cards to keep
            cards_to_keep = set(random.sample(self.cards, nb_to_keep))
            # Rebuild collection of cards with chosen cards
            self.cards = [card for card in self.cards if card in cards_to_keep]
            discarded_cards = [card for card in self.cards if card not in cards_to_keep]
            return discarded_cards
        else:
            print("Cannot discards cards")

    def __str__(self):
        return f'Hand of {self.player_name}:\n' + super().__str__()
