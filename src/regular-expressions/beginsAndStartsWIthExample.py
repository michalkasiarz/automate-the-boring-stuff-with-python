import re

# begins and starts with example

allDigitsRegex = re.compile(r"^\d+$")  # the pattern must start and end with one or more digit
mo = allDigitsRegex.search("123456789")
print(mo.group())  # 123456789
mo = allDigitsRegex.search("1234x56789")
try:
    print(mo.group())                   # AttributeError here, mate!
except AttributeError:
    print("AttributeError here, mate!")
