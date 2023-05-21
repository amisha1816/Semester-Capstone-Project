import pygame as pg
import sys
from level import Level
from button import Button

pg.init() # initializing pygame
level = Level() 
screen = pg.display.set_mode((1300,800)) # creating screen
pg.display.set_caption('Farming Tales')
clock = pg.time.Clock()
        
        
def town(): # method that runs the main island page of our game
    
    while True: # our game loop
       
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
               
            town_button = Button("Town", 40, 10, True) 
            fm_button = Button("Farmer's Market!", 10, 10, True) # creates our farmer market button

        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
        
        
def farmers_market():
    
    while True:
       
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
            
        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions

  
        
island() # he just ran the function like this? I'm not sure if we'll need to add anything ❔
-----------------------------------------------

# Possible Changes to our code (I'm not sure if this would work) 🌷 AM
https://www.youtube.com/watch?v=GMBqjxcKogA

