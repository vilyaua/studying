'''
Написать игру "Rock Scissors Papers":
Играют компьютер и человек. Компьютер каждый ход случайно загадывает свой выбор, а пользователь вводит свой.
Правила:
Rock побеждает Scissors
Scissors -> Papers
Papers -> Rock
в случае одинакового выбора - ничья
Сделать возможность играть несколько раундов до какого-то счета (например до 3-ох)
'''

import random

words = ['rock', 'paper', 'scissors']
score = 3
comp_wins = user_wins = 0
game = 1

while comp_wins < score and user_wins < score:
    print('\nRound ' + str(game))
    game += 1
    comp_choice = random.choice(words)
    n = int(input('make your choice: 0 - rock, 1 - paper, 2 - scissors ... '))
    user_choice = words[n]
    print('User chose: ' + user_choice)
    print('Comp chose: ' + comp_choice)
    if comp_choice == user_choice:
        print('it\'s a RAW! both chose ' + comp_choice)
        continue
    if comp_choice == 'scissors':
        if user_choice == 'paper':
            comp_wins += 1
        else:
            user_wins += 1
    else:
        if comp_choice == 'rock':
            if user_choice == 'scissors':
                comp_wins += 1
            else:
                user_wins += 1
        else:
            if user_choice == 'rock':
                comp_wins += 1
            else:
                user_wins += 1
    print('Comp wins: ' + str(comp_wins) + '... User wins: ' + str(user_wins))

input('\nGame over. Press any key...')
