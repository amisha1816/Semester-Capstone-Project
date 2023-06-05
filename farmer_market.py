
# Farmer's Market 🍉

# imports
import pygame as pg
from setting import *
from character import Character
from timer import Timer
screen = pg.display.set_mode((w,h))


# main class 
class Menu:
    def __init__(self, character, fm_menu): 
  
        # base set-up :)
        self.character = character
        self.fm_menu = fm_menu # allows us to switch on and off the farmer's market
        self.font = pg.font.SysFont('Cambria', 30)

        # fm image
        image = pg.image.load('background/farmers_pic.jpg')
        image = pg.transform.scale(image, (int(image.get_width() * 0.30), int(image.get_height()*0.35)))
        self.image = image

        # layout
        self.width = 300 # width of the entire buying section (left to right)
        self.space = 10 # space between the different blocks
        self.padding = 10

        # options list
        self.options = list(character.crop_stuff.keys()) + list(character.seed_stuff.keys())
        # pulls both our inventory dictionaries from character
        self.buy_border = len(character.crop_stuff) - 1 # allows us to seperate our selling and buying items
        self.base_setup()
    
        # selection
        self.index = 0
        self.timer = Timer(200)
    
    def money_money_money(self): # puts our money value on screen
        money_text = self.font.render(f'${self.character.money}', True, 'Black')  # creates our money value
        money_block = money_text.get_rect()
        
        pg.draw.rect(screen, 'White', money_block.inflate(15,15), 0, 5) # border width is 0, border radius is 6 
        screen.blit(money_text, money_block) # 🌱 blits our money block + money amt on screen 
        
        
    # 🎂 (5/30)
    def base_setup(self): # creates our block names and creates some screen settings! 
        
        # text
        self.item_names = [] 
        self.total_height = 0
        
        for item in self.options: # allows us  to add all our item options to our rendered options list
            self.item_name = self.font.render(item, False, 'Black')
            # ^ format (string, antialias [rounded corners], colour)      
            self.item_names.append(item_name)            
            self.total_height += self.item_name.get_height() + (self.padding * 2)
            # all this is doing is finding the height of each individual block (text + padding) and adding it to our total height
            
        # screen set_up
        self.total_height += (len(self.item_names) - 1) * self.space
        # creates spaces btwn our blocks according to our attribute self.space in our init method
        self.menu_top = h / 2 - self.total_height / 2 # very top of our menu
        self.background = pg.Rect(100, self.menu_top, self.width, self.total_height) # background that pulls everything tgthr
        # 100 is the left point, to make the block be on the left side of the screen
        # ^ this was my pink background in the past
        
        # buy/sell text surface
        self.buy_button = self.font.render('buy', False, 'Blue')
        self.sell_text = self.font.render('sell', False, 'Green')
        
        
    def select_stuff(self): # allows the player to close the farmer's market
        keys = pg.key.get_pressed() # getting all the keys
        self.timer.update_tool()
        
        if keys[pg.K_ESCAPE]: # if player hits escape, display closes
            self.fm_menu() # I'm not too sure about this line, I think I might be calling the wrong method, CHECK WHEN DEBUGGING
  
        if not self.timer.start():
            # allows us to select different blocks
            if keys[pg.K_UP]:
                self.index -= 1
                self.timer.start() # ensures that we're not rushing through the different options

            if keys[pg.K_DOWN]:
                self.index += 1
                self.timer.start()
                
            if keys[pg.K_space]:
                selected_item = self.options[self.index]
                # self.index is directly connected to the item block we've selected, by indexing it we'll receive the correct item name

                if self.index <= self.buy_border: # sell
                    if self.character.crop_stuff[selected_item] > 0: # checking if we can actually sell
                        self.character.crop_stuff[selected_item] -= 1 # reduce inventory after sale
                        self.character.money += SELL_STUFF[selected_item]
                            
                        
                else:
                    seed_price = BUY_STUFF[selected_item]
                    if self.character.money >= seed_price: # checking if they have enough money
                        self.character.seed_stuff[selected_item] += 1 # increasing our inventory for this item
                        self.character.money -= seed_price
                        
                
        # restrict selection
        if self.index < 0:
            self.index = len(self.options) - 1
        # this prevents us from selecting an option that isn't there    
        
        if self.index > len(self.options) - 1:
            self.index = 0
        
    def show_block(self, text, amount, pos, chosen): # actually creates our individual blocks
        
        # what do the parameters do 🤔
        # text → item name
        # amount → inventory amount
        # pos → position of where we want the block to be
        
        block_bg = pg.Rect(self.background.left, pos, self.width, text.get_height()+(self.padding*2)) # creating our background rect  
        # rect → (left, top, width, height)
        # ^ block_bg is the background just for our individual blocks
        # in this case, pos (top) is the only thing thats changing, everything else is staying the same
        pg.draw.rect(screen, 'White', block_bg, 0, 5)
        # 🌱 ^ this line blits the blocks to the screen
        
        # text
        text_rect = text.get_rect(midleft = (self.background.left + 20, block_bg.centery)) ❗❗
        # the +20 slightly shifts it to the right, so it looks cleaner
        self.screen.blit(text, text_rect)
         # 🌱 ^ this line blits the text to the screen
    
        # inventory amounts
        amount_text = self.font.render(str(amount), False, 'Black')
        # we can't render a number to the screen
        # amount is from the show_block parameters
        amount_block = amount_text.get_rect(midright = (self.background.right - 20, block_bg.centery))
        screen.blit(amount_text, amount_block)
        
        if chosen:
            pg.draw.rect(screen, 'black', block_bg, 4, 4)
            # (4, 4) reps the border radius, border width
            
            if self.index <= self.buy_border: # sell
                bs_rect = self.sell_text.get_rect(midleft = (self.background.left + 200, block_bg.centery))
                screen.blit(self.buy_text, bs_rect) # checking if the current block we're on is before the end of the buy border
            else: # but
                bs_rect = self.buy_text.get_rect(midleft = (self.background.left + 200, block_bg.centery))
                screen.blit(self.buy_text, (self.sell_text, bs_rect)
            

    def update(self): # diplays the menu, it's like the button all over again :(
        self.select_stuff()
        screen.blit(self.image, (0,0)) # 0,0, so it fills the whole screen
        # 🌱 blitting our farmer market background on screen
        self.money_money_money()
            
        # 🎂 (5/30
        for item_index, item_name in enumerate(self.item_names): # blitting our text
        # enumerate counts our iterations, counter will be applied to item_index automatically
        # needed this to differentiate btwn selling and buying items (w/ self.buy_border) 
        
            position = self.background.top + item_index * (item_name.get_height() + (self.padding * 2) + self.space)
            amount_list = list(character.crop_stuff.values()) + list(character.seed_stuff.values())
            amount = amount_list[item_index]
            self.show_block(item_name, amount, position, self.index == item_index)
                                              
                
    
              
