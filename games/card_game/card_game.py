class CardGame:
    """
    Represents a card game
    """
    
    MAX_PLAYERS = None
    GAME_NAME = None
    deck = None

    def __init__(self):
        self.players = []
        if self.MAX_PLAYERS == None:
            raise NotImplementedError('Subclasses of CarGame must define MAX_PLAYERS')
        if self.GAME_NAME == None:
            raise NotImplementedError('Subclasses of CarGame must define GAME_NAME')
        if self.deck == None:
            raise NotImplementedError('Subclasses of CarGame must define deck')
    
    def add_players(self, players):
        if len(self.players) + len(players) <= self.MAX_PLAYERS:
            self.players.extend(players)
        else:
            print(f"Error: Max of {self.MAX_PLAYERS} for {self.GAME_NAME}.")

    def show_game_title(self):
        print(f"GAME - {self.GAME_NAME}")
