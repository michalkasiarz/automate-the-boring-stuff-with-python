import re

# looking for an explicit number of pattern appearances

haRegex = re.compile(r"(Ha){3}")    # looking for HaHaHa
mo = haRegex.search("It was very funny for him, - HaHaHaHaHa - he laughed.")
print(mo.group())   # HaHaHa
