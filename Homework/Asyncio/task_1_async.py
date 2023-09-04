# Create a separate asynchronous code to calculate Fibonacci, factorial, squares and cubic for an input number. 
# Schedule the execution of this code using asyncio.gather for a list of integers from 1 to 10. 
# You need to get four lists of results from corresponding functions.
# Rewrite the code to use simple functions to get the same results but using a multiprocessing library. 
# Time the execution of both realizations, explore the results, what realization is more effective, 
# why did you get a result like this.

import asyncio
import time

async def fibonacci_sequence():
    f_sequence = []
    a=0
    b=1
    for i in range(10):
        a,b = b,a+b
        f_sequence.append(b)
        await asyncio.sleep(1)
    print(f"fibonacci sequence: {f_sequence}")

async def square_sequence():
    sq_sequence = []
    for i in range(10):
        sq_sequence.append(i ** 2)
        await asyncio.sleep(1)
    print(f"square sequence: {sq_sequence}")

async def cubic_sequence():
    c_sequence = []
    for i in range(10):
        c_sequence.append(i ** 3)
        await asyncio.sleep(1)
    print(f"cubic sequence: {c_sequence}")            

async def main():
    print(f"started at {time.strftime('%X')}")
    
    task1 = asyncio.create_task(fibonacci_sequence())
    task2 = asyncio.create_task(square_sequence())
    task3 = asyncio.create_task(cubic_sequence())
    await asyncio.gather(task1, task2, task3)
    
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())    
