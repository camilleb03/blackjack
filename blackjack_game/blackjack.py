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
        # TODO: Find a cleaner way to flip last card
        hand.cards[len(hand.cards) - 1].flip()
        print(f"Player {hand.player} has chosen to hit.")

    def stand(self, hand):
        print(f"Player {hand.player} has chosen to stand.")

    def reveal_hands(self):
        for hand in self.hands:
            hand.reveal()
    
    def display_table(self):
        for hand in self.hands:
            print("+---------------+")
            print(hand)
        print("+---------------+")

    def declare_winner(self):
        # TODO: Find way to not favour last player
        winner = self.hands.pop()
        for hand in self.hands:
            if hand.calculate_value() > winner.calculate_value():
                winner = hand
        return winner

    def play(self):
        # Set up the round
        self.set_up()

        # Show current status 
        self.display_table()

        # Declare winner when every player has stand or bust
        winner = self.declare_winner()
        print(f"Player {winner.player} won !")


