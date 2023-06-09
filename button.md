### Button Work (🌷 AM)
https://www.youtube.com/watch?v=16DM5Eem0cI
https://www.thepythoncode.com/article/make-a-button-using-pygame-in-python - website tutorial

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
	
Version 4

``` python	    

import pygame as pg
from setting import * 
#screen = pg.display.set_mode((w,h))

class Button(): # Class that allows the player can press buttons
    def __init__(self, x_pos, y_pos, text_input): # initializing the class
        self.text_input = text_input
        self.font = pg.font.SysFont("ariel",18)
        self.text = self.font.render(self.text_input,True,'white')
        self.image = pg.image.load("fish.png")
        self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.display_surface = pg.display.get_surface()
        self.draw() # automatically calls the draw method once the Button is initialized

    def draw(self):
        # Creating our button's display
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
         
    def check_press(self): # checks if the button has been clickes
        mouse_position = pg.mouse.get_pos() # returns the current position of mouse
        left_click = pg.mouse.get_pressed()[0]
        b_rect = pg.rect.Rect((self.x_pos, self.y_pos), (100, 20))
        if left_click and b_rect.collidepoint(mouse_position):
            return True
            # this is where we would put the code to change the screen to the farmer's market
        else:
            return False
   # Online button 
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Button!")
main_font = pygame.font.SysFont("cambria", 30)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			print("Button Press!")

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")

button_surface = pygame.image.load("fish.png")
button_surface = pygame.transform.scale(button_surface, (200, 150))

button = Button(button_surface, 400, 300, "Start")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			button.checkForInput(pygame.mouse.get_pos())

	screen.fill("purple")

	button.update()
	button.changeColor(pygame.mouse.get_pos())

	pygame.display.update()
```
	
Version 5

```python

import pygame as pg 
from setting import *


# configuration
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((w, h))
font = pg.font.SysFont('Cambria', 14)

# button class
class Button(): # Class that allows the player can press buttons
    def __init__(self, x, y, text): # initializing the class
        self.x = x
        image= pg.image.load('fm button.png')
        image = pg.transform.scale(image, (int(image.get_width() * 0.35), int(image.get_height()*0.35)))
        self.image = image
        self.y = y
        self.text = text
        # new attempt at placing button on screen
        self.button_surface = pg.Surface((10, 20))
        self.button_rect = pg.Rect(self.x,self.y, 10, 20)
        self.button_text = font.render(text, True, 'black')

    def update(self):
        screen.blit(self.image, self.button_rect)
        screen.blit(self.button_text, (self.x + 40, self.y + 30))
	
    def check_press(self): # checks if the button has been clickes
        pos = pg.mouse.get_pos() # returns the current position of mouse
        left_click = pg.mouse.get_pressed()[0]
        self.button_rect = pg.Rect(self.x,self.y, 10, 20)
        if left_click and self.button_rect.collidepoint(pos): # checking to see if the player clicked within the button area
		self.farmer_market() # 🌷 I'm not sure if we need the self
            return True
			
			
        else:
            return False
			
```

Version 6

```python
# this code actually allows us to interact with the button --> meaning when i press it, it works.. its not just nothing happening
# use this to connect to the pop up screen to 

class Button():
    def __init__(self,x,y,text_input):
        image= pg.image.load('fm button.png') # creating the image
        image = pg.transform.scale(image, (int(image.get_width() * 0.35), int(image.get_height()*0.35)))
        self.image = image
        self.x = x
        self.y = y 
        self.text = text_input
        self.button_text = font.render(text_input, True, 'black')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.clicked = False # so only if button is NOT being clicked, can we then click it
    def draw(self):
      # drawing stuffn on screen 
        screen.blit(self.image,(self.rect.x, self.rect.y))
        screen.blit(self.button_text, (self.rect.x + 40, self.rect.y+30))
        # get mouse
        position = pg.mouse.get_pos()
        #check mouseover and clicked
        if self.rect.collidepoint(position):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False: # 0 if left clicked # the == 1 means mouse is being used/clicked rn
                self.clicked = True
                print('clicked')
            if pg.mouse.get_pressed()[0] == 0: # ==0 means mouse is NOT being pressed right
                self.clicked = False # now we can click the button again 
```
