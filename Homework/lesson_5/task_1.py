'''Task 1

The greatest number

Write a Python program to get the largest number from a list of random numbers with the length of 10

Constraints: use only while loop and random module to generate numbers
'''

import random

# generating list with random numbers

numbers = []
i = 0
while i < 10:
    numbers.append(random.randint(0,100))
    i += 1
print(numbers)

# printing max value    
print('Maximum number is', max(numbers))
