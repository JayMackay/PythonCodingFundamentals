# File handling
# Rename a file

# os.rename(path to old filename, path to new filename)

import os

DIR = "Some Files"
OLD_FILENAME = "sixth track"
NEW_FILENAME = "6 track"
EXTENSION = "txt"

os.rename(f"{DIR}/{OLD_FILENAME}.{EXTENSION}", f"{DIR}/{NEW_FILENAME}.{EXTENSION}")
