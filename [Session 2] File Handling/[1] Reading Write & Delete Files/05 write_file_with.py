# File handling
# Write using the with statement

with open("days_of_week.txt", "w") as days_file:

    for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
        days_file.write(f"{weekday}\n")


# Notice: no need to close - done automatically by with statement.
