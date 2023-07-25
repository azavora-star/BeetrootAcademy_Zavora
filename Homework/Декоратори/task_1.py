# Task 1

# Write a decorator that prints a function with arguments passed to it.
# It should print the function, not the result of its execution!
# For example:

# "add called with 4, 5"

def logger(func):
    def wrapper(*args):
       print(f'{func.__name__} called with {args}')
       return func(*args)      
    return wrapper   

@logger
def add(x, y):
   return x + y

@logger
def square_all(*args):
   return [arg ** 2 for arg in args]


add(4, 5)
square_all(1 ,2, 3)