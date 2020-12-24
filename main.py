from blackjack_game import BlackJack, BlackJackHand

def main():
    players = ['Carl','Bill']
    game = BlackJack(players=players)
    game.play()

if __name__ == "__main__":
    main()