import unittest

from playing_cards import Card, FrenchDeck


class TestCard(unittest.TestCase):

    def setUp(self):
        self.deck = FrenchDeck()
        self.card = Card(self.deck.StandardFrenchDeckValue.Eight, self.deck.StandardFrenchDeckSuit.Spades)

    def test_generate_card(self):
        """
        Check that card is created with right info
        """
        data = (self.deck.StandardFrenchDeckValue.Eight, self.deck.StandardFrenchDeckSuit.Spades)
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
        Check the comparison between two equal cards should return True (Spades == Spades and 8 == 8)
        """
        data = Card(self.deck.StandardFrenchDeckValue.Eight, self.deck.StandardFrenchDeckSuit.Spades)
        self.assertTrue(self.card == data)

    def test_compare_eq_two_non_equal_cards(self):
        """
        Check the comparison between two non equal cards should return False (Spades != Hearts and 8 != 9)
        """
        data = Card(self.deck.StandardFrenchDeckValue.Nine, self.deck.StandardFrenchDeckSuit.Hearts)
        self.assertFalse(self.card == data)

    def test_compare_ne_two_cards_suits(self):
        """
        Check the comparison between two not equal cards based on suits should return True (Spades != Hearts)
        """
        data = Card(self.deck.StandardFrenchDeckValue.Eight, self.deck.StandardFrenchDeckSuit.Hearts)
        self.assertTrue(self.card != data)

    def test_compare_ne_two_cards_ranks(self):
        """
        Check the comparison between two not equal cards based on ranks should return True (8 != 9)
        """
        data = Card(self.deck.StandardFrenchDeckValue.Nine, self.deck.StandardFrenchDeckSuit.Spades)
        self.assertTrue(self.card != data)

    def test_compare_ne_two_equal_cards(self):
        """
        Check the comparison between two equal cards should return False
        """
        data = Card(self.deck.StandardFrenchDeckValue.Eight, self.deck.StandardFrenchDeckSuit.Spades)
        self.assertFalse(self.card != data)

    def test_compare_lt_two_numeric_cards_rank(self):
        """
        Check the comparison between ranks of two numeric cards should return True (8 < 9)
        """
        data = Card(self.deck.StandardFrenchDeckValue.Nine, self.deck.StandardFrenchDeckSuit.Spades)
        self.assertTrue(self.card < data)

    def test_compare_lt_one_numeric_one_face_cards_rank(self):
        """
        Check the comparison between ranks of two numeric cards should return True (8 < J)
        """
        data = Card(self.deck.StandardFrenchDeckValue.J, self.deck.StandardFrenchDeckSuit.Spades)
        self.assertTrue(self.card < data)

    def test_compare_lt_two_cards_suit(self):
        """
        Check the comparison between suits of two cards should return True (Hearts < Spades)
        """
        data = Card(self.deck.StandardFrenchDeckValue.Eight, self.deck.StandardFrenchDeckSuit.Hearts)
        self.assertTrue(data < self.card)

    def test_compare_lt_two_cards_rank_suit(self):
        """
        Check the comparison between ranks and suits of two cards should return True (Hearts < Spades and J > 8)
        """
        data = Card(self.deck.StandardFrenchDeckValue.J, self.deck.StandardFrenchDeckSuit.Hearts)
        self.assertTrue(data < self.card)


if __name__ == '__main__':
    unittest.main()
