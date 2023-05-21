# 🌷 AM

import pygame
import sys

class Button(): # Class that allows the player can press buttons
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image # allows us to show user's our button image

        # coordinates
        self.x_pose = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

         # text
        self.text_input = text_input # allows us to store text_input in an object
        self.text = main_font.render(self.text_input, True, "yellow")
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
 
def update(self): # allows us to place image along with text on screen
    screen.blit(self.image, self.rect) # allows us to put our image onto the game screen
    screen.blit(self.image, self.rect) # allows us to place the text for our button onto the game screen

def mouse_check(self, position): # checks for possible button click
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): # checks if the mouse's position is in the button's area
        print("The button has been pressed")
        return True
    return False
