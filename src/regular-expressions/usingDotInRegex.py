import re

# using dot in a regex

atRegex = re.compile(r".at")
mo = atRegex.findall("The cat in the hat sat on the flat mat.")
print(mo)   # ['cat', 'hat', 'sat', 'lat', 'mat']
