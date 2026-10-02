

# Part 5: strings and file handling

# File: working_with_String.py

name = input("Enter your name: ")
city = input("Enter your city: ")

# String operations on user input
print("\n--- String Operations ---")
print(f"Name Length: {len(name)}")
print(f"Upper Case: {name.upper()}")
print(f"Lower Case: {name.lower()}")
print(f"First 3 letters: {name[0:3]}")
print(f"Welcome message: " + "Hello " + name + " from " + city)

# Formatted string
message = f"My name is {name} and I live in {city}."
print("\nFormatted String:", message)

