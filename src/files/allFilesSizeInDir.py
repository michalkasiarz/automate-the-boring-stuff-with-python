import os

# Finding the total size of all files in a folder

trainingDirectory = r"C:\Users\micha\Documents\Training"
totalSize = 0

for filename in os.listdir(trainingDirectory):
    filePath = os.path.join(trainingDirectory, filename)
    if os.path.isfile(filePath):
        totalSize = totalSize + os.path.getsize(filePath)
print("Total size of stuff in " + trainingDirectory + " is: " + str(totalSize) + " bytes.")
