class Player:
    """
    Represents a player in a card game
    """

    def __init__(self, name, money=1000):
        self.name = name
        self.hand = None
        self.money = money

    def set_hand(self, hand):
        self.hand = hand
    
    def place_bet(self):
        pass
