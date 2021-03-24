# Python dict

"""Python has four built in types for collections of data: 
       list, tuple, set and dictionary.
   A dictionary contains key-value pairs.
   A dictionary is ordered (by insertion) and mutable (changeable).
   A dictionary is enclosed in curly brackets.
   Each key must be unique in the dictionary (no duplicates).
"""

# Insertion order
mary = {"name": "Mary", "age": 27, "location": "Birmingham"}
dave = {"age": 24, "location": "Manchester", "name": "Dave"}
print(mary)
print(dave)

# Access the value associated with a key
print(f"Mary's location: {mary['location']}")

# Size of dictionary - use len()
print(f"Length of dictionary dave is {len(dave)}")

# Mutable
dave["location"] = "Glasgow"
print(dave)

# Get a list of keys
print(dave.keys())

for k in dave.keys():
    print(k)

# Get a list of values
print(f"{mary.values()}")

for v in mary.values():
    print(v)

# Get a list of tuples of key-value
print(f"{dave.items()}")

for i in dave.items():
    print(i)

for k, v in dave.items():
    print(f"{k}: {v}")

# Check if key is present
if "age" in mary:
    print("Key age is present in dictionary mary.")
