import random

class Hand():
    """
    Represents a hand of cards
    """
    def __init__(self, player_name):
        self.cards = []
        self.player_name = player_name
    
        
    def get_nb_cards(self):
        if self.cards is None:
            return 0
        return len(self.cards)

    # List starts at 0
    def add_card(self, card, index=0):
        self.cards.insert(index, card)

    def check_enough_cards_in_hand(self, nb_to_remove):
        return len(self.cards) >= nb_to_remove

    def remove_card_by_value(self, card):
        if self.check_enough_cards_in_hand(1):
            self.cards.remove(card)

    def remove_card_by_index(self, index=0):
        if self.check_enough_cards_in_hand(1):
            del self.cards[index]

    def discard_cards(self, nb_to_discard):
        if self.check_enough_cards_in_hand(nb_to_discard):
            nb_to_keep = len(self.cards) - nb_to_discard
            b = set(random.sample(self.cards, nb_to_keep))
            self.cards = [i for i in self.cards if i in b]

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return 'Hand of %s: \n' % (self.player_name) + '\n'.join(res)
        