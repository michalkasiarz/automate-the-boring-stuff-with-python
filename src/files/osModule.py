import os

# using os module

path = os.path.join("folder1", "folder2", "folder3", "folder3", "folder4", "file.exe")
print(path)     # folder1\folder2\folder3\folder3\folder4\file.exe

print()

# printing current path
print("Current directory: " + os.getcwd())

# changing directory
print("Changing directory...")
os.chdir(r"c:\\")

# printing current path
print("Current directory: " + os.getcwd())

# printing absolute path based on current directory
print("Absolute path: " + os.path.abspath("file"))

# checking if a given path is an absolute path
print("Is absolute path? " + str(os.path.isabs(r"..\\..\\folder1\\folder2\\file1.png")))     # False
print("Is absolute path? " + str(os.path.isabs(r"C:\\folder1\\folder2\\file1.png")))         # True

# gives relative path between two
print("Relative path: " + str(os.path.relpath(r"..\\..\\folder1\\folder2\\file1.png", r"c:\\folder1"))) # Relative path: folder2\file1.png


