import pygame as pg
from math import *


### VARIABLES TO TWEAK
screenw, screenh = (1000, 650)
frameRate = 60
connectors = False
lineX = screenw / 2


win = pg.display.set_mode((screenw, screenh))
marks = []

def MoveMarks():
    for m in marks:
        if m[0] > screenw:
            marks.remove(m)
        else:
            m[0] += 1

def RenderMarks():

    for m in marks:
        pg.draw.rect(win, (255, 255, 255), [m[0], m[1], 1, 1])

circles = []

class Circle:

    def __init__(self, frequency, size, parent=None):
        self.frequency = frequency
        self.r = size
        self.angle = 0
        self.child = None
        if parent != None:
            parent.child = self
        self.center = [screenw // 5, screenh // 2]
        self.point = [self.r + self.center[0], self.center[1]]
        circles.append(self)

    def Turn(self):
        self.angle += 2 * pi * self.frequency / frameRate
        self.point = [floor(sin(self.angle) * self.r), floor(cos(self.angle) * self.r)]
        if self.child != None:
            self.child.center = [self.center[0] + self.point[0], self.center[1] + self.point[1]]

    def SetChild(self, child):
        self.child = child

    def Render(self):
        # render circle:
        pg.draw.circle(win, (255, 255, 255), self.center, self.r, 2)

        # render pt
        pg.draw.circle(win, (255, 255, 255), [self.point[0] + self.center[0], self.point[1] + self.center[1]], 4)

        # render connector
        if connectors:
            pg.draw.line(win, (255, 255, 255), self.center, [self.center[0] + self.point[0], self.center[1] + self.point[1]])

    def Mark(self):
        pg.draw.line(win, (255, 255, 255), [self.center[0] + self.point[0], self.center[1] + self.point[1]], [lineX, self.center[1] + self.point[1]])
        marks.append([lineX, self.center[1] + self.point[1]])


# SIN WAVES - CAN TWEAK
c1 = Circle(0.125, 100)
c2 = Circle(0.25, 50, c1)
c3 = Circle(0.5, 25, c2)
c4 = Circle(1, 30, c3)


clock = pg.time.Clock()
update = True
while update:

    clock.tick(frameRate)

    win.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            update = False

    pg.draw.line(win, (255, 255, 255), [lineX, 0], [lineX, screenh])

    for c in circles:
        c.Turn()
        c.Render()

    circles[-1].Mark()

    RenderMarks()
    MoveMarks()

    pg.display.update()