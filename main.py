import pygame as pg
import sys
from level import Level

class Game:
    def __init__(self): # initalizing the class
        pg.init() # initializing pygame
        self.screen=pg.display.set_mode((1300,800)) # creating screen
        self.clock = pg.time.Clock()
        pg.display.set_caption('Farming Tales') # creates caption at top of game screen
        self.level = Level() # creating instances of Level class
    
    def run(self): # method that allows our game to work
        while True:
            for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
                if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                    pg.quit() # essentially quitting game
                    sys.exit() # allows us to end the program
            delta_time=self.clock.tick(60)/500 #help limit the runtime speed of a game
            self.level.run(delta_time) # calling the run method from level class
            pg.display.update() # allows the background to update based on our actions

game= Game() # creating instance
game.run() # running instances 

hi = 'hi'



