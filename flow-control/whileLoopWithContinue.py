# While loop example with continue

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue    # it immediately goes to the beginning of the loop here
    print("Spam is " + str(spam) + ".")
