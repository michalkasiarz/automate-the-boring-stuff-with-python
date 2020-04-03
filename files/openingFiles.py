import os

# opening files

helloFile = open(r"C:\Users\micha\Documents\Training\Hello.txt")
content = helloFile.read()

# printing file content to the console
print(content)

# closing the file
helloFile.close()

# readlines() method - returns a list of Strings

helloFile = open(r"C:\Users\micha\Documents\Training\Hello.txt")
print(helloFile.readlines())
helloFile.close()

# opening file in write mode
helloFile = open(r"C:\Users\micha\Documents\Training\HelloTwo.txt", "w")
helloFile.write("Hi, man!\n")
helloFile.write("Hi, man!\n")
helloFile.write("Hi, man!\n")
helloFile.close()

# another example with write mode
baconFile = open("bacon.txt", "w")
print("Saving data into " + str(os.getcwd()))
baconFile.write("Bacon is not a vegetable.")
baconFile.close()

# append mode
baconFile = open("bacon.txt", "a")
print("Saving data into " + str(os.getcwd()))
baconFile.write("Bacon is delicious!")
baconFile.close()

