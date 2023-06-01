
### Farmer's Market 🍉


Overview of methods in farmer_market:
- ```self.options``` → contains all the items avaliable to sell/buy in the market (pulls from character code)
- ```self.buy_border``` → allows us to seperate our selling and buying items
- ```money_money_money``` → method that puts our money value on screen
- ```close``` → method that allows us to close out of the fm


```python
import pygame as pg
from setting import *
from character import Character
screen = pg.display.set_mode((w,h))

class Menu:
    def __init__(self, character, fm_menu): # fm_menu allows us to switch on and off the farmer's market
  
        # base set-up :)
        self.character = character
        self.fm_menu = fm_menu
        self.font = pg.font.SysFont('Cambria', 14)

        # Adding in our farmer's market image (this code was pulled from the button code!)
        image = pg.image.load('background/farmers_pic.jpg')
        image = pg.transform.scale(image, (int(image.get_width() * 0.30), int(image.get_height()*0.35)))
        self.image = image

        # 🎂 farmer's market buying/selling 
        self.width = 200 # width of the entire buying section (left to right)
        self.space = 10 # space between the different blocks
        self.padding = 8

        self.options = list(self.character.crop_stuff.keys() + self.character.seed_stuff.keys())
        # pulls both our inventory dictionaries from character
        self.buy_border = len(self.crop_stuff) - 1 # allows us to seperate our selling and buying items
        self.block_setup()
    
    # 🎂 (5/30)
    def money_money_money(self): # puts our money value on screen
        money_text = self.font.render(f'$(self.character.money)', True, 'Black')  # creates our money value
        money_block = money_tezt.get_rect(bottom_left = (w / 5, h - 20))
        # so I included w/5 so that our money block would be closer to the left side of the screen
        # ❗ but again we still neet to adjust the coordinates 🤯🤯 ❗
        
        pg.draw.rect(screen, 'White', money_block.inflate(10,10), 0, 5)
        # 0 is for the border width, border radius is 6 (rounding)
        
        sreen.blit(money_text, money_block)
        
        
    # 🎂 (5/30)
    def base_setup(self): # creates our block titles and creates some screen settings! 
        
        # text
        self.item_names = [] 
        
        for item in self.options: # allows us  to add all our item titles to our rendered title list
            item_name = self.font.render(item, False, 'Black')
            # ^ format (string, antialias [rounded corners], colour)      
            self.item_names.append(title)            
            self.total_height += item_names.get_height() + self.padding * 2
            # get_height() is a pg function to return the height of a surface
        
            
        # screen
        self.total_height = 0
        
        self.total_height += (len(self.item_names) - 1) * self.space
        # creates spaces btwn our blocks according to our attribute self.space in our init method
        self.menu_top = h / 2 - self.total_height / 2 
        self.bg.rect = pg.Rect(100, self.menu_top, self.width, self.total_height) # background that pulls everything tgthr
        # ❗ the 100 is just a random placement #, we need to adjust to our coordinates 
        # h is pulled from settings
        # we subtract self.total_height bc the screen display works differently, it's like flipped
        
    def close(self): # allows the player to close the farmer's market
        keys= pg.key.get_pressed() # getting all the keys
        
        if keys[pg.K_ESCAPE]: # if player hits escape, display closes
            self.fm_menu() # I'm not too sure about this line, I think I might be calling the wrong method, CHECK WHEN DEBUGGING
  
    def show_block(self, text, amount, pos): # actually creates our individual blocks
        
        background = pg.Rect(self.all_block.rect.left, top, self.width, block_tiles.get_height()) # creating our background rect
        # ^ similar to how we did in base_setup()
        
        # self.all_block.rect comes from our bg rect in block_setup
        pg.draw.rect(screen, 'White', background, 0, 5)
    
    def update(self): # diplays the menu, it's like the button all over again :(
        self.close()
        screen.blit(self.image, (0,0)) # 0,0, so it fills the whole screen
        self.money_money_money()
            
        # 🎂 (5/30
        for item_index, item_name in enumerate(self.item_names):
        # enumerate counts our iterations, counter will be applied to item_index automatically
        # needed this to differentiate btwn selling and buying items (w/ self.buy_border) 
        
            pos = self.all_block.rect.top + title_index * (item_name.get_height() + (self.padding * 2) + self.space
            # ^ this creates our individual blocks
            self.show_block(title, 0, top)
                                                           
            screen.blit(title,(100, title_index * 50) # ❗CHANGE COORDINATES ❗
                
    
              
