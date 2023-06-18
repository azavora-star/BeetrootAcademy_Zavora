'''Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers
'''

import random

numbers_1 = []
numbers_2 = []
numbers_3 = []

# generating lists with random numbers
i = 0
while i < 10:
    numbers_1.append(random.randint(0,10))
    numbers_2.append(random.randint(0,10))
    i += 1
print(numbers_1)
print(numbers_2)

# creating a list containing common numbers
for i in numbers_1:
    if i in numbers_2:
        numbers_3.append(i) 
print(numbers_3)

# removing duplicates
set_3 = set(numbers_3)
numbers_3 = list(set_3)
print(numbers_3)