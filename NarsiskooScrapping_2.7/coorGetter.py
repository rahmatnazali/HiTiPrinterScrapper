from ctypes import windll, Structure, c_ulong, byref
import time

class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

while True:
    time.sleep(1)
    pos = queryMousePosition()
    print pos
