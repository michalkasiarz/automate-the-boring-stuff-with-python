import re

# using asterisk in a pattern

batRegex = re.compile(r"Bat(wo)*man")   # * means 0 or more (wo) pattern
mo = batRegex.search("The Adventures of Batman")
print(mo.group())   # Batman
mo = batRegex.search("The Adventures of Batwoman")
print(mo.group())   # Batwoman
mo = batRegex.search("The Adventures of Batwowowowowowoman")
print(mo.group())   # Batwowowowowowoman
