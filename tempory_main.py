
### Main
https://www.youtube.com/watch?v=G8MYGDf_9ho

```python

# imports
import pygame as pg
import sys
from level import Level
from button import Button

# initial set-up
pg.init() # initializing pygame
screen = pg.display.set_mode((1300,800)) # creating screen
pg.display.set_caption('Farming Tales')
clock = pg.time.Clock()
level = Level() 
        
# button creation using button class 
fm_button = Button(30, 30)
home_button = Button(10, 20)
      
# Game loop  
while run:
        
        if fm_button.draw(surface):
            print("IT WORKS")
        if home_button.draw(surface)
            print("Home is working")
        
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program

        delta_time=clock.tick(120)/500
        pg.display.update() 
        
 

