import re

# verbose mode with re.verbose

phoneRegex = re.compile(r"""
(\d\d\d-|       # first 3 digits and first dash
\(\d\d\d\)\s)   # -or- first three digits in parentheses, with a space, without dash
(\d\d\d         # next 2 digits
-               # second dash
\d\d\d\d)       # last 4 digits
""", re.VERBOSE | re.IGNORECASE | re.DOTALL)

text = "Here are some numbers: (123) 213-1234 or 435-345-3453."

mo = phoneRegex.findall(text)
print(mo)   # [('(123) ', '213-1234'), ('435-', '345-3453')]

