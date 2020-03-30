import re

# using .* pattern, which basically means: anything

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.findall("First Name: John Last Name: Kowalski")
print(mo)   # [('John', 'Kowalski')]
