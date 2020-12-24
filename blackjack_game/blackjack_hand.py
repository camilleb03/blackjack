from deck_game import Hand

class BlackJackHand(Hand):
    """
    Represents a BlackJack hand of cards
    """

    def __init__(self, player_name):
        Hand.__init__(self,player=player_name)

    def calculate_value(self):
        sum = 0
        contains_ace = False
        for card in self.cards:
            # Assign 10 to J,Q or K
            if card.rank in ('J', 'Q', 'K'):
                sum += 10
            # Assign 11 to A
            elif card.rank in ('A'):
                sum += 11
                contains_ace = True
            else:
                # Assign number on card
                sum += int(card.rank)
        # Check if putting value of 1 for an A is better
        if (sum > 21 and contains_ace):
            sum = sum - 10

        return sum

    def reveal(self):
        for card in self.cards:
            if card.hidden:
                card.flip()
            
