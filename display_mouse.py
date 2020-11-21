import pyautogui
import time

while True:
    try:
        x, y = pyautogui.position()
        print('pixel location: ', x,y)
        print('R, G, B: ', pyautogui.pixel(x, y))
        time.sleep(1)
    except:
        print("Cannot get pixel for the moment")
time.sleep(1)
