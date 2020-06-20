import pygame as pg
from math import *

screenw, screenh = (1920, 1080)

### VARS TO TWEAK
zoom = 450
sharpness = 25
power = 2

screen = pg.display.set_mode((screenw, screenh))

def distance(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)




for x in range(round(-screenw / 2), round(screenw / 2)):
    for y in range(round(-screenh / 2), round(screenh / 2)):

        n = complex(x / zoom, y / zoom)
        c = n
        iterations = 0
        for i in range(sharpness):
            if distance((n.real, n.imag), (0, 0)) >= 2:
                break
            else:
                n = n ** power + c
            iterations += 1
        color = 255 - (sqrt(iterations) / sqrt(sharpness)) * 255
        pg.draw.rect(screen, (color, color, color), (x + screenw / 2, y + screenh / 2, 1, 1))

Update = True

pg.display.update()

while Update:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            Update = False