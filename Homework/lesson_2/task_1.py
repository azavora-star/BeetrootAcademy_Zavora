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