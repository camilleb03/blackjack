from .cards_collection import CardsCollection


class DiscardPile(CardsCollection):
    """
    Represents a pile of discarded cards
    """

    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Discard pile :\n" + super().__str__()

    def pop_card(self):
        if self.cards:
            return self.cards.pop()
        else:
            return None
