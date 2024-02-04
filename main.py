def get_int(prompt):
   i = input(prompt)
   while not i.isnumeric():
      i = input(f'You have entered "{i}".' + 
                f' "{i}" is not a positive integer. Please enter a positive integer:\n')
   return int(i)

def random_gen():
   import random
   number1 = get_int('Choose your first number.\n')
   print()
   number2 = get_int('Choose your second number.\n')
   print()
   if number1 > number2:
      print(random.randint(number2, number1),'is your random number.')
      print()
   if number1 < number2:
      print(random.randint(number1, number2),'is your random number.')
      print()
   if number1 == number2:
      print('Your numbers are the same, please try again')
      print()
      random_gen()

while True:
   random_gen()
