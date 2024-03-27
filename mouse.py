import pyautogui
import keyboard
import time

while True:
    if pyautogui.pixelMatchesColor(167, 176, (57, 134, 67)):
        time.sleep(4)
        keyboard.press_and_release('1')
        time.sleep(0.1)
        keyboard.press_and_release('1')
        time.sleep(4)
    else:
        x_left, y_left = 808, 708
        x_right, y_right = 918, 708
        pyautogui.moveTo(x_left, y_left)
        pyautogui.mouseDown()
        time.sleep(4)
        pyautogui.mouseUp()
        time.sleep(0.5)
        pyautogui.moveTo(x_right, y_right)
        pyautogui.mouseDown()
        time.sleep(4)
        pyautogui.mouseUp()