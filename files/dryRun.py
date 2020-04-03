import os

os.chdir(r"C:\Users\micha\Documents\Training")

for filename in os.listdir():
    if filename.endswith(".txt"):
        # os.unlink(filename)
        print(filename)
