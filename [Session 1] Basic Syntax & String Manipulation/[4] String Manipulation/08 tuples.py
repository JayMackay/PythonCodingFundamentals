# Python tuple

"""Python has four built in types for collections of data: 
       list, tuple, set and dictionary.
   A tuple is ordered (by index) and immutable (unchangeable).
   A tuple is enclosed in round brackets.
   The first index is 0.
   Duplicates are allowed.
"""

fruits = ("apple", "orange", "cherry", "banana")

print(fruits)

# A tuple with only one item:
cars = ("Ford",)
# Notice the comma
print(f"cars: {type(cars)}")

# The following is not a tuple
not_a_tuple = ("BMW")
print(f"not_a_tuple: {type(not_a_tuple)}")

# Size of tuple - use len()
print(f"Length of fruits tuple is {len(fruits)}")

# Elements in a tuple are indexed from zero
print(fruits[0]) 

# Slicing can be used
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])

# Error - immutable
fruits[1] = "pear"
print(fruits)
# After first run, comment above out and run again to see rest.

# Concatenation
first = (1, 2, 3, 4)
second = (5, 6, 7, 8)
concat = first + second
print(f"concat: {concat}")

# Repetition
repeated_tuple = ("a",) * 4
print(f"repeated_tuple: {repeated_tuple}")

# Membership
if 7 in second:
    print("The number 7 is in the tuple second.")

# min and max
print(f"Max of fruits is: {max(fruits)}")
print(f"Min of fruits is: {min(fruits)}")

# Convert list to tuple
evens_list = [2, 4, 6, 8]
evens_tuple = tuple(evens_list)
print(f"evens_tuple: {evens_tuple}")
