class Player:
    """
    Represents a player in a card game
    """

    def __init__(self, name):
        self.name = name
        self.hand = None

    def set_hand(self, hand):
        self.hand = hand
