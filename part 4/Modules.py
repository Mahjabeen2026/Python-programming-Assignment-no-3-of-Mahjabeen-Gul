
# Part 4: Functions and Modules

# File: Modules.py
# Task: Import and use custom modules

import MyModule
from MyModule import square, pi

# Using MyModule
print(MyModule.say_hello("Ahmed"))
print("Square of 5 is:", MyModule.square(5))
print("Is 10 Even?", MyModule.is_even(10))

# Using directly imported functions
print("\nDirect import:")
print("Square of 6:", square(6))
print("Value of pi:", pi)

# Built-in module example
import math
print("\nUsing math module:")
print("sqrt of 16:", math.sqrt(16))