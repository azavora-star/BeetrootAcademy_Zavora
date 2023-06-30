# Task 2

# Write a function that takes in two numbers from the user via input(), call the numbers a and b, 
# and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given by the input function were not numbers, 
# and if value b was zero (cannot divide by zero).   

def task_2():
    a = input('type first number\n')
    b = input('type second number\n')
    try:
        a = float(a)
        b = float(b)
        a / b
    except ValueError:
        print('Please use numbers only!')
    except ZeroDivisionError:
        print("Second number can't be zero!")
    else:
        print(a ** 2 / b)

task_2()