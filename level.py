#level

import pygame as pg
from character import Character
class Level:
    def __init__(self):
        self.surface_dimensions = pg.display.get_surface() # basically gets the screen dimensions from main.py
        self.all_sprites=pg.sprite.Group() # Group important feauture of pg, helps us draw/update sprite actions
        # self.all_sprites will be the 'container' that stores our sprites
        self.setup()
    def setup(self):
        self.character = Character((320,320),self.all_sprites) # creating instances of character class
    def run(self,delta_time):
        self.surface_dimensions.fill('black') # so we do not see preivious frame
        self.all_sprites.draw(self.surface_dimensions) # we want our spirites to be drawn on self.surface_dimensions
        self.all_sprites.update(delta_time)#updates sprite actions # is important since it calls update method on all our sprites
