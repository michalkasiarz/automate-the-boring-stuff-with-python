# for loop with lists

# printing values from a list
for i in [0, 1, 2, 3, 4]:
    print(i)


print()


# printing values from a list with a range
for i in range(0, 5):
    print(i)

print()

# range with step 2

myListWithStep2 = list(range(0, 10, 2))
print(myListWithStep2)
myListWithStep2 = myListWithStep2 + ["cat", "dog", "hot-dog"]
print(myListWithStep2)

print()

for i in range(len(myListWithStep2)):
    print("List value: " + str(myListWithStep2[i]) + ".")
