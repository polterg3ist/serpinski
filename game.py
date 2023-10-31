import pygame as pg
import pygame.time
from graph import MainDot, Dot


class Game:
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.dot_a = MainDot(x=250, y=650)
        self.dot_b = MainDot(x=475, y=250)
        self.dot_c = MainDot(x=700, y=650)
        self.new_dot = Dot(pos=(450, 350))
        self.dots = [self.dot_a, self.dot_b, self.dot_c, self.new_dot]
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
                self.dots = [self.dot_a, self.dot_b, self.dot_c]
                self.cooldown_start = pygame.time.get_ticks()
                self.cooldown = True

    def cooldowns(self):
        if self.cooldown:
            current_time = pg.time.get_ticks()
            if current_time - self.cooldown_start >= self.cooldown_duration:
                self.cooldown = False