

```python
import pygame as pg
from setting import *
from character import Character
from timer import Timer
screen = pg.display.set_mode((w,h))


# main class 
class Menu:
    def __init__(self, character, fm_menu): 
  
        # base set-up
        self.character = character
        self.fm_menu = fm_menu # allows us to switch on and off the farmer's market
        self.font = pg.font.SysFont('Cambria', 30) # for item names
        self.small_font = pg.font.SysFont('Cambria', 20) # for sell/buy text

        # image
        image = pg.image.load('background/farmers_pic.jpg')
        image = pg.transform.scale(image, (int(image.get_width() * 0.30), int(image.get_height()*0.35)))
        self.image = image

        # layout
        self.width = 350 # width of the entire buying section
        self.space = 10 # vertical space between the different blocks
        self.padding = 10

        # options list
        self.options = list(character.crop_stuff.keys()) + list(character.seed_stuff.keys())
        # crop_stuff is a dictionary in character, by using .keys() and list() we're taking all the item names and turning it into one list
        self.buy_border = len(character.crop_stuff) - 1 # allows us to seperate our selling and buying item
        self.base_setup()
    
        # selection
        self.index = 0 # current block position, e.g. if on the top right box it would be 2, the bottom right would be 5
        self.timer = Timer(200)

    
    def money_money_money(self): # puts our money block and money amount
        
        
        money_text = self.font.render(f'${self.character.money}', True, 'Black')  # creates our money value
        money_block = money_text.get_rect()
        
        pg.draw.rect(screen, 'White', money_block.inflate(15,15), 0, 5)
        screen.blit(money_text, money_block) # blits our money block and money amt on screen 
        
        
    def base_setup(self): # creates our item names, backgrounds and some screen settings
        
        # item names
        self.item_names = [] 
        self.total_height = 0
        
        for item in self.options: # adds all our item options to our rendered options list
            self.item_name = self.font.render(item, False, 'Black')   
            self.item_names.append(item)            
            self.total_height += self.item_name.get_height() + (self.padding * 2)
            # ^ adding the height of this specific block (in accordance to the text height) to our overal height
            
        # screen settings
        self.total_height += (len(self.item_names) - 1) * self.space # calculates the spaces needed based on our amount of blocks/items
        self.menu_top = h / 2 - self.total_height / 2 # defining the top of our menu
        
        # background
        self.background = pg.Rect(100, self.menu_top, self.width, self.total_height)
        # background that pulls everything tgthr
        # not being blitted to the screen, however we reference this with our screen positioning
        
        # buy/sell text
        self.buy_text = self.small_font.render('sell', False, 'Red')
        self.sell_text = self.small_font.render('buy', False, 'Green')
        
        
    def select_stuff(self): 
        keys = pg.key.get_pressed() # getting all the keys
        self.timer.update_tool()
        
        if keys[pg.K_ESCAPE]: # allows the player to close the farmer's market
            self.fm_menu()
  
        if not self.timer.start(): # allows us to select different blocks
            if keys[pg.K_UP]:
                self.index -= 1
                self.timer.start() # ensures that we're not rushing through the different options

            if keys[pg.K_DOWN]:
                self.index += 1
                self.timer.start()
                
            if keys[pg.K_SPACE]:
                selected_item = self.options[self.index]
                # self.index is directly connected to the item block we've selected, by indexing it with our options we'll receive the correct item name

                if self.index <= self.buy_border: # for selling items
                    if self.character.crop_stuff[selected_item] > 0: # checking if the player have the selected_item
                        self.character.crop_stuff[selected_item] -= 1 # reduce inventory after sale
                        self.character.money += SELL_STUFF[selected_item] # adds money made to player's total money
                            
                        
                else:  # for buying
                    seed_price = BUY_STUFF[selected_item] # referencing the price from the BUY_STUFF dictionary in settings
                    if self.character.money >= seed_price: # checking if the players have enough money for the seed item
                        self.character.seed_stuff[selected_item] += 1 # increasing player's inventory for this item
                        self.character.money -= seed_price # subtracting money the player spent from their total money
                        
                
        # restrict selection
        if self.index < 0:
            self.index = len(self.options) - 1
        # this prevents us from selecting an option that isn't there    
        
        if self.index > len(self.options) - 1:
            self.index = 0
        
    def show_block(self, item_name, amount, pos, chosen): # actually creates our individual blocks, text, amount
        
        # what do the parameters do
        # item_name → item name
        # amount → inventory amount
        # pos → position of where we want the block to be
        # chosen → creates black border + buy/sell text around selected block
        
        # block
        block_bg = pg.Rect(self.background.left, pos, self.width,30 +(self.padding*2)) # creating our individual blocks  
        pg.draw.rect(screen, 'White', block_bg, 0, 5) # blits the blocks to the screen
        
        # text
        text = self.font.render(str(item_name), False, 'Black') # creating our rendered text
        text_rect = text.get_rect(midleft = (self.background.left + 20, block_bg.centery)) 
        screen.blit(text, text_rect) # blits the text to the screen
    
        # amount
        amount_text = self.font.render(str(amount), False, 'Black') # creating our rendered text
        amount_block = amount_text.get_rect(midright = (self.background.right - 20, block_bg.centery))
        screen.blit(amount_text, amount_block) # blits the text to the screen
        
        if chosen: # if current block is selected
            pg.draw.rect(screen, 'black', block_bg, 4, 4) # creates black border
            
            if self.index <= self.buy_border: # sell
                bs_rect = self.sell_text.get_rect(midleft = (self.background.left + 250, block_bg.centery))
                screen.blit(self.sell_text, bs_rect) # blits the buy text to the screen
                
            else: # buy
                bs_rect = self.buy_text.get_rect(midleft = (self.background.left + 250, block_bg.centery))
                screen.blit(self.buy_text, bs_rect)
            

    def update(self): # this method is what runs everything
        self.select_stuff() # to check which buttons the player is pressing
        screen.blit(self.image, (0,0)) # blitting the farmer's market background to the screen
        self.money_money_money() # creating the money block
            
        for item_index, item_name in enumerate(self.item_names):
        # enumerate counts our iterations (starts at 0), counter will be applied to item_index automatically
        # needed this to differentiate btwn selling and buying items (w/ self.buy_border) 
        
            position = self.background.top + item_index * (30 + (self.padding * 2) + self.space) # creats the top for each block
            amount_list = list(self.character.crop_stuff.values()) + list(self.character.seed_stuff.values())
            amount = amount_list[item_index]
            self.show_block(item_name, amount, position, self.index == item_index)
            
            
```

---


``` python
import pygame as pg
from setting import *
from character import Character
from timer import Timer
screen = pg.display.set_mode((w,h))


class Menu:
    def __init__(self, character, fm_menu): 
  
        # base set-up
        self.character = character
        self.fm_menu = fm_menu # allows us to switch on and off the farmer's market
        self.font = pg.font.SysFont('Cambria', 30) # for the title font
        self.small_font = pg.font.SysFont('Cambria', 20) # for the buy/sell font

        # image
        image = pg.image.load('background/farmers_pic.jpg')
        image = pg.transform.scale(image, (int(image.get_width() * 0.30), int(image.get_height()*0.35)))
        self.image = image

        # layout
        self.width = 350 # width of the entire buying section
        self.space = 10 # vertical space between the different blocks
        self.padding = 10 # space from block top/bottom to text

        # options list
        self.options = list(character.crop_stuff.keys()) + list(character.seed_stuff.keys()) # character.crop_stuff.keys is within 
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
            self.item_names.append(item)            
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
        self.buy_text = self.small_font.render('buy', False, 'Red')
        self.sell_text = self.small_font.render('sell', False, 'Green')
        
        
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
                
            if keys[pg.K_SPACE]:
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
        
    def show_block(self, item_name, amount, pos, chosen): # actually creates our individual blocks
        
        # what do the parameters do 🤔
        # text → item name
        # amount → inventory amount
        # pos → position of where we want the block to be
        
        block_bg = pg.Rect(self.background.left, pos, self.width,30 +(self.padding*2)) # creating our background rect  
        # rect → (left, top, width, height)
        # ^ block_bg is the background just for our individual blocks
        # in this case, pos (top) is the only thing thats changing, everything else is staying the same
        pg.draw.rect(screen, 'White', block_bg, 0, 5)
        # 🌱 ^ this line blits the blocks to the screen
        
        text = self.font.render(str(item_name), False, 'Black')
        text_rect = text.get_rect(midleft = (self.background.left + 20, block_bg.centery))
        
        # the +20 slightly shifts it to the right, so it looks cleaner
        screen.blit(text, text_rect)
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
                bs_rect = self.sell_text.get_rect(midleft = (self.background.left + 250, block_bg.centery))
                screen.blit(self.sell_text, bs_rect) # checking if the current block we're on is before the end of the buy border
            else: # buy
                bs_rect = self.buy_text.get_rect(midleft = (self.background.left + 250, block_bg.centery))
                screen.blit(self.buy_text, bs_rect)
            

    def update(self): # diplays the menu, it's like the button all over again :(
        self.select_stuff()
        screen.blit(self.image, (0,0)) # 0,0, so it fills the whole screen
        # 🌱 blitting our farmer market background on screen
        self.money_money_money()
            
        # 🎂 (5/30
        for item_index, item_name in enumerate(self.item_names): # blitting our text
        # enumerate counts our iterations, counter will be applied to item_index automatically
        # needed this to differentiate btwn selling and buying items (w/ self.buy_border) 
        
            text_height = list(item_name)
            position = self.background.top + item_index * (30 + (self.padding * 2) + self.space)
            amount_list = list(self.character.crop_stuff.values()) + list(self.character.seed_stuff.values())
            amount = amount_list[item_index]
            self.show_block(item_name, amount, position, self.index == item_index)
```
