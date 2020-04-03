import shelve

# using shelve module

shelfFile = shelve.open("Mydata")
shelfFile["dogs"] = ["Rex", "Fox", "Dog", "Spook", "Fatsy"]
shelfFile.close()

shelfFile = shelve.open("Mydata")
print(shelfFile["dogs"])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
