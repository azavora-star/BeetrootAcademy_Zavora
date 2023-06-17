'''The birthday greeting program.

Write a program that takes your name as input, and then your age as input and greets you with the following:

“Hello <name>, on your next birthday you’ll be <age+1> years”   
'''

user_name = input('Hellow my friend! What is your name?\n')
age = int(input(f'Nice to meet you {user_name}! And how old are you?\n'))

print(f'Dear {user_name}, on your next birthday you will be ' + str(age + 1) + ' years')
