import pprint

# Simple app that counts the number of characters
# in 'With Fire and Sword' by Henryk Sienkiewicz (English version)

f = open("C:\\Users\\micha\\Desktop\\WithFireAndSword.txt", "r")

message = f.read()

count = {}  # access is going through a key

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
