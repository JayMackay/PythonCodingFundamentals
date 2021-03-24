# List all files in a directory

import os

DIR = "Some Files"

print(f"Directory listing of {DIR}:")

for file in os.listdir(f"{DIR}"):
    print(f"{file}")
