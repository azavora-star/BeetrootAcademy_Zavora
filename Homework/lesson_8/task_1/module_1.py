# Task 1

# Imports practice

#  Make a directory with 2 modules; make a function in one of them; then import this function in the other module and use that in your script of choice.


from  module_2 import lullaby

user_choice = input('Do you want me to sing a lullaby for you tonigh? y\\n\n')

if user_choice == 'y':
    lullaby()
else:
    print('Good night')