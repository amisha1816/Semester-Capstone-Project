import pygame as pg
from setting import *
from pytmx.util_pygame import load_pygame

class Dirt_Bloop(pg.sprite.Sprite):
    def __init__(self,pos,surf,groups):
        super().__init__(groups)
        self.image = surf
        self.rect=self.image.get_rect(bottomleft=pos)
        self.z=LAYERS['dirt_dirt']

class Ground_Dirt:
    def __init__(self,all_sprites):
        self.all_sprites = all_sprites
        self.dirt=pg.sprite.Group()
        self.dirt_image=pg.image.load('Sprout Lands - Sprites - Basic pack/Objects/dirt.png')
        self.dirt_grid()
        self.hit_rect()
        
    def dirt_grid(self):
        ground = pg.image.load('Sprout Lands - Sprites - Basic pack/House/ground.png')
        horizontal_tile_count= 125
        vertical_tile_count = 95
        self.grid= [ [[] for col in range(horizontal_tile_count)] for row in range(vertical_tile_count)]

        for x,y, _ in load_pygame(f'map data/mappy map.tmx').get_layer_by_name('farming land').tiles():
            self.grid[y][x].append("F") # all the blocks we can farm on will be assigned "F" --> after we will cycle through this list and can tell which ones we can use/not
    def hit_rect(self):
        self.hit_rects=[]
        for index_row,row in enumerate(self.grid):
            for index_cell,cell in enumerate(row):
                if "F" in cell:
                    x= index_cell * tile_size
                    y= index_row * tile_size
                    rect= pg.Rect(x,y,tile_size,tile_size)
                    self.hit_rects.append(rect)
    def hit(self,point):
        for rect in self.hit_rects:
            if rect.collidepoint(point):
                x=rect.x//tile_size
                y=rect.y//tile_size
                if 'F' in self.grid[y][x]:
                    self.grid[y][x].append('X') # so if something is planted on this spot, label it as 'X', this will mean we cannot plant anything on top of this
                    self.dirt_patches()
    def dirt_patches(self):
        self.dirt.empty()
        for index_row,row in enumerate(self.grid):
            for index_cell,cell in enumerate(row):
                if "X" in cell:
                    Dirt_Bloop((index_cell * tile_size , index_row * tile_size + 64),self.dirt_image,[self.all_sprites,self.dirt]) # the -32 and +64 helps adjust the location so the block appears right in front of the character
    
    def watering_the_shitlings(self,water_droplings):
        for dirt_sprite in self.dirt.sprites():
            if dirt_sprite.rect.collidepoint(water_droplings):
                print('waterrrrrrrrrrrrrrrrrr')
