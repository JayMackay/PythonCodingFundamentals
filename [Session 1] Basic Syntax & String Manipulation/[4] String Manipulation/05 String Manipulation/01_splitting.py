#https://realpython.com/python-string-split-concatenate-join/

# Strings are immutable.
# Immutable means they cannot be changed.
# Strings are also objects.
# Objects have methods that allow you to work with them.
# split() is one such method - it returns a list.

# default is to use whitespace

elements = "A simple sentence with a few words.".split()

print(elements)
print(f"The number of words is: {len(elements)}")
