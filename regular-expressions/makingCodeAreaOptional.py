import re

# Making code area optional by using ?

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d")
mo = phoneRegex.search("My phone is 111-444-1234, call me now")
print(mo.group())   # 111-444-123
mo = phoneRegex.search("My phone is 444-1234, I don't know the area code.")
print(mo.group())   # 444-123

# can escape a question mark by \ in front of it, like \?
