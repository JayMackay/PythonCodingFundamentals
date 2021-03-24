# https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
# https://www.binaryconvert.com/convert_signed_short.html

print(7)
print(~7)

print(-9)
print(~-9)

"""
In 16-bit two's complement binary, 7 is:
0000000000000111

Therefore the invert/complement of 7 is:
1111111111111000

Which, in 16-bit two's complement, is equivalent to:
-8

Short way of working out value:
~x = -x - 1

E.g.
x = 7
~x = -7 - 1
   = -8

y = -9
~y = -(-9) - 1
   = 9 - 1
   = 8
"""

"""
16-bit two's complement integer bit values:
-32,768 16384 8192 4096 2048 1024 512 256 128 64 32 16 8 4 2 1
"""
