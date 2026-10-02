

# File: Master Class\Dictionaries.py

# Dictionary - CRUD
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}
print("Original Dict:", student)

# Create / Add
student["grade"] = "A"
print("After Add:", student)

# Read
print("Student Name:", student["name"])

# Update
student["age"] = 21
print("After Update:", student)

# Delete
del student["course"]
print("After Delete:", student)