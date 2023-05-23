
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
#town_button = pressed
new_press = True # checks if we just pressed the button
    
# Game loop  
run = True 
while run:
    # button creation using button class 
    town_button = Button( 10, 20,"Town Button")
    fm_button = Button(30, 30,"Farmer's Market")

    # Checks if buttons have been clicked
    #if pg.mouse.get_pressed()[0] and new_press:
     #   new_press = False

    # not pg.mouse.get_pressed()[] and not new_press:
        #new_press = True
 
    for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
        if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
            pg.quit() # essentially quitting game
            sys.exit() # allows us to end the program
        delta_time=clock.tick(120)/500
        level.run(delta_time)
        pg.display.update()
