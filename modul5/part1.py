# import Module
import random

import my_functions
import time
import math
import sys

print(sys.path)
  # sys.path.append('C:\\Users\\Name\\PycharmProjects\\PEP22G05\\modul5')
# sys.path.append('C:\\Users\\Name\\PycharmProjects\\PEP22G05\\modul5')


import modul4.part1


#   print(my_functions)
print(my_functions.factorial(6))

print(type(random))
result = random.random()
print(result)
result = random.randint(1, 5)
print(result)


import time
result = time.time()
print(result)

time.sleep(10)

from time import sleep
print ('before sleep')
sleep(5)
print('after sleep')

my_imported_var == 'Local'
from my_functions import *
print(my_imported_var)


# import Package