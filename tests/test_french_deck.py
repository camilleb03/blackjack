import unittest

from playing_cards import FrenchDeck

class TestFrenchDeck(unittest.TestCase):
    
    def test_init_cards(self):
        """
        Test that the deck contains 52 cards
        """
        data = 52
        deck = FrenchDeck()
        self.assertEqual(len(deck.cards), 52)
        

if __name__ == '__main__':
    unittest.main()