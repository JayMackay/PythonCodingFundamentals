def user_numbers():
    """Another function example.
       The user is asked to enter a name, and 4 separate numbers and displays 
       their sum.
       It stores the 4 numbers in local variables num_1 ... num_4
    """

    #Get the user's name 
    user = input("Please enter your name: ")

    # Ask the user for their numbers and convert to integer
    num_1 = int(input("Enter your first number: "))
    num_2 = int(input("Enter your second number: "))
    num_3 = int(input("Enter your third number: "))
    num_4 = int(input("Enter your fourth number: "))

    # Add them up
    sum_num = num_1 + num_2 + num_3 + num_4

    # Display the sum
    print("The sum of these numbers is " + str(sum_num))

    # End of function


user_numbers()
