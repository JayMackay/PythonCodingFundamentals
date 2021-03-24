def reverse_string(str):
    """Reverse the given string with slicing"""
    # start = 0, stop = len(str), hence range is whole string.
    # step = -1, hence go backwards through range.
    reversed_str = str[::-1]
    return reversed_str    # return the reversed string to the caller

str = "TechTalent Academy"

print(f"The original string is: {str}")
print(f"The reverse string is : {reverse_string(str)}") # call function
