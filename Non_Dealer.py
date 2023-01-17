'''Non_Dealer class inherits player
    for players that are not dealers
    they do not have auto play, must make their own calls
'''

from Card import values
from Player import Player


class Non_Dealer(Player):

    def __init__(self, name, balance):
        super(Non_Dealer, self).__init__(name)
        self.hand = []
        self.balance = balance
        self.value = 0
        self.bet = 0
        self.card_value = 0

    def place_bet(self):

        while True:
            self.bet = super(Non_Dealer, self).place_bet()
            # self.bet = Player.place_bet(self)
            if self.balance < self.bet:
                print(f'Your current balance is {self.balance}, you cannot bet over that amount ')
            else:
                self.balance -= self.bet
                break

    def hit(self, deck):
        r = deck.deal_one_card()
        self.hand.append(r)
        return r

    def stand(self):
        pass

    def hand_value(self):
        # if theres an Ace that can be 1 or 11, players choice
        # if theres an Ace that can be 1 or 11, players choice
        v = [values[card.rank] for card in self.hand]
        c = 0
        for card in self.hand:
            if card.rank == 'Ace':
                print('This hand has two possible totals')
                print(f'\t1. The Ace as 11 = {sum(v, 10)}')
                print(f'\t2. The Ace as 1: {sum(v)}')

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
        else:
            print(f'The value of your hand is {sum(v, c)}')
            self.card_value = sum(v, c)

    def print_hand(self):
        super(Non_Dealer, self).print_hand()

    def print_one_card(self):
        print(self.hand[0])

    def turn(self, deck):
        # self.place_bet()
        # print()

        print(f'{self.name} your current hand is: ')
        self.print_hand()
        self.hand_value()

        if self.card_value > 21:
            print('BUST!')
            # return to main control and the next turn occurs
            return

        print()

        while True:

            play = input("Enter 'y' enter for an additional card or 'n' to stand: ").capitalize()

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
            else:
                print('***Incorrect entry, try again.***')

            print('Would you like another card?')
