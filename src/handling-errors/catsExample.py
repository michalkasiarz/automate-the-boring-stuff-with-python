# Catching errors - another example

print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That is a lot of cats!")

    elif int(numCats) >= 0:
        print("That is not that many cats.")
    else:
        print("You've entered wrong value, man!")
except ValueError:
    print("You did not enter a number.")
