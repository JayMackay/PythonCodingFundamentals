def reverse_string(str):
    """Reverse the given string with a while loop"""
    reversed_str = ""   # Declare an empty string to store the reversed string in
    count = 0
    while count < len(str):
        reversed_str = str[count] + reversed_str
        count += 1
    return reversed_str    # return the reversed string to the caller

str = "TechTalent Academy"

print(f"The original string is: {str}")
print(f"The reverse string is : {reverse_string(str)}") # call function
