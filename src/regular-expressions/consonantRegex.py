import re

# consonant regex

doubleVowelRegex = re.compile(r"[^aeiouAEIOU]")     # looking for everything that is NOT
mo = doubleVowelRegex.findall("Robocop eats baby food.")
print(mo)   # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
