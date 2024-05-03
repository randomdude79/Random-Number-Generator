import random
import statistics
import os
import sys

numbers_list = []

def clear():
    os.system('clear')


def exit_program():
    sys.exit()

def is_an_integer(s):
    return s.isdigit()

def get_int(prompt):
    while True:
        i = input(prompt)
        if i == "//clear":
            clear()
            print('Console cleared!\n')
        elif i == "//exit":
            exit_program()
        elif i == "/feedback":
            feedback = input('What is your feedback?\n')
            email = input('What is your email? We will use this only to respond to you.\n')
            with open('feedback.txt', 'a') as feed:
                feed.write(f'{feedback}\nEmail: {email}\n\n')
            print('Thank you for your feedback!')
            if input('Would you like to exit? (Yes/No)\n').lower() == 'yes':
                exit_program()
        elif is_an_integer(i):
            return int(i)
        else:
            print(f'Invalid input: "{i}". Please enter an integer.\n')

def random_gen():
    global seed
    number1 = get_int('Choose your first number.\n')
    number2 = get_int('Choose your second number.\n')
    seed_question = input('Would you like to use a seed? (Yes/No)\n').lower()
    seed = get_int('What is your seed?\n') if seed_question == 'yes' else random.randint(0, 70368744177664)
    random.seed(seed)
    amount = get_int('How many numbers do you want to generate?\n')
    if number1 > number2:
        numbers = (random.randint(number2, number1) for _ in range(amount))
    else:
        numbers = (random.randint(number1, number2) for _ in range(amount))
    print('Your random numbers are:')
    for num in numbers:
        print(num)
        numbers_list.append(num)
    random.seed()
    if input('Would you like to find the average of all your numbers? (Yes/No)\n').lower() == 'yes':
        print('\nThe average of all your numbers is:', statistics.mean(numbers_list), '\n')
    if input('Would you like to know your seed? (Yes/No)\n').lower() == 'yes':
        print(seed)
    while True:
        random_gen()

while True:
    random_gen()
