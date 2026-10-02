

# Task 1 Python Basic Input/output


# Part 1 – Python Basics & Input/Output


# 1. Print messages using print()
print("Welcome to Python Calculator")
print("----------------------------")

# 2. Read input from the user
name = input("Enter your name: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 3. Use basic arithmetic operators (+, -, *, /)
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print(f"\nHello {name}!")
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")

# 4. Simple calculator program
print("\n--- Simple Calculator ---")
op = input("Enter operator (+, -, *, /): ")
a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))

if op == '+':
    print(f"Result: {a + b}")
elif op == '-':
    print(f"Result: {a - b}")
elif op == '*':
    print(f"Result: {a * b}")
elif op == '/':
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid operator!")


