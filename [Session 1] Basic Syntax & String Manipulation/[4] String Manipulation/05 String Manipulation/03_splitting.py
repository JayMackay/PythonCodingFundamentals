# Specify the separator

# Split using single comma
fruits = "Apple,Orange,Pear,Banana,Mango".split(",")

print(f"List of fruits: {fruits}")

for fruit in fruits:
    print(fruit)

print("----------") # separate output so we can see what's going on easier

# Split using comma followed by space
colours = "Red, Orange, Green, Blue, Indigo, Violet".split(", ")

print(f"List of colours: {colours}")

for colour in colours:
    print(colour)
