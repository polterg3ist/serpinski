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
        dots_amount = int(self.distance // 5) or 2

        mult = self.distance / dots_amount
        position = self.vec.copy()

        for _ in range(dots_amount-1):
            position.x += self.direction.x * mult
            position.y += self.direction.y * mult
            dot = Dot(pos=(position.x, position.y), radius=1, color='black')
            self.dots.append(dot)

    def draw(self):
        for dot in self.dots:
            dot.draw()


class RandDot(Dot):
    def __init__(self, vertices: tuple, lines: tuple, dots: list = None, first=False, color='green'):
        super().__init__(color=color, radius=1)
        if first:
            self.x, self.y = self.get_xy_random(lines)
        else:
            self.x, self.y = self.get_xy_vertex(vertices, dots)

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

    def get_xy_vertex(self, vertices: tuple, dots: list):
        vertex = choice(vertices)
        last_dot = dots[-1]
        print(last_dot.x, last_dot.y, vertex.x, vertex.y)
        vertex_vec = pg.math.Vector2(vertex.x, vertex.y)
        last_dot_vec = pg.math.Vector2(last_dot.x, last_dot.y)
        direction = (vertex_vec - last_dot_vec).normalize()
        distance = (vertex_vec - last_dot_vec).magnitude() // 2
        last_dot_vec.x += direction.x * distance
        last_dot_vec.y += direction.y * distance

        return last_dot_vec.x, last_dot_vec.y



