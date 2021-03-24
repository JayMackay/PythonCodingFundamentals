# File handling
# Create a file.

# Run the code swapping the commented out writes and compare the results.

months_file = open("months.txt", "x") # tells Python to create the file

for month in ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]:
    months_file.write(month) 
    #months_file.write(f"\n{month}")

months_file.close()
