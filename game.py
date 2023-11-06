import pygame as pg
from graph import MainDot, LineDots, RandDot, FirstDot
from buttons import Buttons
from random import choice


class Game:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.show_outline = True
        self.vertices, self.lines, self.last_dot = self.create_triangle()
        self.buttons = Buttons(self)
        self.dot_create_cooldown = False
        self.dot_create_cooldown_duration = 0
        self.dot_create_cooldown_start = 0
        self.game_stop = False
        self.n = 1

    def run(self):
        self.buttons.run()
        if not self.game_stop:
            self.create_dot()
            self.dot_cooldown()

    def create_triangle(self):
        self.screen.fill('black')
        self.n = 0
        dot_a = MainDot()
        dot_b = MainDot()
        dot_c = MainDot()
        dot_line_ab = LineDots((dot_a.x, dot_a.y), (dot_b.x, dot_b.y))
        dot_line_bc = LineDots((dot_b.x, dot_b.y), (dot_c.x, dot_c.y))
        dot_line_ca = LineDots((dot_c.x, dot_c.y), (dot_a.x, dot_a.y))

        vertices = (dot_a, dot_b, dot_c)
        lines = (dot_line_ab, dot_line_bc, dot_line_ca)
        random_vertex = choice(vertices)
        first_dot = FirstDot(vertex=random_vertex, color='yellow')

        dots = [dot_a, dot_b, dot_c, first_dot]

        for dot in dots:
            dot.draw()

        if self.show_outline:
            for line in lines:
                line.draw()

        return vertices, lines, dots[-1]

    def create_dot(self):
        if not self.dot_create_cooldown:
            self.n += 1
            dot = RandDot(self.vertices, self.last_dot, 'yellow')
            dot.draw()
            self.last_dot = dot
            self.dot_create_cooldown = True
            self.dot_create_cooldown_start = pg.time.get_ticks()

    def dot_cooldown(self):
        if self.dot_create_cooldown:
            current_time = pg.time.get_ticks()
            if current_time - self.dot_create_cooldown_start >= self.dot_create_cooldown_duration:
                self.dot_create_cooldown = False
