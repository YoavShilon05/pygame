import pygame as pg
from math import *
import time
import threading

screenw = 1920
screenh = 1080
win = pg.display.set_mode((screenw, screenh))

def Distance(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)


### VARS
r = 500
n = 500
p = 2

def Calc():

    pg.draw.circle(win, (255, 255, 255), (screenw//2, screenh//2), r, 2)

    pts = []

    for i in range(n):
        pt = (r * cos(i / n * 2 * pi) + screenw / 2, r * sin(i / n * 2 * pi) + screenh / 2)
        pts.append(pt)

    for i in range(len(pts)):
        pg.draw.line(win, (255, 255, 255), pts[i % n], pts[p * i % n])



update = True

def Repeat():
    while update:
        win.fill((0, 0, 0))
        Calc()
        global p
        p += 1
        time.sleep(1)
        pg.display.update()
        time.sleep(0.1)


newThread = threading.Thread(target=Repeat)
newThread.start()
while update:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            update = False
            newThread.join()

