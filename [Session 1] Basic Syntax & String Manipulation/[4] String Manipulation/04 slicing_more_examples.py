# Python slicing - more examples

# Slice syntax: start:stop:step

#       01234567891111111
#                 0123456
text = "some example text"
print(text)

print(f"a. {text[3:15]}")    # first:last+1
print(f"b. {text[:15]}")     # start:last+1
print(f"c. {text[3:]}")      # first:end
print(f"d. {text[3:15:2]}")  # first:last+1:step(2)
print(f"e. {text[3::3]}")    # first:end:step(3)
print(f"f. {text[:15:2]}")   # start:last+1:step(2)
print(f"g. {text[::3]}")     # start:end:step(3)

print(f"h. {text[14:2:-1]}") # first:last-1:step(backwards)
print(f"i. {text[::-3]}")    # start:end:step(3 backwards)

print()
