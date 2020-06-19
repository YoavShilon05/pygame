import pygame as pg
from math import *

screenw, screenh = (1000, 650)

win = pg.display.set_mode((screenw, screenh))

frameRate = 60
line = screenw / 2
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

    def Mark(self):
        pg.draw.line(win, (255, 255, 255), [self.center[0] + self.point[0], self.center[1] + self.point[1]], [line, self.center[1] + self.point[1]])
        marks.append([line, self.center[1] + self.point[1]])


c1 = Circle(0.5, 100)
c2 = Circle(1, 50, c1)

circles = [c1, c2]

clock = pg.time.Clock()
update = True
while update:

    clock.tick(frameRate)

    win.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            update = False

    pg.draw.line(win, (255, 255, 255), [line, 0], [line, screenh])

    for c in circles:
        c.Turn()
        c.Render()

    circles[-1].Mark()

    RenderMarks()
    MoveMarks()

    pg.display.update()