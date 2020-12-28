from games.card_game import CardGame
from playing_cards import FrenchDeck, Hand
from games.card_game import Player

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

    def play_turn(self):
        card1 = self.hands[0]
    
    def play(self):
        pass