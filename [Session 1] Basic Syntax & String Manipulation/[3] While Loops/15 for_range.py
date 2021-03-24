# for loop with range statement

# Notice that the end value is not included.
for number in range(1, 6):
    print(number)

print("----------")

# When no start is given, 0 is used.
for value in range(9):
    print(value)

print("----------")

# range() can include a step.
for item in range(3, 27, 4):
    print(item)
