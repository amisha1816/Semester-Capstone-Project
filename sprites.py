from setting import *

class Generic(pg.sprite.Sprite):
    def __init__(self,pos,surf,groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox=self.rect.copy() #.inflate((-self.rect.width*0.25,-self.rect.height*0.75))

class Flowers(Generic):
    def __ini__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy() #.inflate(-self.rect.width*0.5,-self.rect.height*0.75)
class Shitty_Trees(Generic):
    def __ini__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy() #.inflate(-self.rect.width*0.5,-self.rect.height*0.75)
class Idiotic_Farmers_Market(Generic):
     def __ini__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy().inflate((self.rect.width*1.5,self.rect.height*1.5))
