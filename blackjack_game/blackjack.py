from .blackjack_hand import BlackJackHand
from deck_game import FrenchDeck

class BlackJack():
    """
    Represents a blackjack game
    """
    def __init__(self, players):
        self.deck = FrenchDeck()
        self.hands = []
        self.player_names = players

    def first_round(self):
        for name in self.player_names:
            self.hands.append(BlackJackHand(player_name=name))

    def hit(self, hand):
        pass

    def stand(self):
        pass

    def show_hands(self):
        pass

    def play(self):
        pass