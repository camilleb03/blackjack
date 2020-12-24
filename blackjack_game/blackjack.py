from .blackjack_hand import BlackJackHand
from deck_game import FrenchDeck

class BlackJack():
    """
    Represents a blackjack self
    """

    BUSTED_SCORE = 22
    MAX_DEALER_SCORE = 17

    def __init__(self, players):
        self.deck = FrenchDeck()
        # Shuffle deck
        self.deck.shuffle()
        self.hands = []
        self.player_names = players
        self.dealer = BlackJackHand(player_name='Dealer')

    def set_up(self):
        # For all real players
        for name in self.player_names:
            # Assign a hand to every player
            hand = BlackJackHand(player_name=name)
            # Deal two cards to each player
            self.deck.deal_cards(hand, 2)
            # Turn them up
            hand.reveal()
            hand.calculate_value()
            # Add the card to the hands
            self.hands.append(hand)

        # For dealer (computer)
        self.deck.deal_cards(self.dealer, 2)
        # Make only one card visible
        self.dealer.cards[0].flip()
    
    def play_dealer_turn(self):
        # Dealer keeps hitting until his score is over 17
        while (self.dealer.calculate_value() < self.MAX_DEALER_SCORE):
            self.deck.deal_cards(self.dealer, 1)
        if self.dealer.calculate_value() >= self.BUSTED_SCORE:
            self.dealer.did_bust()

    def hit(self, hand):
        self.deck.deal_cards(hand, 1)
        hand.cards[len(hand.cards)-1].flip()
        print(f"Player {hand.player_name} has chosen to hit.")

    def stand(self, hand):
        print(f"Player {hand.player_name} has chosen to stand.")

    def reveal_hands(self):
        for hand in self.hands:
            hand.reveal()
    
    def display_table(self):
        print("+----- TABLE -----+")
        self.display_hand_value(self.dealer)
        for hand in self.hands:
            self.display_hand_value(hand)

    def display_hand_value(self, hand):
        print(hand)
        print(f"Value of {hand.value}")
        print("+----------------+")

    def declare_winner(self):
        winners = []
        # Check who won between dealer and each player
        for hand in self.hands:
            # Both busted, then neither win
            if hand.busted and self.dealer.busted:
                print(f"Player {hand.player_name} and {self.dealer.player_name} \
                        busted with value {hand.value} and {self.dealer.value}.")
                continue
            # Dealer busted, then player win
            if self.dealer.busted:
                winners.append(hand)
                print(f"{self.dealer.player_name} busted with value {self.dealer.value}.")
                continue
            # Player busted, then dealer win
            if hand.busted:
                print(f"Player {hand.player_name} busted with value {hand.value}")
                continue
            # Neither busted, compare hand value
            if hand.calculate_value() > self.dealer.calculate_value():
                winners.append(hand)

        return winners

    def play(self):
        print("+----------------+")
        print('BlackJack')
        print("+----------------+")
        # Set up the round
        self.set_up()
        # For each player
        for player in self.hands:
            # Print hand of dealer
            print(self.dealer)
            # Print hand of player and its current value
            self.display_hand_value(player)
            is_turn_over = False
            # Current player's turn
            print(f"Player {player.player_name}'s turn")
            while (not is_turn_over and not player.busted):
                user_decision = input('Hit (h) | Stand (s) : ').lower()
                # Player has decided to hit
                if user_decision == 'h':
                    self.hit(player)
                    # Calculate player's hand value
                    player.calculate_value()
                    if player.value >= self.BUSTED_SCORE:
                        # Player busted
                        player.did_bust()
                    # Show player's hand
                    self.display_hand_value(player)

                # Player has decided to stand
                elif user_decision == 's':
                    self.stand(player)
                    is_turn_over = True
            

        # Dealer's turn
        self.play_dealer_turn()
        self.dealer.reveal()

        # Show final table (all hands)
        self.display_table()

        # Declare winners
        winners = self.declare_winner()
        for player in self.hands:
            if player in winners:
                print(f"Player {player.player_name} won !")
            else:
                print(f"Player {player.player_name} lost !")
