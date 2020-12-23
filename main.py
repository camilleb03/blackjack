from deck_game.french_deck import FrenchDeck
from deck_game.card import Card
from deck_game.hand import Hand

def main():
    deck = FrenchDeck()
    deck.shuffle()
    hand = Hand()
    deck.deal_cards(hand, 5)
    print(deck)
    print("----")
    print(hand)

main()