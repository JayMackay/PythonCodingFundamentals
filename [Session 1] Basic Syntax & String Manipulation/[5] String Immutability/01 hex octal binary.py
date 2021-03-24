z = 10
y = 0xA # hexadecimal
x = 0o12 # octal
w = 0b1010 # binary

print(z)
print(y)
print(x)
print(w)

print("----------")
print("Without prefix")

print(f"{y:x}")
print(f"{y:X}")
print(f"{x:o}")
print(f"{w:b}")

print("----------")
print("With prefix")

print(f"{hex(y)}")
print(f"{oct(x)}")
print(f"{bin(w)}")

# See: https://docs.python.org/3/library/functions.html#hex
# for various formatting options.
