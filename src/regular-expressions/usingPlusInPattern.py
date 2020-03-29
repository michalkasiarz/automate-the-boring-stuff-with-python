import re

# using plus in a pattern

batRegex = re.compile(r"Bat(wo)+man")  # * means at least 1 or more (wo) pattern
mo = batRegex.search("The Adventures of Batman")
try:
    print(mo.group())  # None
except AttributeError:
    print("AttributeError, Sire!")
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())  # Batwoman
mo = batRegex.search("The Adventures of Batwowowowowowoman")
print(mo.group())  # Batwowowowowowoman
