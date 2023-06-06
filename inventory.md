
### Inventory

![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/ca2592ff-871f-4bba-8ceb-3c86d0b90826)
*so this is my current plan rn, I think I'm going to do similar to the farmer's market with blocks, but they'll include the sprite and the text


```python

# imports
import pygame as pg
from setting import *
from character import Character
from timer import Timer
screen = pg.display.set_mode((w,h))


# main class 
class Inventory:
    def __init__(self, inventory_menu): 
  
        self.inventory_menu = inventory_menu
        self.font = pg.font.SysFont('Cambria', 30)
        self.img_list = (______________, ____________________)
        
        # spacing
        self.total_width = 800
        self.total_height = 600
        
        self.v_space = 30 # space between the different rows
        self.h_space = 60 # space btwn the different blocks within the row

        # options list
        self.options = list(character.crop_stuff.keys()) + list(character.seed_stuff.keys())
        self.row_setup()
    
        # selection
        self.index = 0
        self.timer = Timer(200)
        
# ----------------------------------------------------------------------------------------------------------------------------
        
     def base_setup(self): # creates our block names and creates some screen settings! 
        
        # text
        self.item_names = [] 
        
        for item in self.options: # allows us  to add all our item options to our rendered options list
            
            self.item_name = self.font.render(item, False, 'Black')
            self.item_names.append(item_name)            
            
            
            
            
        # screen set_up
        self.total_height += (len(self.item_names) - 1) * self.space
        # creates spaces btwn our blocks according to our attribute self.space in our init method
        self.menu_top = h / 2 - self.total_height / 2 # very top of our menu
        self.background = pg.Rect(200, self.menu_top, self.width, self.total_height) # background that pulls everything tgthr
        
        
        
# ----------------------------------------------------------------------------------------------------------------------------
        
    def select_stuff(self): # allows the player to close the inventory
        keys = pg.key.get_pressed() # getting all the keys
        self.timer.update_tool()
        
        if keys[pg.K_ESCAPE]: # if player hits escape, display closes
            self.inventory_menu()
  
        if not self.timer.start():
            # allows us to select different blocks
            if keys[pg.K_UP]:
                self.index -= 1
                self.timer.start() # ensures that we're not rushing through the different options

            if keys[pg.K_DOWN]:
                self.index += 1
                self.timer.start()
                        
                
        # restrict selection
        if self.index < 0:
            self.index = len(self.options) - 1 
        
        if self.index > len(self.options) - 1:
            self.index = 0
            
# ----------------------------------------------------------------------------------------------------------------------------
        
   
        
              
