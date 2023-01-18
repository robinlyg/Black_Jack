'''Non_Dealer class inherits player
    for players that are not dealers
    they do not have autoplay, must make their own calls
'''

from Card import values
from Player import Player


class Non_Dealer(Player):
    """Call is made to super but non dealer has an extra attribute, balance"""

    def __init__(self, name, balance):
        super(Non_Dealer, self).__init__(name)
        self.balance = balance

    '''Non dealer has an extra check to make when making a bet, they can not bet over their balance'''

    def place_bet(self):

        while True:
            self.bet = super(Non_Dealer, self).place_bet()
            # self.bet = Player.place_bet(self)
            if self.balance < self.bet:
                print(f'Your current balance is {self.balance}, you cannot bet over that amount ')
            else:
                self.balance -= self.bet
                break

    '''A non dealer has to make more decisions than a dealer when theres an Ace involved'''

    def hand_value(self):

        # add each value to a list for easy calculation
        v = [values[card.rank] for card in self.hand]
        # c is our choice on ace value when one appears, the initial value of an Ace is 1
        c = 0
        # check if any cards in hand are an Ace, if so a determination on value of the ace is made
        for card in self.hand:
            # if there is an Ace we display the possible values and allow the user to choose
            if card.rank == 'Ace':
                print('This hand has two possible totals')
                print(f'\t2. The Ace as 1: {sum(v)}')
                # the initial value of an Ace is 1 so we add 10 to the sum of the hand
                print(f'\t1. The Ace as 11 = {sum(v, 10)}')

                # use a while loop and try/except to ensure correct input
                i = 0
                while i != 1 or i != 11:
                    try:
                        i = int(input("\tWhich Ace value would you like to continue with, enter 1 or 11: "))
                        if i == 1:
                            c = 0
                            break

                        if i == 11:
                            c = 10
                            break

                    except:
                        print("Whoops wrong entry type")
                        continue
        # if no ace, present the sum and set self card_value to sum of hand
        else:
            print(f'The value of your hand is {sum(v, c)}')
            self.card_value = sum(v, c)

    '''a turn is a loop allowing the player to hit or stand'''

    def turn(self, deck):
        # present the player with their hand and its value
        print(f'{self.name} your current hand is: ')
        self.print_hand()
        self.hand_value()

        # if the value of the hand is greater than 21 it's a bust and turn ends
        if self.card_value > 21:
            print('BUST!')
            # return to main control and the next turn occurs
            return

        print()
        # if not a bust they have the choice to hit or stand
        while True:

            # ask player if they want to hit or stand
            play = input("Enter 'y' enter for an additional card or 'n' to stand: ").capitalize()

            # if a hit we deal another card, show that card and the new value of the hand
            # also check if the new value is over 21 and a bust, if so end turn
            if play == 'Y':
                print()
                # lets show what card was delt
                print('Dealer deals an additional card')
                print(f'Card delt: {self.hit(deck)}')
                print()
                self.hand_value()
                print()
                # if they bust break and end turn
                if self.card_value > 21:
                    print(f"ITS A BUST")
                    break
            # in the case of a stand the next player takes their turn
            elif play == 'N':
                print(f'{self.name} your turn has ended.')
                break
            # if y or n is not entered we ask the user to try again and allow the loop to continue
            else:
                print('***Incorrect entry, try again.***')

            print('Would you like another card?')
