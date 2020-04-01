import os

# walking the directory tree

for folderName, subfolders, filenames in os.walk(r"C:\Users\micha\Documents\Training"):
    print("The folder is " + folderName + ".")
    print("The subfolders in " + folderName + " are: " + str(subfolders) + ".")
    print("The filenames in " + folderName + " are: " + str(filenames) + ".")
    print()
