# https://www.youtube.com/watch?v=T4IX36sP_0c&t=21547s # currently at 5:57:00


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
        self.width = 300 # width of the entire buying section (left to right)
        self.space = 10 # space between the different blocks
        self.padding = 8

        self.options = list(self.character.crop_stuff.keys() + self.character.seed_stuff.keys())
        # pulls both our inventory dictionaries from character
        self.buy_border = len(self.crop_stuff) - 1 # allows us to seperate our selling and buying items
        self.text_in()
    
 
    
    def close(self): # allows the player to close the farmer's market
        keys= pg.key.get_pressed() # getting all the keys
        
        if keys[pg.K_ESCAPE]: # if player hits escape, display closes
            self.fm_menu() # I'm not too sure about this line, I think I might be calling the wrong method, CHECK WHEN DEBUGGING
  
      def update(self): # diplays the menu, it's like the button all over again :(
          self.close()
          screen.blit(self.image, (0,0)) # 0,0, so it fills the whole screen
```

🎂 Notes
- so within the farmer's market, do we want furniture items/decor?
  - we discussed this when starting our project but I'm not sure how the actual application of this will work on our map
  - it's pretty easy to add if we want tho all we have to do is near Aroush's original inventory in character we add a furniture dictionary and then add it to self.options in this file
