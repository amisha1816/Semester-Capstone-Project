
import pygame as pg
from setting import *
screen = pg.display.set_mode((w,h))

class Menu:
  def __init__(self, character, fm_menu): # fm_menu allows us to switch on and off the farmer's market
  
    # base set-up :)
    self.character = character
    self.fm_menu = fm_menu
    self.font = pg.font.SysFont('Cambria', 14)
    
    # Adding in our farmer's market image (this code was pulled from the button code!)
    image = pg.image.load('background/farmers_pic.jpg')
    image = pg.transform.scale(image, (int(image.get_width() * 0.30), int(image.get_height()*0.35)))
    self.image = image
    
  def close(self): # allows the player to close the farmer's market
    keys= pg.key.get_pressed() # getting all the keys
    
    if keys[pg.K_ESCAPE]: # if player hits escape, display closes
        self.fm_menu() # I'm not too sure about this line, I think I might be calling the wrong method, CHECK WHEN DEBUGGING
  
  def update(self): # diplays the menu, it's like the button all over again :(
      self.close()
      screen.blit(self.image, (0,0)) # 0,0, so it fills the whole screen
