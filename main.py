import pygame as pg
from game import Game


class Main:
    def __init__(self):
        pg.init()
        pg.display.set_caption("SERPINSKI")
        self.FPS = 60
        self.start_ticks = pg.time.get_ticks()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((900, 900))
        self.game = Game()

    def run(self):
        while True:
            self.screen.fill('black')
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
            self.game.run()
            pg.display.update()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    game = Main()
    game.run()
