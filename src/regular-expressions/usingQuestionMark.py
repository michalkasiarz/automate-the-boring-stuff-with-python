import re

# using question mark -> for something that appears 1 or 0 times (preceding pattern)

batRegex = re.compile(r"Bat(wo)?man")
mo = batRegex.search("The Adventures of Batman")
print(mo.group())  # Batman

mo = batRegex.search("The Adventures of Batwoman")
print((mo.group()))  # Batwoman


