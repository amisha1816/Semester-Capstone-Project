

```python
import pygame as pg
from character import Character
from overlay import Overlay
from sprites import Generic, Flowers,Shitty_Trees,Idiotic_Walls
from setting import *
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.surface_dimensions = pg.display.get_surface() # basically gets the screen dimensions from main.py
        self.all_sprites= CameraGroup() # very important!!! sprites need to be in this class so they can appear on the screen!!!
        self.collision_sprites = pg.sprite.Group()  # to keep track of what sprites CAN BE collided with
        #pg.sprite.Group() # Group important feauture of pg, helps us draw/update sprite actions
        # self.all_sprites will be the 'container' that stores our sprites
        self.tree_sprites = pg.sprite.Group() # will be used to help player know where trees are 
        self.setup() # callings method so all tiled features appear
        self.overlay = Overlay(self.character)
        
        # 🌷 farmer's market 🌷
        self.fm_active = False
        
    def setup(self):
        tmx_data = load_pygame(f'map data/mappy map.tmx') # helps us access tiled info
        #ground/grass
        for layer in ['Grass','Grass detailing']:
            for x,y,surf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x*tile_size,y*tile_size),surf,self.all_sprites,LAYERS['ground'])
        # fence
        for x,y,surf in tmx_data.get_layer_by_name('Fence').tiles():
            Generic((x*tile_size,y*tile_size),surf,[self.all_sprites,self.collision_sprites],LAYERS['fence'])
        # flowers
        for obj in tmx_data.get_layer_by_name('Flower obj'):
            Flowers((obj.x,obj.y),obj.image,[self.all_sprites,self.collision_sprites])
        #trees
        for obj in tmx_data.get_layer_by_name('Tree obj'):
            Shitty_Trees((obj.x,obj.y),obj.image,[self.all_sprites,self.collision_sprites,self.tree_sprites],self.adding_to_inventory)
        #hills
        for x,y,surf in tmx_data.get_layer_by_name('hills').tiles():
            Generic((x*tile_size,y*tile_size),surf,self.all_sprites,LAYERS['Hills'])
        #house door
        for x,y,surf in tmx_data.get_layer_by_name('House').tiles():
            Generic((x*tile_size,y*tile_size),surf,self.all_sprites,LAYERS['House Walls/bottom'])
        # house walls
        for obj in tmx_data.get_layer_by_name('Housey'):
            Idiotic_Walls((obj.x,obj.y),obj.image,[self.all_sprites,self.collision_sprites])
        # furniture 
        for x,y,surf in tmx_data.get_layer_by_name('house stuff').tiles():
            Generic((x*tile_size,y*tile_size),surf,self.all_sprites,LAYERS['Furniture'])
        # water
        for x,y,surf in tmx_data.get_layer_by_name('water').tiles():
            Generic((x*tile_size,y*tile_size),surf,self.all_sprites,LAYERS['Water'])
        # characterrrrr
        self.character = Character(
            location = (1550,1400),
            group = self.all_sprites,
            collision_sprites = self.collision_sprites,
            trees = self.tree_sprites)  # creating instances of character class
            farmer_market = self.farmer_market # 🌷
    
    # farmer's market method 🌷
    def farmer_market(self):
        self.fm_active = not self.fm_active # allows us to switch our farmer's market on and off with the farmer's market method
    
    def adding_to_inventory(self,thing):
        self.character.crop_stuff[thing] += 1 # crop_stuff is inventory dictionary i made in character.py --> here we are increasing the number of that good

    def run(self,delta_time):
        #self.surface_dimensions.fill('pink') # so we do not see preivious frame
        #self.all_sprites.draw(self.surface_dimensions) # we want our spirites to be drawn on self.surface_dimensions
        self.all_sprites.custom_draw(self.character)
        self.all_sprites.update(delta_time)#updates sprite actions # is important since it calls update method on all our sprites
        self.overlay.display()
        print(self.character.crop_stuff)

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
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer: # layer being one of the values from the LAYERS dictionary
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image,offset_rect) # and if it is ^ then i want to draw that layer # this does not change position, it just draws the sprite whenever sprite.rect will be
                # to see character hitbox and rectangle --> for now it is commented out but it useful to check when looking at collisions
                # if sprite == character:
                 #    pg.draw.rect(self.display_surface,'red',offset_rect,5)
                  #    hitbox_rect = character.hitbox.copy()
                   #   hitbox_rect.center = offset_rect.center 
                    #  pg.draw.rect(self.display_surface,'green',hitbox_rect,5)
                      
```
