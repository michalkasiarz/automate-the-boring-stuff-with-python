import shutil

# Working on files and folders using shutil module

# Copying file to another folder
shutil.copy(r"C:\Users\micha\Documents\Training\HelloTwo.txt", r"C:\Users\micha\Documents\Training\Folder1")

# Copying file to another folder with a new name
shutil.copy(r"C:\Users\micha\Documents\Training\HelloTwo.txt", r"C:\Users\micha\Documents\Training\Folder1\new_spam.txt")

# Copying file to another folder with a new name
shutil.copy(r"C:\Users\micha\Documents\Training\HelloTwo.txt", r"C:\Users\micha\Documents\Training\Folder1\new_spam.txt")

# Copying folder with all the stuff (backup copying)
shutil.copytree(r"C:\Users\micha\Documents\Training\Folder1", r"C:\Users\micha\Documents\Training\Folder1_backup")

# moving file to a new location
shutil.move(r"C:\Users\micha\Documents\Training\Folder1\new_spam.txt", r"C:\Users\micha\Documents\Training")

# renaming file - in fact, moving file to a new location with a new name
shutil.move(r"C:\Users\micha\Documents\Training\Folder1\new_spam.txt", r"C:\Users\micha\Documents\Training\Folder1\old_spam.txt")
