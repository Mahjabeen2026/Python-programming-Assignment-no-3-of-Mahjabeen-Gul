

# Part 3: Data Structures


# File: Master Class\Lists.py - Lists, Tuples, Sets

# 1. Lists - CRUD
fruits = ["apple", "banana", "mango"]
print("Original List:", fruits)

# Create - Add
fruits.append("orange")
print("After Append:", fruits)

# Read
print("First fruit:", fruits[0])

# Update
fruits[1] = "grapes"
print("After Update:", fruits)

# Delete
fruits.remove("apple")
print("After Delete:", fruits)

# 2. Tuple (Immutable)
my_tuple = (10, 20, 30)
print("\nTuple:", my_tuple)
print("Tuple first value:", my_tuple[0])

# 3. Set (No duplicate values)
my_set = {1, 2, 2, 3, 4}
print("\nSet (duplicate remove):", my_set)
my_set.add(5)
print("After Add in Set:", my_set)

