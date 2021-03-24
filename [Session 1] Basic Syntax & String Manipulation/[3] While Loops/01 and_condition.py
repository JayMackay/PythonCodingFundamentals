# and condition

age = int(input("What is your age? "))

if age > 17 and age < 60:
    print("You can learn to drive")
else:
    print("You cannot learn to drive")

# Many programming languages don't have the following syntax
if 17 < age < 60:
    print("You can learn to drive")
else:
    print("You cannot learn to drive")
