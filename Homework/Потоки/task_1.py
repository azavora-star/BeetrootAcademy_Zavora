# A shared counter

# Make a class called Counter, and make it a subclass of the Thread class in the Threading module. 
# Make the class have two global variables, one called counter set to 0, and another called rounds set to 100.000. 
# Now implement the run() method, let it include a simple for-loop that iterates through rounds (e.i. 100.000 times) 
# and for each time increments the value of the counter by 1. 
# Create 2 instances of the thread and start them, then join them and check the result of the counter, 
# it should be 200.000, right? 
# Run it a couple of times and consider some different reasons why you get the answer that you get.


# importing threading module along with Thread class
import threading
from threading import Thread

# creating class Counter (sub class of Thread) and implementing run() method
class Counter(Thread):
    counter = 0
    rounds = 100000

    def run(self):
        for i in range(self.rounds):
            self.counter += 1
            # print(self.counter)  

# creating 2 insances of Counter class
t1 = Counter()
t2 = Counter()

# starting and running run() method for 2 instances created
t1.start()
t2.start()

t1.join()
t2.join()

# printing result
print("Done!, count is", t1.counter + t2.counter)



