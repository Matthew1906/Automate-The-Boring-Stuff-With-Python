# standard library

import random, sys, math, os

print(random.randint(1,20))

# we can also import the functions instantly from

from random import *

print(randint(1,22))

# sys library to exit

import sys
print("jello")
sys.exit() #instantly exits
print("hello")

# import other libraries using pip functions

import pandas

# global and local scopes

eggs = 100
def printEggs(num):
    # eggs = num
    print(eggs)

printEggs(10)
