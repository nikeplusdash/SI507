# create the Hand with an initial set of cards
from cards import *

class Hand:
    '''a hand for playing card '''
    def __init__(self, init_cards: list):
        '''
        init the hand instance

        Parameters
        -------------------
        init_cards: a list of card instance
        the instance should be created using the card class in card.py

        Attributes
        -------------------
        cards: list
        use the init_cards to create self.cards
        a list of cards instance, indicating the cards in the hand        
        '''
        self.cards = init_cards


    def add_card(self, card):
        '''
        add a card to hand
        silently fails if the card is already in the hand
        assuming there is only one deck with 52 cards (except jokers)
        two different cards instance with the same rank and suit are 
        regarded as one card
        
        for example:
            card1 = Card(suit=0,rank=2)
            card2 = Card(suit=0,rank=2)
            card1 and card2 are regarded as the same card

        Parameters
        -------------------
        card: card instance
        a card to add

        Returns
        -------
        None
        ''' 
        if card not in self.cards:
            self.cards.append(card)

    def remove_card(self, card):
        '''
        remove a card from the hand

        Parameters
        -------------------
        card: card instance
        a card to remove

        Returns
        -------
        the removed card instance, or None if the card was not in the Hand
        '''
        if card in self.cards:
            self.cards.remove(card)
            return card
        else:
            return None


    def draw(self, deck):
        '''
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card

        Parameters
        -------------------
        deck: deck instance
        a deck from which to draw
        
        Returns
        -------
        None
        '''
        draw_card = deck.deal_card()
        self.add_card(draw_card)
    
    def remove_pairs(self):
        '''
        remove all the pairs in the hand

        Parameters
        -------------------
        None

        Returns
        -------
        None
        '''
        card_counts = {}
        for card in self.cards:
            card_counts[card] = card_counts.get(card, 0) + 1

        for card, count in card_counts.items():
            if count % 2 == 0:
                for _ in range(count):
                    self.cards.remove(card)