from playing_cards import Hand


class BlackJackHand(Hand):
    """
    Represents a BlackJack hand from FrenchDeck of cards
    """
    BUSTED_SCORE = 22

    def __init__(self, player_name):
        Hand.__init__(self, player_name=player_name)
        self.busted = False

    @property
    def value(self):
        new_value = 0
        contains_ace = False
        for card in self.cards:
            # Assign 10 to J,Q or K
            if card.rank in ('J', 'Q', 'K'):
                new_value += 10
            # Assign 11 to A
            elif card.rank in 'A':
                new_value += 11
                contains_ace = True
            else:
                # Assign number on card
                new_value += int(card.rank)
        # Check if putting value of 1 for an A is better
        if new_value > 21 and contains_ace:
            new_value = new_value - 10
        return new_value

    def reveal(self):
        for card in self.cards:
            if card.hidden:
                card.flip()

    # TODO: Add a hide(self) method

    @property
    def busted(self):
        return self.value >= self.BUSTED_SCORE

    @busted.setter
    def busted(self, busted):
        self._busted = busted
