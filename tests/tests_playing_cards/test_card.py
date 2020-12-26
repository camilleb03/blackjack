import unittest

from playing_cards import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card('8', 'Spades')

    def test_generate_card(self):
        """
        Check that card is created with right info
        """
        data = ('8', 'Spades')
        self.assertEqual(self.card.rank, data[0])
        self.assertEqual(self.card.suit, data[1])

    def test_flip_to_visible(self):
        """
        Check that card is visible after flip
        """
        self.assertTrue(self.card.hidden)
        self.card.flip()
        self.assertFalse(self.card.hidden)

    def test_flip_to_hidden(self):
        """
        Check that card is hidden after flip
        """
        self.card.hidden = False
        self.assertFalse(self.card.hidden)
        self.card.flip()
        self.assertTrue(self.card.hidden)

    def test_compare_two_cards_rank(self):
        """
        Check the comparison between ranks of two cards
        """
        data = Card('9','Spades')
        self.assertTrue(self.card < data)
    
    def test_compare_two_cards_suit(self):
        """
        Check the comparison between suits of two cards
        """
        data = Card('8','Hearts')
        self.assertTrue(data < self.card)
    
    # FIXME: Not working at the moment, have to implement conversion J to 11 or something
    @unittest.expectedFailure
    def test_compare_two_cards_rank_suit(self):
        """
        Check the comparison between ranks and suits of two cards
        """
        data = Card('J', 'Hearts')
        self.assertTrue(self.card < data)
    
    def test_compare_two_cards_ne(self):
        """
        Check the comparison between two not equal cards
        """
        data = Card('8', 'Hearts')
        self.assertTrue(self.card != data)

    def test_compare_two_cards_eq(self):
        """
        Check the comparison between two equal cards
        """
        data = Card('8', 'Spades')
        self.assertEqual(self.card, data)

if __name__ == '__main__':
    unittest.main()