import random
from .cards_collection import CardsCollection


class Deck(CardsCollection):
    """
    Represents a deck of cards
    """

    def __init__(self, nb_decks=1):
        super().__init__()
        self.nb_decks = nb_decks

    def __str__(self):
        return f"Deck :\n" + super().__str__()

    def deal_cards(self, hand, nb_to_deal):
        if self.check_enough_cards(nb_to_deal):
            for i in range(nb_to_deal):
                # Adds card to the end of hand
                hand.add_card(self.cards.pop())
        # TODO: Do something when there is not enough cards to deal
        else:
            print("Cannot deal cards")
    
    def deal_hands(self, nb_cards_per_hand, nb_hands):
        if self.check_enough_cards(nb_cards_per_hand * nb_hands):
            all_hands = []
            # Generate a hand for all hands
            for h in range(nb_hands):
                hand = []
                # Generate cards for a hand
                for c in range(nb_cards_per_hand):
                    # Remove card
                    card_to_deal = self.remove_card_by_index()
                    hand.append(card_to_deal)
                all_hands.append(hand)
            return all_hands
        else:
            print("Cannot deal cards")
    
    # TODO: Implement Fischer-Yates method ?
    def shuffle(self):
        random.shuffle(self.cards)

    def build(self):
        raise NotImplementedError("A deck needs cards in it")
