import re

# Robocop regex example

prime = "Serve the public trust.\nProtect the innocent.\nUpload the law."
print(prime)
print()
dotStarRegex = re.compile(r".*")    # matches everything except the newline
mo = dotStarRegex.search(prime)
print(mo.group())   # Serve the public trust.
print()

# using DOTALL

dotStarRegex = re.compile(r".*", re.DOTALL)    # matches everything except the newline
mo = dotStarRegex.search(prime)
print(mo.group())    # Serve the public trust.
# Protect the innocent.
# Upload the law.
