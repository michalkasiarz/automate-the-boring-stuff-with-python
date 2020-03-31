import os

# using os module

path = os.path.join("folder1", "folder2", "folder3", "folder3", "folder4", "file.exe")
print(path)     # folder1\folder2\folder3\folder3\folder4\file.exe

trainingFile = r"C:\\Temp\\file.txt"
trainingDirectory = r"C:\\Temp"

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

# gives last directory from a path
print("Last directory: " + str(os.path.dirname(r"C:\\folder1\\folder2\\file1.png")))    # Last directory: C:\\folder1\\folder2

# pulls out the last part after the last set of slashes
print("Base name: " + str(os.path.basename(r"C:\\folder1\\folder2\\file1.png")))        # file1.png

# checking if given path exists
print("Path exists: " + str(os.path.exists(r"C:\\file.doc")))                           # False
print("Path exists: " + str(os.path.exists(r"C:\\Program Files\\")))                    # True

# checking if given file exists
print("File exists: " + str(os.path.isfile(r"C:\\somefile.txt")))                      # False
print("File exists: " + str(os.path.isfile(trainingFile)))                             # True

# checking if given directory exists
print("Directory exists? " + str(os.path.isdir(trainingDirectory)))                     # True
print("Directory exists? " + str(os.path.isdir(r"C:\\SecretFolder\\")))                 # False

# getting size of an file in bytes
print("Sizes in bytes of " + str(os.path.basename(trainingFile)) + " is: " + str(os.path.getsize(trainingFile)))    # 12

# listing the inside of a directory
print("You are in: " + str(os.getcwd()) + "\n\n" + str(os.listdir(os.getcwd())))
