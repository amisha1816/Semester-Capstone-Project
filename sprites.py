import pygame as pg

from setting import *

class Generic(pg.sprite.Sprite):
    def __init__(self,pos,surf,groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        
        # Amisha added this part in on May 11!
       self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75) # adjusting the size of the hitbox based off our sprites!
       # ** WILL NEED TO ADJUST NUMBERS BASED OF OUR ACTUAL SPRITES **
        
