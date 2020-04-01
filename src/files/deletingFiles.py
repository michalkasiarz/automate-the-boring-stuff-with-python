import os
import shutil

# Deleting files
# You can deleting file in 3 ways

path = r"C:\Users\micha\Documents\Training"

# os.rmdir will delete (only) an empty folder
try:
    os.rmdir(r"C:\Users\micha\Documents\Training")
    print("Folder deleted")
except OSError:
    print("OSError: Folder not empty")

try:
    os.rmdir(r"C:\Users\micha\Documents\Training\Folder1\to_delete")
    print("Folder deleted")
except OSError:
    print("OSError: Folder not empty")

# os.unlink will delete a single file

# shutil.rmtree() deletes a folder and its entire contents

shutil.rmtree(r"C:\Users\micha\Documents\Training\Folder1\folder_with_content")


