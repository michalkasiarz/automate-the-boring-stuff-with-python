import re

# looking for a number that has at least three digits, up to 5

# greedy match here
# it tries to find the longest possible match

digitRegex = re.compile(r"(\d){3,5}")
mo = digitRegex.search("1234567890")
print(mo.group())   # 12345

# non-greedy match
# it tries to find the smallest possible String

digitRegex = re.compile(r"(\d){3,5}?")  # ? means non-greedy match after {}
mo = digitRegex.search("1234567890")
print(mo.group())   # 123
