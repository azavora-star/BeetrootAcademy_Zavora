# Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number. 
# Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. 
# You need to get four lists of results from corresponding functions.
# Rewrite the code to use simple functions to get the same results but using a multiprocessing library. 
# Time the execution of both realizations, explore the results, what realization is more effective, 
# why did you get a result like this.

import multiprocessing
import time

def fibonacci_sequence():
    f_sequence = []
    a=0
    b=1
    for i in range(10):
        a,b = b,a+b
        f_sequence.append(b)
    print(f"fibonacci sequence: {f_sequence}")

def square_sequence():
    sq_sequence = []
    for i in range(10):
        sq_sequence.append(i ** 2)
    print(f"square sequence: {sq_sequence}")

def cubic_sequence():
    c_sequence = []
    for i in range(10):
        c_sequence.append(i ** 3)
    print(f"cubic sequence: {c_sequence}")            

print(f"started at {time.strftime('%X')}")
    
process1 = multiprocessing.Process(fibonacci_sequence())
process2 = multiprocessing.Process(square_sequence())
process3 = multiprocessing.Process(cubic_sequence())

process1.start()
process2.start()
process3.start()

process1.join()
process2.join()
process3.join()

print(f"finished at {time.strftime('%X')}")

