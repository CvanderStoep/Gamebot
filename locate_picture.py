"""""
Locates an image on the screen and moves the mouse to that location
Can be useful in games to locate objects and perform an action; for example mouseclick
The picture has to be in .png format
The picture has to be in 100% format (no zoom in / zoom out)
"""

import pyautogui
import time

while True:
    start = pyautogui.locateCenterOnScreen('lexy.png')  # If the file is not a png file it will not work
    print(start)
    pyautogui.moveTo(start)  # Moves the mouse to the coordinates of the image
    time.sleep(5)  # sleep for 5 seconds to allow the user to close picture?
