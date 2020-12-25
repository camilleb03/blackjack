class Hand():
    """
    Represents a hand of cards
    """
    def __init__(self, player_name):
        self.cards = []
        self.player_name = player_name
    
    def sort(self, order=False):
        self.cards.sort(reverse=order)

    def remove_card(self, card):
        if self.check_enough_cards_in_deck(1):
            self.cards.remove(card)

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return 'Hand of %s: \n' % (self.player_name) + '\n'.join(res)
        