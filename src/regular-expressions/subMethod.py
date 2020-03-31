import re

# more on sub method

import re

# Names regex

namesRegex = re.compile(r"Agent (\w)\w*")   # taking first letter of the name as a group
mo = namesRegex.findall("Agent Alice gave the secret document to Agent Bob.")
print(mo)

# sub method for replacing
mo = namesRegex.sub(r"Agent \1****", "Agent Alice gave the secret document to Agent Bob.")
print(mo)   # Agent A**** gave the secret document to Agent B****.




