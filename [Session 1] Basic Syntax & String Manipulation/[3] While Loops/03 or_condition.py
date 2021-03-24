# or condition

number = int(input("Enter a number smaller than 10: "))
	
if number == 1 or number == 3 or number == 5:
    print("You entered an ODD number")
else:
    print("You entered an EVEN number")

# What's missing from this program?

# Alternative that means we don't need or
if number in [1, 3, 5]:
    print("You entered an ODD number")
else:
    print("You entered an EVEN number")
