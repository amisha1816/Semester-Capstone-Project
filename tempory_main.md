
### Main
https://www.youtube.com/watch?v=G8MYGDf_9ho

```python

import pygame as pg
import sys
from level import Level
from button import Button

pg.init() # initializing pygame
screen = pg.display.set_mode((1300,800)) # creating screen
pg.display.set_caption('Farming Tales')
clock = pg.time.Clock()
level = Level() 
        
      
# Game loop  
def town(): # method that runs the main island page of our game
    
    while True: # our game loop
       
        # buttons :)
        town_button = Button("Town", 40, 10, True) 
        fm_button = Button("Farmer's Market!", 10, 10, True) # creates our farmer market button
            
        # toggle control for our buttons!
        if pg.mouse.get_pressed()[0] and new_press:
            new_press = False
            if fm.check_press():
                if fm_button:
                    fm_button = False
                else:
                    fm_button = True
                
                # this makes sure that once the farmer's market button is clicked, the only way to get out of the page is by clicking the home screen
                
            
        if not pygame.mouse.get_pressed()[0] and not new_press:
            new_press = True
            
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program

        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
        
        
def farmers_market():
    
    scrreen.fill('black')
    while True:
       
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
            
        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions

  
        
town() # he just ran the function like this? I'm not sure if we'll need to add anything ❔
-----------------------------------------------

# Possible Changes to our code (I'm not sure if this would work) 🌷 AM
https://www.youtube.com/watch?v=GMBqjxcKogA

