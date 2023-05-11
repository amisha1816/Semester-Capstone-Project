import pygame as pg
from setting import *
import os 

class Overlay:
    def __init__(self,player):
        self.display_surface = pg.display.get_surface()
        self.player = player
        self.tools_surf={tool: pg.image.load(f'overlay/{tool}.png').convert_alpha() for tool in player.tool}
        self.seeds_surf={seed: pg.image.load(f'overlay/{seed}.png').convert_alpha() for seed in player.seeds}
        print(self.tools_surf)
        print(self.seeds_surf)
    def display(self):
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom = OVERLAYER_POSITIONS['seed']) # making a rectangle around seed and basing the midbottom coor ofit based on overlayer_pos from setting.pu
        self.display_surface.blit(seed_surf,(seed_rect)) # now we are putting it on the screen
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom = OVERLAYER_POSITIONS['tool'])
        self.display_surface.blit(tool_surf,(tool_rect))


     