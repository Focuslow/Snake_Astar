# snek

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from snek import snake
from segment import segment
from Pathfind import pathfind

def drawGrid(size, rows, surface):
    square = size // rows

    x = 0  # Keeps track of the current x
    y = 0  # Keeps track of the current y
    for l in range(rows):  # We will draw one vertical and one horizontal line each loop
        x = x + square
        y = y + square

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, size))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (size, y))


def updateWindow(surface):
    surface.fill((0, 0, 0))  # black screen

    #test draw A*
    dis = size // rows
    if path:
        try:
            for d in path[1:]:
                row = d.pos[0]
                col = d.pos[1]
                pygame.draw.rect(surface, [0,0,255], (row*dis+1, col*dis+1, dis-2, dis-2))
        except TypeError:
            print(p)
            print(path)


    s.draw(surface)
    snack.draw(surface)
    drawGrid(size, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass


def main():
    global size, rows, s, snack, path
    size = 500  # size of win to change also change in segment
    rows = 20 #num of rows has to change in segment also
    win = pygame.display.set_mode((size, size))  # create square windon

    s = snake((255, 0, 0), (10, 0))
    snack = segment(randomSnack(rows, s), color=(0, 255, 0))
    # snack = segment((10,15), color=(0, 255, 0))
    clock = pygame.time.Clock()
    path=0


    # path = pathfind(s, snack, rows)  #automatic pathfinding


    run = True

    while run:
        pygame.time.delay(1)  # delay

        #how fast is tick rate
        if len(s.body)<100:
            clock.tick(10)
           # clock.tick(100) automatic fast tick rate
        else:
            clock.tick(10)
        s.move()      #manual move
        #s.move(path)  #automatic move
        # path = pathfind(s, snack, rows)  #autmatic pathfinding
        if s.body[0].pos[0] == snack.pos[0] and s.body[0].pos[1] == snack.pos[1]:
            s.addsegment()
            snack = segment(randomSnack(rows, s), color=(0, 255, 0))
            # path = pathfind(s, snack, rows)  #automatic pathfinding

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: ', + len(s.body))
                message_box('You Lost!', 'Your score was ' + str(len(s.body)))
                s.reset((10, 10))
                # path = pathfind(s, snack, rows) #automatic pathfinding
                break

        updateWindow(win)  # update win


main()
