from games.card_game import CardGame
from playing_cards import FrenchDeck

class War(CardGame):
    """
    Represents a war game
    Reference : https://bicyclecards.com/how-to-play/war/
    """
    def __init__(self, nb_decks):
        self.GAME_NAME = "War"
        self.MAX_PLAYERS = 2
        self.deck = FrenchDeck(nb_decks)
        super().__init__()
