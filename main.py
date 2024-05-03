from better_profanity import profanity
import statistics

global randomInt1, randomInt2, seed, numbersList

profanitye = False
profanityf = False


def detect_profanitye(email):
    global profanitye
    profanitye = bool(profanity.contains_profanity(email))
    if profanitye:
        email = '*' * len(email)
    return email


def detect_profanityf(feedback):
    global profanityf
    profanityf = bool(profanity.contains_profanity(feedback))
    if profanityf:
        feedback = '*' * len(feedback)
    return feedback


seed = []
numbersList = []


def copy(seed):
    with open('seed.txt', 'w') as s:
        s.write(str(seed))
        print('Check seed.txt for your seed')


def clear():
    import os
    os.system('clear')


def exit_program():
    import sys
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
            random_gen(username)
    while i == 'updates':
        with open('noncode/UpdateLog.txt', 'r') as f:
            print(f.read())
            print('Current version: 1.6.3')
            print(
                'For more, check out https://github.com/randomdude79/Random-Number-Generator'
            )
            while True:
                random_gen(username)
    while i == "exit":
        exit_program()
    while i == "feedback":
        print()
        feedback = input('What is your feedback?\n')
        print()
        email = input(
            'What is your email? We will use this only to respond to you.\n')
        email = detect_profanitye(email)
        feedback = detect_profanityf(feedback)
        try:
            with open('feedback.txt', 'a') as feed:
                feed.write(feedback + '\n' + 'Email:' + email + '\n' + '\n')
                print()
                print(
                    'Thank you for your feedback! We will take a look at it.')
                print()
            exit_input = input('Would you like to exit?\n')
            if exit_input == 'Yes' or exit_input == 'yes':
                exit_program()
            if exit_input == 'No' or exit_input == 'no':
                while True:
                    random_gen(username)
        except Exception:
            print('Something went wrong.')
            random_gen(username)

    while not is_an_integer(i):
        i = input(f'You have entered "{i}".' +
                  f' "{i}" is not an integer. Please enter an integer.\n')
    return int(i)


def random_gen(username):
    global randomInt1, randomInt2, seed, numbersList
    import random

    # Reset variables at the beginning of the function
    randomInt1 = None
    randomInt2 = None
    seed = None
    numbersList = []
    print(f'Hello, {username}!')
    # Generate a new random seed for each function call
    seedquestion0 = input('Would you like to use a seed?\n')
    print()
    if seedquestion0 == 'Yes' or seedquestion0 == 'yes':
        seed = input('Enter a seed:\n')
        random.seed(seed)
    elif seedquestion0 == 'No' or seedquestion0 == 'no':
        seed = random.randint(-9223372036854775808, 9223372036854775807)
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
                        random_gen(username)
                else:
                    while True:
                        random_gen(username)
            elif seedquestion == 'No' or seedquestion == 'no':
                while True:
                    random_gen(username)
        if amount == 1:
            randomInt1 = random.randint(number2, number1)
            print('Your random number is:\n', randomInt1)
        random.seed()
        print()
    if number1 < number2:
        if amount > 1:
            print('Your random numbers are:')
            for i in range(amount):
                randomInt2 = random.randint(number1, number2)
                print(randomInt2)
                numbersList.append(randomInt2)
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
                        random_gen(username)
                else:
                    while True:
                        random_gen(username)
            elif seedquestion == 'No' or seedquestion == 'no':
                while True:
                    random_gen(username)
        if amount == 1:
            randomInt2 = random.randint(number1, number2)
            print('Your random number is:\n', randomInt2)
        random.seed()
        print()
    if number1 == number2:
        print('Your numbers are the same, please try again\n')
        random_gen(username)
    if number1 == 69 and number2 == 420:
        print('Did you have to do that?\n')
    if number1 == 420 and number2 == 69:
        print('Did you have to do that?\n')

username = input('What username would you like to use?\n')
while True:
    random_gen(username)
