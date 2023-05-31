import pygame as pg
from setting import*

class Transistion:
    def __init__(self,reset,player):
        self.surface = pg.display.get_surface() # we want this to happen on main display screen soo
        self.reset=reset
        self.character = player
        # for overlay/background image
        self.image = pg.Surface((w,h))
        self.bg_color = 255
        self.speed = -15
    def play(self):
        self.bg_color += self.speed
        self.image.fill((self.bg_color,self.bg_color,self.bg_color))
        self.surface.blit(self.image,(0,0), special_flags=pg.BLEND_RGBA_MULT)
