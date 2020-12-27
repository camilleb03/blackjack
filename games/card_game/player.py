class Player:
    """
    Represents a player in a card game
    """

    def __init__(self, name):
        self.name = name
        self._hand = None

    @property
    def hand(self):
        return self._hand()

    @hand.setter
    def hand(self, new_hand):
        self._hand = new_hand
