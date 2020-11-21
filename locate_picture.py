import pyautogui
import time
while True:
    start = pyautogui.locateCenterOnScreen('start.png')#If the file is not a png file it will not work
    print(start)
    time.sleep(1)
    pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image
