import pygame as pg
from graph import MainDot, LineDots, RandDot
from buttons import Buttons
from show_info import show_text


class Game:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.vertices, self.lines, self.dots = self.create_triangle()
        self.buttons = Buttons(self)
        self.dot_create_cooldown = False
        self.dot_create_cooldown_duration = 0
        self.dot_create_cooldown_start = 0

    def run(self):
        for dot in self.dots:
            dot.draw()
        self.buttons.run()
        self.create_dot()
        self.dot_cooldown()
        show_text(f"DOTS={len(self.dots)} | DELAY={self.dot_create_cooldown_duration}")

    def create_triangle(self):
        dot_a = MainDot()
        dot_b = MainDot()
        dot_c = MainDot()
        dot_line_ab = LineDots((dot_a.x, dot_a.y), (dot_b.x, dot_b.y))
        dot_line_bc = LineDots((dot_b.x, dot_b.y), (dot_c.x, dot_c.y))
        dot_line_ca = LineDots((dot_c.x, dot_c.y), (dot_a.x, dot_a.y))

        vertices = (dot_a, dot_b, dot_c)
        lines = (dot_line_ab, dot_line_bc, dot_line_ca)
        dot_rand = RandDot(vertices, lines, first=True, color='yellow')

        dots = [dot_a, dot_b, dot_c, dot_line_ab, dot_line_bc,
                     dot_line_ca, dot_rand]

        return vertices, lines, dots

    def create_dot(self):
        if not self.dot_create_cooldown:
            dot = RandDot(self.vertices, self.lines, self.dots, color='yellow')
            self.dots.append(dot)
            self.dot_create_cooldown = True
            self.dot_create_cooldown_start = pg.time.get_ticks()

    def dot_cooldown(self):
        if self.dot_create_cooldown:
            current_time = pg.time.get_ticks()
            if current_time - self.dot_create_cooldown_start >= self.dot_create_cooldown_duration:
                self.dot_create_cooldown = False
