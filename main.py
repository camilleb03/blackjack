import sys

from games import BlackJack, War

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
    while len(players) < MAX_PLAYERS:
        user_name: str = input(f'Enter name of player {len(players) + 1} : ')
        if len(user_name) == 0:
            if len(players) == 0:
                print("You have to enter one player minimum")
                continue
            else:
                # TODO: Make print prettier here
                print(f"Welcome {players} !")
                break
        if user_name.lower() == 'dealer' or (user_name in players):
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


def start_war(players):
    # BlackJack game is starting
    war = War(nb_decks=1)
    war.show_game_title()
    war.add_players(players=players)
    war.set_up()

def main():
    # Enter all player participating
    # players = register_players()
    players = ['Boh', 'Bah']
    start_war(players=players)
    

def main2():
    # Enter all player participating
    # players = register_players()
    players = ['Boh', 'Bah', 'Beh']
    show_actions_menu()
    # Enter game mode
    while True:
        user_action: str = input("Enter action: ")
        if user_action.lower() == 'b':
            start_blackjack(players)

        # Verify if user wants to quit
        if user_action.lower() == "q":
            # Quit game
            print("Thanks for playing!")
            sys.exit()


if __name__ == "__main__":
    main()
