import pyautogui
import time
while True:
    time.sleep(2)
    posi = pyautogui.position()
    print (posi)
    im = pyautogui.screenshot()
    pixel = im.getpixel((posi))
    print(pixel)