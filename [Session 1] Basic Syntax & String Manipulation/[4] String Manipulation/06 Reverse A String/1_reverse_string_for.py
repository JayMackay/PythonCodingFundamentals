def reverse_string(str):
    """Reverse the given string with a for loop"""
    reversed_str = ""   # Declare an empty string to store the reversed string in
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str    # return the reversed string to the caller

str = "TechTalent Academy"

print(f"The original string is: {str}")
print(f"The reverse string is : {reverse_string(str)}") # call function
