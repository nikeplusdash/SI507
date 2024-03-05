import unittest
import cards
import hand

class TestCard(unittest.TestCase):
    def test_construct_Card(self):
        c1 = cards.Card(0, 2)
        c2 = cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        queen_card = cards.Card(0, 12)
        self.assertEqual(queen_card.rank_name, "Queen")

        return queen_card.rank_name, "Queen"
    
    def test_q2(self):
        '''
        1. fill in your test method for question 2:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        clubs_card = cards.Card(1, 1)
        self.assertEqual(clubs_card.suit_name, "Clubs")

        return clubs_card.suit_name, "Clubs"

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        king_of_spades = cards.Card(3, 13)
        self.assertEqual(king_of_spades.__str__(), "King of Spades")

        return king_of_spades.__str__(), "King of Spades"
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a eck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card_deck = cards.Deck()
        self.assertEqual(len(card_deck.cards), 52)

        return len(card_deck.cards), 52

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card_deck = cards.Deck()
        self.assertIsInstance(card_deck.deal_card(), cards.Card)

        return card_deck.deal_card(), cards.Card
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card_deck = cards.Deck()
        card_deck.deal_card()

        self.assertEqual(len(card_deck.cards), 51)

        return len(card_deck.cards), 51    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card_deck = cards.Deck()
        removed_card = card_deck.deal_card()
        card_deck.replace_card(removed_card)

        self.assertEqual(len(card_deck.cards), 52)

        return len(card_deck.cards), 52

    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        card_deck = cards.Deck()
        removed_card = card_deck.deal_card()
        card_deck.replace_card(removed_card)
        card_deck.replace_card(removed_card)
        card_deck.replace_card(removed_card)
        card_deck.replace_card(removed_card)

        self.assertEqual(len(card_deck.cards), 52)

        return len(card_deck.cards), 52

class TestHand(unittest.TestCase):
    def test_init(self):
        '''
        test if the hand is initialized properly
        '''
        card_deck = cards.Deck()
        cards_in_hand = [card_deck.deal_card() for _ in range(3)]
        my_hand = hand.Hand(cards_in_hand)

        self.assertIsInstance(my_hand, hand.Hand)

        return my_hand, hand.Hand
    
    def test_testAddAndRemove(self):
        '''
        test if the add_card and remove_card methods work properly
        '''
        card_deck = cards.Deck()
        cards_in_hand = [card_deck.deal_card() for _ in range(3)]
        my_hand = hand.Hand(cards_in_hand)
        self.assertEqual(len(my_hand.cards), 3)

        removed_card = card_deck.deal_card()
        my_hand.add_card(removed_card)
        self.assertEqual(len(my_hand.cards), 4)

        my_hand.remove_card(removed_card)
        self.assertEqual(len(my_hand.cards), 3)

        return len(my_hand.cards), 3

    def test_draw(self):
        '''
        test if the draw method works properly
        '''
        card_deck = cards.Deck()
        cards_in_hand = [card_deck.deal_card() for _ in range(3)]
        my_hand = hand.Hand(cards_in_hand)
        self.assertEqual(len(my_hand.cards), 3)

        my_hand.draw(card_deck)
        self.assertEqual(len(my_hand.cards), 4)
        
        return len(my_hand.cards), 4

if __name__=="__main__":
    unittest.main()