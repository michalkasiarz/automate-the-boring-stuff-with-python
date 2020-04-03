import re

# Names regex

namesRegex = re.compile(r"Agent \w+")
namesRegex.findall("Agent Alice gave the secret document to Agent Bob.")

# sub method for replacing
mo = namesRegex.sub("REDACTED", "Agent Alice gave the secret document to Agent Bob.")
print(mo)   # REDACTED gave the secret document to REDACTED.




