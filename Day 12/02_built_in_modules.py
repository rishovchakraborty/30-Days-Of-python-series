# math	        Mathematical operations
# random	        Random numbers
# datetime       	Date & time
# os	            OS operations
# sys         	Python runtime info

from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2


import sys

print(sys.path)


from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive


# mypackage/   FOLDER BECOMES PACKAGE
# │
# ├── __init__.py
# ├── file1.py
# ├── file2.py
