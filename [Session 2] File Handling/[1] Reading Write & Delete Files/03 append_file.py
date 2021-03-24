# File handling
# Append to a file.

# Run the code swapping the commented out writes and compare the results.

days_file = open("days_of_week.txt", "a") # tells Python append only

for weekend_day in ["Sat", "Sun"]:
    days_file.write(weekend_day) 
    #days_file.write(f"\n{weekend_day}")

days_file.close()


# Notice the basic pattern:
#   open file
#   process
#   close file
