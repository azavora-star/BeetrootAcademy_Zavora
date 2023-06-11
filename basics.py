#Lesson:"Перші Кроки" 

'''Task 1

Run the python interpreter via the terminal. 
Get familiar with running python commands in the terminal, work with output, etc.'''

print('Done')
 
###########################################################################################################################################################################

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

# Case 1: appying 'end' parameter
# Expected Outcome: 'У царя Трояна цапині вуха?'
print(msg1, end = '?')

# Case 2: appying 'sep' parameter
# Expected Outcome: 'У царя Трояна цапині вуха?!! Точно, я атвічаю'
print(msg1, msg2, sep= ' ?!! ')

# Case 3: appying both 'sep' and 'end' parameters
# Expected Outcome: 'У царя Трояна цапині вуха?!! Точно, я атвічаю'
print(msg1, msg2, end= ', бля!', sep= '?!! ')

#############################################################################################################################################################################
 
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
