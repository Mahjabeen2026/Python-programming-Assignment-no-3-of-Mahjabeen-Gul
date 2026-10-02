

"""Part 2: Control Flow and Loops."""

# File: Contorl_Flow_Conditionals_and_loops.py
# Hands-on project: multiplication table using loops

num = int(input("Enter a number for table: "))

print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

