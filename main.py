from deck_game import FrenchDeck, Hand

def main():
    deck = FrenchDeck()
    deck.shuffle()
    hand = Hand()
    deck.deal_cards(hand, 5)
    print(deck)
    print("----")
    print(hand)

main()