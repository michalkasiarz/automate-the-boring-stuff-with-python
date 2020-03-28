# Introduction to dictionaries
# Dictionaries are unordered

myCat = {"size": "fat", "color": "gray", "disposition": "lazy"}
for key in myCat.keys():
    print(key)

print()

for value in myCat.values():
    print(value)

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

print()

# if in dict
isInDict = 5211 in my_dict
print(isInDict)     # True
print()
isInDict = 1111 in my_dict
print(isInDict)     # False

print()

# items() method
print("my_dict items: " + str(list(my_dict.items())))

print()

# keys() method
print("my_dict keys: " + str(list(my_dict.keys())))

print()

# values() method
print("my_dict values: " + str(list(my_dict.values())))

print()


