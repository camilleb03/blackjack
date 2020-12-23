from deck_game.deck import Deck

class FrenchDeck(Deck):
    """
    Defines french deck of cards
    """
    card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    card_ranks = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']