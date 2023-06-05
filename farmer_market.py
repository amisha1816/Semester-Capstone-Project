
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
    
    # 🎂 (5/30)
    def money_money_money(self): # puts our money value on screen
        money_text = self.font.render(f'${self.character.money}', True, 'Black')  # creates our money value
        money_block = money_text.get_rect()
        
        pg.draw.rect(screen, 'White', money_block.inflate(15,15), 0, 5) # border width is 0, border radius is 6 
        screen.blit(money_text, money_block)
        # 🌱 blits our money block + money amt on screen 
        
        
    # 🎂 (5/30)
    def base_setup(self): # creates our block names and creates some screen settings! 
        
        # text
        self.item_names = [] 
        self.total_height = 0
        
        for item in self.options: # allows us  to add all our item options to our rendered options list
            self.item_name = self.font.render(item, False, 'Black')
            # ^ format (string, antialias [rounded corners], colour)      
            self.item_names.append(item_name)            
            self.total_height += self.item_name.get_height() + 20 + (self.padding * 2)
            # get_height() is a pg function to return the height of a surface
        
            
        # screen set_up
        self.total_height += (len(self.item_names) - 1) * self.space
        # creates spaces btwn our blocks according to our attribute self.space in our init method
        self.menu_top = h / 2 - self.total_height / 2 # very top of our menu
        self.bg = pg.Rect(100, self.menu_top, self.width, self.total_height) # background that pulls everything tgthr
        # ^ rect that ties together our everything tgthr
        
    def select_stuff(self): # allows the player to close the farmer's market
        keys= pg.key.get_pressed() # getting all the keys
        
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
                
        
        # restrict selection
        if self.index < 0:
            self.index = len(self.options) - 1
        # this prevents us from selecting an option that isn't there    
        
        if self.index > len(self.options) - 1:
            self.index = 0
        
    def show_block(self, text, amount, pos, chosen): # actually creates our individual blocks
        
        background = pg.Rect(self.bg.left, pos, self.width, text.get_height()+(self.padding*2)) # creating our background rect  
        # self.all_block.rect comes from our bg rect in block_setup
        pg.draw.rect(screen, 'White', background, 0, 5)
        
        text_rect = text.get_rect(self.bg.left + 20, background))
        # the +20 slightly shifts it to the right, so it looks cleaner
        self.screen.blit(text, text_rect)
    
        # inventory amounts :0
        amount_text = self.font.render(str(amount), False, 'Black')
        # we can't render a number to the screen
        # amount is from the show_block parameters
        amounts_block = amount_text.get_rect(self.bg.right - 20, bg_rect.centery)
        screen.blit(amount_text, amount_block)
        
        if chosen:
            pg.draw.rect(screen, 'black', background, 4, 4)
            # (4, 4) reps the border radius, border width
        
    
    def update(self): # diplays the menu, it's like the button all over again :(
        self.select_stuff()
        screen.blit(self.image, (0,0)) # 0,0, so it fills the whole screen
        # 🌱 blitting our farmer market bg on screen
        self.money_money_money()
            
        # 🎂 (5/30
        for item_index, item_name in enumerate(self.item_names): # blitting our text
        # enumerate counts our iterations, counter will be applied to item_index automatically
        # needed this to differentiate btwn selling and buying items (w/ self.buy_border) 
        
            position = self.bg.top + item_index * (item_name.get_height() + (self.padding * 2) + self.space)
            # self.bg is the rect, the .pos is the top, (item_name.get_height() + (self.padding * 2) + self.space) allows us to create our blocks while item_index controls where they are
           
            amount_list = self.options = list(character.crop_stuff.values()) + list(character.seed_stuff.values())
            # ^ pretty similar to our self.options list
            
            amount = amount_list(item_index)
            
            self.show_block(item_name, amount, position, self.index == item_index)
                                              
            # screen.blit(item_name,(250, item_index * 50)) # ❗CHANGE COORDINATES ❗F
                
    
              
