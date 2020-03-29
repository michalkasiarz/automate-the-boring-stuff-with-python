import re

# digit regex, looking for a number that has at least three digits, up to 5

digitRegex = re.compile(r"(\d){3,5}")
mo = digitRegex.search("1234567890")
print(mo.group())   # 12345
