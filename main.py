import pygame as pg
import sys
from level import Level

pg.init() # initializing pygame
screen = pg.display.set_mode((1300,800)) # creating screen
clock = pg.time.Clock()
pg.display.set_caption('Farming Tales')
level = Level() 
        
def main_page(): # method that runs the main page of our game
    while True:
        
        # 🌷AM
        mouse_pressing_button = pygame.mouse.get_post()
        
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
            
        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
 
main_page() # he just ran the function like this? I'm not sure if we'll need to add anything ❔
-----------------------------------------------

# Possible Changes to our code (I'm not sure if this would work) 🌷 AM
https://www.youtube.com/watch?v=GMBqjxcKogA

