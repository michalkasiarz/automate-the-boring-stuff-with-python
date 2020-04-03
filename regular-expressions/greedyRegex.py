import re

# greedy regex example

text = "<To serve humans> for dinner.>"

nonGreedyRegex = re.compile(r"<(.*)>")
mo = nonGreedyRegex.findall(text)
print(mo)   # ['To serve humans> for dinner.']
