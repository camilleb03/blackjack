from blackjack_game import BlackJack, BlackJackHand

def main():
    players = ['Carl','Bill']
    game = BlackJack(players=players)
    game.start()

    print("----")
    for hand in game.hands:
        print(hand)
        print(hand.calculate_value())
    
    game.reveal_hands()
    for hand in game.hands:
        print(hand)
        print(hand.calculate_value())

main()