### Button Work (🌷 AM)
https://www.youtube.com/watch?v=16DM5Eem0cI


Version 1

```python

class Button(): # Class that allows the player can press buttons
    def __init__(self, image, x_pos, y_pos, text):
        self.image = image # allows us to show user's our button image

        # coordinates
        self.x_pose = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

         # text
        self.text_input = text_input # allows us to store text_input in an object
        self.text = main_font.render(self.text_input, True, "--------")
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
 
def update(self): # allows us to place image along with text on screen
    screen.blit(self.image, self.rect) # allows us to put our image onto the game screen
    screen.blit(self.image, self.rect) # allows us to place the text for our button onto the game screen

def mouse_check(self, position): # checks for possible button click
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): # checks if the mouse's position is in the button's area
        print("The button has been pressed")
        return True
    return False

```

Version 2 !!CURRENT VERSION!!

```python

class Button(): # Class that allows the player can press buttons
    def __init__(self, image, x_pos, y_pos, text, work): # initializing the class
        self.image = image 
        self.x_pose = x_pos
        self.y_pos = y_pos
        self.text = text
        self.work = work # allows us to enable and disable our function
        self.draw() # automatically calls the draw method once the Button is initialized
        
    def draw(self):
        
        # Creating our button's display
        b_text = font.render(self.text, True, 'black')
        b_rect = pg.image.rect.Rect((self.x_pos, self.y_pos), (100, 20)) # creating button's rect, coordinates (x_pos, y_post) + size
        

        if self.work: # checks if the button has been enabled
            if self.check_click():
                pg.draw.rect(screen, 'pink', b_rect, 0, 10) # make's our button display to be pink when clicked
            else:
                pg.draw.rect(screen, 'yellow', b_rect, 0, 10) # make's our button display to be yellow when not clicked  
            screen.blit(b_text, (self.x_post + 2, self.y_pos + 2))
        else:
            pg.draw.rect(screen, 'black', b_rect, 0, 10) # make's our button display black if disabled
  
    def check_press(self): # checks if the button has been clickes
        mouse_position = pg.mouse.get_pos() # returns the current position of mouse
        left_click = pg.mouse.get_pressed()[0]
        b_rect = pg.image.rect.Rect((self.x_pos, self.y_pos), (100, 20))
        if left_click and b_rect.collidepoint(mouse_pos) and self.enabled: # checking to see if the player has clicked an enabled button
            return True
            # this is where we would put the code to change the screen to the farmer's market
        else:
            return False
 ```
 
Version 3

```python

import pygame as pg
from setting import * 
screen = pg.display.set_mode((w,h))
font_name = pg.font.match_font("ariel")

class Button(): # Class that allows the player can press buttons
    def __init__(self, x_pos, y_pos, text): # initializing the class
        #self.image = image 
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.draw() # automatically calls the draw method once the Button is initialized

    def draw(self):
        
        # Creating our button's display
        b_text = font.render(self.text, True, 'black')
        b_rect = pg.rect.Rect((self.x_pos, self.y_pos), (100, 20))
        pg.draw.rect(screen, 'pink' b_rect, 0, 5)
        screen.blit(b_text, (self.x_pos + 3, self.y_pos + 3))
         
    def check_press(self): # checks if the button has been clickes
        mouse_position = pg.mouse.get_pos() # returns the current position of mouse
        left_click = pg.mouse.get_pressed()[0]
        b_rect = pg.rect.Rect((self.x_pos, self.y_pos), (100, 20))
        if left_click and b_rect.collidepoint(mouse_position):
            return True
            # this is where we would put the code to change the screen to the farmer's market
        else:
            return False
 
 
 
```
