#############################################################################################################################################################################

#Lesson1:"Перші Кроки" 

#############################################################################################################################################################################
'''Task 1

Run the python interpreter via the terminal. 
Get familiar with running python commands in the terminal, work with output, etc.'''

print('Done')
 
#######################################################################################################

'''Task 2

Create a python program named "task2", and use the built-in function 'print' in it several times. 
Try to pass "sep", "end" params and pass several parameters separated by commas. 
Also, provide a comment text above each print statement, mentioned above, 
with the expected output after execution of the particular print statement.

(Ex.
# 'hello world'
print("hello world")
)'''

######### task2 programm ########

msg1 = 'У царя Трояна цапині вуха'
msg2 = 'Точно, я атвічаю'

# Case 1: applying 'end' parameter
# Expected Outcome: 'У царя Трояна цапині вуха?'
print(msg1, end = '?')

# Case 2: applying 'sep' parameter
# Expected Outcome: 'У царя Трояна цапині вуха?!! Точно, я атвічаю'
print(msg1, msg2, sep= '?!! ')

# Case 3: applying both 'sep' and 'end' parameters
# Expected Outcome: 'У царя Трояна цапині вуха?!! Точно, я атвічаю, бля!'
print(msg1, msg2, end= ', бля!', sep= '?!! ')

############################################################################################################
 
'''Task 3
Write a program, which has two print statements to print the following text 
(capital letters "O" and "H", made from "#" symbols):

#########
#       #
#       #
#       #
#########

#       #
#       #
#########
#       #
#       #

Pay attention that usage of spaces is forbidden, as well as creating the whole result 
text string using """ """, use '\n' and '\t' symbols instead.
'''
# creating string blocks to use in print statements
horizontal = '\n#########'
vertical = '\n#\t#'

# printing 'O'
print(horizontal, vertical * 3, horizontal)

# printing 'H'
print(vertical * 2, horizontal, vertical * 2)

#############################################################################################################################################################################

#Lesson2:"Змінні та примітивні типи даних"

#############################################################################################################################################################################

'''Task 1

The greeting program.

Make a program that has your name and the current day of the week stored as separate variables and then prints a message like this:

     "Good day <name>! <day> is a perfect day to learn some python."

Note that  <name> and <day> are predefined variables in source code.

An additional bonus will be to use different string formatting methods for constructing result string.'''

# Setting up variables
name = 'David'
surname = 'Copperfield'
day = 'Monday'

# Printing the phrase with f-string formatting
print(f'Good day {name} {surname}! {day} is a perfect day to learn some python')

# Printing the phrase using format method
print('Good day {} {}! {} is a perfect day to learn some python'.format(name, surname, day))

############################################################################################################

'''Task 2

Manipulate strings.

Save your first and last name as separate variables, then use string concatenation to add them together with a white space in between and print a greeting.'''

# Setting up variables

first_name = 'Andrey'
last_name = 'Zavora'

print('Hello, ' + first_name + ' ' + last_name + ', welcome to the real world!')

############################################################################################################

"""Task 3

Using python as a calculator.

Make a program with 2 numbers saved in separate variables a and b, then print the result for each of the following: 

    Addition
    Subtraction
    Division
    Multiplication
    Exponent (Power)
    Modulus
    Floor division"""

# Reading input of two numbers

a = int(input('Please specify any number from 1 to 100\n'))
b = int(input('Please specify any number from 1 to 100\n'))

print(f"Your numbers are {a} and {b}. And now I'll show you some magic math can do!!!")

print('Addition of two numbers =', a + b)
print('Substruction of two numbers =', a - b)
print('Division of two numbers =', a / b) 
print('Multiplication of two numbers =', a * b)
print('Power of two numbers =', a ** b)
print('Modulus of two numbers =', a % b)
print('Floor division of two numbers =', a // b) 