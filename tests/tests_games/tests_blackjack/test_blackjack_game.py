import unittest

from games.blackjack_game import BlackJack, BlackJackHand
from playing_cards import Card

class TestBlackJackGame(unittest.TestCase):

    def setUp(self):
        self.blackjack = BlackJack(['Test1', 'Test2', 'Test3'])

    def test_generate_blackjack_game(self):
        """
        Check that blackjack game is created with right info
        """
        self.assertEqual(self.blackjack.player_names, ['Test1', 'Test2', 'Test3'])
        self.assertIsInstance(self.blackjack.dealer, BlackJackHand)
        self.assertEqual(self.blackjack.dealer.player_name.lower(), 'dealer')
    
    def test_set_up_blackjack_game_nb_players_equals_nb_hands(self):
        """
        Check that the number of hands is the same as the number of players
        """
        self.assertEqual(len(self.blackjack.player_names), 3)
        self.assertEqual(len(self.blackjack.hands), 3)

    def test_set_up_blackjack_game_hands_has_two_cards(self):
        """
        Check that the number of cards per hand is two for everyone (including dealer)
        """
        for hand in self.blackjack.hands:
            self.assertEqual(len(hand.cards), 2)
        self.assertEqual(len(hand.cards), 2)

    def test_set_up_blackjack_game_all_cards_visible_except_dealer(self):
        """
        Check that the all cards are revealed except for one card in the dealer's hand
        """
        for hand in self.blackjack.hands:
            for card in hand.cards:
                self.assertFalse(card.hidden)
        self.assertFalse(self.blackjack.dealer.cards[0].hidden)
        self.assertTrue(self.blackjack.dealer.cards[1].hidden)
    
    def test_set_up_blackjack_game_all_hands_has_value_over_zero(self):
        """
        Check that every hand (including dealer's) has a value over 0
        """
        for hand in self.blackjack.hands:
            self.assertGreater(hand.value, 0)
        self.assertGreater(self.blackjack.dealer.value, 0)
    
    def test_hit_adds_one_card_to_player_hand(self):
        """
        Check that hit adds one card to the player's hand
        """
        data = BlackJackHand ('Test')
        self.assertEqual(len(data.cards), 0)
        self.blackjack.hit(data)
        self.assertEqual(len(data.cards), 1)
        self.blackjack.hit(data)
        self.assertEqual(len(data.cards), 2)
    
    def test_hit_adds_type_Card_to_player_hand(self):
        """
        Check that hit adds a object of type Card in player's hand
        """
        data = BlackJackHand('Test')
        self.blackjack.hit(data)
        self.assertIsInstance(data.cards[0], Card)

if __name__ == '__main__':
    unittest.main()