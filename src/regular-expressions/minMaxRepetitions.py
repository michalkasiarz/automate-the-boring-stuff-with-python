import re

# indicating a minimum and a maximum number of repetitions in a regex

haRegex = re.compile(r"(ha){3,5}")  # from 3 to 5 repetitions
mo = haRegex.search("That is very funny, hahahahahahahahaha!")
print(mo.group())   # hahahahaha, 5 hahahas are allowed here to print
