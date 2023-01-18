from Dealer import Dealer
from Non_Dealer import Non_Dealer
from Deck import Deck


# pay debts(players[]) the dealer is always the last in the list Notice: when a player places a bet, its immediately
# deducted from their balance so when they tie or are paid they should also get their bet back

def pay_debts(player_list):
    print('And the hand result is: ')
    # if a player is over 21 they lose their bet
    for player in player_list[0:-1]:
        print(f'Dealers bet was: {player_list[-1].bet}')
        if player.card_value > 21:
            print(f'{player.name} busted')

        # if the dealer busts, anyone who had not busted gets paid
        elif player_list[-1].card_value > 21:
            print(f'Dealer pays {player.name}')
            player.balance += player_list[-1].bet

        # any player with a higher value than the dealer gets paid
        elif player.card_value > player_list[-1].card_value:
            player.balance = player.bet + player_list[-1].bet + player.balance
            print(f'Dealer pays {player.name}')

        # any player with a value less than dealer, pays the dealer
        elif player.card_value < player_list[-1].card_value:
            print(f'{player.name} pays Dealer')

        # in the case of a tie, both dealer and player keep their bet
        else:
            player.balance += player_list.bet
            print(f'{player.name} ties with Dealer')

        print(f'{player.name}, your account balance is: {player.balance}.')


def main():
    # first we ask for the dealer, there is only one
    dealer_name = input('Please enter the name of your dealer: ')
    dealer = Dealer(dealer_name)

    '''Ask for number of players, excluding the dealer, ensure its within bounds and an int'''
    while True:
        try:
            num_players = int(input("Please enter the number of players (max is 5): "))
            if num_players < 6 > 0:
                break
            else:
                print("Too many players at the table, try again.")
                continue
        except TypeError:
            print('Incorrect input try again')

    # will use a list to store our players in, the dealer will be added last
    ''' ask users for each players name and balance
        add each to list '''
    player_list = []
    for i in range(0, num_players):
        while True:
            try:
                name, balance = input(f'Player {i + 1} please enter your name and account balance: ').split()
                balance = int(balance)
                player_list.append(Non_Dealer(name, balance))
                break
            except ValueError:
                print(f"Incorrect player entry please try to enter Player {i + 1} again")

    # add in dealer at end of list
    player_list.append(dealer)

    ''' the game play is held in a while loop, so players can play as many rounds as they would like'''
    while True:

        # each round there's a full deck shuffled
        deck = Deck()
        deck.shuffle()

        # for each player in the list, deal 2 cards
        for i in range(0, 2):
            for player in player_list:
                player.hand.append(deck.deal_one_card())

        # for each player, place bet before cards are delt
        for player in player_list:
            print(f'{player.name} please place your bet.')
            player.place_bet()
            print()

        print()

        # each player takes their turn, the dealer last (at the end of the list)
        for player in player_list:
            print(f'{player.name}, its your turn.')
            player.turn(deck)
            print()

        # call pay_debts to settle up the round
        pay_debts(player_list)

        # clear hand from this round
        for player in player_list:
            player.hand = []

        # if any player has a zero balance, or balance less than buy in they are removed from list
        for player in player_list[0:-1]:
            if player.balance < 20:
                print(f"{player.name}, you are out of funds, game over.")
                player_list.remove(player)

        # each player is asked if they would like to continue
        for player in player_list[0:-1]:
            while True:
                char = input(f'{player.name}, would you like to continue, Y or N: ').capitalize()
                if char == 'N':
                    print(f'Thank you {player.name} for playing.')
                    player_list.remove(player)
                    break
                elif char == 'Y':
                    break
                else:
                    print(f'Incorrect entry, try again')

        # if only the dealer is left program ends
        if len(player_list) == 1:
            print('All players have left.')
            break


if __name__ == '__main__':
    main()
