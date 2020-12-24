from deck_game import Hand

class BlackJackHand(Hand):
    """
    Represents a BlackJack hand of cards
    """

    def __init__(self, player_name):
        Hand.__init__(self,player=player_name)
        self.cards_status = []

    def calculate_value(self):
        sum = 0
        contains_ace = False

        for card in self.cards:
            if card.rank in ('J' or 'Q' or 'K'):
                sum += 10
            elif card.rank in ('A'):
                sum += 11
                contains_ace = True
            else:
                sum += int(card.rank)
        # Check if putting value of 1 for an ace is better
        if (sum > 21 and contains_ace):
            sum = sum - 10

        return sum
            
