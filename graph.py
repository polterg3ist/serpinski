import pygame as pg
from random import randint, choice


class Dot:
    def __init__(self, pos: tuple = (0, 0), radius=5, color='green'):
        self.x, self.y = pos
        self.radius = radius
        self.color = color
        self.screen = pg.display.get_surface()

    def draw(self):
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class MainDot(Dot):
    def __init__(self, pos: tuple = (0, 0),  radius=1, color='red'):
        self.screen = pg.display.get_surface()
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.radius = radius
        self.x = pos[0] or randint(50, self.screen_width-self.radius)
        self.y = pos[1] or randint(50, self.screen_height-self.radius)
        self.color = color

        super().__init__((self.x, self.y), radius, color)


class LineDots(Dot):
    def __init__(self, start: tuple, end: tuple):
        super().__init__(start)
        self.dots = []
        self.vec = pg.math.Vector2(x=start[0], y=start[1])
        self.top_vec = pg.math.Vector2(x=end[0], y=end[1])
        self.direction = (self.top_vec-self.vec).normalize()
        self.distance = (self.top_vec - self.vec).magnitude()

        self.create_dots()

    def create_dots(self):
        dots_amount = int(self.distance // 20) or 2

        mult = self.distance / dots_amount
        position = self.vec.copy()

        for _ in range(dots_amount-1):
            position.x += self.direction.x * mult
            position.y += self.direction.y * mult
            dot = Dot(pos=(position.x, position.y), radius=1)
            self.dots.append(dot)

    def draw(self):
        for dot in self.dots:
            dot.draw()


class FirstDot(Dot):
    def __init__(self, color, radius: int = 1, full_random=False, vertex=None, lines=None):
        """
        :param color:
        :param radius:
        :param full_random:
        :param vertex:
        :param lines:

        full random argument means that first dot would create in random place inside of triangle
        Otherwise first dot would create near to some MainDot
        In second variant dot will never spawn in a 'wrong place'
        """
        super().__init__(color=color, radius=radius)
        # if full_random flag activated lines should be provided
        # if full_random flag isn't activated argument 'vertex' should be provided
        if full_random:
            self.x, self.y = self.get_xy_random(lines)
        else:
            self.x, self.y = self.get_xy_vertex(vertex)

    def get_xy_vertex(self, vertex):
        return vertex.x+1, vertex.y+1

    def get_xy_random(self, lines: tuple):
        rand_dot_1 = choice(lines[-1].dots)
        rand_dot_2 = choice(lines[-2].dots)
        dot1_vec = pg.math.Vector2(x=rand_dot_1.x, y=rand_dot_1.y)
        dot2_vec = pg.math.Vector2(x=rand_dot_2.x, y=rand_dot_2.y)
        direction = (dot1_vec - dot2_vec).normalize()
        distance = (dot1_vec - dot2_vec).magnitude() // 2
        dot1_vec.x -= direction.x * distance
        dot1_vec.y -= direction.y * distance

        return dot1_vec.x, dot1_vec.y


class RandDot(Dot):
    def __init__(self, vertices: tuple, last_dot, color='green'):
        super().__init__(color=color, radius=1)
        self.x, self.y = self.get_xy_vertex(vertices, last_dot)

    def get_xy_vertex(self, vertices: tuple, last_dot):
        vertex = choice(vertices)
        vertex_vec = pg.math.Vector2(vertex.x, vertex.y)
        last_dot_vec = pg.math.Vector2(last_dot.x, last_dot.y)
        direction = (vertex_vec - last_dot_vec).normalize()
        distance = (vertex_vec - last_dot_vec).magnitude() / 2
        last_dot_vec.x += round(direction.x * distance)
        last_dot_vec.y += round(direction.y * distance)

        return last_dot_vec.x, last_dot_vec.y
