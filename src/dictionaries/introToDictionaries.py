# Introduction to dictionaries
# Dictionaries are unordered

myCat = {"size": "fat", "color": "gray", "disposition": "lazy"}
for item in myCat.keys():
    print(item)

print()

for item in myCat.values():
    print(item)

print()

for item in myCat.items():
    print(item)

print()

my_list = [1, 2, 3, 4]
your_list = [2, 1, 4, 3]
print("List comparison: " + str(my_list == your_list))     # False, cause the order is different,
# what matters for lists

print()

# comparing dictionaries

my_dict = {231: "Hello", 5211: "Hi", 1: "Good morning"}
your_dict = {5211: "Hi", 231: "Hello", 1: "Good morning"}
print("Dict comparison: " + str(my_dict == your_dict))
# gives True, because the order of the items doesn't matter for dictionaries,
# they are unordered


