import pygame as pg
from setting import *
from timer import Timer
screen = pg.display.set_mode((w,h))

# main class 
class Inventory:
    def __init__(self, character, inventory_menu):
  
        # base set-up
        self.character = character
        self.inventory_menu = inventory_menu
        self.font = pg.font.SysFont('Cambria', 24)
        self.images = ['Sprout Lands - Sprites - Basic pack/Objects/wood.png','Sprout Lands - Sprites - Basic pack/Objects/applee.png','Sprout Lands - Sprites - Basic pack/Objects/corn.png','Sprout Lands - Sprites - Basic pack/Objects/tomatos.png','Sprout Lands - Sprites - Basic pack/Objects/seed  bag.png','Sprout Lands - Sprites - Basic pack/Objects/seed  bag.png','Sprout Lands - Sprites - Basic pack/Characters/cow.webp' ] # ❗ insert item images here
        
         # options list
        self.options = list(self.character.crop_stuff.keys()) + list(self.character.seed_stuff.keys())
        
        # rows
        self.first_row = self.options[:3]
        self.second_row = self.options[3:]

        # selection
        self.index = 0 # current block position, e.g. if on the top right box it would be 2, the bottom right would be 5
        self.timer = Timer(200)
        
        # spacing and padding
        self.v_space = 30 # space between the different rows
        self.h_space = 30 # space btwn the different blocks within the row
        
        # sizing 
        self.total_width = 1000
        self.total_height = 600
        self.block_width = (self.total_width - (self.h_space * 4)) / 3
        self.block_height = (self.total_height - (self.v_space * 3)) / 2
        
        self.txt_bg()
                             
# ___________________________________________________________________________________________________________________________

    def txt_bg(self): # creates the text and background
        
        # text
        self.item_names = [] 
        
        # rendering text and additing it to our self.item_names
        for item in self.options:
            self.item_name = self.font.render(item, False, 'Black')    
            self.item_names.append(item)            
            
 
        self.top = h / 2 - self.total_height / 2
        self.background = pg.Rect(150, self.top, self.total_width, self.total_height)
        # ^ this is the brown base background of the inventory
        
# ___________________________________________________________________________________________________________________________
    
    def select_stuff(self):
        keys = pg.key.get_pressed() 
        self.timer.update_tool()

        if keys[pg.K_SLASH]: # if player hits escape, display closes
            self.inventory_menu()

        if not self.timer.start():

            if keys[pg.K_g]:
                self.index -= 1
                self.timer.start()

            if keys[pg.K_h]:
                self.index += 1
                self.timer.start()

            if keys[pg.K_DOWN]:
                self.index += len(self.first_row)
                self.timer.start()

            if keys[pg.K_UP]:
                self.index -= len(self.first_row)
                self.timer.start()
                    
        # restrict selection
        if self.index < 0:
            self.index = len(self.options) - 1 
        
        if self.index > len(self.options) - 1:
            self.index = 0
                            
# ___________________________________________________________________________________________________________________________ 

    def block(self, item_name, left, top, amount, img, chosen): # creates all the blocks

        # block background
        block_bg = pg.Rect(left, top, self.block_width, self.block_height)

        # left (l) → defined later within update method
        # top (t) → distance from top that's defined in update method
        # self.block_width → created in init
        # self.block_height → created in txt_bg method

        pg.draw.rect(screen, 'White', block_bg, 0, 5) # blits the blocks to the screen

        # text
        text = self.font.render(str(item_name), False, 'Black')
        text_rect = text.get_rect(bottomleft = (block_bg.left + 40, block_bg.bottom - 60))
        screen.blit(text, text_rect) # blits the text to the screen
    
        # amounts
        amount_text = self.font.render(str(amount), False, 'Black')
        amount_block = amount_text.get_rect(bottomleft = (block_bg.left + 40, block_bg.bottom - 20))
        screen.blit(amount_text, amount_block) # blits the text to the screen

        # images
        img_position = img.get_rect(center = (block_bg.centerx-10, block_bg.centery-40)) # img positioning based off the center of the block
        screen.blit(img, img_position)
        
        if chosen:
            pg.draw.rect(screen, 'black', block_bg, 6, 5) # creating the border when an item is selected
            
# ___________________________________________________________________________________________________________________________ 
            
    def update(self):
        self.select_stuff()
        pg.draw.rect(screen, 'Brown', self.background)

        for item_index, item_name in enumerate(self.item_names):
            
            if item_index <= 2: # checking if the item is in the first row
                top = self.top + self.v_space
                left = self.background.left + (self.block_width * item_index) + (self.h_space * (item_index + 1))
                # left is based of the amount of blocks (self.block_width * item_index) and the horizontal spaces btwn them
   
            if item_index >= 3: # checking if the item is in the second row
                top = self.top + self.v_space + self.block_height + self.v_space
                left = self.background.left + (self.block_width * (item_index-3)) + (self.h_space * ((item_index-3) + 1))

            # image
            img_link = self.images[item_index] # getting correct file name for the specific item's corresponding image
            img = pg.image.load(img_link) # blitting this to the screen
            img = pg.transform.scale(img,(120,120)) # resizing

            # amount
            amount_list = list(self.character.crop_stuff.values()) + list(self.character.seed_stuff.values())
            amount = amount_list[item_index]
            
            self.block(item_name, left, top, amount, img, self.index == item_index) 
 

'''import pygame as pg
from setting import *
from timer import Timer
screen = pg.display.set_mode((w,h))

# main class 
class Inventory:
    def __init__(self, character, inventory_menu): # basic set_up
  
        self.character = character
        self.inventory_menu = inventory_menu
        self.font = pg.font.SysFont('Cambria', 30)
        self.images = ['Sprout Lands - Sprites - Basic pack/Characters/cow.webp','Sprout Lands - Sprites - Basic pack/Characters/cow.webp','Sprout Lands - Sprites - Basic pack/Characters/cow.webp','Sprout Lands - Sprites - Basic pack/Characters/cow.webp','Sprout Lands - Sprites - Basic pack/Characters/cow.webp','Sprout Lands - Sprites - Basic pack/Characters/cow.webp' ] # ❗ insert item images here
        
         # options list
        self.options = list(self.character.crop_stuff.keys()) + list(self.character.seed_stuff.keys())
        
        # rows
        self.first_row = self.options[:3]
        self.second_row = self.options[3:]

        # selection
        self.index = 0
        self.timer = Timer(200)
        
        # spacing and padding
        self.v_space = 30 # space between the different rows
        self.h_space = 30 # space btwn the different blocks within the row
        self.tb_padding = 10 # padding at the top of the block (top to img start) * at the bottom of the block (txt bottom to block bottom)
        self.img_txt_padding = 5 # padding btwn img and txt
        # in total per block there will be 25 of padding
        
        # sizing 
        self.total_width = 1000
        self.total_height = 600
        self.block_width = (self.total_width - (self.h_space * 4)) / 3
        self.block_height = (self.total_height - (self.v_space * 3)) / 2
        # so based on my current math, each block should be 180 by 160        

        self.txt_bg()
                             
# ___________________________________________________________________________________________________________________________

    def txt_bg(self): # creates our text and background
        
        # text
        self.item_names = [] 
        
        # rendering text and additing it to our text_item
        for item in self.options:
            self.item_name = self.font.render(item, False, 'Black')    
            self.item_names.append(item)            
            
 
        self.top = h / 2 - self.total_height / 2
        self.background = pg.Rect(150, self.top, self.total_width, self.total_height) # background that pulls everything together ❗ 400

# ___________________________________________________________________________________________________________________________
    
    def select_stuff(self):
        keys = pg.key.get_pressed() 
        self.timer.update_tool()

        if keys[pg.K_SLASH]: # if player hits escape, display closes
            self.inventory_menu()

        if not self.timer.start():

            if keys[pg.K_g]:
                self.index -= 1
                self.timer.start()

            if keys[pg.K_h]:
                self.index += 1
                self.timer.start()

            if keys[pg.K_DOWN]:
                self.index += len(self.first_row)
                self.timer.start()

            if keys[pg.K_UP]:
                self.index -= len(self.first_row)
                self.timer.start()
                    
        # restrict selection
        if self.index < 0:
            self.index = len(self.options) - 1 
        
        if self.index > len(self.options) - 1:
            self.index = 0
                            
# ___________________________________________________________________________________________________________________________ 

    def block(self, item_name, left, top, img, chosen): # creates blocks (bg, text, amount, border)

        block_bg = pg.Rect(left, top, amount, self.block_width, self.block_height)

        # pos (l) → defined later within update method
        # top (t) → distance from top that's defined in update method
        # self.block_width → created in init
        # self.block_height → created in txt_bg method

        pg.draw.rect(screen, 'White', block_bg, 0, 5)
        # 🌱 ^ this line blits the blocks to the screen

        # text
        text = self.font.render(str(item_name), False, 'Black')
        text_rect = text.get_rect(bottomleft = (block_bg.centerx, block_bg.top + 160))
        screen.blit(text, text_rect)
         # 🌱 ^ this line blits the text to the screen
    
        # amounts
        amount_text = self.font.render(str(amount), False, 'Black')
        amount_block = amount_text.get_rect(bottomleft = (block_bg.centerx, block_bg.top + 160))
        screen.blit(amount_text, amount_block)
        
        # images
        img_position = img.get_rect(topleft = (block_bg.centerx, block_bg.centery)) # 🐋
        screen.blit(img, img_position) # 🐋
        
        if chosen:
            pg.draw.rect(screen, 'green', block_bg, 6, 5) # border when item is selected (this doesn't really do much'''
            
# ___________________________________________________________________________________________________________________________ 
            
    def update(self):
        self.select_stuff()
        pg.draw.rect(screen, 'Black', self.background)

        for item_index, item_name in enumerate(self.item_names):
            # enumerate count starts at 0
            
            if item_index <= 2:
                left = self.background.left + (self.block_width * item_index) + (self.h_space * (item_index + 1))
            else:
                new_item_index = item_index - 3
                left = self.background.left + (self.block_width * new_item_index) + (self.h_space * (new_item_index + 1))
            
            if item_index <= 2:
                top = self.top + self.v_space
                # + 20 is just for an inden
   
            if item_index >= 3:
                top = self.top + self.v_space + self.block_height + self.v_space
                # img_position = (self.background.left + (self.block_width * item_name.index) + (self.h_space * (self.index + 1) + 20), top)
            
            amount_list = list(self.character.crop_stuff.values()) + list(self.character.seed_stuff.values())
            amount = amount_list[item_index]
            
            # images
            img_link = self.images[item_index] # 🐋
            img = pg.img.load(img_link) # 🐋
            
            self.block(item_name, left, top, img, amount, self.index == item_index) 
 
