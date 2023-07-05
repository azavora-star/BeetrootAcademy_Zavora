# Task 2

# The sys module.

#  The “sys.path” list is initialized from the PYTHONPATH environment variable. Is it possible to change it from within Python? If so, does it affect where Python looks for module files? Run some interactive tests to find it out.

import sys

# let's update sys.path variable to start searching modules from "/home/azavora/Projects/BeetrootAcademy_Zavora/Homework/lesson_8/task_1" folder
sys.path.append('/home/azavora/Projects/BeetrootAcademy_Zavora/Homework/lesson_8/task_1/')
print(sys.path)
print('\n\n')      

import module_2

module_2.lullaby()
