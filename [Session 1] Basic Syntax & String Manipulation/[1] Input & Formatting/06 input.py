name = input("What is your name?")

print(name)

print(f"Hello {name}") # preferred syntax
print("Hello " + name) # alternative syntax
print("Hello", name) # alternative syntax

# input() always returns a string
print(f"name is of type: {type(name)}")


city = input("What City do you live in?")

print(f"{city} is a cool place to live.")
