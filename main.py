import statistics

numbersList = []


def clear():
  import os
  os.system('clear')


def animate(key):
  import sys
  import time

  for a in range(key):
    sys.stdout.write('Generating your numbers        \r')
    time.sleep(0.75)
    sys.stdout.write('Generating your numbers.       \r')
    time.sleep(0.75)
    sys.stdout.write('Generating your numbers..      \r')
    time.sleep(0.75)
    sys.stdout.write('Generating your numbers...     \r')
    time.sleep(0.75)
  sys.stdout.write('Cleaning up                      \r')
  time.sleep(0.75)
  sys.stdout.write('Cleaning up.                     \r')
  time.sleep(0.75)
  sys.stdout.write('Cleaning up..                    \r')
  time.sleep(0.75)
  sys.stdout.write('Cleaning up...                   \r')
  time.sleep(0.75)
  sys.stdout.write('Almost done                      \r')
  time.sleep(0.75)
  sys.stdout.write('Almost done.                     \r')
  time.sleep(0.75)
  sys.stdout.write('Almost done..                    \r')
  time.sleep(0.75)
  sys.stdout.write('Almost done...                   \r')
  time.sleep(1)
  sys.stdout.write('                                 \r')


def exit():
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
  while i == "/clear":
    clear()
    print('Console cleared!\n')
    while True:
      random_gen()
  while i == "/exit":
    exit()
  while i == "/feedback":
    print()
    feedback = input('What is your feedback?\n')
    print()
    email = input(
        'What is your email? We will use this only to respond to you.\n')
    try:
      with open('feedback.txt', 'a') as feed:
        feed.write(feedback + '\n' + 'Email:' + email + '\n' + '\n')
        print()
        print('Thank you for your feedback! We will take a look at it.')
        print()
        exit_input = input('Would you like to exit?\n')
        if exit_input == 'Yes' or exit_input == 'yes':
          exit()
        if exit_input == 'No' or exit_input == 'no':
          while True:
            random_gen()
    except Exception:
      print('Something went wrong.')
      random_gen()

  while not is_an_integer(i):
    i = input(f'You have entered "{i}".' +
              f' "{i}" is not an integer. Please enter an integer.\n')
  return int(i)


def random_gen():
  global randomInt1
  global randomInt2
  import random
  number1 = get_int('Choose your first number.\n')
  print()
  number2 = get_int('Choose your second number.\n')
  print()
  amount = get_int('How many numbers do you want to generate?\n')
  number1 = int(number1)
  number2 = int(number2)
  if number1 > number2:
    if amount > 1:
      if amount > 50:
        print('This might take a while.\n')
        if amount > 100:
          key = 3
          animate(key)
        if amount <= 100:
          key = 1
          animate(key)
      print('Your random numbers are:')
      for i in range(amount):
        randomInt1 = random.randint(number2, number1)
        randomInt1 = int(randomInt1)
        print(randomInt1)
        numbersList.append(randomInt1)
      question = input('Would you like to find the average of all your numbers?\n')
      if question == 'Yes' or question == 'yes':
        print('\nThe average of all your numbers is:',statistics.mean(numbersList),'\n')
        while True:
          random_gen()
      elif question == 'No' or question == 'no':
        while True:
          random_gen()
    if amount == 1:
      randomInt1 = random.randint(number2, number1)
      print('Your random number is:\n', randomInt1)
    print()
  if number1 < number2:
    if amount > 1:
      if amount > 50:
        print('This might take a while.\n')
        if amount > 100:
          key = 3
          animate(key)
        if amount <= 100:
          key = 1
          animate(key)
      print('Your random numbers are:')
      for i in range(amount):
        randomInt2 = random.randint(number1, number2)
        print(randomInt2)
        numbersList.append(randomInt2)
      question = input('Would you like to find the average of all your numbers?\n')
      if question == 'Yes' or question == 'yes':
        print('\nThe average of all your numbers is:',statistics.mean(numbersList),'\n')
        while True:
          random_gen()
      elif question == 'No' or question == 'no':
        while True:
          random_gen()
      resultsList = []
    if amount == 1:
      randomInt2 = random.randint(number1, number2)
      print('Your random number is:\n', randomInt2)
    print()
  if number1 == number2:
    print('Your numbers are the same, please try again\n')
    random_gen()
  if number1 == 69 and number2 == 420:
    print('Did you have to do that?\n')
  if number1 == 420 and number2 == 69:
    print('Did you have to do that?\n')


while True:
  random_gen()
