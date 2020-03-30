import re

# non-greedy regex example

text = "<To serve humans> for dinner.>"

nonGreedyRegex = re.compile(r"<(.*?)>")     # ? means as little match as possible
mo = nonGreedyRegex.findall(text)
print(mo)   # ['To serve humans']
