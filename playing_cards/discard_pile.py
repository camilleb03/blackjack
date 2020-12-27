from .collection_cards import CardsCollection

class DiscardPile(CardsCollection):
    """
    Represents a pile of discarded cards
    """
    def __init__(self):
        CardsCollection.__init__(self)
    
    def get_top_card(self):
        if self.cards:
            return self.cards[self.get_nb_cards() - 1]
        else:
            return None
    