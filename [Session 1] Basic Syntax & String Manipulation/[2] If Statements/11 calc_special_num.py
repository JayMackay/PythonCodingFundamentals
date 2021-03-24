def calc_special_num():
    """Another function example.
       Also shows converting string to integer.
    """
    user = input("Please enter your name: ")

    age = int(input("Enter your age: ")) # string from input() must be converted to int
    number = int(input("Enter a number: "))
    day_of_month = int(input("Enter the day of the month today: "))

    special = number * age + day_of_month

    print(f"Hello {user}. Your special number is {special}.")


calc_special_num()
