import pygame as pg
from setting import *
from pytmx.util_pygame import load_pygame

class Dirt_Bloop(pg.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect=self.image.get_rect(topleft=pos)
        self.z=LAYERS['dirt_dirt']

class Ground_Dirt:
    def __init__(self,all_sprites):
        self.all_sprites = all_sprites
        self.dirt=pg.sprite.Group()
        self.dirt_image=pg.image.load('Sprout Lands - Sprites - Basic pack/Objects/dirt.png')
        self.dirt_grid()
        self.hit_rect()
        #requirements
        # if the area is farmable
        # if the soil has been watered
        # is the soil has a plant on it