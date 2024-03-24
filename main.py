import random
import statistics
import os
import sys
import time

numbersList = []


def clear():
    os.system('clear')


def animate(message):
    for _ in range(4):
        for c in '|/-\\':
            sys.stdout.write(f'{message} {c}\r')
            sys.stdout.flush()
            time.sleep(0.1)


def exit_program():
    sys.exit()


def get_int(prompt):
    while True:
        try:
            i = int(input(prompt))
            return i
        except ValueError:
            print("Please enter an integer.\n")


def random_gen():
    global numbersList
    numbersList = []
    number1 = get_int('Choose your first number:\n')
    number2 = get_int('Choose your second number:\n')
    seed_choice = input('Would you like to use a seed? (Yes/No)\n')
    if seed_choice.lower() == 'yes':
        seed = get_int('Enter your seed:\n')
        random.seed(seed)
    else:
        random.seed()

    amount = get_int('How many numbers do you want to generate?\n')
    print('Generating your numbers...')
    time.sleep(1)

    start, end = min(number1, number2), max(number1, number2)
    random_numbers = [random.randint(start, end) for _ in range(amount)]
    numbersList.extend(random_numbers)

    print('Your random numbers are:')
    for num in random_numbers:
        print(num)

    avg_choice = input('Would you like to find the average of all your numbers? (Yes/No)\n')
    if avg_choice.lower() == 'yes':
        print('\nThe average of all your numbers is:', statistics.mean(numbersList), '\n')

    print()
    return


while True:
    random_gen()
