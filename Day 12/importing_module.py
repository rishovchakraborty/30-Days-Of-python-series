# import 02_math_utils # error in names

# ❌ cannot start with a digit

# ❌ cannot contain special characters (except _)

# ✅ must start with a letter or _


import math_utils 

print(math_utils.mul(3,2))

# Import specific items 

from math_utils import PI as p  # alising
# print(PI)  #3.14
print(p)
print(math_utils.mul(3,2)) # error


