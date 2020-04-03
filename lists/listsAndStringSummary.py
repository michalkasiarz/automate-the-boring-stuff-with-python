# Lists and Strings similarities

import copy

# ['H', 'e', 'l', 'l', 'o', ',', ' ', 'm', 'a', 'n', '!']
print(list("Hello, man!"))

print()

for i in "Hello!":
    print(i)

# Strings are immutable!

a = "Cat"
print(a)
# a[0] = "c"  # TypeError here!

spam = 42
cheese = spam  # i.e. cheese = 42, because spam is 42 now
print(cheese)

print()

# reference type
spam = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(spam)
cheese = spam  # creates another reference to a list object
cheese[1] = "NEW VALUE"
print("Cheese: " + str(cheese))  # ['A', 'NEW VALUE', 'C', 'D', 'E', 'F', 'G', 'H']
print("Spam: " + str(spam))  # that is also changed: # ['A', 'NEW VALUE', 'C', 'D', 'E', 'F', 'G', 'H']

print()

# copy module
spam = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(spam)
cheese = copy.deepcopy(spam)  # creates new object
cheese[1] = "NEW VALUE"
print("Cheese: " + str(cheese))
print("Spam: " + str(spam))

# code formatting

spam = ["apples",
        "oranges",
        "bananas",
        "cats"]

#   Four score and seven and something more and more! Remember! That is is still one line!
print("Four score and seven" + \
      " and something more" + \
      " and more!" + \
      " Remember!" + \
      " That is is still one line!")
