import re

# 12 Days of Christmas example

f = open(r"C:\Users\micha\Documents\PythonProjects\automated-software-testing-with-python\12DaysOfChristmas.txt", "r")

lyrics = f.read()

xmasRegex = re.compile(r"\d+\s\w+")
mo = xmasRegex.findall(lyrics)
print(mo)   # ['12 Drummers', '11 Pipers', '10 Lords', '9 Ladies', '8 Maids', '7 Swans', '6 Geese', '5 Golden', '4 Calling', '3 French', '2 Turtle', '1 Partridge']

