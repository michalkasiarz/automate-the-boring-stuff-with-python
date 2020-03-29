import re

# First regex example

message = input("Type some text: ")

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.findall(message)
print(mo)
