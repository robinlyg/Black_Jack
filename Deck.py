import Card
import random


class Deck:
    def __init__(self):
        # list of cards
        self.all_cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                card = Card.Card(suit,rank)
                self.all_cards.append(card)

    '''no return value'''

    def shuffle(self):
        random.shuffle(self.all_cards)

    '''returns one card from the end of the list'''

    #def deal_one_card(self):

    def deal_one_card(self):
        return self.all_cards.pop()