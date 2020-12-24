from .blackjack_hand import BlackJackHand
from deck_game import FrenchDeck

class BlackJack():
    """
    Represents a blackjack self
    """
    def __init__(self, players):
        self.deck = FrenchDeck()
        # Shuffle deck
        self.deck.shuffle()
        self.hands = []
        self.player_names = players

    def set_up(self):
        for name in self.player_names:
            # Assign a hand to every player
            hand = BlackJackHand(player_name=name)
            # Deal two cards to each player
            self.deck.deal_cards(hand, 2)
            # Make only one card visible
            hand.cards[0].flip()
            # Add the card to the hands
            self.hands.append(hand)

    def hit(self, hand):
        self.deck.deal_cards(hand, 1)
        print(f"Player {hand.player} has chosen to hit.")

    def stand(self, hand):
        print(f"Player {hand.player} has chosen to stand.")

    def reveal_hands(self):
        for hand in self.hands:
            hand.reveal()

    def play(self):
        self.set_up()
        print("----")
        for hand in self.hands:
            print(hand)