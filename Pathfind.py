import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from segment import segment


class Node():
    def __init__(self, pos):
        self.f = None
        self.g = None
        self.h = None
        self.pos = pos
        self.parent = None


def children(point, grid):
    x, y = point.pos
    links = []

    # check right edge
    if x == len(grid) - 1:
        # check bottom right corner
        if y == len(grid) - 1:
            for d in [(x - 1, y), (x, y - 1), (x, 0), (0, y)]:
                links.append([grid[d[0]][d[1]]])
        # check top right corner
        elif y == 0:
            for d in [(x - 1, y), (x, len(grid) - 1), (x, y+1), (0, y)]:
                links.append([grid[d[0]][d[1]]])
        # rest of the edge
        else:
            for d in [(x - 1, y), (x, y - 1), (x, y + 1), (0, y)]:
                links.append([grid[d[0]][d[1]]])

    # check left edge
    elif x == 0:
        # check top left corner
        if y == 0:
            for d in [(len(grid) - 1, y), (x, len(grid) - 1), (x, y + 1), (x + 1, y)]:
                links.append([grid[d[0]][d[1]]])
        #check bottom left corner
        elif y == len(grid)-1:
            for d in [(len(grid) - 1, y), (x, y - 1), (x, 0), (x + 1, y)]:
                links.append([grid[d[0]][d[1]]])

        # rest of the edge
        else:
            for d in [(len(grid) - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
                links.append([grid[d[0]][d[1]]])

    # check bottom edge
    elif y == len(grid)-1:
        for d in [(x - 1, y), (x, y - 1), (x, 0), (x + 1, y)]:
            links.append([grid[d[0]][d[1]]])

    # check top edge
    elif y == 0:
        for d in [(x - 1, y), (x, len(grid) - 1), (x, y + 1), (x + 1, y)]:
            links.append([grid[d[0]][d[1]]])

    else:
        for d in [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]:
            links.append([grid[d[0]][d[1]]])

    return links


def pathfind(snake, snack, rows):
    start = snake.head.pos
    end = snack.pos
    snake_body = []
    for body in snake.body:
        snake_body.append(body.pos)
    openlist = []
    closedlist = []
    cell = [[Node((j, i)) for i in range(rows)] for j in range(rows)]
    finish = cell[end[0]][end[1]]
    # inicialize start node
    current = cell[start[0]][start[1]]
    current.f = 0.0
    current.g = 0.0
    current.h = 0.0
    current.parent_i = start[0]
    current.parent_j = start[1]

    openlist.append(current)

    while openlist:
        current = min(openlist, key=lambda o: o.g + o.h)

        if current == finish:
            path = []
            while current.parent:
                path.append(current)
                current = current.parent
            path.append(current)
            return path[::-1]

        openlist.remove(current)

        closedlist.append(current)

        nodes = children(current, cell)
        for f in nodes:
            for node in f:
                if node in closedlist:
                    continue

                if node in openlist:
                    new_g = current.g + 1

                    if node.g > new_g:
                        node.g = new_g
                        node.parent = current

                else:
                    if node.pos in snake_body:
                        node.h = 900000
                        closedlist.append(node)

                    else:
                        node.g = current.g + 1
                        hx=[]
                        hy=[]
                        hx.append(abs(node.pos[0] - finish.pos[0]))
                        hx.append(abs(node.pos[0]-len(cell)-1)+abs(0-finish.pos[0]))
                        hx.append(abs(node.pos[0]-0)+abs(len(cell)-1-finish.pos[0]))
                        hxmin = min(hx)
                        hy.append(abs(node.pos[1] - finish.pos[1]))
                        hy.append(abs(node.pos[1] - len(cell) - 1) + abs(0 - finish.pos[1]))
                        hy.append(abs(node.pos[1] - 0) + abs(len(cell) - 1 - finish.pos[1]))
                        hymin = min(hy)
                        node.h = (hxmin + hymin)
                        node.parent = current
                        openlist.append(node)




