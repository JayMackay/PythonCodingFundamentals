# File handling
# Read using the with statement

with open("modules.txt", "r") as modules_file:
    # Read next line
    line = modules_file.readline()

    # while line is not empty, process it
    while line:
        print(f">{line.rstrip()}<")
        line = modules_file.readline() 


# Notice: no need to close - done automatically by with statement.
