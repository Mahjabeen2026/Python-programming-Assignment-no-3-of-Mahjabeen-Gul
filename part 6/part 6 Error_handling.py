

# Part 6: Exception and Error Handling
#file : Error_Handling.py


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter numbers only!")
finally:
    print("Finally block executed.")
