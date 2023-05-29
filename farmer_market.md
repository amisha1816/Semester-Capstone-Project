
### Farmer's Market Code 🍉

```python
import pygame as pg
from settings import *

class Menu:
  def __init__(self, character, fm_menu): # fm_menu allows us to switch on and off the farmer's market
  
    # base set-up :)
    self.character = character
    self.fm_menu = fm_menu
    self.display_surface = pg.display.get_surface()
    self.font = pg.font.SysFont('Cambria', 24)
    
  def close(self): # allows the player to close the farmer's market, we don't need to code a back button 🎉
    keys = pg.keys.get_pressed() # getting all the keys
    
    if keys[pg. K_ESCAPE]: # if player hits escape, display closes
        self.fm_menu() # I'm not too sure about this line, I think I might be calling the wrong method, CHECK WHEN DEBUGGING
  
  def update(self): # diplays the menu, it's like the button all over again :(
      self.input()
      self.display_surface.blit(pg.Surface((1500, 1200)), (0,0)
      # format is (Surface(dimensions), (coordinates)                            
```

Current farmer market methods, classes and more (so I don't get confused)
- ```farmer_market``` (within level)
- ```self.fm_active``` (within level twice!) → allows us to switch btwn the  farmer's market being on and off 

---

### Image Options
![Farmer's Market Image 2](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/7a1e60bc-6fca-45a7-8b60-d662cb1dc46b)
![Farmer's Market Image 1](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/9b3b7cff-f0d1-4ceb-8009-e543f8e4bc5a)
*Both these images are from [free.pik]([url](https://www.freepik.com/free-photos-vectors/market-stall)), they have lots of other options if we want!*
🌷 Personally I prefer the second option, I think 

---

### What's left to do:

- Connect clicking the button to the opening of the farmer's market. Can most likely use get_pressed and check_click methods from button to do this!
![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/161a32f6-2280-439b-8343-ec389cf597dc)
*This is how the tutorial did it for reference*
*We'll need to call the method farmer_market to make this work

