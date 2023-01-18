'''
    player class will be inherited by our dealer and non dealers
    the two share attributes: hand, name and bet
    and actions: turn, hit, stand, place bet
'''
from Deck import Deck

class Player:

    """both a dealer and non dealer have a hand, bet and name and card_value aka the hands numeric value"""
    def __init__(self, name):
        self.name = name
        self.bet = 0
        self.hand = []
        self.card_value=0

    '''each can "hit" or take another card, a card from the deck is taken off the deck and handed to the hand'''
    def hit(self, deck):
        r = Deck.deal_one_card(deck)
        self.hand.append(r)
        return r

    '''each need to see their hand, loop through hand to print each card'''
    def print_hand(self):
        for card in self.hand:
            print(card)

    '''each will place a bet this will differ but for dealer and non dealer it must be an int '''
    def place_bet(self):

        while True:
            try:
                self.bet = int(input("Enter the amount you would like to bet: "))
                return self.bet
            except:
                print("Not a valid input, please try again")

    '''each and stand which is really just a pass and their turn is over 
        and take a turn which will be different for each player type'''
    def stand(self):
        pass

    def turn(self, deck):
        pass
