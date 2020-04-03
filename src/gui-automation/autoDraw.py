import pyautogui

# auto-drawing


def automateDraw():
    pyautogui.click()
    distance = 200
    while distance > 0:
        print(distance, 0)
        pyautogui.dragRel(distance, 0, duration=0.1)  # move right
        distance = distance - 25
        print(0, distance)
        pyautogui.dragRel(0, distance, duration=0.1)  # move down
        print(-distance, 0)
        pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
        distance = distance - 25
        print(0, distance)
        pyautogui.dragRel(0, -distance, duration=0.1)  # move up
