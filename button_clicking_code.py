# this code actually allows us to interact with the button --> meaning when i press it, it works.. its not just nothing happening
# use this to connect to the pop up screen to 

class Button():
    def __init__(self,x,y,text_input):
        image= pg.image.load('fm button.png') # creating the image
        image = pg.transform.scale(image, (int(image.get_width() * 0.35), int(image.get_height()*0.35)))
        self.image = image
        self.x = x
        self.y = y 
        self.text = text_input
        self.button_text = font.render(text_input, True, 'black')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
        self.clicked = False # so only if button is NOT being clicked, can we then click it
    def draw(self):
      # drawing stuffn on screen 
        screen.blit(self.image,(self.rect.x, self.rect.y))
        screen.blit(self.button_text, (self.rect.x + 40, self.rect.y+30))
        # get mouse
        position = pg.mouse.get_pos()
        #check mouseover and clicked
        if self.rect.collidepoint(position):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False: # 0 if left clicked # the == 1 means mouse is being used/clicked rn
                self.clicked = True
                print('clicked')
            if pg.mouse.get_pressed()[0] == 0: # ==0 means mouse is NOT being pressed right
                self.clicked = False # now we can click the button again 
