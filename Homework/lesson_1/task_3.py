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