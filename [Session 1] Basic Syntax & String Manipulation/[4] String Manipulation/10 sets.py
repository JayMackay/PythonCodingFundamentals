# Python set

"""Python has four built in types for collections of data: 
       list, tuple, set and dictionary.
   A set is unordered.
   The items within a set cannot be changed, but new items can be added.
   A set is enclosed in curly brackets.
   Each value must be unique in the set (no duplicates).
"""

# Unordered
veggies = {"carrot", "cauliflower", "broccoli", "potato"}
print(veggies)

# Size of set - use len()
print(f"Length of set veggies is {len(veggies)}")

# Access items
for veg in veggies:
    print(veg)

# Add a new item
veggies.add("leek")
print(veggies)

# Add several items - from another set
more_veggies = {"pea", "sweetcorn"}

veggies.update(more_veggies)

print(veggies)

# Add several items - from an iterable (e.g. list)
more_veg_list = ["beetroot", "cabbage"]

veggies.update(more_veg_list)

print(veggies)

# Combine two sets to produce a third - use union
fruits = {"apple", "orange", "cherry", "banana"}

fruit_and_veg = veggies.union(fruits)

print(fruit_and_veg)

# There are many other set methods
