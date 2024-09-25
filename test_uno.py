import unittest
from deck import get_deck, shuffle_deck, draw_cards
from player import can_play

class TestUnoGame(unittest.TestCase):

    def test_get_deck(self):
        deck = get_deck()
        self.assertEqual(len(deck), 108)  # UNO deck contains 108 cards

    def test_shuffle_deck(self):
        deck = get_deck()
        shuffled_deck = shuffle_deck(deck.copy())
        self.assertNotEqual(deck, shuffled_deck)  # Shuffled deck should not be in the same order

    def test_draw_cards(self):
        deck = get_deck()
        cards = draw_cards(deck, 7)
        self.assertEqual(len(cards), 7)
        self.assertEqual(len(deck), 101)  # After drawing 7 cards, 101 should be left in the deck

    def test_can_play(self):
        discard_card = ["Red", 5]
        hand = [["Blue", 5], ["Red", 3], ["Green", "Skip"], ["Wild", "Wild"]]
        self.assertTrue(can_play(discard_card, hand)) 

if __name__ == "__main__":
    unittest.main()
