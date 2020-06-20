import pygame as pg
import random
import time
from typing import List
from queue import Queue

# VARIABLES TO TWEAK
screenw, screenh = (500, 500)
blockSize = 50
blockPadding = 5
# farmerate (ms)
framerate = 150


snake : List[List[int]] = [[(screenw / blockSize) // 2, (screenh / blockSize) // 2]]
direction = [0, 0]
apple = None
directionQ = Queue()

win = pg.display.set_mode((screenw, screenh))

update = True
while update:

    pg.time.delay(1)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            update = False

    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        update = False

    # set directions

    if keys[pg.K_UP]:
        if not direction == [0, -1]:
            directionQ.put([0, -1])
            direction = [0, -1]
    elif keys[pg.K_RIGHT]:
        if not direction == [1, 0]:
            directionQ.put([1, 0])
            direction = [1, 0]
    elif keys[pg.K_DOWN]:
        if not direction == [0, 1]:
            directionQ.put([0, 1])
            direction = [0, 1]
    elif keys[pg.K_LEFT]:
        if not direction == [-1, 0]:
            directionQ.put([-1, 0])
            direction = [-1, 0]


    if pg.time.get_ticks() % framerate == 0:

        win.fill((0, 0, 0))

        if directionQ.qsize() > 0:
            direction = directionQ.get()


        # generate apple if not exists
        if apple == None:
            apple = [random.randint(0, screenw / blockSize - 1), random.randint(0, screenh / blockSize - 1)]

        #render apple
        pg.draw.rect(win, (255, 0, 0), [apple[0] * blockSize + blockPadding, apple[1] * blockSize + blockPadding, blockSize - blockPadding * 2, blockSize - blockPadding * 2])

        pg.display.update()

        # check apple collision

        if snake[-1] == apple:
            snake.insert(0, snake[0])
            apple = None


        # move snake
        snake.append([snake[-1][0] + direction[0], snake[-1][1] + direction[1]])
        snake.pop(0)

        #render snake

        for blockIndex in range(len(snake)):
            block = snake[blockIndex]
            pg.draw.rect(win, (255, 255, 255), [block[0] * blockSize + blockPadding, block[1] * blockSize + blockPadding, blockSize - blockPadding * 2, blockSize - blockPadding * 2])

            # check for self collision
            if snake[-1] == block and blockIndex != len(snake) -1: # if there is collision and current block is not the head.
                update = False
                break


        #check border collision
        if snake[-1][0] < 0 or snake[-1][0] * blockSize > screenw or snake[-1][1] < 0 or snake[-1][1] * blockSize > screenh:
            update = False

    pg.display.update()