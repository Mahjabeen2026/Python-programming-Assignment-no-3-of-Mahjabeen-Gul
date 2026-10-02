

# Part 10: Loops hands-on project

# Loops_hands_on_project.py - With Exception Handling

print("--- Loops Hands-on Project ---")

try:
    # For Loop
    print("\n1. For Loop:")
    for i in range(1, 6):
        print(f"Number: {i}")

    # While Loop with user input + exception
    print("\n2. While Loop - Countdown:")
    try:
        n = int(input("Enter number for countdown: "))
        while n > 0:
            print(n)
            n -= 1
    except ValueError:
        print("Error: Please enter a valid integer.")

    # Nested Loop
    print("\n3. Nested Loop - Pattern:")
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()

    # Loop through list with exception
    print("\n4. Loop through list:")
    courses = ["Python", "AI", "Web Dev"]
    try:
        for course in courses:
            print(course)
    except Exception as e:
        print(f"Error in loop: {e}")

except Exception as e:
    print(f"Main Error: {e}")

finally:
    print("\nProgram finished successfully with exception handling!")
    