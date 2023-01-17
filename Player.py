'''
    player class will be inherited by our dealer and non dealers
    since the two still share attributes and actions
'''
import abc

from Deck import  Deck
from abc import ABC, abstractmethod


#global deck
#deck = Deck.Deck()

class Player: #(ABC):
    #everyone has a hand, an account, turn,
    #everyone can hit, stand, bet, win, lose
   # @abstractmethod
    def __init__(self,name):
        self.name = name
        self.bet = 0
        self.hand = []

    #@abstractmethod
    def hit(self,deck):
        r = Deck.deal_one_card(deck)
        return r

    @abstractmethod
    def print_hand(self):
        for card in self.hand:
            print(card)

    #@abstractmethod
    def place_bet(self):
        bet = 0
        while True:
            try:
                bet = int(input("Enter the amount you would like to bet: "))
                return bet
            except:
                print("Not a valid input, please try again")

    #@abstractmethod
    def stand(self):
        pass


