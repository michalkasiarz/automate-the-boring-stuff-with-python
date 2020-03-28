#   Is only-like methods
import pyperclip

text = """
Then that knight, whom neither captivity nor wounds nor grief nor the
terrible Burdabut could bring down, was brought down by happiness. His
hands dropped at his side, great drops of sweat came out on his
forehead; he fell on his knees, covered his face with his hands, and
leaning his head against the wall of the ravine, remained in silence,
evidently thanking God."""

only_whitespace = "               "

only_numbers = "21143"

only_text = "Hello"

title = "The Title Style"

# isalpha method
print(only_text.isalpha())  # True
print(text.isalpha())   # False

# isspace method
print(only_whitespace.isspace())    # True
print("The surely are some spaces".isspace())   # True

# isdecimal method
print(only_numbers.isdecimal())     # True, although it is a String

# istitle method
print(title.istitle())      # True

# isalnum method
print("razdwatrzy123".isalnum())    # True

# startswith and endswith methods
print("Hello World".startswith("Hello"))    # True
print("Hello World".endswith("World"))    # True

# join method

to_be_joined = ["cats", "dogs", "hot-dogs", "avengers"]
joined_text = ", ".join(to_be_joined)
print(joined_text)

# split method

print(text.split())

# ljust and rjust method

print("Hello".rjust(100, "-"))
print("Hello".ljust(100, "*"))

# center method

print("Hello".center(100, "="))

# strip, rstrip, lstrip methods

rjusted = "Hello".rjust(30, "/")

print(rjusted)

rjusted_stripped = rjusted.strip("/")

print(rjusted_stripped)

text_with_spaces = "    Hello                    "
print(text_with_spaces)
print(text_with_spaces.strip())

# replace method

spam = "Hello there!"
spam = spam.replace("e", "XYZ")
print(spam)

# pyperclip module

pyperclip.copy(spam)
copied_stuff = pyperclip.paste()
print(copied_stuff)
