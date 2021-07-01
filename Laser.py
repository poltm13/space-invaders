from p5 import *

class Laser:

  def __init__(self, x0, y0):
    self.posX = x0
    self.posY = y0
    self.vel = -20
    self.size = 20

  def update(self):
    self.posY += self.vel
  

  def render(self):
    stroke_weight(self.size/3)
    stroke(255, 0, 0)
    point(self.posX, self.posY)


  def hits(self, enemies):
    for enemy in enemies:
      dx = abs(self.posX - enemy.posX)
      dy = abs(self.posY - enemy.posY) 
      threshold = enemy.size/2 + self.size/2
      if dx < threshold and dy < threshold:
        return enemies.index(enemy) + 1
  
    return 0


  def offScreen(self):
    return self.posY > 690 or self.posY < 0
