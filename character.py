#character
import pygame as pg
import os
from timer import Timer

class Character(pg.sprite.Sprite): # py.sprite.Sprite -> Simple base class for visible game objects
    # Sprite --> container class to hold and manage multiple Sprite objects
    def __init__(self,location,group):
        super().__init__(group) # we pass group so when we create instance of this class, object will be inside our group
        # groups -->  allows you to hold and manage multiple Sprite objects
        self.image = pg.Surface((32,64)) # pg.Surface -> for representing images to create a new image object.
        self.rect=self.image.get_rect(center = location) # self.image.get_rect -> returns rect covering the entire surface
        self.direction = pg.math.Vector2() # will be important when character turns and switches directions --> we will need to flip the sprite
        self.position = pg.math.Vector2(self.rect.center) # this is what controls/keeps track of our characters location--> can take floating points
        self.speed = 100
        self.animation_array=[] # making this as 'self' so can be called in other methods 
        self.action=2 # self.action=0 --> run self.action=1--> harvesting self.action=2 --> idle (based on animation_types list below)
        self.index=0 # this is used to call specfic img for sprite animations
        self.current_time=pg.time.get_ticks() # will be used when moving on to next animation 
        self.flip = 0 # just setting to 0 aka an empty value --> since if i give it value true/false initially.. after the left/right key is unpressed this goes back to the value assigned which is majorly screwing up character orientation
        
        #timers
        self.timers = {
            'tool use': Timer(60000,self.use_tool) #sets our timer for one minute 
        }
        
        # player's tools
        self.current_tool = 'watering can'
        
        
        animation_types=['Run','Harvesting','Idle']
        for animation in animation_types:
            temp_array=[] # we are first going to load the animation pics in here THEN append this to animation_array
            #we doing this rather than appending staraight to animation_array since after each animation type the array needs to be emptied for the next animation type to be loaded in 
            num_of_frames = len(os.listdir(f'animations/{animation}')) ## counting the number of items in each animation folder 
            for num in range(1,num_of_frames): # the num above will be here so we can cycle through right num of animations for each folder -so we not calling img 14 in folder with only 10 img
                image = pg.image.load(f'animations/{animation}/{animation} ({num}).png') #loading images from overall animation folder and then accessing the spefcic folder - ie animation/harvesting/harvesting (1).png
                image = pg.transform.scale(image, (int(image.get_width() * 0.3), int(image.get_height()*0.3))) #scaling images down so they not massive
                temp_array.append(image)
            self.animation_array.append(temp_array)

    def use_tool(self):
        print(self.current_tool)
                
    def updating_animation(self):
        animation_cooldown=50 # time for img lasts before going to next img ( idle.1 (wait 50 ms) idle.2 (wait 50ms) idle.3....)
        self.image=self.animation_array[self.action][self.index] # indexing our index --> eg self.animation_array has 3 lists in it so we using[self.action] to call a specfic list then [self.index] to call a spefic item of that list
        if pg.time.get_ticks() - self.current_time > animation_cooldown: # if the time now minus self.current_time is greater than 50.. time to move on to next image
            self.current_time = pg.time.get_ticks() # updating time
            self.index+=1
        if self.index == len(self.animation_array[self.action]):# if the index is greater than/equal to total num of img..then reset back to begining 
            self.index=0

    def update_action(self,new_action): # if we start moving we can no longer be at self.action(2) (idling) so we got to update it to moving (self.action(0))
        if new_action != self.action:
            self.action = new_action
            self.index = 0 # resetting index 
            self.current_time=pg.time.get_ticks() # resetting time

    def keyboard_input(self):
        keys= pg.key.get_pressed() # is a list that returns all the possible keys that can be pressed 
        # for character moving up - down
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
        self.image=pg.transform.flip(self.image,self.flip,False) # based on direction of character, the image may need to be flipped
    
        # tool use
        if keys[pg.K_q]:
            self.timers['tool use'].activate()
            
        
    def movement(self,delta_time):
        # moving in left/right
        self.position.x += self.direction.x*self.speed*delta_time # character location based on the direction character moving, the speed and the delta_time# delta_time helps with the movement of the object
        self.rect.centerx = self.position.x
        # delta_time is important since it adds the delayed effect when character moves therefore makes it look more realistic
        # moving up/down
        self.position.y += self.direction.y*self.speed*delta_time # character location based on the direction character moving, the speed and the delta_time# delta_time helps with the movement of the object
        self.rect.centery = self.position.y
        # We can just write write self.position together without breaking it into its components BUT when we factor in jumping, we need to only access the y coor
    
    def update(self,delta_time): # will update our sprite --> this connects to update method on level
        self.updating_animation() 
        self.keyboard_input() # move method controls character movement therefore we call it in update method so characters movement shown
        self.movement(delta_time)
