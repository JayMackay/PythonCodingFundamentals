# Recursion is when a function calls itself.
# There must be a stopping condition or the calls will go on forever, leading to
# a stack overflow and the program crashing.

def reverse_string(str):
    """Reverse the given string with recursion"""
    if len(str) <= 1: # stopping condition for recursion
        return str
    else:
        return reverse_string(str[1:]) + str[0] # recursive call

str = "Academy"

print(f"The original string is: {str}")
print(f"The reverse string is : {reverse_string(str)}") # call function
