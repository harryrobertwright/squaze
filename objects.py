import random
from screen import Screen
from colour import Colour
import pygame

class Player:
    def __init__(self, width=35, height=35, x_pos=0, y_pos=845, colour=Colour.BLACK):
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.colour = colour
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

class Obstacle:
    def __init__(self):
        self.width = random.randrange(25, 100, 5)
        self.height = random.randrange(25, 100, 5)
        self.x_pos = random.randrange(1, 1000, 5)
        self.y_pos = random.randrange(1, 750, 5)
        self.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
