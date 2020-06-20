import pygame as pg
from math import *
import time
import threading

### VARIABLES TO TWEAK
screenw, screenh = (1920, 1080)
# radius
r = 500
# number of points
p = 500
# the first number of table in sequence
n = 2


win = pg.display.set_mode((screenw, screenh))

def Distance(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)


def Calc():

    pg.draw.circle(win, (255, 255, 255), (screenw//2, screenh//2), r, 2)

    pts = []

    for i in range(pts):
        pt = (r * cos(i / pts * 2 * pi) + screenw / 2, r * sin(i / pts * 2 * pi) + screenh / 2)
        pts.append(pt)

    for i in range(len(pts)):
        pg.draw.line(win, (255, 255, 255), pts[i % pts], pts[n * i % pts])



update = True

def Repeat():
    while update:
        win.fill((0, 0, 0))
        Calc()
        global n
        n += 1
        time.sleep(1)
        pg.display.update()
        time.sleep(0.1)

# make a thread for the function to repeat and main thread is for event listening
newThread = threading.Thread(target=Repeat)
newThread.start()
while update:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            update = False
            newThread.join()

