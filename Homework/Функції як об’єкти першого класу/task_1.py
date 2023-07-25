#  Write a Python program to detect the number of local variables declared in a function.

def func_1(a):
    b = a ** 2
    c = b ** 3

def func_2():
    pass

print(func_1.__code__.co_nlocals)
print(func_2.__code__.co_nlocals)