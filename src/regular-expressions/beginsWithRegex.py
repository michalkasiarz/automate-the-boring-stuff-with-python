import re

# begins with regex

beginsWithHelloRegex = re.compile(r"^Hello")
mo = beginsWithHelloRegex.findall("Ekhm... Hello there!")
print(mo)   # None
mo = beginsWithHelloRegex.findall("Hello there!")
print(mo)   # ['Hello']
