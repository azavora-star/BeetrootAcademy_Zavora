# Write a Python program to access a function inside a function (Tips: use function, which returns another function)

def func1():
    def func2():
        print('Hello, world')
    return func2()        

func1()    