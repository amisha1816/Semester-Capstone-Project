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
    def dirt_grid(self):
        ground = pg.image.load('Sprout Lands - Sprites - Basic pack/House/ground.png')
        horizontal_tile_count= 125
        vertical_tile_count = 95
        self.grid= [ [[] for col in range(horizontal_tile_count)] for row in range(vertical_tile_count)]

        for x,y, _ in load_pygame(f'map data/mappy map.tmx').get_layer_by_name('farming land').tiles():
            self.grid[y][x].append("F") # all the blocks we can farm on will be assigned "F" --> after we will cycle through this list and can tell which ones we can use/not
     def hit_rect(self):
        self.hit_rect=[]
        for index_row,row in enumerate(self.grid):
            for index_cell,cell in enumerate(row):
                if "F" in cell:
                    x= index_cell * tile_size
                    y= index_row * tile_size
                    rect= pg.Rect(x,y,tile_size,tile_size)
                    self.hit_rect.append(rect)
