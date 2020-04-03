# Advanced String syntax

# escape characters
import pprint

cat = "Meow: \"I like to meow everyday!\""
print(cat)

print("There's a\nnewline here!")
print("And\there's a tab,\tand here again!")

# raw String
print(r"That is Carol\'s cat\n\nHe says: \"That is weird!\"")
# no escape characters there

# triple quotes
print("""Dear Peter,\n\n
Eve's cat has been arrested for\t\t\ncatnapping,
\tcat burglary\n\t\tand extortion.\n\nSincerely,\n\nBob""")

print()

# How many characters are in
# "With Fire and Sword" in English translation?
f = open("C:\\Users\\micha\\Desktop\\WithFireAndSword.txt", "r")
print("How many characters are in \"With Fire and Sword\"\nin English translation?")
book = f.read()
print(len(book))
