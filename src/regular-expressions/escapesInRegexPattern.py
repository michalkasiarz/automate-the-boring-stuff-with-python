import re

# Escapes in regex pattern

regex = re.compile(r"(\+\*\?)+")   # looking for +*? in a text, has to appear 1 or more times
mo = regex.search("I just learned how to use +*? regex syntax. Isn't is wonderful?")
print(mo.group())   # +*?

# Quick recap

#   ? means 0 or 1
#   * means 0 or more
#   * means 1 or more
