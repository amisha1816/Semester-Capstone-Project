import pygame as pg
import sys
from level import Level

pg.init() # initializing pygame
screen = pg.display.set_mode((1300,800)) # creating screen
clock = pg.time.Clock()
pg.display.set_caption('Farming Tales')
level = Level() 
        
def island(): # method that runs the main page of our game
    
    while True:
        
        mouse_pressing_button = pygame.mouse.get_post() # checks if we pressed any button
       
        fm_button = Button(image = pg.imade.load("-------------------"), pos=("------"),
                               text_input = "ISLAND", font = get_font("----"), base_color = "_______", colour = "---------")
        
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(Play_Mouse_POS):
                    menu()
                
            
        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
        
        
def farmers_market():
    
    while True:
        
        mouse_pressing_button = pygame.mouse.get_post() # checks if we pressed any button
        
        screen.fill("Black") # currently just here to check if everythings working
        
        island_button = Button(image = pg.imade.load("-------------------"), pos=("------"),
                               text_input = "ISLAND", font = get_font("----"), base_color = "_______", colour = "---------")
        
        
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(Play_Mouse_POS):
                    menu()
                
            
        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
 
def menu():
    
    while True:
        
        # Current test
        screen.fill("Black") # currently just here to check if everythings working
        
        # button
        mouse_pressing_button = pygame.mouse.get_post() # checks if we pressed any button
        island_button = Button(image = pg.imade.load("-------------------"), pos=("------"),
                               text_input = "ISLAND", font = get_font("----"), base_color = "_______", colour = "---------")
        
        # base
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_back.checkForInput(Play_Mouse_POS):
                    menu()
                
            
        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
  
        
menu() # he just ran the function like this? I'm not sure if we'll need to add anything ❔
-----------------------------------------------

# Possible Changes to our code (I'm not sure if this would work) 🌷 AM
https://www.youtube.com/watch?v=GMBqjxcKogA

