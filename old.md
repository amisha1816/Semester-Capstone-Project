## Main 

#### Version 1 (this was pulled from original main.py)

```python
import pygame as pg
import sys
from level import Level
from button import Button

pg.init() # initializing pygame
level = Level() 
screen = pg.display.set_mode((1300,800)) # creating screen
pg.display.set_caption('Farming Tales')
clock = pg.time.Clock()
town_button_work = True # setting us to start on town setting
        
        
def town(): # method that runs the main island page of our game
    
    while True: # our game loop
       
        # buttons :)
        town_button = Button("Town", 40, 10, True) 
        fm_button = Button("Farmer's Market!", 10, 10, True) # creates our farmer market button
            
        # toggle control for our buttons!
        if pg.mouse.get_pressed()[0] and new_press:
            new_press = False
            if fm.check_press():
                if fm_button:
                    fm_button = False
                else:
                    fm_button = True
                
                # this makes sure that once the farmer's market button is clicked, the only way to get out of the page is by clicking the home screen
                
            
        if not pygame.mouse.get_pressed()[0] and not new_press:
            new_press = True
            
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program

        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
        
        
def farmers_market():
    
    scrreen.fill('black')
    while True:
       
        for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
            if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
                pg.quit() # essentially quitting game
                sys.exit() # allows us to end the program
            
        delta_time=clock.tick(120)/500
        pg.display.update() # allows the background to update based on our actions
```
  
#### Version 2

```python
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
    
# Game loop  
run = True 
while run:
    # button creation using button class 
    town_button = Button(10, 20,"Town Button")
    fm_button = Button(30, 30,"Farmer's Market")

    town_button.check_press()
    fm_button.check_press()
    # Checks if buttons have been clicked
    #if pg.mouse.get_pressed()[0] and new_press:
     #   new_press = False

    # not pg.mouse.get_pressed()[] and not new_press:
        #new_press = True
 
    for event in pg.event.get(): # pg.event.get is a function that will return the list of events that can be processed one after another)
        if event.type == pg.QUIT: # event.type --> pg object for representing events. pg handles all its event messaging through an event queue. 
            pg.quit() # essentially quitting game
            sys.exit() # allows us to end the program
        delta_time=clock.tick(120)/500
        level.run(delta_time)
        pg.display.update()
```

#### Version 3

```python
import pygame as pg
import sys
from level import Level
from button import Button

# initial set-up
pg.init()
pg.display.set_caption('Farming Tales')
clock = pg.time.Clock()
screen = pg.display.set_mode((1300,800))
level = Level()

fm_button = Button(1150,670, "Farmer's Market")

# Game loop  
run = True 
while run:
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()

    fm_button.update()
    fm_button.check_press() # 🌷

    pg.display.update() # allows a portion of the screen to be blitted
    delta_time = clock.tick(120)/500
    level.run(delta_time) 
``` 

---
