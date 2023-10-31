import pygame as pg
from random import randint


class MainDot():
    def __init__(self, x=None, y=None, radius=10, color='red'):
        self.screen = pg.display.get_surface()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.radius = radius
        self.x = x or randint(50, self.screen_width-self.radius)
        self.y = y or randint(50, self.screen_height-self.radius)
        self.color = color

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class Dot:
    def __init__(self, pos: tuple, radius=5, color='yellow'):
        self.x, self.y = pos
        self.radius = radius
        self.color = color
        self.screen = pg.display.get_surface()

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)