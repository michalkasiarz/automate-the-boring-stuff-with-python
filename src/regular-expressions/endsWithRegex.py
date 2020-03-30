import re

# ends with regex example

endsWithByeRegex = re.compile(r"Bye!$")
mo = endsWithByeRegex.findall("OK, that's all. Bye! Take care!")
print(mo)   # [] i.e. None
mo = endsWithByeRegex.findall("OK, that's all. Bye!")
print(mo)   # ['Bye!']

