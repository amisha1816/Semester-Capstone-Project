
Version 1

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

Version 2

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
