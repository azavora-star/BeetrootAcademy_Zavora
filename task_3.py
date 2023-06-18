'''Task 3

Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration'''

import random

numbers = []
numbers_1 = []

i = 0
while i in range(100):
    i += 1
    numbers.append(i)
    if i % 7 == 0 and i % 5 !=0:
        numbers_1.append(i)
print(numbers)
print(numbers_1)    
