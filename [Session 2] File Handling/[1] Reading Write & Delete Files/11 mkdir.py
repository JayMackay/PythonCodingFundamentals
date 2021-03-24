# File handling
# Create a directory.

# Try running this twice.

import os

TEMP_DIR_01 = "temp_folder_01"

os.mkdir(TEMP_DIR_01)

print(f"Is directory in cwd? {os.path.exists(TEMP_DIR_01)}")

TEMP_DIR_02 = "Some Files/tmp_folder_02"

os.mkdir(TEMP_DIR_02)

print(f"Is directory Some Files? {os.path.exists(TEMP_DIR_02)}")
