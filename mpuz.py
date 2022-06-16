import random
import time 
import os
import re

def color_numbers(text, color='32'):
    colored_text = re.sub(r'(\d)', lambda m: f'\033[1;{color}m{m.group(1)}\033[0m', text)
    return colored_text


def mpuz():
    letters = [chr(x) for x in range(65, 65+10)]
    random.shuffle(letters)
    x = random.randint(100, 999)
    y = random.randint(10, 99)
    z0 = x * (y%10)
    z1 = x * (y//10)
    z = x*y
    letters_x = [letters[int(i)] for i in str(x)]
    letters_y = [letters[int(i)] for i in str(y)]
    letters_z0 = [letters[int(i)] for i in str(z0)]
    letters_z1 = [letters[int(i)] for i in str(z1)]
    letters_z = [letters[int(i)] for i in str(z)]

    X = '  '.join(letters_x)
    Y = '  '.join(letters_y)
    Z0 = '  '.join(letters_z0)
    Z1 = '  '.join(letters_z1)
    Z = '  '.join(letters_z)


    spacex = ' '*(len(Z) - len(X))
    spacey = ' '*(len(Z) - len(Y)-2)
    line = '-'*(len(Z)+1)
    spacez0 = ' '*(len(Z) - len(Z0))
    output = f'''
    {spacex}{X}
    x {spacey}{Y}
    {line}
    {spacez0}{Z0}
    {Z1}

    {Z}'''

    posibilities = list(set(letters_x + letters_y + letters_z))
    c = 0
    trials = []

    message = '''
    Welcome to mpuz game:
    Multiply two numbers and find the missing letter.
    -------------------------------------------------
    '''

    os.system('cls||clear')
    while True:
        print(message)
        trials_text = f'You have {c} wrong trials ' + str(trials)
        print(color_numbers(trials_text, '31'))
        print(color_numbers(output))
        if len([x for x in output if x in letters]) == 0:
            print('You won!')
            replay = input('Do you want to play again? ([y]/n): ')
            if replay in 'y':
                mpuz()
            else:
                print('Bye!')
                return
            return
        while True:
            guess = input('Enter your guess: ')
            try:
                guess = int(guess)
                break
            except:
                if guess == 'q':
                    print('Bye!')
                    return
                pass
            print('Please enter a number!, enter q to quit.')

        print(guess)
        idx = [i for i,x in enumerate(output) if x == letters[guess]]
        if len(idx) == 0:
            c+=1
            trials.append(guess)
        else:
            for i in idx:
                output = output.replace(output[i], str(guess))

        time.sleep(.2)
        os.system('cls||clear')

mpuz()
