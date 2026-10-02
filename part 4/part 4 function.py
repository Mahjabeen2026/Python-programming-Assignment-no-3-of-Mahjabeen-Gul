

# Part 4-Function and Modules

# File: Master Class\Funtions.py
# Task: Create reusable functions with parameters and return values

# Simple function with parameter
def greet(name):
    return f"Hello, {name}!"

# Function with return value
def add(a, b):
    return a + b

# Calling functions
print(greet("Ali"))
print("Sum is:", add(10, 20))

def multiply(x, y):
    result = x * y
    return result

print("Multiply:", multiply(5, 6))