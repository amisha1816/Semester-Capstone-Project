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
    def __init__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy() # used for collisions 
        # applesss
        self.apple_surface = pg.image.load(f'Sprout Lands - Sprites - Basic pack/Objects/apple.png') # loading in apple image
        self.apple_position = APPLE_POSITION['tree'] # calling the apple position dictionary from settings - this determines where the apples will go on tree
        self.apple_sprites = pg.sprite.Group() # giving the apple images there on sprite group to make it easier to manage 
        self.more_fruit() # calling method which spawns apples

    def more_fruit(self):
        print('working')
        for pos in self.apple_position:
            if randint(0,10) < 4: # this helps limit how many apples are being spawned 
                x = pos[0] + self.rect.left # this and the line below helps us in playing the apple in the right position on the tree and not just on the coordinate on the screen
                y = pos[1] + self.rect.top
                Generic(
                pos = (x,y),
                surf= self.apple_surface,
                groups = [self.apple_sprites,self.groups()[0]], 
                # self.groups is calling upon all the groups that Shitty_tree is in, so if we look at level we see it is in [self.all_sprites,self.collision_sprites]
                # and by calling [0], we are telling this to also be added to self.all_spirtes  this is important so the apples are visable
                z = LAYERS['fruit'])
class Idiotic_Farmers_Market(Generic):
     def __ini__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy().inflate((self.rect.width*1.5,self.rect.height*1.5))
