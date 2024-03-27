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
        time.sleep(2)
        keyboard.press_and_release('a', 4)
        time.sleep(0.5)
        keyboard.press_and_release('d', 4)