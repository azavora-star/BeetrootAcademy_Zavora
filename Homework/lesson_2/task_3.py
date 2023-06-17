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