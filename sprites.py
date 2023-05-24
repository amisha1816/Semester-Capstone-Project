from setting import *
from random import randint,choice
from timer import Timer 

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

        # tree shit
        self.health = 5 # number of hits till tree dies
        self.alive = True # once health is 0, tree dies and no more apples will come once tree gone
        self.tree_stump = pg.image.load(f'Sprout Lands - Sprites - Basic pack/Objects/tree stump.png')
        self.tree_timer = Timer(200)
        self.hitbox=self.rect.copy() #.inflate(-self.rect.width*0.5,-self.rect.height*0.75)
        
        # applesss
        self.apple_surface = pg.image.load(f'Sprout Lands - Sprites - Basic pack/Objects/apple.png') # loading in apple image
        self.apple_position = APPLE_POSITION['tree'] # calling the apple position dictionary from settings - this determines where the apples will go on tree
        self.apple_sprites = pg.sprite.Group() # giving the apple images there on sprite group to make it easier to manage 
        self.more_fruit()
        
     def tree_hits(self):
        self.health -= 1
        # for removing an apple
        if len(self.apple_sprites.sprites()) > 0: # checking how many apples left on tree, if there are no apples then yah
            random_apple = choice(self.apple_sprites.sprites()) # this selects a random apple from tree to kill off in next line
            random_apple.kill() # removing apple from the screen

    def more_fruit(self):
        for pos in self.apple_position:
            if randint(0,10) < 4: # this helps limit how many apples are being spawned 
                x = pos[0] + self.rect.left
                y = pos[1] + self.rect.top
                Generic(
                pos = (x,y),
                surf= self.apple_surface,
                groups = [self.apple_sprites,self.groups()[0]], # # self.groups is calling upon all the groups that Shitty_tree is in, so if we look at level
                #, we see it is in [self.all_sprites,self.collision_sprites], and by calling [0], we are telling this to also be added to self.all_spirtes 
                #this is important so the apples are visable
                z = LAYERS['fruit'])
                
      def is_tree_alive(self):
        if self.health <= 0: # essentially when the tree "dies" and we get the required amount of hits..
            self.image = self.tree_stump # we are calling the tree stump pic
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom) # and since we are changing the image, we need to redefine/remake the image rect
            self.hitbox = self.rect.copy().inflate(-10,-self.rect.height*0.6)
            self.alive = False 
            
    def update(self,delta_time):
        if self.alive:
            self.is_tree_alive()

class Idiotic_Farmers_Market(Generic):
     def __ini__(self,pos,surf,groups):
        super().__init__(pos,surf,groups)
        self.hitbox=self.rect.copy().inflate((self.rect.width*1.5,self.rect.height*1.5))
