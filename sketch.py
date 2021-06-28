from p5 import *
from Spaceship import Spaceship

height = 690
width = 600
start = False
lasers = []
penguins = []
spaceship = None
stars = None
shipImg = None

def setup():
  # Creates window
  size(width, height)
  # Sets all drawing as white
  stroke(255)
  #no_loop()
  global spaceship
  spaceship = Spaceship(width, height)

def draw():
  # Sets black background
  background(0)
  global spaceship
  spaceship.update()
  spaceship.render()

def mouse_pressed():
  loop()

def key_pressed():
  if (key == ' '):
    # lasers.push(new Laser(spaceShip.posX, spaceShip.posY - spaceShip.size/2));
    loop()

if __name__ == '__main__':
    run()
