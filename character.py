#character
import pygame as pg
import os
from timer import Timer
from setting import *

class Character(pg.sprite.Sprite): # py.sprite.Sprite -> Simple base class for visible game objects
    # Sprite --> container class to hold and manage multiple Sprite objects
    def __init__(self,location,group,collision_sprites,trees,interation,farmer_market,dirt, inventory): 
        super().__init__(group) # we pass group so when we create instance of this class, object will be inside our group
        # groups -->  allows you to hold and manage multiple Sprite objects
        self.image = pg.Surface((100,100)) # pg.Surface -> for representing images to create a new image object.
        self.rect=self.image.get_rect(center = location) # self.image.get_rect -> returns rect covering the entire surface
        self.hitbox=self.rect.copy() #.inflate((-50,-50)) # we are making a collision dector by first copying the characters rect and the "inflating" said rectangle by sizing it down
        self.collision_sprites = collision_sprites
        self.z = LAYERS['main'] # this means every sprite will have a z postion
        self.direction = pg.math.Vector2() # will be important when character turns and switches directions --> we will need to flip the sprite
        self.position = pg.math.Vector2(self.rect.center) # this is what controls/keeps track of our characters location--> can take floating points
        self.speed = 150
        self.animation_array=[] # making this as 'self' so can be called in other methods 
        self.action=2 # self.action=0 --> run self.action=1--> harvesting self.action=2 --> idle (based on animation_types list below)
        self.index=0 # this is used to call specfic img for sprite animations
        self.current_time=pg.time.get_ticks() # will be used when moving on to next animation 
        self.flip = 0 # just setting to 0 aka an empty value --> since if i give it value true/false initially.. after the left/right key is unpressed this goes back to the value assigned which is majorly screwing up character orientation
        self.timers = {
            'tool use': Timer(300,self.using_tool), #sets our timer for one minute 
            'tool switch': Timer(200),
            'seed use': Timer(300,self.using_seed), #sets our timer for one minute 
            'seed switch': Timer(200)
        }

        self.tool =['watercan','axe','hoe]
        self.tool_index=0
        self.selected_tool = self.tool[self.tool_index]

        self.seeds=['corn','tomatos']
        self.seed_index=0
        self.selected_seed = self.seeds[self.seed_index]

        self.tree_sprites = trees
        self.interaction = interaction
        self.new_day = False
        self.dirt_layer = dirt

        self.farmer_market = farmer_market
        self.inventory = inventory
        
        self.crop_stuff = {
            'apple': 0,
            'corn': 0,
            'tomato': 0
        }
        
        # 🎂 list of seeds that we can buy from the farmer's market
        self.seed_stuff = {
            'corn_seed': 100, # temporary 100 just so I can see if the amounts are blitting properly
            'tomato_seed': 0 
        }
        
        self.money = 100 # money we automatically give Lucy!
        
        animation_types=['Run','Harvesting','Idle','Hoe']
        for animation in animation_types:
            temp_array=[] # we are first going to load the animation pics in here THEN append this to animation_array
            #we doing this rather than appending staraight to animation_array since after each animation type the array needs to be emptied for the next animation type to be loaded in 
            num_of_frames = len(os.listdir(f'animations/{animation}')) ## counting the number of items in each animation folder 
            for num in range(1,num_of_frames): # the num above will be here so we can cycle through right num of animations for each folder -so we not calling img 14 in folder with only 10 img
                image = pg.image.load(f'animations/{animation}/{animation} ({num}).png') #loading images from overall animation folder and then accessing the spefcic folder - ie animation/harvesting/harvesting (1).png
                image = pg.transform.scale(image, (int(image.get_width() * 0.25), int(image.get_height()*0.25))) #scaling images down so they not massive
                temp_array.append(image)
            self.animation_array.append(temp_array)
        #print(self.animation_array)

    def updating_animation(self):
        animation_cooldown=20 # time for img lasts before going to next img ( idle.1 (wait 50 ms) idle.2 (wait 50ms) idle.3....)
        self.image=self.animation_array[self.action][self.index] # indexing our index --> eg self.animation_array has 3 lists in it so we using[self.action] to call a specfic list then [self.index] to call a spefic item of that list
        if pg.time.get_ticks() - self.current_time > animation_cooldown: # if the time now minus self.current_time is greater than 50.. time to move on to next image
            self.current_time = pg.time.get_ticks() # updating time
            self.index+=1
        if self.index == len(self.animation_array[self.action]):# if the index is greater than/equal to total num of img..then reset back to begining 
            self.index=0
        #if self.timers['tool use'].active: # checking if watercanning is being used rn is yah then....
         #   print('in use')
          #  self.index = 0 
            #self.update_action(1)
            
    def update_timer(self):
        for timer in self.timers.values():
            timer.update_tool()

    def update_action(self,new_action): # if we start moving we can no longer be at self.action(2) (idling) so we got to update it to moving (self.action(0))
        if new_action != self.action:
            self.action = new_action
            self.index = 0 # resetting index 
            self.current_time=pg.time.get_ticks() # resetting time

     def using_tool(self):
        keys= pg.key.get_pressed()
        if self.selected_tool == 'axe' and keys[pg.K_a]:
            for tree in self.tree_sprites.sprites(): # if there are still trees in this group
                if tree.rect.collidepoint(self.target_location):
                    tree.tree_hits()
                    print('hit')
        if self.selected_tool== 'hoe' and keys[pg.K_s]:
            self.dirt_layer.hit(self.target_location)
             
    def get_target_location(self):
        if self.direction.x == 1:
            self.target_location = self.rect.center + pg.math.Vector2(80,0)
        elif self.direction.x == -1:
             self.target_location = self.rect.center + pg.math.Vector2(-80,0)
    
    def using_seed(self):
        pass

    def keyboard_input(self):
        keys= pg.key.get_pressed() # is a list that returns all the possible keys that can be pressed 
        # for character moving up - down
        if keys[pg.K_a]:
            if self.selected_tool == 'axe':
                self.update_action(1)
                self.timers['tool use'].start()
        elif keys[pg.K_s]:
            if self.selected_tool == 'hoe':
                self.update_action(3)
                self.timers['tool use'].start()
        else:
            if keys[pg.K_UP]: 
                self.direction.y = -1 # start moving up by 1 
                self.update_action(0)
            elif keys[pg.K_DOWN]: 
                self.direction.y = 1# # start moving down by 1 
                self.update_action(0)
            else:
                self.direction.y=0 # if character not moving up/down it is just staying still
            #for character moving left-right
            if keys[pg.K_RIGHT]: 
                self.direction.x = 1  # start moving right by 1 
                self.update_action(0) # start running 
                self.flip=False 
            elif keys[pg.K_LEFT]: 
                self.direction.x = -1 # start moving left by 1 
                self.update_action(0) # start running 
                self.flip=True 
            else:
                self.direction.x =0 # if character not moving left/right it is just staying still
            if self.direction.x == 0 and self.direction.y == 0:
                self.update_action(2) # stop movind and idle 
            # for watercan movement
    
        if keys[pg.K_q] and not self.timers['tool switch'].active: # just used to switch between tools
            self.timers['tool switch'].start()
            self.tool_index += 1
            # if tool index > len of tools --> tool index =0
            self.tool_index = self.tool_index if self.tool_index < len(self.tool) else 0
            self.selected_tool = self.tool[self.tool_index]
            print(self.selected_tool)
        # for restarting day
        if keys[pg.K_TAB]:
            collided_interaction_sprites = pg.sprite.spritecollide(self,self.interaction,False) # if the player ( self) collides with the bed ( self.interaction), do we want it destoyed? NO ( false)
            if collided_interaction_sprites:
                if collided_interaction_sprites[0].name == 'cozy bed':
                    self.update_action(2) # ensuring character is idle 
                    print('clicked bish')
                    self.new_day = True
        # for seeds
        if keys[pg.K_LCTRL]:
            self.timers['seed use'].start()
            #self.update_action(1) # --> after we add animation with seeds
        if keys[pg.K_e] and not self.timers['seed switch'].active: # just used to switch between seeds 
            self.timers['seed switch'].start()
            self.seed_index += 1
            # if tool index > len of tools --> tool index =0
            self.seed_index = self.seed_index if self.seed_index < len(self.seeds) else 0
            self.selected_seed = self.seeds[self.seed_index]
            print(self.selected_seed)
        self.image=pg.transform.flip(self.image,self.flip,False) # based on direction of character, the image may need to be flipped
        
        if keys[pg.K_RETURN]: # if enter was pressed then we are opening up the farmers market page 
            self.farmer_market()   
                    
        if keys[pg.K_i]: 
            self.inventory_screen()


    def collide(self,direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite,'hitbox'): # hasattr means "has attribute"
                if sprite.hitbox.colliderect(self.hitbox): #colliderect detects collisions between rectangles 
                    if direction == 'horizontal':
                        if self.direction.x >0: # moving right
                            self.hitbox.right=sprite.hitbox.left
                        if self.direction.x < 0: # moving left
                            self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx # saying whereever character appears, we want hitbox to appear
                        self.position.x = self.hitbox.centerx
                    if direction == 'vertical':
                        if self.direction.y < 0: # moving up
                            self.hitbox.top= sprite.hitbox.bottom
                        if self.direction.y > 0: # moving down
                            self.hitbox.bottom=sprite.hitbox.top
                        self.rect.centery = self.hitbox.centery # saying whereever character appears, we want hitbox to appear
                        self.position.y = self.hitbox.centery
                        
    def movement(self,delta_time):
        # moving in left/right
        self.position.x += self.direction.x*self.speed*delta_time # character location based on the direction character moving, the speed and the delta_time# delta_time helps with the movement of the object
        self.hitbox.centerx = round(self.position.x) # this is so hitbox and character move together to track collisions # we need to round this value so python does not interupt the decimal in a weird way
        self.rect.centerx = self.hitbox.centerx
        self.collide('horizontal')
        # delta_time is important since it adds the delayed effect when character moves therefore makes it look more realistic
        # moving up/down
        self.position.y += self.direction.y*self.speed*delta_time # character location based on the direction character moving, the speed and the delta_time# delta_time helps with the movement of the object
        self.hitbox.centery=round(self.position.y)
        self.rect.centery = self.hitbox.centery
        self.collide('vertical')
      
        # We can just write write self.position together without breaking it into its components BUT when we factor in jumping, we need to only access the y coor
    
    def update(self,delta_time): # will update our sprite --> this connects to update method on level
        self.update_timer()
        self.get_target_location()
        self.updating_animation() 
        self.keyboard_input() # move method controls character movement therefore we call it in update method so characters movement shown
        self.movement(delta_time)
```
