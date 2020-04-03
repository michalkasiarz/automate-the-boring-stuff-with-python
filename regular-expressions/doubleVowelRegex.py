import re

# double vowel regex

doubleVowelRegex = re.compile(r"[aeiouAEIOU]{2}")   # looking for two vowels in a row
mo = doubleVowelRegex.findall("Robocop eats baby food.")
print(mo)
