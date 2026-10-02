

# Part 2: Control Flow and Loops


# File: Master Class\Loops.py

# 1. for loop
print("For Loop:")
for i in range(1, 6):
    print(i)

# 2. while loop
print("\nWhile Loop:")
x = 1
while x <= 5:
    print(x)
    x += 1

# 3. break & continue
print("\nBreak & Continue:")
for i in range(1, 10):
    if i == 5:
        continue 
    if i == 8:
        break 
    print(i)

# 4. Nested loop example (star pattern)
print("\nNested Loop Pattern:")
for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
