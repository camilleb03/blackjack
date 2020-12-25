import unittest

from playing_cards import FrenchDeck, Card, Hand

class TestFrenchDeck(unittest.TestCase):

    def setUp(self):
        self.deck = FrenchDeck()
    
    def test_generate_cards(self):
        """
        Check that deck contains 52 cards
        """
        data = 52
        self.assertEqual(len(self.deck.cards), 52)

    def test_add_card(self):
        """
        Check card is added at the end
        """
        data = Card('8', 'Spades')
        self.deck.add_card(data)
        self.assertEqual(len(self.deck.cards), 53)
        self.assertEqual(self.deck.cards[53-1], data)

    def test_remove_card_valid(self):
        """
        Check card is not in the deck after removing it
        """
        data = Card('8', 'Spades')
        self.deck.remove_card(data)
        self.assertEqual(len(self.deck.cards), 51)
        self.assertFalse(data in self.deck.cards)
    
    # TODO: Complete test
    def test_remove_card_invalid(self):
        """
        Check when there is enough cards to be removed from the deck
        """
        pass

    def test_deal_cards_right_number_in_deck(self):
        """
        Check when dealing 2 cards, the deck has 50 cards
        """
        data = Hand(player_name='testing')
        self.deck.deal_cards(data, 2)
        self.assertEqual(len(self.deck.cards), 50)

    def test_deal_cards_right_number_in_hand(self):
        """
        Check when dealing 2 cards, the hand has 2 cards
        """
        data = Hand(player_name='testing')
        self.deck.deal_cards(data, 2)
        self.assertEqual(len(data.cards), 2)

    def test_deal_cards_right_card(self):
        """
        Check that the right card was dealt into hand
        """
        data = Hand(player_name='testing')
        card = self.deck.cards[len(self.deck.cards)-1]
        self.deck.deal_cards(data, 1)
        self.assertEqual(data.cards[0], card)

    def test_check_enough_cards_in_deck_returnTrue(self):
        """
        Check when there is enough cards to be removed from the deck
        """
        data = 7
        self.assertTrue(self.deck.check_enough_cards_in_deck(data))

    def test_check_enough_cards_in_deck_returnFalse(self):
        """
        Check when there is not enough cards to be removed from the deck
        """
        data = 56
        self.assertFalse(self.deck.check_enough_cards_in_deck(data))
        
if __name__ == '__main__':
    unittest.main()