# List methods

spam = ["Hello", "Hi", "Howdy", "Eyes"]
print(spam.index("Howdy"))     # returns the index with that value - 2

#   print(spam.index("Go, Ranger!"))    # ValueError will be raised here

# append adds an element to the END of the list
spam.append("Hi")   # adding an element with the same value - Hi

print(spam)

print(spam.index("Hi"))     # in case of doubled values,
# will return index of the first found - 1

# insert method on a list adds an element on any index you want
# everything else is bumped up
spam.insert(2, "Chicken")
print(spam)

spam.insert(20, "Cattie")   # in case the index is too high,
# it goes to the end of the list
print(spam)

print(spam.index("Cattie")) # the index of Cattie is now 6

