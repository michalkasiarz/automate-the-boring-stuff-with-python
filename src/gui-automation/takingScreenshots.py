import pyautogui

# screenshots

# taking a screenshot
pyautogui.screenshot(r"C:\Users\micha\Documents\Training\example_screenshot.png")

# printing the location (center) of a given pic on the screenshot
print(str(pyautogui.locateCenterOnScreen(r"C:\Users\micha\Documents\Training\tessy\6.jpg")))

