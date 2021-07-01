from p5 import *

class Spaceship:

  def __init__(self, width, height):
    self.shipImg = load_image('./assets/ship.png')
    self.size = 50
    self.window_width = width
  
    self.posX = width/2
    self.posY = 5*height/6
    
    self.vel = 6

  def hits(self, enemy):
    dx = abs(self.posX - enemy.posX)
    dy = abs(self.posY - enemy.posY) 
    threshold = enemy.size/2 + self.size/2
    if dx < threshold and dy < threshold:
      return True
    return False

  def update(self):
    # Move right if 'D' or '->' is pressed 
    if (key_is_pressed and (key == "D" or key == "d" or key == "RIGHT")):
      self.posX = self.posX + self.vel if (self.posX + self.vel + self.size/2 < self.window_width) else self.posX
    # Move left if 'A' or '<-' is pressed
    if (key_is_pressed and (key == "A" or key == "a" or key == "LEFT")):  
      self.posX = self.posX - self.vel if (self.posX - self.vel - self.size/2 > 0) else self.posX

  def render(self):
    image_mode(CENTER)
    image(self.shipImg, self.posX, self.posY, self.size, self.size)