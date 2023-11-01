import pygame as pg
from random import randint


class MainDot:
    def __init__(self, x=None, y=None, radius=5, color='red'):
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


class LineDots(MainDot):
    def __init__(self, start:tuple, end:tuple):
        super().__init__(x=start[0], y=start[1])
        self.dots = []
        self.vec = pg.math.Vector2(x=start[0], y=start[1])
        self.top_vec = pg.math.Vector2(x=end[0], y=end[1])
        self.direction = (self.top_vec-self.vec).normalize()
        self.distance = (self.top_vec - self.vec).magnitude()

    def create_dot(self):
        dots_ammount = int(self.distance // 10) or 2

        mult = self.distance / dots_ammount
        position = self.vec.copy()

        for _ in range(dots_ammount-1):
            position.x += self.direction.x * mult
            position.y += self.direction.y * mult
            dot = Dot(pos=(position.x, position.y))
            self.dots.append(dot)

    def draw(self):
        for dot in self.dots:
            dot.draw()