# from __future__ import print_function

__author__ = 'rahmat'
# 07 July 2017 10:36 AM

import pyautogui
import math
import time

def anotherExamplpe():
    pyautogui.moveTo(100, 150)
    pyautogui.moveRel(0, 10)  # move mouse 10 pixels down
    pyautogui.dragTo(100, 150)
    pyautogui.dragRel(0, 10)  # drag mouse 10 pixels down

for i in range(500):
    x = int(500+math.sin(math.pi*i/100)*500)
    y = int(500+math.cos(i)*100)
    pyautogui.moveTo((x,y))
    time.sleep(.01)