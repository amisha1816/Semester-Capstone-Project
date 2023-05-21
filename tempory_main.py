
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
town_button = pressed
new_press = True # checks if we just pressed the button
    
# Game loop  
while run:
    # button creation using button class 
    town_button = Button("Town Button", 10, 20, town_button_work)
    fm_button = Button("Farmer's Market", 30, 30, fm_button_work)

    # Checks if buttons have been clicked
    if pg.mouse.get_pressed()[0] and new_press:
        new_press = False

    if not pg.mouse.get_pressed()[] and not new_press:
        new_press = True
 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program

        delta_time=clock.tick(120)/500
        pg.display.update() 
        
 

