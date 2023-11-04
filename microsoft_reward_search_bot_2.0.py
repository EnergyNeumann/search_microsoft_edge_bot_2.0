#code by Richard Neumann (Energy Neumann)

import pyautogui
import time
import random

#failsafe to give you security, if you need to break the code
pyautogui.FAILSAFE = True
time.sleep(2)

#button function
def searching():
    for i in range(0, 36):
        time.sleep(3)
        randons = random.randint(1, 100000000000000)
        pyautogui.click(x=564, y=46)
        pyautogui.write(str(randons))
        pyautogui.press('enter')

searching()

