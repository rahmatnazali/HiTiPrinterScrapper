# from __future__ import print_function

__author__ = 'rahmat'
# 07 July 2017 10:44 AM

from ScrappingLibrary import *
import os

def listen(dirName):
    while True:
        time.sleep(2)
        for file in os.listdir(dirName):
            if file.endswith(".jpg"):
                print(os.path.join("E:\\rahmat\\Desktop", file))
                printImage()

listen("E:/rahmat/Desktop")