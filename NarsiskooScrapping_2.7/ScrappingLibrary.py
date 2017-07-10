# from __future__ import print_function

__author__ = 'rahmat'
# 07 July 2017 12:43 PM

import pyautogui
import time

sleepTime = 1

def sleep():
    time.sleep(sleepTime)

def printImage():
    print "Printing.."
    time.sleep(5)
    clickFileButton()
    clickDesktopButton()
    clickNewestImage()
    clickOk1()
    clickPlus()
    clickOk2()
    deleteImage()

def deleteImage():
    time.sleep(5)
    clickFileButton()
    clickDesktopButton()
    clickNewestImage()
    pressDelete()
    clickOk3()
    clickOk3()
    clickCancel()

def clickWrapper(x, y):
    try:
        pyautogui.click(x, y)
    except:
        pass

def clickFileButton():
    clickWrapper(413, 146)
    return sleep()

def clickDesktopButton(isIsi = False):
    if isIsi:
        clickWrapper(545, 200)
    else:
        clickWrapper(550, 203)
    return sleep()

def clickNewestImage():
    clickWrapper(703, 250)
    return sleep()

def clickOk1():
    clickWrapper(1007, 554)
    return sleep()

def clickPlus():
    clickWrapper(594, 349)
    return sleep()

def clickOk2():
    clickWrapper(1125, 693)
    return sleep()

def pressDelete():
    pyautogui.press('delete')
    return sleep()

def clickOk3(isIsi = False):
    if isIsi:
        clickWrapper(750, 434)
    else:
        clickWrapper(752, 481)
    return sleep()

def clickCancel(isIsi = False):
    if isIsi:
        clickWrapper(1010, 587)
    else:
        clickWrapper(1010, 587)
    return sleep()
