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

print(spam.index("Cattie"))     # the index of Cattie is now 6

# remove method
spam.remove("Howdy")    # removes Howdy
print(spam)

# sort method - ASCII-betical order, Uppercase char comes before lowercase
spam = [7, 4, 2, 64, 12, 5, 88, 5, 22, 1]
print(spam)
spam.sort()     # it returns sorted list
print(spam)

# reverse sorting
print(spam)
spam.sort(reverse=True)     # reverse sorting
print(spam)

# ASCII-betical order
spam = ["Red", "blue", "Alice", "Bob", "Blue", "al", "bob"]
print(spam)     # ['Red', 'blue', 'Alice', 'Bob', 'Blue', 'al', 'bob']
spam.sort()
# Uppercase names comes first in ASCII-betical order!
print(spam)     # ['Alice', 'Blue', 'Bob', 'Red', 'al', 'blue', 'bob']

# Alphabetical order
spam = ["z", "R", "s", "a", "H", "w", "J", "o", "c", "f"]
print(spam)
spam.sort(key=str.lower)       # it sorts as if everything is lowercase
print(spam)
