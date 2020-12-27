import unittest
import itertools
from playing_cards import FrenchDeck, Card, Hand

class TestFrenchDeck(unittest.TestCase):

    def setUp(self):
        self.deck = FrenchDeck()
    
    def test_generate_one_deck_length(self):
        """
        Check that deck contains 52 cards
        """
        self.assertEqual(len(self.deck.cards), 52)
    
    def test_generate_three_decks_length(self):
        """
        Check that deck contains 156 cards
        """
        self.deck = FrenchDeck(nb_decks=3)
        self.assertEqual(len(self.deck.cards), 156)

    def test_generate_multiple_decks_card_references(self):
        """
        Check when one card is modified, the other version is not (deepcopy)
        """
        self.deck = FrenchDeck(nb_decks=2)
        self.assertEqual(self.deck.cards[0], self.deck.cards[52])
        self.deck.cards[0].suit = 'Hearts'
        self.assertNotEqual(self.deck.cards[0], self.deck.cards[52])
        self.assertIsNot(self.deck.cards[0], self.deck.cards[52])
    
    def test_generate_cards_content(self):
        """
        Check that deck contains all combinations of ranks and suits
        """
        for idx, i in enumerate(itertools.product(self.deck.card_suits, self.deck.card_ranks)):
            card = Card(i[1],i[0])
            self.assertEqual(self.deck.cards[idx].rank, card.rank)
            self.assertEqual(self.deck.cards[idx].suit, card.suit)
        # self.assertCountEqual(self.deck.cards, data)

    def test_generate_cards_order(self):
        """
        Check that deck contains 52 cards in ascending order
        A to K ; Sapdes to Clubs
        """
        data = Card('A', 'Spades')
        data2 = Card('K', 'Clubs')
        self.assertEqual(self.deck.cards[0].rank, data.rank)
        self.assertEqual(self.deck.cards[0].suit, data.suit)
        self.assertEqual(self.deck.cards[len(self.deck.cards)-1].rank, data2.rank)
        self.assertEqual(self.deck.cards[len(self.deck.cards)-1].suit, data2.suit)

    # FIXME: Mock something to test better if by any chance the first or last card stay at the same position
    def test_shuffle_cards_in_deck(self):
        """
        Check that deck is shuffled correctly
        """
        data = Card('A', 'Spades')
        data2 = Card('K', 'Clubs')
        self.deck.shuffle()
        self.assertTrue((self.deck.cards[0].rank != data.rank) or (self.deck.cards[0].suit !=data.suit))
        self.assertTrue((self.deck.cards[len(self.deck.cards)-1].rank != data2.rank) or (self.deck.cards[len(self.deck.cards)-1].suit !=data2.suit))

    
    # FIXME: Not working because of card comparison (lesser than)
    @unittest.skip("WIP : less_than not implemented yet")
    def test_sort_cards_in_deck(self):
        """
        Check that deck is sorted correctly by suits and ranks
        """
        data = Card('A', 'Spades')
        data2 = Card('K', 'Clubs')
        self.deck.shuffle()
        self.deck.sort()
        self.assertEqual(self.deck.cards[0].rank, data.rank)
        self.assertEqual(self.deck.cards[0].suit, data.suit)
        self.assertEqual(self.deck.cards[len(self.deck.cards)-1].rank, data2.rank)
        self.assertEqual(self.deck.cards[len(self.deck.cards)-1].suit, data2.suit)

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
    
    def test_remove_card_invalid(self):
        """
        Check when there is enough cards to be removed from the deck
        """
        self.deck.deal_cards(Hand('Test'), len(self.deck.cards))
        self.assertEqual(len(self.deck.cards), 0)
        self.deck.remove_card(Card('8', 'Spades'))
        self.assertEqual(len(self.deck.cards), 0)

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