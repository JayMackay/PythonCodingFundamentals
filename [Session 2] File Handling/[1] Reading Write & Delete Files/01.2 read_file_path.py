# File handling
# Read a file.

# In this one, the file is not in the same directory as the code.

interview_file = open("Some Files/interview_coding.txt", "r")

line = interview_file.readline()

while line:
    print(f"{line.rstrip()}")
    line = interview_file.readline() 

interview_file.close()


# Notice the basic pattern:
#   open file
#   process
#   close file
