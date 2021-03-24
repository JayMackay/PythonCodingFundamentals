# File handling
# Read a file.

# Run the code with and without the rstrip() line commented out.

# file_obj = open(filename, mode)

modules_file = open("modules.txt", "r") # tells Python read only

# Read next line
line = modules_file.readline()

# While line is not empty, print it out
# (Blank lines actually contain one invisible end of line character)
while line:
    print(f">{line}<")
    #print(f">{line.rstrip()}<")
    line = modules_file.readline() 

modules_file.close()


# Notice the basic pattern:
#   open file
#   process
#   close file
