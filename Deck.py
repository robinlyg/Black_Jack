"""Deck class
    builds a full deck of card using the Card class
    contains a shuffle and deal one card methods
"""
import Card
import random

'''initiate deck: builds a full deck using the Card class lists of suit and rank'''


class Deck:
    def __init__(self):
        # list of cards
        self.all_cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card.Card(suit, rank)
                self.all_cards.append(card)

    '''shuffle the deck of cards using random.shuffle'''

    def shuffle(self):
        random.shuffle(self.all_cards)

    '''deal one card, takes the last card and pops it off the list'''

    def deal_one_card(self):
        return self.all_cards.pop()
