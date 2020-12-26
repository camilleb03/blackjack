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
    
    def test_compare_eq_two_cards(self):
        """
        Check the comparison between two equal cards should return True
        """
        data = Card('8', 'Spades')
        self.assertTrue(self.card == data)
    
    def test_compare_eq_two_non_equal_cards(self):
        """
        Check the comparison between two non equal cards should return False
        """
        data = Card('9', 'Hearts')
        self.assertFalse(self.card == data)
    def test_compare_ne_two_cards_suits(self):
        """
        Check the comparison between two not equal cards based on suits should return True
        """
        data = Card('8', 'Hearts')
        self.assertTrue(self.card != data)
    
    def test_compare_ne_two_cards_ranks(self):
        """
        Check the comparison between two not equal cards based on ranks should return True
        """
        data = Card('9', 'Spades')
        self.assertTrue(self.card != data)

    def test_compare_ne_two_equal_cards(self):
        """
        Check the comparison between two equal cards should return False
        """
        data = Card('8', 'Spades')
        self.assertFalse(self.card != data)

    @unittest.skip("WIP : less_than not implemented yet")
    def test_compare_lt_two_numeric_cards_rank(self):
        """
        Check the comparison between ranks of two numeric cards should return True if greater
        """
        data = Card('9','Spades')
        self.assertTrue(self.card < data)

    @unittest.skip("WIP : less_than not implemented yet")
    def test_compare_lt_one_numeric_one_face_cards_rank(self):
        """
        Check the comparison between ranks of two numeric cards should return True
        """
        data = Card('J','Spades')
        self.assertTrue(self.card < data)
    
    @unittest.skip("WIP : less_than not implemented yet")
    def test_compare_lt_two_cards_suit(self):
        """
        Check the comparison between suits of two cards should return True
        """
        data = Card('8','Hearts')
        self.assertTrue(data < self.card)
    
    @unittest.skip("WIP : less_than not implemented yet")
    def test_compare_lt_two_cards_rank_suit(self):
        """
        Check the comparison between ranks and suits of two cards should return True
        """
        data = Card('J', 'Hearts')
        self.assertTrue(self.card < data)
    

if __name__ == '__main__':
    unittest.main()