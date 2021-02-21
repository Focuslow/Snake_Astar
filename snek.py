import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
from segment import segment


class snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = segment(pos)  # The head will be the front of the snake
        self.body.append(self.head)  # We will add head (which is a cube object)
        # to our body list

        # These will represent the direction our snake is moving
        self.dirnx = 0
        self.dirny = 1

    def move(self, path=0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # moving with keys
        if path == 0:
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_LEFT]:
                    if self.head.dirnx == 1:
                        continue
                    else:
                        self.dirnx = -1
                        self.dirny = 0

                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]:

                    if self.head.dirnx == -1:
                        continue
                    else:
                        self.dirnx = 1
                        self.dirny = 0

                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:

                    if self.head.dirny == 1:
                        continue
                    else:
                        self.dirnx = 0
                        self.dirny = -1

                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:

                    if self.head.dirny == -1:
                        continue
                    else:
                        self.dirnx = 0
                        self.dirny = 1

                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        # moving using pathfinding
        if path:
            x_edge = False
            y_edge = False
            # moving through edge on x
            if abs(path[1].pos[0] - path[1].parent.pos[0]) > 18:
                x_edge = True
            # moving through edge on y
            if abs(path[1].pos[1] - path[1].parent.pos[1]) > 18:
                y_edge = True

            # moving verticaly
            if path[1].pos[0] == self.head.pos[0]:
                # down
                if (path[1].pos[1] > self.head.pos[1] and not y_edge) or (y_edge and path[1].pos[1] < self.head.pos[1]):
                    if self.head.dirny == 1:
                        pass
                    else:
                        self.dirnx = 0
                        self.dirny = 1

                        self.turns[(self.head.pos[0],self.head.pos[1])] = [self.dirnx,self.dirny]

                # up
                elif (path[1].pos[1] < self.head.pos[1] and not y_edge) or (
                        y_edge and path[1].pos[1] > self.head.pos[1]):
                    if self.head.dirny == -1:
                        pass
                    else:
                        self.dirnx = 0
                        self.dirny = -1

                        self.turns[(self.head.pos[0],self.head.pos[1])] = [self.dirnx,self.dirny]

            # moving horizontaly
            elif path[1].pos[1] == self.head.pos[1]:
                # right
                if (not x_edge and path[1].pos[0] > self.head.pos[0]) or (x_edge and path[1].pos[0] < self.head.pos[0]):
                    if self.head.dirnx == 1:
                        pass
                    else:
                        self.dirnx = 1
                        self.dirny = 0

                        self.turns[(self.head.pos[0],self.head.pos[1])] = [self.dirnx,self.dirny]

                # left
                if (not x_edge and path[1].pos[0] < self.head.pos[0]) or (x_edge and path[1].pos[0] > self.head.pos[0]):
                    if self.head.dirnx == -1:
                        pass
                    else:
                        self.dirnx = -1
                        self.dirny = 0

                        self.turns[(self.head.pos[0],self.head.pos[1])] = [self.dirnx,self.dirny]

            path.remove(path[1])

        for i, c in enumerate(self.body):
            p = tuple([c.pos[0],c.pos[1]])

            try:
                if p in self.turns:
                    turn = self.turns[p]
            except TypeError:
                p=c.pos[:]
                qq = self.turns
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])

                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])

                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])

                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)

                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)

                else:
                    c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        self.head = segment(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addsegment(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(segment((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(segment((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(segment((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(segment((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
