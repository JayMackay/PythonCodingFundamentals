# AND with two Boolean values entered by user.
# Combines various things we've learned: function, loop and if.
# Also, demonstrates how to force user to a enter valid value.

def get_user_input_boolean(prompt_str):

    user_input = "ZZZ"

    # The loop only allows the user to enter the text "True" or "False"
    while user_input != "True" and user_input != "False":
        user_input = input(prompt_str)

    # Convert string input to Boolean equivalent
    if user_input == "True":
        user_input_boolean = True
    else:
        user_input_boolean = False

    return user_input_boolean


a = get_user_input_boolean("Enter first True or False ")

b = get_user_input_boolean("Enter second True or False ")

# A reminder of a non-f-string print statement. Uses concatenation instead.
print (str(a) + " AND " + str(b) + " is...")

print(a and b)
