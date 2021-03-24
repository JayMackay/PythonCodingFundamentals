# File handling
# Write to a file.

# Run the code swapping the commented out writes and compare the results.

weekdays_file = open("days_of_week.txt", "w") # tells Python write only

for weekday in ["Mon", "Tue", "Wed", "Thu", "Fri"]:
    weekdays_file.write(weekday) 
    #weekdays_file.write(f"{weekday}\n")

weekdays_file.close()


# Notice the basic pattern again:
#   open file
#   process
#   close file
