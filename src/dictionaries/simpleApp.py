# Simple app that counts the number of characters per char in a String

message = "It was a bright cold day in April, and the clocks were striking thirteen."

count = {}  # access is going through a key

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1


print(count)
