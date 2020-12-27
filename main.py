import sys

from games import BlackJack

MAX_PLAYERS = 4


def show_actions_menu():
    print("|---------------- GAMES -----------------")
    print("| b - Blackjack")
    print("| q - Quit game")
    print("|----------------------------------------")


def register_players():
    players = []
    # Max player of 4
    print("+------------ PLAYERS ------------+")
    # TODO: Ask user to enter nb of players to register instead of imposing MAX to 4
    while (len(players) < MAX_PLAYERS):
        user_name = input(f'Enter name of player {len(players) + 1} : ')
        if (len(user_name) == 0):
            if (len(players) == 0):
                print("You have to enter one player minimum")
                continue
            else:
                # TODO: Make print prettier here
                print(f"Welcome {players} !")
                break
        if (user_name.lower() == 'dealer' or (user_name in players)):
            print(f"You cannot choose {user_name} as name")
            continue
        players.append(user_name)
    return players


def start_blackjack(players):
    # BlackJack game is starting
    blackjack = BlackJack(players=players)
    blackjack.show_game_title()
    blackjack.show_game_help_menu()
    blackjack.play()


def main():
    # Enter all player participating
    players = register_players()

    show_actions_menu()
    # Enter game mode
    while (True):
        user_action = input("Enter action: ")
        if (str(user_action).lower() == 'b'):
            start_blackjack(players)

        # Verify if user wants to quit
        if (str(user_action).lower() == "q"):
            # Quit game
            print("Thanks for playing!")
            sys.exit()


if __name__ == "__main__":
    main()
