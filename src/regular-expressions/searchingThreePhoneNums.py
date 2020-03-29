import re

# looking for three phone numbers separated (or not) by a comma

phoneRegex = re.compile(r"((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}")
mo = phoneRegex.search("My numbers are: 111-1111, 222-222-2222, 333-3333. Give me yours, mate!. OK, write them down: 444-4444, 555-5555, 666-6666, 777-777-7777.")
print(mo.group())   # 111-1111, 222-222-2222, 333-3333

