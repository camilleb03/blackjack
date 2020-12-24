from blackjack_game import BlackJack, BlackJackHand

MAX_PLAYERS = 4

def main():
    players =[]
    # Enter all player participating
    while(len(players) < MAX_PLAYERS):
        user_name = input('Enter your name : ')
        if (len(user_name) == 0):
            if(len(players) == 0):
                print(f"You have to enther one player minimum")
                continue
            else:
                # TODO: Make print prettier here
                print(f"Welcome {players} !")
                break
        if (user_name.lower() == 'dealer'):
            print(f"You cannot choose {user_name} as name")
            continue
        players.append(user_name)

    # Replay
    while(True):
        user_action = input("Enter action (p to play) : ")
        if (user_action == 'p'):
            # BlackJack game is starting
            game = BlackJack(players=players)
            game.play()


if __name__ == "__main__":
    main()