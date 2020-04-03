import re

# using question mark -> for something that appears 1 or 0 times (preceding pattern)

batRegex = re.compile(r"Bat(wo)?man")
mo = batRegex.search("The Adventures of Batman")
print(mo.group())  # Batman

mo = batRegex.search("The Adventures of Batwoman")
print((mo.group()))  # Batwoman

# another example with ? inside pattern

dinRegex = re.compile(r"dinner\?")   # we are looking for dinner?
mo = dinRegex.search("Do you fancy a dinner? Because he does not. So sad.")
print(mo.group())

