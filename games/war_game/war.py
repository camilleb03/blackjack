from playing_cards import FrenchDeck, Hand
from games.card_game import CardGame, GameStatus

class War(CardGame):
    """
    Represents a war game
    Reference : https://bicyclecards.com/how-to-play/war/
    """

    def __init__(self, nb_decks):
        self.GAME_NAME = "War"
        self.MAX_PLAYERS = 2
        self.deck = FrenchDeck(nb_decks)
        self.deck.shuffle()
        super().__init__()

    def create_hands(self):
        for i in range(self.MAX_PLAYERS):
            self.hands.append(Hand(self.player_names[i]))

    def distribute_cards(self):
        for i in range(len(self.deck.cards) // self.MAX_PLAYERS):
            hands = self.deck.deal_hands(1, self.MAX_PLAYERS)
            for j in range(self.MAX_PLAYERS):
                self.hands[j].add_cards(hands[j])

    def set_up(self):
        self.create_hands()
        self.distribute_cards()

    def find_best_card(self, c0, c1):
        if c0.rank.value == c1.rank.value:
            return None
        elif c0.rank.value > c1.rank.value:
            return c0
        else:
            return c1

    # TODO: What to do when there is not enough cardsin deck to draw ???
    def declare_war(self, current_cards):
        user_decision = input('War (w) : ').lower()
        battle_cards = self.draw_current_battle_cards()
        hidden_cards = self.draw_current_battle_cards(is_hidden=True)
        if None in (battle_cards or hidden_cards):
            return
        self.show_current_round_cards(battle_cards)
        current_cards.extend(battle_cards)
        current_cards.extend(hidden_cards)
        best_card = self.find_best_card(battle_cards[0], battle_cards[1])
        if best_card is None:
            print(f"WAR DECLARED !")
            self.declare_war(current_cards)
        # c1 > c2 -> player 1 wins
        elif best_card == current_cards[0]:
            self.hands[0].add_cards(current_cards)
            print(f"Player {self.hands[0].player_name} won this round !")
        # c1 < c2 -> player 2 wins
        else:
            self.hands[1].add_cards(current_cards)
            print(f"Player {self.hands[1].player_name} won this round !")

    def show_current_hands_status(self):
        print(f"{self.hands[0].player_name} ({self.hands[0].get_nb_cards()}) VS"
                f" {self.hands[1].player_name} ({self.hands[1].get_nb_cards()})")

    def show_current_round_cards(self, current_cards):
        print(f"{current_cards[0]} VS {current_cards[1]}")

    def draw_current_battle_cards(self, is_hidden=False):
        current_cards = []
        # Draw each 1 card
        for player in self.hands:
            battle_card = player.remove_card_by_index(0)
            # Return hidden cards -> flip cards that are not hidden
            if battle_card is not None:
                if is_hidden and not battle_card.hidden:
                    battle_card.flip()
                # Return visible cards -> flip cards that are hidden
                if not is_hidden and battle_card.hidden:
                    battle_card.flip()
            current_cards.append(battle_card)
        return current_cards

    def play_round(self):
        # Show current hands length
        self.show_current_hands_status()
        # TODO: Validation input
        user_decision = input('Battle (b) : ').lower()
        current_cards = self.draw_current_battle_cards()
        
        # Show two cards in battle
        self.show_current_round_cards(current_cards)
        # Compare the two cards
        best_card = self.find_best_card(current_cards[0], current_cards[1])
        # Value is equal -> WAR
        if best_card is None:
            print(f"WAR DECLARED !")
            self.declare_war(current_cards)
        # c1 > c2 -> player 1 wins
        elif best_card == current_cards[0]:
            self.hands[0].add_cards(current_cards)
            print(f"Player {self.hands[0].player_name} won this round !")
        # c1 < c2 -> player 2 wins
        else:
            self.hands[1].add_cards(current_cards)
            print(f"Player {self.hands[1].player_name} won this round !")
    
    def is_game_over(self):
        return (self.hands[0].get_nb_cards() or self.hands[1].get_nb_cards()) == 0

    def play(self):
        self.set_up()
        round_number = 1
        while not self.is_game_over():
            print(f"----- Round {round_number} -----")
            self.play_round()
            round_number += 1
        print("Game over !")