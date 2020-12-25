import unittest

from games.blackjack_game import BlackJackHand

class TestBlackJackHand(unittest.TestCase):

    def setUp(self):
        self.hand = BlackJackHand('test')

    def test_generate_blackjack_hand(self):
        """
        Check that hand is created with right info
        """
        pass

if __name__ == '__main__':
    unittest.main()