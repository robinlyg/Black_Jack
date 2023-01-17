from Dealer import Dealer
from Non_Dealer import Non_Dealer
from Deck import Deck


# pay debts()
def pay_debts(player, dealer):
    print('And the hand result is: ')
    if player.card_value > 21:
        print('Player busted')
        return
    if dealer.card_value > 21:
        print('Dealer busted')
        player.balance += dealer.bet
        return
    if player.card_value > dealer.card_value:
        print('dealer pays player')
        player.balance += (player.bet + dealer.bet)
        return
    if player.card_value < dealer.card_value:
        print('player pays dealer')
        return


def main():
    # need my deck of cards
    deck = Deck()
    deck.shuffle()
    # need dealer
    dealer = Dealer('Ben')
    # non dealer players
    robin = Non_Dealer('Robin', 100)
    # need to deal each player 2 cards first
    ##good add would be they can see one card of the 2
    while True or robin.balance < 1:
        robin.hand = []
        dealer.hand = []

        for i in range(0, 2):
            robin.hand.append(deck.deal_one_card())
            dealer.hand.append(deck.deal_one_card())

        # place bets before cards are delt
        print(f'{robin.name} please place your bet.')
        robin.place_bet()
        print()

        print(f'{dealer.name} please place your bet.')
        dealer.place_bet()
        print()

        print(f'{robin.name} Its your turn')
        robin.turn(deck)
        print()

        print(f'{dealer.name} Its your turn')
        dealer.turn(deck)
        print()
        pay_debts(robin, dealer)

        if robin.balance < 1:
            print(f'{robin.name}, you are out of money, come back another time.')
            break

        again = input(
            f'{robin.name}, would you like to play another round? hit enter "y" for yes or "n" for no ').capitalize()
        if again == 'Y':
            print()
            continue
        else:
            print(f'Game over, thanks for playing!')
            break


if __name__ == '__main__':
    main()
