import sys
import random

def exit_program():
    sys.exit()

def get_int(prompt):
    while True:
        i = input(prompt)
        if i == "-0":
            print('-0 is not an integer. Please try again.\n')
        elif i.lower() == "exit":
            exit_program()
        elif i.lower() == "feedback":
            process_feedback()
        elif not i.isdigit():
            print(f'You have entered "{i}". "{i}" is not an integer. Please enter an integer.\n')
        else:
            return int(i)

def process_feedback():
    feedback = input('What is your feedback?\n')
    email = input('What is your email? We will use this only to respond to you.\n')
    try:
        with open('feedback.txt', 'a') as feed:
            feed.write(f'{feedback}\nEmail: {email}\n\n')
            print('Thank you for your feedback! We will take a look at it.\n')
            if input('Would you like to exit? (Yes/No): ').lower() == 'yes':
                exit_program()
            else:
                while True:
                    random_gen()
    except Exception:
        random_gen()

def random_gen():
    number1 = get_int('Choose your first number:\n')
    number2 = get_int('Choose your second number:\n')

    if number1 > number2:
        print('Your random number is', random.randint(number2, number1))
    elif number1 < number2:
        print('Your random number is', random.randint(number1, number2))
    else:
        print('Your numbers are the same, please try again.\n')

    if (number1, number2) in [(69, 420), (420, 69)]:
        print('Did you have to do that?\n')

while True:
    random_gen()

while True:
  random_gen()
