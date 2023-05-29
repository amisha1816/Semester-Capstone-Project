
### Farmer's Market Code 🍉

```pythonscreen = pg.display.set_mode((1300,800))
import pygame as pg
from settings import *
screen = pg.display.set_mode((1300,800))

class Menu:
  def __init__(self, character, fm_menu): # fm_menu allows us to switch on and off the farmer's market
  
    # base set-up :)
    self.character = character
    self.fm_menu = fm_menu
    self.font = pg.font.SysFont('Cambria', 14)
    
    # Adding in our farmer's market image (this code was pulled from the button code!)
    image = pg.image.load('❗ ADD IN FILE NAME ❗')
    image = pg.transform.scale(image, (int(image.get_width() * 0.30), int(image.get_height()*0.35)))
    self.image = image
    
  def close(self): # allows the player to close the farmer's market
    keys = pg.keys.get_pressed() # getting all the keys
    
    if keys[pg. K_ESCAPE]: # if player hits escape, display closes
        self.fm_menu() # I'm not too sure about this line, I think I might be calling the wrong method, CHECK WHEN DEBUGGING
  
  def update(self): # diplays the menu, it's like the button all over again :(
      self.close()
      screen.blit(self.image, (500, 500)) 
```
---

### Image Options
![Farmer's Market Image 2](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/7a1e60bc-6fca-45a7-8b60-d662cb1dc46b)
![Farmer's Market Image 1](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/9b3b7cff-f0d1-4ceb-8009-e543f8e4bc5a)
*Both these images are from [free.pik]([url](https://www.freepik.com/free-photos-vectors/market-stall)), they have lots of other options if we want!*
🌷 Personally I prefer the second option, I think 

---

### What's left to do:


### Possible Errors
- the layout is my main worry. I'm not sure if my placement of certain code blocks is wrong
  - like within button, I call the farmer_market method within level if the button has been pressed, however the video did this within level in his game loop. I added in the line ```fm_button.check_press() # 🌷``` within the game loop on our main page so I think we should be ok

![image](https://github.com/amisha1816/Semester-Capstone-Project/assets/129302600/3795f9a2-cbcd-41cf-b172-a23ba3e806d0)

