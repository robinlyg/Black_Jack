'''dealer class
    for the dealer auto play logic
 '''
from Card import values
from Player import Player
from Deck import Deck


class Dealer(Player):
    """the dealer calls super with no extra attributes """

    def __init__(self, name):
        super(Dealer, self).__init__(name)

    """ the dealers hand value, calculated the same as the non dealer but there are automated plays included
        the dealer does not have option as frequently as a non dealer"""

    def hand_value(self):

        # add each value to a list for easy calculation
        v = [values[card.rank] for card in self.hand]
        # c is our choice on ace value when one appears
        c = 0
        # check if any cards in hand are an Ace, if so a determination on value of the ace is made
        for card in self.hand:
            if card.rank == 'Ace':
                print('\n**This hand contains an Ace**')
                # if the sum of the hand using 11 is 17 or greater but not a bus then the dealer is forced to take 11
                # as the value
                if 17 <= sum(v, 11) < 22:
                    # we set c to 10 because the Ace's set value is 1 so we add 10
                    c = 10
                    print(f'The Aces value will be 11 the total value = {sum(v, c)}')
                # if the sum of the hand using 11 is less than 17 then the dealer can make their own choice
                # we display each option for the user to choose from
                else:
                    print('The dealer has a choice')
                    print(f'\t1. The Ace as 1: {sum(v)}')
                    print(f'\t1. The Ace as 11: {sum(v, 10)}')

                    # using a while and try/except to ensure proper input is used
                    i = 0
                    while i != 1 or i != 11:
                        try:
                            i = int(input("\tWhich Ace value would you like to continue with, enter 1 or 11: "))
                            if i == 1:
                                c = 0
                                break

                            elif i == 11:
                                c = 10
                                break

                        except:
                            print("Whoops wrong entry type")
                            continue
        # if no ace, present the sum and set self card_value to sum of hand
        else:
            print(f'The value of your hand is {sum(v, c)}')
            self.card_value = sum(v, c)

    '''Dealers turn flow '''

    def turn(self, deck):

        # present the dealers hand and its value
        print(f'{self.name}, Dealer, your hand is: ')
        self.print_hand()
        self.hand_value()

        # if the value is over 21 its a buts
        if self.card_value > 21:
            print('BUST!')
            # return to main control and the next turn occurs
            return
        # if the value is greater than 16 their turn ends
        elif self.card_value > 16:
            print('Dealers hand is 17 or greater, dealer turn ends')
            return

        print()
        # if neither a bust nor greater than 16 the dealer continues their turn
        while True:

            # the dealer can choose to hit or stand
            play = input("Enter 'y' enter for an additional card or 'n' to stand: ").capitalize()

            # if hit, print the card delt and the new value of the hand
            if play == 'Y':
                print('\n')
                # let's show what card was delt
                print('Dealer takes an additional card')
                print(f'Card delt: {self.hit(deck)}\n')
                self.hand_value()
                print()

                # if value is over 17 the turn ends
                if 17 < self.card_value <= 21:
                    print(f'Dealer has a hand of value 17 or greater')
                    break

                # if they bust break and end turn
                if self.card_value > 21:
                    print(f"ITS A BUST")
                    break
            # if play == "N" end turn
            elif play == 'N':
                break
            # catch an incorrect entry
            else:
                print('***Incorrect entry, try again.***')

            print('Would you like another card?')
