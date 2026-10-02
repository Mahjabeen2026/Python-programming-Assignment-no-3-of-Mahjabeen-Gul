
# Part 5 Strings and file Handling


# File: Master Class\Strings.py
# Task: String operations

text = "Hello Python World"

print("Original:", text)
print("Length:", len(text))
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Slicing [0:5]:", text[0:5])
print("Slicing [6:]:", text[6:])

# Concatenation
first_name = "Ali"
last_name = "Ahmed"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Other useful methods
print("Replace:", text.replace("World", "Students"))
print("Split:", text.split())