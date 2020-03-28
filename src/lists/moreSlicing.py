# More lists slicing

spam = ["dog", "cat", "rabbit", "parrot", "eagle", "horse", "mouse", "hobbit"]
print(spam)

print()

print(spam[:2])     # prints all the values up to but not including with index 2
print(spam[1:])     # prints all the values starting from the one with the 1 index

# returning the size of a list
print(len(spam))

# deleting rabbit :(
del spam[2]     # deleting value with index 2
print(spam)     # no rabbit there!

# returning the size of a list again
print(len(spam))

# adding lists
print(spam + spam)
print(spam + ["yet another pet!"])

# checking if value is in spam
print("python" in spam)     # False, no python there!
spam.append("python")       # adding python to the spam list
print("python" in spam)     # True
