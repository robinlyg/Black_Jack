'''dealer class
    for the dealer auto play logic
 '''
from Card import values
from Player import Player
from Deck import Deck


class Dealer(Player):

    def __init__(self, name):
        super(Dealer, self).__init__(name)
        self.name = name
        self.hand = []
        self.card_value = 0

    def print_hand(self):
        for card in self.hand:
            print(card)

    def place_bet(self):
        self.bet = super(Dealer, self).place_bet()

    def hit(self, deck):
        r = Deck.deal_one_card(deck)
        self.hand.append(r)
        return r

    def stand(self):
        pass

    def hand_value(self):
        # if theres an Ace that can be 1 or 11, players choice
        v = [values[card.rank] for card in self.hand]
        c = 0

        for card in self.hand:
            if card.rank == 'Ace':
                print('\n**This hand contains an Ace**')
                if 17 <= sum(v, 11) < 22:
                    c = 10
                    print(f'The Aces value will be 11 the total value = {sum(v, c)}')
                else:
                    print('The dealer has a choice')
                    print(f'\t1. The Ace as 1: {sum(v)}')
                    print(f'\t1. The Ace as 11: {sum(v, 10)}')

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

        else:
            print(f'The value of your hand is {sum(v, c)}')
            self.card_value = sum(v, c)

    def print_one_card(self):
        print(self.hand[0])

    def turn(self, deck):

        # self.place_bet()
        # print()
        print(f'{self.name}, Dealer, your hand is: ')
        self.print_hand()
        self.hand_value()

        if self.card_value > 21:
            print('BUST!')
            # return to main control and the next turn occurs
            return
        elif self.card_value > 16:
            print('Dealers hand is 17 or greater, dealer turn ends')
            return

        print()

        while True:

            play = input("Enter 'y' enter for an additional card or 'n' to stand: ").capitalize()

            if play == 'Y':
                print('\n')
                # let's show what card was delt
                print('Dealer takes an additional card')
                print(f'Card delt: {self.hit(deck)}\n')
                self.hand_value()
                print()

                # if value is over 17
                if 17 < self.card_value <= 21:
                    print(f'Dealer has a hand of value 17 or greater')
                    break

                # if they bust break and end turn
                if self.card_value > 21:
                    print(f"ITS A BUST")
                    break
            # in the case of a stand the next player takes their turn
            elif play == 'N':
                break
            else:
                print('***Incorrect entry, try again.***')

            print('Would you like another card?')
