import re

# findAll method

f = open(r"C:\Users\micha\Documents\PythonProjects\automated-software-testing-with-python\resume1.txt", "r")

resume = f.read()

phoneRegex = re.compile(r"(\(\d\d\d\))?[\s-](\d\d\d-\d\d\d)")
mo = phoneRegex.findall(resume)
print(mo)   # [('(410)', '444-555'), ('(420)', '666-777')]

