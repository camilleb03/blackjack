from blackjack_game import BlackJack, BlackJackHand
import sys

MAX_PLAYERS = 4

def show_actions_menu():
    print("|------------ POSSIBLE GAMES ------------")
    print("| b - Blackjack")
    print("| q - Quit game")
    print("|----------------------------------------")

def add_players():
    players =[]
    # Max player of 4
    print("+------------ PLAYERS ------------+")
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

    return players

def main():
    # Enter all player participating
    players = add_players()

    show_actions_menu()

    # Replay
    while(True):
        user_action = input("Enter action: ")
        if (str(user_action).lower() == 'b'):
            # BlackJack game is starting
            game = BlackJack(players=players)
            game.show_game_title()
            game.show_game_help_menu()
            game.play()
        
        # Verify if user wants to quit
        if (str(user_action).lower() == "q"):
            # Quit game
            print("Thanks for playing!")
            sys.exit()

if __name__ == "__main__":
    main()