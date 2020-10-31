from deck_game.deck import Deck
from deck_game.card import Card
from deck_game.hand import Hand
from deck_game.constants import SUITS, RANKS

def main():
    deck = Deck()
    card = Card(4,0)
    deck.remove_card(card)
    print(deck)

main()