

# Part 5: String and File Handling

# File: File_Handling.py
# Task: Read/write text files (students.txt, data.txt)

# Write to students.txt
with open("students.txt", "w") as file:
    file.write("Ali - A+\n")
    file.write("Sara - A\n")
    file.write("Ahmed - B\n")

print("students.txt created successfully")

# Read from students.txt
print("\nReading students.txt:")
with open("students.txt", "r") as file:
    content = file.read()
    print(content)

# Write to data.txt
with open("data.txt", "w") as file:
    file.write("This is data file.\n")
    file.write("Python File Handling Example.")

print("\ndata.txt created successfully")

# Read data.txt
print("\nReading data.txt:")
with open("data.txt", "r") as file:
    print(file.read())

# Append mode
with open("students.txt", "a") as file:
    file.write("Zain - A+\n")

print("\nAfter appending, new students.txt:")
with open("students.txt", "r") as file:
    print(file.read())