
import pygame as pg

class Timer:
    def __init__(self,duration,func = None):
        self.duration = duration
        self.func = func
        self.start_time=0
        self.active = False
    def start(self):
        self.active = True
        self.start_time = pg.time.get_ticks()
    def stop(self):
        self.active = False
        self.start_time = 0
    def update_tool(self):
        current_time = pg.time.get_ticks() # will get the current time
        if current_time - self.start_time >= 300: # checking if the time is up
            self.stop()
            if self.func:
                self.func()

