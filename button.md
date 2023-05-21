### Button Work (🌷 AM)
https://www.youtube.com/watch?v=16DM5Eem0cI


Version 1

```python

class Button(): # Class that allows the player can press buttons
    def __init__(self, image, x_pos, y_pos, text):
        self.image = image # allows us to show user's our button image

        # coordinates
        self.x_pose = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))

         # text
        self.text_input = text_input # allows us to store text_input in an object
        self.text = main_font.render(self.text_input, True, "--------")
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
 
def update(self): # allows us to place image along with text on screen
    screen.blit(self.image, self.rect) # allows us to put our image onto the game screen
    screen.blit(self.image, self.rect) # allows us to place the text for our button onto the game screen

def mouse_check(self, position): # checks for possible button click
    if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom): # checks if the mouse's position is in the button's area
        print("The button has been pressed")
        return True
    return False

```

Version 2

```python

class Button(): # Class that allows the player can press buttons
    def __init__(self, image, x_pos, y_pos, text, work): # initializing the function
        self.image = image # allows us to show user's our button image
        self.x_pose = x_pos
        self.y_pos = y_pos
        self.text = text
        self.work = work
        self.draw() # automatically calls the draw method once the Button is initialized
        
    def draw(self): # creatings the button's action
        b_text = font.render(self.text, True, 'black')
        b_rect = pg.image.rect.Rect((self.x_pos, self.y_pos), (100, 20))
        
        if self.work:
            if self.check_press():
                pg.draw.rect(screen, 'yellow', b_rect, 0, 10)
            else:
                pg.draw.rect(screen, 'red', b_rect, 0, 10)
        
        else:
            pg.draw.rect(screen, 'black', b_rect, 0, 10)
            
        pg.draw.rect(screen, 'red', b_rect, 0, 10)
        screen.blit(b_text, (self.x_post + 3, self.y_pos))

    def check_press(self): # checks if the button has been clickes
        mouse_position = pg.mouse.get_pos() # returns the current position of mouse
        left_click = pg.mouse.get_pressed()[0]
        b_rect = pg.image.rect.Rect((self.x_pos, self.y_pos), (100, 20))
        if left_click and b_rect.collidepoint(mouse_pos) and self.enabled: # checking to see if the player has clicked an enabled button
            return True
        else:
            return False
```

Version 3

```python
class Button(): # Class that allows the player can press buttons
    def __init__(self, image, x, y, pressed):
        self.image = image 
        self.pressed = pressed
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.rect = self.image.get_rect()
        self.draw()

    def draw(self, surface): 
        
        # creating button display (will need to adjust this to our liking 🌱)
        button_text = font.render(self.text, True, 'black')
        button_rect = pg.rect.Rect((self.x_pos, self.y_pos), (150, 25)
        pg.draw.rect(screem, 'yellow', button_rect, 0, 10)                          
        surface.blit(self.text, (self.rect.x, self.rect.y)) # place button on screen
        
                                   
        action = False
        
        pos = pg.mouse.get_pos() # finds mouse position
        if self.rect.collidepoint(pos): # checks if mouse is mouse touching button's rect
            if pg.mouse.get_pressed()[0] == 1 and self.pressed == False:
                # pg method that checks if a left click is happening
                action = True
                

        return action # action will be opening up a new screen





