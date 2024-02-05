import random

def is_positive_integer(s):
    try:
        return int(s) > 0
    except ValueError:
        return False

def get_positive_int(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "Feedback":
            handle_feedback()
        elif is_positive_integer(user_input):
            return int(user_input)
        else:
            print(f'You have entered "{user_input}". Please enter a positive integer.')

def handle_feedback():
    feed = input('What is your feedback?\n')
    try:
        with open('feedback.txt', 'a') as feedback_file:
            feedback_file.write(feed + '\n')
            print('\nThank you for your feedback!\n')
    except Exception:
        print('Something went wrong with feedback submission.')

def generate_random_number():
    number1 = get_positive_int('Choose your first number.\n')
    number2 = get_positive_int('Choose your second number.\n')
    
    if number1 != number2:
        print(random.randint(min(number1, number2), max(number1, number2)), 'is your random number.\n')
    else:
        print('Your numbers are the same, please try again.\n')

while True:
    generate_random_number()
