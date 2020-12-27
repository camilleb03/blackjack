from games.card_game import Player

class BlackJackPlayer(Player):
    """
    Represents a blackjack player in
    """

    def __init__(self, name, money=1000):
        super().__init(name)
        self.busted = False
        self.money = money

    def place_bet(self):
        pass
