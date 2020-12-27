import unittest

from games.blackjack_game import BlackJackHand
from playing_cards import Card


class TestBlackJackHand(unittest.TestCase):

    def setUp(self):
        self.hand = BlackJackHand('test')

    def test_generate_blackjack_hand(self):
        """
        Check that blackjack hand is created with right info
        """
        self.assertEqual(self.hand.value, 0)
        self.assertEqual(self.hand.busted, False)

    def test_calculate_value_blackjack_hand_no_face_cards(self):
        """
        Check that two non face cards return the right value for hand
        """
        card1 = Card('8', 'Spades')
        card2 = Card('9', 'Spades')
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.assertEqual(self.hand.value, 17)

    def test_calculate_value_blackjack_hand_two_face_cards(self):
        """
        Check that two face cards return the right value for hand
        """
        card1 = Card('K', 'Spades')
        card2 = Card('Q', 'Spades')
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.assertEqual(self.hand.value, 20)

    def test_calculate_value_blackjack_hand_one_face_cards(self):
        """
        Check that one face card and one non-face card return the right value for hand
        """
        card1 = Card('8', 'Spades')
        card2 = Card('Q', 'Spades')
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.assertEqual(self.hand.value, 18)

    def test_calculate_value_blackjack_hand_with_ace_below_21(self):
        """
        Check that an Ace card and one other card return the right value for hand
        """
        card1 = Card('9', 'Spades')
        card2 = Card('A', 'Spades')
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.assertEqual(self.hand.value, 20)

    def test_calculate_value_blackjack_hand_with_ace_above_21(self):
        """
        Check that an Ace card and two other cards return the right value for hand
        """
        card1 = Card('8', 'Spades')
        card2 = Card('Q', 'Spades')
        card3 = Card('A', 'Spades')
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.hand.add_card(card3)
        self.assertEqual(self.hand.value, 19)

    def test_reveal_hand_all_cards_hidden(self):
        """
        Check that all cards are visible in hand if all cards were hidden before
        """
        card1 = Card('8', 'Spades')
        card2 = Card('Q', 'Spades')
        card3 = Card('A', 'Spades')
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.hand.add_card(card3)
        self.hand.reveal()
        for card in self.hand.cards:
            self.assertFalse(card.hidden)

    def test_reveal_hand_one_card_visible(self):
        """
        Check that all cards are visible in hand if one card was visible and other were hidden before
        """
        card1 = Card('8', 'Spades', hidden=False)
        card2 = Card('Q', 'Spades', hidden=True)
        card3 = Card('A', 'Spades', hidden=True)
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.hand.add_card(card3)
        self.hand.reveal()
        for card in self.hand.cards:
            self.assertFalse(card.hidden)

    def test_hand_busted(self):
        """
        Check that busted attribute is True when hand has a value above 21
        """
        card1 = Card('8', 'Spades')
        card2 = Card('Q', 'Spades')
        card3 = Card('9', 'Spades')
        self.hand.add_card(card1)
        self.hand.add_card(card2)
        self.hand.add_card(card3)
        self.assertTrue(self.hand.busted)


if __name__ == '__main__':
    unittest.main()
