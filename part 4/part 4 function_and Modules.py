
# Part 4: Functions and Modules
# File: Functions_and_Modules.py
# Final file with all concepts

# 1. Default argument
def greet_user(name, city="Lahore"):
    return f"Hello {name} from {city}"

print(greet_user("Ali")) 
print(greet_user("Sara", "Karachi")) # default override

# 2. *args - Multiple arguments
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("\n*args example:")
print("Sum:", add_all(1, 2, 3))
print("Sum:", add_all(10, 20, 30, 40))

# 3. **kwargs - Key-Value arguments
def show_student(**kwargs):
    print("\n**kwargs example:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

show_student(name="Ahmed", age=21, grade="A")

# 4. Import custom module use
import MyModule
print("\nCustom module use:")
print(MyModule.say_hello("Final Student"))