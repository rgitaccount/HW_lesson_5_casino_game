import check_guess
from envparse import env
import os

env.read_envfile('settings.env')

MY_MONEY = int(os.environ.get('MY_MONEY'))
SPINWHEEL_SIZE = int(os.environ.get('SPINWHEEL_SIZE'))


def play_game():
    bank = MY_MONEY
    game_is_on = True
    print('Welcome to Casino Royale!')
    while game_is_on:
        win_or_loss = check_guess.make_bet(bank, SPINWHEEL_SIZE)
        bank += win_or_loss
        print(f'Your bank is {bank} $.\n')
        dialog = str(input('Would you like to continue? Type Y/N: '))
        if dialog.lower() == 'n':
            game_is_on = False
            print('Good bye!')


play_game()
