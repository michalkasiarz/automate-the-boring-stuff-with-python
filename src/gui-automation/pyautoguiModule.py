import pyautogui


# pyautogui module

def mousePosition():
    print("Current position of the mouse on the screen: " + str(pyautogui.position()))


# prints the current position of the mouse on the screen
mousePosition()

# moving mouse to specific coordinates
pyautogui.moveTo(10, 10, duration=3)
mousePosition()

# moving mouse relatively
pyautogui.moveRel(200, 0, duration=2)
mousePosition()

# clicking on a specific point
pyautogui.click(x=10, y=10)
mousePosition()
