import os
import shutil
from os.path import join

# walking the directory tree
for folderName, subfolders, filenames in os.walk(r"C:\Users\micha\Documents\Training"):
    print("The folder is " + folderName + ".")
    print("The subfolders in " + folderName + " are: " + str(subfolders) + ".")
    print("The filenames in " + folderName + " are: " + str(filenames) + ".")
    print()

    # looping through subfolders
    for subfolder in subfolders:
        # try-except block
        if "Folder2" in subfolder:
            try:
                # if folder is named "Folder2", then try to remove it
                print("Removing directory: " + subfolder)
                os.rmdir(join(folderName, subfolder))
            except FileNotFoundError:
                # if file not found, print info
                print("FileNotFound")
            except OSError:
                # if folder is not empty, print info
                print("Folder not empty, Sir!")

    # looping through filenames
    for file in filenames:
        # if a file has BMP extension, then make a copy with .backup extension
        if file.endswith(".bmp"):
            shutil.copy(join(folderName, file), join(folderName, file + ".backup"))
