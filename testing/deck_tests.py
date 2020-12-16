from card import Card
from deck import Deck
import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        #sets a single card as 'A of Hearts'
        self.card = Card('A', 'Hearts')
        
        
    def test_init(self):
        """cards should have a suit and a value"""
        #the card assigned in the setUP
        self.assertEqual(self.card.suit, 'Hearts')
        self.assertEqual(self.card.value, 'A')
        
        
    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), 'A of Hearts')
        
        
class DeckTests(unittest.TestCase):
        def setUp(self):
            self.deck = Deck()
            #setup sets deck to the full deck through Deck()
            #runs before every test case
            
        def test_init(self):
            """decks should have a cards attribute, which is a list of 52 items"""
            #doesn't test if all 52 items are cards, just that there are 52 things in this list
            self.assertTrue(isinstance(self.deck.cards, list))
            self.assertEqual(len(self.deck.cards), 52)

        def test_repr(self):
            """should print out deck of 52 cards"""
            self.assertEqual(repr(self.deck), 'Deck of 52 cards')
            
            
        def test_count(self):
            """count of deck should be 52 cards and should be 51 after running a pop"""
            self.assertEqual(self.deck.count(), 52)
            self.deck.cards.pop()
            self.assertEqual(self.deck.count(), 51)
            
        
        def test_deal_sufficient_cards(self):
            """should print out message on _deal() when there is enough cards to deal"""
            cards = self.deck._deal(10)
            self.assertEqual(len(cards), 10)
            self.assertEqual(self.deck.count(), 42)

        def test_deal_insufficient_cards(self):
            """should deal the remaining cards in the deck"""
            cards = self.deck._deal(100)
            self.assertEqual(len(cards), 52)
            self.assertEqual(self.deck.count(), 0)

        def test_deal_no_cards(self):
            """_deal should throw ValueErrorif the deck is empty when calling _deal"""
            #first line deals the entire deck self.deck.count() is 52 so we deal 52
            self.deck._deal(self.deck.count())
            #raises ValueError when 1 card id dealt when the deck is empty
            with self.assertRaises(ValueError):
                self.deck._deal(1)

        def test_deal_card(self):
            """deal_card should remove a single card from the deck"""
            #card will be the last card in the deck
            card = self.deck.cards[-1]
            #self.deck.deal() is also the last card in the deck
            dealt_card = self.deck.deal_card()
            self.assertEqual(card, dealt_card)
            self.assertEqual(self.deck.count(), 51)

        def test_deal_hand(self):
            """deal_hand should deal the number of cards passed in as an argument"""
            cards = self.deck.deal_hand(20)
            self.assertEqual(len(cards), 20)
            self.assertEqual(self.deck.count(), 32)
            
            
        def test_shuffle_full_deck(self):
            """shuffle should shuffle the deck if the deck is full"""
            #sets the cards variable to one instance of the deck
            cards = self.deck.cards[:]
            #shuffles the initial deck (not cards)
            self.deck.shuffle()
            #checks if cards and self.deck.cards are not the same (self.deck.cards has been shuffled
            self.assertNotEqual(cards, self.deck.cards)
            #checks if self.deck contains 52 cards necessary to run shuffle()
            self.assertEqual(self.deck.count(), 52)
            
        def test_shuffle_not_full_deck(self):
            """throws a ValueError when shuffling a not full deck"""
            #deals 1 card from the deck which makes self.deck.count() 51
            self.deck._deal(1)
            #tries shuffling the 51 card deck and raises a valueerror.
            with self.assertRaises(ValueError):
                self.deck.shuffle()

























if __name__ == '__main__':
    unittest.main()