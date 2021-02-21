import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class segment(object):
    rows = 20
    size = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        if self.pos[0] + self.dirnx > self.rows - 1:
            self.pos = (0, self.pos[1] + self.dirny)
        elif self.pos[1] + self.dirny > self.rows - 1:
            self.pos = [self.pos[0] + self.dirnx, 0]
        elif self.pos[0] + self.dirnx < 0:
            self.pos = (self.rows - 1, self.pos[1] + self.dirny)
        elif self.pos[1] + self.dirny < 0:
            self.pos = (self.pos[0] + self.dirnx, self.rows - 1)
        else:
            self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.size // self.rows
        row = self.pos[0]
        col = self.pos[1]

        pygame.draw.rect(surface, self.color, (row * dis + 1, col * dis + 1, dis - 2, dis - 2))

        if eyes:  # Draws the eyes
            centre = dis // 2
            radius = 3
            circleMiddle = (row * dis + centre - radius, col * dis + 8)
            circleMiddle2 = (row * dis + dis - radius * 2, col * dis + 8)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)
