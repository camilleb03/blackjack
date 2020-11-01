from deck_game.deck import Deck
from deck_game.card import Card
from deck_game.hand import Hand
from deck_game.constants import SUITS, RANKS

def main():
    deck = Deck()
    deck.shuffle()
    hand = Hand()
    deck.deal_cards(hand, 5)
    print(deck)
    print("----")
    print(hand)

main()