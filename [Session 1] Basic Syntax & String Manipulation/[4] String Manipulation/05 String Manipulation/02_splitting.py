# Specify the separator

# Split using single pipe

elements = "A|simple|sentence|with|pipes|instead|of|spaces.".split("|")

# Works for a nice string
print(elements)
print(f"The number of words is: {len(elements)}")

print("----------") # separate output so we can work out what's going on easier

elements = "||||This||example||||||includes|many|||pipes|||".split("|")

# Now not so good
print(elements)
print(f"The number of words is: {len(elements)}")

print("----------") # separate output so we can see what's going on easier

elements = "    This  example      includes many   spaces   ".split()

# Above split defaulted to using whitespace. Again result is now not good.
print(elements)
print(f"The number of words is: {len(elements)}")
