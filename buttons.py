import pygame as pg


class Buttons:
    def __init__(self, game):
        self.cooldown = False
        self.cooldown_duration = 300
        self.cooldown_start = 0
        self.game = game

    def run(self):
        self.events()
        self.cooldowns()

    def events(self):
        keys = pg.key.get_pressed()
        if not self.cooldown:
            if keys[pg.K_ESCAPE]:
                self.game.vertices, self.game.lines, self.game.dots = self.game.create_triangle()
                self.cooldown_start = pg.time.get_ticks()
                self.cooldown = True
            if keys[pg.K_MINUS] or keys[pg.K_EQUALS]:
                self.cooldown_start = pg.time.get_ticks()
                self.cooldown = True
            if keys[pg.K_MINUS]:
                self.game.dot_create_cooldown_duration -= 100

            if keys[pg.K_EQUALS]:
                self.game.dot_create_cooldown_duration += 100

    def cooldowns(self):
        if self.cooldown:
            current_time = pg.time.get_ticks()
            if current_time - self.cooldown_start >= self.cooldown_duration:
                self.cooldown = False