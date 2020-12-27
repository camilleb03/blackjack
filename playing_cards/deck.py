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

    def build(self):
        raise NotImplementedError("A deck needs cards in it")
