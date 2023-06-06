
### Inventory

![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/ca2592ff-871f-4bba-8ceb-3c86d0b90826)
*so this is my current plan rn, I think I'm going to do similar to the farmer's market with blocks, but they'll include the sprite and the text*

---


```python

# imports
import pygame as pg
from setting import *
from character import Character
from timer import Timer
screen = pg.display.set_mode((w,h))

# ___________________________________________________________________________________________________________________________

# main class 
class Inventory:
    def __init__(self, inventory_menu): # basic set_up
  
        self.inventory_menu = inventory_menu
        self.font = pg.font.SysFont('Cambria', 30)
        self.img_list = (______________, ____________________)
        
        # sizing
        self.total_width = 600
        self.total_height = 450
        
        # spacing and padding
        self.v_space = 30 # space between the different rows
        self.h_space = 60 # space btwn the different blocks within the row
        self.tb_padding = 10 # padding at the top of the block (top to img start) * at the bottom of the block (txt bottom to block bottom)
        self.img_txt_padding = 5 # padding btwn img and txt
        
        # options list
        self.options = list(character.crop_stuff.keys()) + list(character.seed_stuff.keys())
        self.row_setup()
        
        # rows
        self.option_border = (len(self.options) - 1) // 2 # allows us to split our list in two, for two sepetate rows
        self.first_row = self.options[:option_border]
        self.second_row = self.options[option_border:]

        # selection
        self.index = 0
        self.timer = Timer(200)
        
        # images
        self.images = [____________________, _________________] # ❗ insert item images here
        
# ___________________________________________________________________________________________________________________________

    def txt_bg(self): # creates our text and background
        
        # text
        self.item_names = [] 
        self.total_height = 0
        
        # rendering text and additing it to our text_item
        for item in self.options:
            self.item_name = self.font.render(item, False, 'Black')    
            self.item_names.append(item)            
            
        # screen set_up
        self.height = ((tb_padding + 100 + img_txt_padding + 30 + tb_padding) * 2) + self.v_space # ❗ 30 is for text, 100 is for img
        self.top = h / 2 - self.height / 2
        self.background = pg.Rect(400, self.top, self.width, self.height) # background that pulls everything together ❗ 400

# ___________________________________________________________________________________________________________________________
    
    def select_stuff(self):
        keys = pg.key.get_pressed() 
        self.timer.update_tool()

            if keys[pg.K_ESCAPE]: # if player hits escape, display closes
                self.fm_menu()

            if not self.timer.start():

                if keys[pg.K_LEFT]:
                    self.index -= 1
                    self.timer.start()

                if keys[pg.K_RIGHT]:
                    self.index += 1
                    self.timer.start()

                if keys[pg.K_DOWN]:
                    self.index += 3
                    self.timer.start()

                if keys[pg.K_UP]:
                    self.index -= 1
                    self.timer.start()
                    
        # restrict selection
        if self.index < 0:
            self.index = len(self.options) - 1 
        
        if self.index > len(self.options) - 1:
            self.index = 0

                  
