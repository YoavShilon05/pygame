import pygame

### VARIABLES TO TWEAK
screenw, screenh = (1000, 1000)
Dots = [(400, 800), (400, 400), (800, 400)]
iterations = 12


screen = pygame.display.set_mode((screenw, screenh))

def R(A, B):
    dot = (0.5 * (A[0] + B[0] - B[1] + A[1]), 0.5 * (A[1] + B[1] + B[0] - A[0]))
    return dot


def L(A, B):
    dot = (0.5 * (A[0] + B[0] + B[1] - A[1]), 0.5 * (A[1] + B[1] - B[0] + A[0]))
    return dot

for i in range(iterations):

    pygame.draw.lines(screen, (255, 255, 255), False, Dots)
    pygame.display.update()

    screen.fill((0, 0, 0))

    direction = 0 #if direction is even - RIGHT, if direction is odd - LEFT

    NewLines = Dots.copy()

    for l in range(len(Dots) - 1):

        CurrentDot = Dots[l]
        NextDot = Dots[l + 1]

        Dot = (0, 0)
        if direction % 2 == 0: #RIGHT
            Dot = R(CurrentDot, NextDot)
        else:
            Dot = L(CurrentDot, NextDot)

        NewLines.insert(2 * (l + 1) - 1, Dot)


        direction += 1


    Dots = NewLines.copy()

    pygame.draw.lines(screen, (255, 255, 255), False, Dots)
    pygame.display.update()

Update = True
while Update == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Update = False