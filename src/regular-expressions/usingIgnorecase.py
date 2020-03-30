import re

# using re.IGNORECASE

vowelRegex = re.compile(r"[aeiou]", re.I)  # ignore case instruction: re.I or re.IGNORECASE
mo = vowelRegex.findall("Al, why does you programming book talk about RoboCop so much?")
print(mo)
