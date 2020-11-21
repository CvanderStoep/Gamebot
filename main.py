""""
Gamebot for magic piano.
https://www.agame.com/game/magic-piano-tiles
locate the black tiles and click.
line1 .. line4 indicate the 4 positions you want to click on the screen

You can use the routine display_mouse.py to find the locations

"""

from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)  # This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# input('press enter to start, press q to quit:\n')
while not keyboard.is_pressed('q'):

    line1 = Point(2500, 400)
    line2 = Point(2600, 400)
    line3 = Point(2700, 400)
    line4 = Point(2800, 400)
    try:
        if pyautogui.pixel(line1.x, line1.y)[0] == 0:
            click(line1.x, line1.y)
        if pyautogui.pixel(line2.x, line2.y)[0] == 0:
            click(line2.x, line2.y)
        if pyautogui.pixel(line3.x, line3.y)[0] == 0:
            click(line3.x, line3.y)
        if pyautogui.pixel(line4.x, line4.y)[0] == 0:
            click(line4.x, line4.y)
    except:
        print("Cannot get pixel for the moment")
