#   Introduction to data structure

def printCats(cats):
    for item in cats:
            print("Cat info: \n")
            print("Name: " + str(item.get("name")) +
                  "\nAge: " + str(item.get("age")) +
                  "\nColor: " + str(item.get("color")))
            print()


cat = {"name": "Parys", "age": 7, "color": "gray"}

allCats = []  # this is going to be a list of dictionaries

allCats.append({"name": "Parys", "age": 7, "color": "gray"})
allCats.append({"name": "Burek", "age": 5, "color": "white"})
allCats.append({"name": "Mruczek", "age": 12, "color": "black"})
allCats.append({"name": "Fajter", "age": 2, "color": "black-white"})

printCats(allCats)
