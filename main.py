import statistics
import random
import time
import os
import sys

global randomInt1, randomInt2, seed, numbersList, version

command_history = []

version = "1.12.1"

seed = []
numbersList = []

def copy(seed):
    with open('seed.txt', 'w') as s:
        s.write(str(seed))
        print('Check seed.txt for your seed')

def clear():
    os.system('clear')

def exit_program():
    sys.exit()

def is_an_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def get_int(prompt):
    i = input(prompt)
    while i == "-0":
        print('-0 is not an integer. Please try again.')
        print()
        i = input(prompt)
    while i == "clear":
        clear()
        print('Console cleared!\n')
        while True:
            random_gen()
    while i == 'updates':
        with open('noncode/UpdateLog.txt', 'r') as f:
            print(f.read())
            print(f'Current version: {version}')
            print(
                'For more, check out https://github.com/randomdude79/Random-Number-Generator'
            )
            while True:
                random_gen()
    while i == 'update':
        clear()
        for i in range(3):
            sys.stdout.write('Updating   \r')
            time.sleep(0.5)
            sys.stdout.write('Updating.  \r')
            time.sleep(0.5)
            sys.stdout.write('Updating.. \r')
            time.sleep(0.5)
            sys.stdout.write('Updating...\r')
            time.sleep(0.5)
        os.system('git restore *')
        os.system('git pull')
        for i in range(3):
            sys.stdout.write('Restarting   \r')
            time.sleep(0.5)
            sys.stdout.write('Restarting.  \r')
            time.sleep(0.5)
            sys.stdout.write('Restarting.. \r')
            time.sleep(0.5)
            sys.stdout.write('Restarting...\r')
            time.sleep(0.5)
        clear()
        print(f'Version: {version}')
        os.system('python main.py')
    while i == "exit":
        exit_program()
    while not is_an_integer(i):
        i = input(f'You have entered "{i}".' +
                  f' "{i}" is not an integer. Please enter an integer.\n')
    return int(i)

def random_gen():
    randomInt1 = None
    seed1 = seed2 = seed3 = seed4 = ''
    numbersList = []
    seedquestion0 = input('Would you like to use a seed?\n')
    print()
    if seedquestion0 == 'Yes' or seedquestion0 == 'yes':
        seed = int(input('Enter a seed:\n'))
        random.seed(seed)
    else:
        for i in range(5):
            seed1 += str(random.randint(0, 9))
        for i in range(5):
            seed2 += str(random.randint(0, 9))
        for i in range(5):
            seed3 += str(random.randint(0, 9))
        for i in range(5):
            seed4 += str(random.randint(0, 9))
        seed = int(seed1 + seed2 + seed3 + seed4)
        random.seed(seed)
    number1 = get_int('Choose your first number.\n')
    print()
    number2 = get_int('Choose your second number.\n')
    print()
    amount = get_int('How many numbers do you want to generate?\n')
    print()
    number1 = int(number1)
    number2 = int(number2)
    if number1 > number2:
        pass
    else:
        number1, number2 = number2, number1
    
    if amount > 1:
            print('Your random numbers are:')
            for i in range(amount):
                randomInt1 = random.randint(number2, number1)
                randomInt1 = int(randomInt1)
                print(randomInt1)
                numbersList.append(randomInt1)
            random.seed()
            print()
            question = input(
                'Would you like to find the average of all your numbers?\n')
            if question == 'Yes' or question == 'yes':
                print('\nThe average of all your numbers is:',
                      statistics.mean(numbersList), '\n')
            elif question == 'No' or question == 'no':
                print()
            seedquestion = input('Would you like to know your seed?\n')
            if seedquestion == 'Yes' or seedquestion == 'yes':
                print('Your seed is: ', seed)
                copy_seed = input('Would you like to copy the seed?\n')
                if copy_seed == 'Yes' or copy_seed == 'yes':
                    copy(seed)
                    while True:
                        random_gen()
                else:
                    while True:
                        random_gen()
            elif seedquestion == 'No' or seedquestion == 'no':
                while True:
                    random_gen()
    if amount == 1:
            randomInt1 = random.randint(number2, number1)
            print('Your random number is:\n', randomInt1)
    random.seed()
    print()
    
while True:
    random_gen()
