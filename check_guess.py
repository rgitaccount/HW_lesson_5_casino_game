from random import choice


def get_bet_number(spinwheel_size):
    user_bet_num = None
    integer_input = False
    while not integer_input:
        try:
            user_bet_num = input(f'Please choose a slot between 1 and {spinwheel_size}: ')
            int(user_bet_num)
            break
        except ValueError:
            print(f'Bet number should be integer.')
    return int(user_bet_num)


def make_bet(bank, spinwheel_size):
    bet_is_done = False
    user_win_loss = 0
    numbers_list = list(range(1, spinwheel_size))
    user_bet_num = get_bet_number(spinwheel_size)

    while not bet_is_done:
        user_bet_sum = int(input('Please make a bet: '))
        if user_bet_sum > bank:
            print(f'Your bank has only {bank}$.')
        else:
            print(f'Your bet number is: {user_bet_num}')
            casino_num = choice(numbers_list)
            print(f'Casino number is : {casino_num} ')

            if user_bet_num == casino_num:
                user_win_loss = user_bet_sum * 2
                print(f'You won {user_win_loss}!')
            else:
                user_win_loss = user_bet_sum * (-1)
                print(f'You lost {user_bet_sum}!')
            bet_is_done = True
    return user_win_loss
