
Within Character
```python
if keys[pg.K_RETURN]: # if enter was pressed
    self.farmer_market()  
```
---

Within main
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

# Game loop  
run = True 
while run:
 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() 
            sys.exit()

    pg.display.update() # allows a portion of the screen to be blitted
    delta_time = clock.tick(120)/500
    level.run(delta_time) 
```
