
# Farmer's Market 🍉

'''
Overview of methods in farmer_market:
- ```self.options``` → contains all the items avaliable to sell/buy in the market (pulls from character code)
- ```self.buy_border``` → allows us to seperate our selling and buying items
- ```money_money_money``` → method that puts our money value on screen
- ```close``` → method that allows us to close out of the fm
'''

import pygame as pg
from setting import *
from character import Character
screen = pg.display.set_mode((w,h))

class Menu:
    def __init__(self, character, fm_menu): # fm_menu allows us to switch on and off the farmer's market
  
        # base set-up :)
        self.character = character
        self.fm_menu = fm_menu
        self.font = pg.font.SysFont('Cambria', 30)

        # Adding in our farmer's market image (this code was pulled from the button code!)
        image = pg.image.load('background/farmers_pic.jpg')
        image = pg.transform.scale(image, (int(image.get_width() * 0.30), int(image.get_height()*0.35)))
        self.image = image

        # 🎂 farmer's market buying/selling 
        self.width = 300 # width of the entire buying section (left to right)
        self.space = 10 # space between the different blocks
        self.padding = 10

        self.options = list(character.crop_stuff.keys()) + list(character.seed_stuff.keys())
        # pulls both our inventory dictionaries from character
        self.buy_border = len(character.crop_stuff) - 1 # allows us to seperate our selling and buying items
        self.base_setup()
    
    # 🎂 (5/30)
    def money_money_money(self): # puts our money value on screen
        money_text = self.font.render(f'${self.character.money}', True, 'Black')  # creates our money value
        money_block = money_text.get_rect()
        # so I included w/5 so that our money block would be closer to the left side of the screen
        # ❗ but again we still neet to adjust the coordinates 🤯🤯 ❗
        
        pg.draw.rect(screen, 'White', money_block.inflate(15,15), 0, 5)
        # 0 is for the border width, border radius is 6 (rounding)
        
        screen.blit(money_text, money_block)
        # 🌱 blits our money block + money amt on screen (rn no coordinates are needed bc we want to keep it in the top left
        
        
    # 🎂 (5/30)
    def base_setup(self): # creates our block titles and creates some screen settings! 
        
        # text
        self.item_names = [] 
        self.total_height = 0
        
        for item in self.options: # allows us  to add all our item options to our rendered options list
            item_name = self.font.render(item, False, 'Black')
            # ^ format (string, antialias [rounded corners], colour)      
            self.item_names.append(item_name)            
            self.total_height += (item_name.get_height() +20) + self.padding * 2
            # get_height() is a pg function to return the height of a surface
        
            
        # screen
              
        self.total_height += (len(self.item_names) - 1) * self.space
        # creates spaces btwn our blocks according to our attribute self.space in our init method
        self.menu_top = h / 2 - self.total_height / 2 
        self.bg = pg.Rect(100, self.menu_top, self.width, self.total_height) # background that pulls everything tgthr
        # ❗ the 100 is just a random placement #, we need to adjust to our coordinates 
        # h is pulled from settings
        # we subtract self.total_height bc the screen display works differently, it's like flipped
        
    def close(self): # allows the player to close the farmer's market
        keys= pg.key.get_pressed() # getting all the keys
        
        if keys[pg.K_ESCAPE]: # if player hits escape, display closes
            self.fm_menu() # I'm not too sure about this line, I think I might be calling the wrong method, CHECK WHEN DEBUGGING
  
    def show_block(self, text, amount, pos): # actually creates our individual blocks
        
        background = pg.Rect(self.bg.left, pos, self.width, text.get_height()+(self.padding*2)) # creating our background rect  
        # self.all_block.rect comes from our bg rect in block_setup
        pg.draw.rect(screen, 'White', background, 0, 5)
        
        text_rect = text.get_rect(self.bg.left + 20, background))
        self.screen.blit(text, text_rect)
    
    def update(self): # diplays the menu, it's like the button all over again :(
        self.close()
        screen.blit(self.image, (0,0)) # 0,0, so it fills the whole screen
        # 🌱 blitting our farmer market bg on screen
        self.money_money_money()
            
        # 🎂 (5/30
        for item_index, item_name in enumerate(self.item_names): # blitting our text
        # enumerate counts our iterations, counter will be applied to item_index automatically
        # needed this to differentiate btwn selling and buying items (w/ self.buy_border) 
        
            position = self.bg.pos + item_index * (item_name.get_height() + (self.padding * 2) + self.space)
            # self.bg is the rect, the .pos is the top, (item_name.get_height() + (self.padding * 2) + self.space) allows us to create our blocks while item_index controls where they are
           
            # ^ this creates our individual blocks
            self.show_block(item_name, 0, position)
                                              
            screen.blit(item_name,(250, item_index * 50)) # ❗CHANGE COORDINATES ❗F
                
    
              
