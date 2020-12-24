from blackjack_game import BlackJack, BlackJackHand

def main():
    players = ['Carl','Bill']
    game = BlackJack(players=players)
    print(len(game.deck.cards))
    game.first_round()
    game.deck.shuffle()

    game.deck.deal_cards(game.hands[0], 2)
    game.deck.deal_cards(game.hands[1], 2)
    print(len(game.deck.cards))

    print("----")
    print(game.hands[0].calculate_value())
    print(game.hands[1])

main()