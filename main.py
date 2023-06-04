
# This is the new version from April 30th

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

'''
KEYS BEING USED:

up: K_UP
down: K_DOWN
left:K_LEFT
right:K_RIGHT
using axe: K_a
using hoe:K_s
switching tools:K_q
switching seeds:K_e
new day: K_TAB
entering farmers market: K_RETURN
leaving farmers market: K_ESCAPE
seed timer: K_LCTRL'''
