#! python3

import pyperclip
import webbrowser
import sys


# Webbrowser module

sys.argv  # ["webBrowserModule.py", "Rynek 1", "Lublin"]

# Check if command line arguments were passed
if len(sys.argv) > 1:
    # ["webBrowserModule.py", "Rynek 1", "Lublin"] -> Lublin, Rynek 1
    address = " ".join(sys.argv[1:])
else:
    address = pyperclip.paste()

print(sys.path)

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open("https://www.google.com/maps/place/" + str(address))

