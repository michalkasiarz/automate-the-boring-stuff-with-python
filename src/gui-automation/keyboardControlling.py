import autoDraw
import pyautogui

# keyboard controlling

# clicking on 100x100 position
pyautogui.click(100, 100)

# typing "Hello world" with 0.2 interval
pyautogui.typewrite("Hello world!", interval=0.2)

# clicking on 100x100 position
pyautogui.click(100, 100)

# printing pyautogui keyboard keys
print(pyautogui.KEYBOARD_KEYS)

# typing some characters and going with arrow keys to the left
pyautogui.typewrite(['left', 'left'], interval=0.5)

# moving the mouse
pyautogui.moveTo(176, 1174)

# clicking
pyautogui.click()

# typing "paint"
pyautogui.typewrite('paint', interval=0.3)

# pressing enter
pyautogui.hotkey('enter')

# moving the mouse
pyautogui.moveTo(400, 400)

# clicking
pyautogui.click()

# automateDraw() call
autoDraw.automateDraw()

# moving the mouse
pyautogui.moveTo(800, 800)

# automateDraw() call
autoDraw.automateDraw()

# moving the mouse
pyautogui.moveTo(1100, 400)

# automateDraw() call
autoDraw.automateDraw()

# moving the mouse
pyautogui.moveTo(325, 70)

# clicking
pyautogui.click()

# moving the mouse
pyautogui.moveTo(690, 496)

# clicking
pyautogui.click()

# typing "paint"
pyautogui.typewrite('Hello world!', interval=0.3)
