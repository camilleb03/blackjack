from .blackjack_hand import BlackJackHand
from playing_cards import FrenchDeck, GameStatus

class BlackJack():
    """
    Represents a blackjack game
    Reference : https://bicyclecards.com/how-to-play/blackjack/
    """

    MAX_DEALER_SCORE = 17

    def __init__(self, players):

        self.deck = FrenchDeck()
        # Shuffle deck
        self.deck.shuffle()
        self.hands = []
        self.player_names = players
        self.dealer = BlackJackHand(player_name='Dealer')

        # Set up the round
        self.set_up()

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
        self.dealer.calculate_value()

    def hit(self, hand):
        self.deck.deal_cards(hand, 1)
        hand.cards[len(hand.cards)-1].flip()
        print(f"Player {hand.player_name} has chosen to hit.")

    def stand(self, hand):
        print(f"Player {hand.player_name} has chosen to stand.")
    
    def show_table(self):
        print("+----- TABLE -----+")
        self.show_hand_value(self.dealer)
        for hand in self.hands:
            self.show_hand_value(hand)

    def show_hand_value(self, hand):
        print(hand)
        print(f"Value of {hand.value}")
        print("+----------------+")
    
    """
    Old function that does not manage TIE
    def find_winners(self):
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
    """

    def calculate_player_status(self):
        players_status = []
        # Check who won between dealer and each player
        for hand in self.hands:
            # Player busted, then dealer win (no matter if dealer busted or not)
            if hand.busted:
                players_status.append(tuple((hand, GameStatus.LOSE)))
                print(f"Player {hand.player_name} busted with value {hand.value}")
                continue
            # Dealer busted, then player win (passed the busted check)
            # FIXME: Prints as many times as the number of players
            if self.dealer.busted:
                players_status.append(tuple((hand, GameStatus.WIN)))
                print(f"{self.dealer.player_name} busted with value {self.dealer.value}.")
                continue
            # Neither busted, compare hand value
            # Player has higher score -> WIN
            if hand.value > self.dealer.value:
                players_status.append(tuple((hand, GameStatus.WIN)))
            elif (hand.value == self.dealer.value):
                # PLayer and Dealer has the same score -> =21
                if (hand.value == 21):
                    # Both have a blackjack -> TIE
                    if (len(hand.cards) == 2 and (len(self.dealer.cards) == 2)):
                        players_status.append(tuple((hand, GameStatus.TIE)))
                        print(f"Player {hand.player_name} AND {self.dealer.player_name} have a Blackjack.")
                    # Player has blackjack -> WIN
                    elif (len(hand.cards) == 2):
                        players_status.append(tuple((hand, GameStatus.WIN)))
                        print(f"Player {hand.player_name} has a Blackjack.")
                    # Dealer has blackjack -> LOSE
                    elif (len(hand.cards) == 2):
                        players_status.append(tuple((hand, GameStatus.LOSE)))
                        print(f"{self.dealer.player_name} has a Blackjack.")
                    # Player and Dealer do not have blackjack -> TIE
                    else:
                        players_status.append(tuple((hand, GameStatus.TIE)))
                        print(f"Neither Player {hand.player_name} nor {self.dealer.player_name} has a Blackjack.")
                # PLayer and Dealer has the same score -> <21
                else:
                    players_status.append(tuple((hand, GameStatus.TIE)))
                    print(f"Player {hand.player_name} and {self.dealer.player_name} obtained {hand.value}.")
            # Player has a value lower than Dealer -> LOSE
            else:
                players_status.append(tuple((hand, GameStatus.LOSE)))

        return players_status

    def show_game_players_status(self, players_status):
        for player_status in players_status:
            if player_status[1] == GameStatus.WIN:
                print(f"Player {player_status[0].player_name} won !")
            if player_status[1] == GameStatus.TIE:
                print(f"Player {player_status[0].player_name} tied !")
            if player_status[1] == GameStatus.LOSE:
                print(f"Player {player_status[0].player_name} lost !")

    def show_game_title(self):
        print("+--------------------------------+")
        print("+            BlackJack           +")
        print("+--------------------------------+")

    def show_game_help_menu(self):
        print("+------------- HELP -------------+")
        print("Goal : \n Each participant attempts \n to beat the dealer by getting a \n count as close to 21 as possible,\n without going over 21 (busting).")
        print("Rules : \n A player must decide to : \n-stand (not ask for another card)\n-hit (ask another card to get \n closer to a count of 21).")
        print("+--------------------------------+")

    def show_player_dealer_hands(self, player):
        # Print hand of dealer
        print(self.dealer)
        print("+----------------+")
        # Print hand of player and its current value
        self.show_hand_value(player)
        # Current player's turn
        print(f"Player {player.player_name}'s turn")

    def play_player_turn(self, player):
        is_turn_over = False
        while (not is_turn_over and not player.busted):
            user_decision = input('Hit (h) | Stand (s) : ').lower()
            # Player has decided to hit
            if user_decision == 'h':
                self.hit(player)
                # Calculate player's hand value
                player.calculate_value()
                # Determine if player busted or not
                player.did_bust()
                # Show player's hand
                self.show_hand_value(player)
            # Player has decided to stand
            elif user_decision == 's':
                self.stand(player)
                is_turn_over = True
            # Wrong input
            else:
                pass

    def play_dealer_turn(self):
        # Dealer keeps hitting until his score is over 17
        while (self.dealer.calculate_value() < self.MAX_DEALER_SCORE):
            self.deck.deal_cards(self.dealer, 1)
        # Determine if dealer did bust
        self.dealer.did_bust()
    
    def play(self):
        # For each player
        for player in self.hands:
            self.show_player_dealer_hands(player)
            self.play_player_turn(player)

        # Dealer's turn
        self.play_dealer_turn()
        self.dealer.reveal()

        # Show final table (all hands)
        self.show_table()

        # Find game status for each player
        players_status = self.calculate_player_status()
        self.show_game_players_status(players_status)
