# introduction to lists

a = ["cat", "bat", "rat", "elephant"]
print(a)

print()

spam = ["cat", "bat", "rat", "elephant"]
print(spam[0])  # prints the first item in the list - cat
print(spam[-1])     # prints the last element in the list - elephant

print()

# lists of lists
spam = [["cat", "bat"], [10, 20, 30, 40, 50], ["round", "random", "goes"]]

print(spam[1][2])  # prints 30
print(spam[0][1])   # prints bat
print(spam[2][2])   # prints goes

print()

# cat goes round
print(spam[0][0], end="     ")
print(spam[2][2], end="     ")
print(spam[2][0])

print()

spam = ["cat", "bat", "rat", "eagle", "hamster", "rabbit"]
# slicing lists
print(spam[2:4])    # rat, eagle

#   assigning new values

print(spam)
spam[1] = "NEW VALUE, GUYS!"
print(spam)
