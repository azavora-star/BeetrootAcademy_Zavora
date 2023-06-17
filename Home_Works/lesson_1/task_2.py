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