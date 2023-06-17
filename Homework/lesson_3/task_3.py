'''
Task 3

The math quiz program.
Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
'''

answer = input('What would be the result of this expression: 4+4*2?\n')

if answer != "12":
    print('Your answer is not correct!')
else:
    print('You are right!')    
