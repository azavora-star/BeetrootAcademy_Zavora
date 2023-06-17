'''The Guessing Game.

Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.'''

import random

random_number = random.randrange(1,100)
user_input = int(input('I have a random number in my memory (from 1 to 100). Can you guess what is it?\n'))

if user_input != random_number:
    print('Not correct!!')
    print(f'The right number is {random_number}')
else:
    print('Correct!')