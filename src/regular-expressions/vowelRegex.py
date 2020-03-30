import re

# Vowel regex

vowelRegex = re.compile(r"[aeiouAEIOU]")
mo = vowelRegex.findall("Robocop eats baby food.")
print(mo)
