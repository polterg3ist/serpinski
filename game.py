import pygame as pg
import pygame.time
from graph import MainDot, Dot, LineDots


class Game:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.dot_a = MainDot(x=250, y=650)
        self.dot_b = MainDot(x=475, y=250)
        self.dot_c = MainDot(x=700, y=650)
        self.dot_line_ab = LineDots((self.dot_a.x, self.dot_a.y), (self.dot_b.x, self.dot_b.y))
        self.dot_line_bc = LineDots((self.dot_b.x, self.dot_b.y), (self.dot_c.x, self.dot_c.y))
        self.dot_line_ca = LineDots((self.dot_c.x, self.dot_c.y), (self.dot_a.x, self.dot_a.y))
        self.dot_line_ab.create_dot()
        self.dot_line_bc.create_dot()
        self.dot_line_ca.create_dot()
        #self.new_dot = Dot(pos=(450, 350))
        self.dots = [self.dot_a, self.dot_b, self.dot_c, self.dot_line_ab, self.dot_line_bc, self.dot_line_ca]
        self.cooldown = False
        self.cooldown_duration = 300
        self.cooldown_start = 0

    def run(self):
        for dot in self.dots:
            dot.draw()
        self.events()
        self.cooldowns()

    def events(self):
        keys = pg.key.get_pressed()
        if not self.cooldown:
            if keys[pg.K_ESCAPE]:
                self.dot_a = MainDot()
                self.dot_b = MainDot()
                self.dot_c = MainDot()
                self.dot_line_ab = LineDots((self.dot_a.x, self.dot_a.y), (self.dot_b.x, self.dot_b.y))
                self.dot_line_bc = LineDots((self.dot_b.x, self.dot_b.y), (self.dot_c.x, self.dot_c.y))
                self.dot_line_ca = LineDots((self.dot_c.x, self.dot_c.y), (self.dot_a.x, self.dot_a.y))
                self.dot_line_ab.create_dot()
                self.dot_line_bc.create_dot()
                self.dot_line_ca.create_dot()
                self.dots = [self.dot_a, self.dot_b, self.dot_c, self.dot_line_ab, self.dot_line_bc,
                             self.dot_line_ca]
                self.cooldown_start = pygame.time.get_ticks()
                self.cooldown = True

    def cooldowns(self):
        if self.cooldown:
            current_time = pg.time.get_ticks()
            if current_time - self.cooldown_start >= self.cooldown_duration:
                self.cooldown = False