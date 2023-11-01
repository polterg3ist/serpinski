import pygame as pg
pg.init()

font = pg.font.SysFont('Times New Roman', 14)


def show_text(text, x=10, y=10):
    screen = pg.display.get_surface()
    text = font.render(str(text), True, 'white')
    text_surf = text.get_rect(topleft=(x, y))
    screen.blit(text, text_surf)
