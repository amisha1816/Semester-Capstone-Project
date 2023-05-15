import pygame as pg
import sys
from level import Level

class Game:
    def __init__(self): # initalizing the class
        pg.init() # initializing pygame
        current_page = PageState()
        self.screen=pg.display.set_mode((1300,800)) # creating screen
        self.clock = pg.time.Clock()
        pg.display.set_caption('Farming Tales') # creates caption at top of game screen
        self.level = Level() # creating instances of Level class
    
    class PageState(): # Class that determines which page/screen the user is seeing
        def __init__(self):
            self.page = 'main_page' #this line causes the player to always start/open the game with the main page!
            
        def page_manager(self): # this method always us to easily control which page we're on
            if self.page == 'main_page':
                self.main_page()
            if self.page == 'fm_page':
                self.fm_page()
                
        def main_page(self): # method that runs the main page of our game
            for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
                if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                    pg.quit() # essentially quitting game
                    sys.exit() # allows us to end the program
                self.level.run(delta_time) # calling the run method from level class
                pg.display.update() # allows the background to update based on our actions
            
       def fm_page(self): # method that opens the farmer's market pop up
            for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
                if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                    pg.quit() # essentially quitting game
                    sys.exit() # allows us to end the program
                self.level.run(delta_time) # calling the run method from level class
                pg.display.update() # allows the background to update based on our actions
        
    
    def run(self): # method that allows our game to work
        while True:
            current_page.page_manager() # calls the page_manager method from main_page
            delta_time=self.clock.tick(60)/500 #help limit the runtime speed of a game
            


game= Game() # creating instance
game.run() # running instances 




