import pygame as pg
from setting import*

class Transistion:
    def __init__(self,reset,player):
        self.surface = pg.display.get_surface() # we want this to happen on main display screen soo
        self.reset=reset
        self.character = player
        # for overlay/background image
        self.image = pg.Surface((w,h))
        self.bg_color = 222
        self.transistion_speed = -15
    def play(self):
        self.bg_color += self.transistion_speed # will help us have fading away affect --> darkness decreases as time passes
        if self.bg_color <= 0:
            self.transistion_speed *= -1 # once it reaches 0, reset it
            self.bg_color = 0 
            self.reset()
        if self.bg_color > 222:
            self.bg_color = 222
            self.character.new_day = False
            self.transistion_speed = -15
        self.image.fill((self.bg_color,self.bg_color,self.bg_color))
        self.surface.blit(self.image,(0,0), special_flags=pg.BLEND_RGBA_MULT)
