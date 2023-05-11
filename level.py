import pygame as pg
from character import Character
from overlay import Overlay
from sprites import Generic
from setting import *
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.surface_dimensions = pg.display.get_surface() # basically gets the screen dimensions from main.py
        self.all_sprites= CameraGroup()
        #pg.sprite.Group() # Group important feauture of pg, helps us draw/update sprite actions
        # self.all_sprites will be the 'container' that stores our sprites
        self.setup()
        self.overlay = Overlay(self.character)
    def setup(self):
        self.character = Character((320,320),self.all_sprites) # creating instances of character class
        Generic(
            pos = (0,0),
            surf=pg.image.load(f'background/background.jpg').convert_alpha(),
            groups= self.all_sprites,
            z=LAYERS['ground'] ) # I ADDED THIS TODAY
        #self.character = Character((320,320),self.all_sprites) # creating instances of character class
    def run(self,delta_time):
        self.surface_dimensions.fill('pink') # so we do not see preivious frame
        #self.all_sprites.draw(self.surface_dimensions) # we want our spirites to be drawn on self.surface_dimensions
        self.all_sprites.custom_draw(self.character)
        self.all_sprites.update(delta_time)#updates sprite actions # is important since it calls update method on all our sprites
        self.overlay.display()

class CameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface() # getting screen dimensions
        self.offset = pg.math.Vector2() # will be used for moving camera -
    def custom_draw(self, character):# i am making this relative to player so it draws based on where player goes
        self.offset.x = character.rect.centerx  - w / 2# player.rect.centerx is used to get position of player
        self.offset.y = character.rect.centery - h /2 # this and line above ensures player is always at center of the screen
        # the offset shows how much we going to shift the screen relative to the player
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer: # layer being one of the values from the LAYERS dictionary
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image,offset_rect) # and if it is ^ then i want to draw that layer # this does not change position, it just draws the sprite whenever sprite.rect will be

