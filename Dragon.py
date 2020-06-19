import pygame
import math
pygame.init()

screen = pygame.display.set_mode((1000, 1000))
Lines = [(400, 800), (400, 400), (800, 400)]


iterations = 3

NewLines = Lines
for i in range(iterations):

    pygame.draw.lines(screen, (255, 255, 255), False, Lines)
    pygame.display.update()

    direction = 0 #if direction is even - RIGHT, if direction is odd - LEFT

    for l in range(len(Lines)):

        CurrentDot = Lines[l]
        NextDot = Lines[l + 1]
        Dot = (0, 0)

        if direction % 2 == 0: #RIGHT
            Dot = (NextDot[0], CurrentDot[1])
        else:
            Dot = (CurrentDot[0], NextDot[1])

        NewLines.insert(l + 1, Dot)

        direction += 1
    else:
        Lines = NewLines

print(Lines)

Update = True
while Update == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Update = False