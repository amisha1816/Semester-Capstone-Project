We would name this something like timer!

```python


class Timer:
  def __init__(self, duration, func = None):
    self.duration = duration
    self.func = func
    self.start_time = 0
    self.active = False
    
    def start(self):
      self.active = True
      self.start_time = pygame.time.get_ticks()
    
    def stop(self):
      self.active = False
      self.start_time = 0
      
    def update(self):
      current_time = pygame.time.get_ticks() # will get the current time
      if current_time - self.start_time >= 300 # checking if the time is up
        if self.func:
          self.func()
