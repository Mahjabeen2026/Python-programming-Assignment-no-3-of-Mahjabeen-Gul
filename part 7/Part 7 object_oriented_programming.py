

# Part 7: Object-Orient

# File: object_oriented_programming.py
# Part 7 - OOP Basics

# 1. Simple Class with Constructor, Methods, Objects
class Student:
    def __init__(self, name, age, grade):
        # Constructor - runs when object is created
        self.name = name
        self.age = age
        self.grade = grade

    def show_details(self):
        # Method
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    def is_passed(self):
        return self.grade != "F"

# Creating Objects
print("--- Creating Objects ---")
s1 = Student("Ali", 21, "A")
s2 = Student("Sara", 20, "B")

s1.show_details()
s2.show_details()

# 2. Encapsulation Example (private variable with __)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New Balance: {self.__balance}")

    def get_balance(self):
        # Getter method to access private data
        return self.__balance

print("\n--- Encapsulation ---")
acc = BankAccount("Ahmed", 1000)
acc.deposit(500)
print(f"Current Balance: {acc.get_balance()}")
# print(acc.__balance) # This will give error because it's private