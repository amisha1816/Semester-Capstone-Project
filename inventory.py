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

            if keys[pg.K_LEFT]:
                self.index -= 1
                self.timer.start()

            if keys[pg.K_RIGHT]:
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

    def block(self, item_name, left, top, amount, chosen): # creates blocks (bg, text, amount, border)

        block_bg = pg.Rect(left, top, self.block_width, self.block_height)

        # pos (l) → defined later within update method
        # top (t) → distance from top that's defined in update method
        # self.block_width → created in init
        # self.block_height → created in txt_bg method

        pg.draw.rect(screen, 'White', block_bg, 0, 5)
        # 🌱 ^ this line blits the blocks to the screen

        # text
        text = self.font.render(str(item_name), False, 'Black')
        text_rect = text.get_rect(midleft = (100, 100))
        # screen.blit(text, text_rect)
         # 🌱 ^ this line blits the text to the screen
    
        # amounts
        amount_text = self.font.render(str(amount), False, 'Black')
        amount_block = amount_text.get_rect(midleft = (100, 100))
        # screen.blit(amount_text, amount_block)
        
        if chosen:
            pg.draw.rect(screen, 'black', block_bg, 4, 4) # border when item is selected (this doesn't really do much
            
# ___________________________________________________________________________________________________________________________ 
            
    def update(self):
        self.select_stuff()
        pg.draw.rect(screen, 'Black', self.background)

        for item_index, item_name in enumerate(self.item_names):
            
            left = self.background.left + (self.block_width * self.index) + (self.h_space * (self.index + 1))

            if item_index <= 3:
                top = self.top + self.v_space
                # img_position = (self.background.left + (self.block_width * self.index) + (self.h_space * (self.index + 1) + 20), top)
                # + 20 is just for an inden
   
            '''else:
                top = self.v_space * 2 + self.block_height
                img_position = (self.background.left + (self.block_width * self.index) + (self.h_space * (self.index + 1) + 20), top)
            '''
    
            # img
            # img = self.images[item_index]
            # img_surf = pg.Surface(img_position)
            # screen.blit(img_surf, img_position)
            
            # amount
            amount_list = list(self.character.crop_stuff.values()) + list(self.character.seed_stuff.values())
            amount = amount_list[item_index]
            
            self.block(item_name, left, top, amount, self.index == item_index) 
 
