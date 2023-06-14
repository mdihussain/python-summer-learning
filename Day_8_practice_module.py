#MD Hussain
#Day 8
#Modules

#Math_operations.py

import math_operations

result = math_operations.add(10, 5)
print(result)

result = math_operations.subtract(10, 5)
print(result)

#to call wihtout module name prefix

from math_operations import add

result = add (46, 6)
print(result)

#to import multiple specific functions

from math_operations import add, subtract

result1 = add(4, 9)
result2 = subtract(4, 9)

print(result1)
print(result2)

#to rename a function imported from a module

from math_operations import add as addition

result = addition(4, 5)
print(result)

#example

import math_operations as np

result4 = np.add(4, 5)
