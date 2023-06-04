import pygame as pg
from setting import *
from pytmx.util_pygame import load_pygame

class Dirt_Bloop(pg.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect=self.image.get_rect(topleft=pos)
        self.z=LAYERS['dirt_dirt']
