from deck_game import Hand

class BlackJackHand(Hand):
    """
    Represents a BlackJack hand of cards
    """

    def __init__(self, player_name):
        Hand.__init__(self,player_name=player_name)
        self.value = 0
        self.busted = False

    def calculate_value(self):
        self.value = 0
        contains_ace = False
        for card in self.cards:
            # Assign 10 to J,Q or K
            if card.rank in ('J', 'Q', 'K'):
                self.value += 10
            # Assign 11 to A
            elif card.rank in ('A'):
                self.value += 11
                contains_ace = True
            else:
                # Assign number on card
                self.value += int(card.rank)
        # Check if putting value of 1 for an A is better
        if (self.value > 21 and contains_ace):
            self.value = self.value - 10

        return self.value

    def reveal(self):
        for card in self.cards:
            if card.hidden:
                card.flip()

    def did_bust(self):
        self.busted = (not self.busted)
        
            
