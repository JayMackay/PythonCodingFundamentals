"""You may ask how you can check whether the user entered a valid digit.
   The following are suggestions.
"""

import sys

def display_menu():
    print("1 - All Running Trainers")
    print("2 - All Classic Trainers")
    print("3 - All Boots and Shoes")


def validate_menu_option1(menu_option):
    # Check that what the user entered can be cast to int
    if menu_option.isdigit():
        menu_option = int(menu_option)
    else:
        menu_option = None

    return menu_option


def validate_menu_option2(menu_option):
    # Check that what the user entered can be cast to int
    if menu_option >= "0" and menu_option <= "9":
        menu_option = int(menu_option)
    else:
        menu_option = None

    return menu_option


display_menu()

menu_option = input("Select an option 1, 2 or 3: ")
menu_option = validate_menu_option1(menu_option)

if menu_option == None:
    print("You did not enter a digit")
    sys.exit()

if menu_option == 1:
    print("These are all the Running Trainers")
elif menu_option == 2:
    print("These are all the Classics")
elif menu_option == 3:
    print("These are all the Boots and Shoes")
else:
    print("You didn't choose the correct option")
