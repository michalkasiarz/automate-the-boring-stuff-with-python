import re

# using dot in a regex

atRegex = re.compile(r".at")    # matches everything that has one char before at
mo = atRegex.findall("The cat in the hat sat on the flat mat.")
print(mo)   # ['cat', 'hat', 'sat', 'lat', 'mat']
atRegex = re.compile(r".{1,2}at")    # matches everything that has one or two chars before at
mo = atRegex.findall("The cat in the hat sat on the flat mat.")
print(mo)   # [' cat', ' hat', ' sat', 'flat', ' mat']
