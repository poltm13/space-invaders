from p5 import *
from Spaceship import Spaceship
from Stars import Stars
from Enemy import Enemy
from Laser import Laser
from random import randint

height = 690
width = 600
start = False
gameOver = False
lasers = []
enemies = []
spaceship = None
stars = None

shipImg = None
startImg = None
spaceInvImg = None
gameOverImg = None

def imagesPreload():
  global startImg
  startImg = load_image('./assets/start-text.png')

  global spaceInvImg
  spaceInvImg = load_image('./assets/Title2.png')

  global gameOverImg
  gameOverImg = load_image('./assets/GameOver.png')

def setup():
  # Creates window
  size(width, height)
  # Sets all drawing as white
  stroke(255)
  #no_loop()
  global spaceship
  spaceship = Spaceship(width, height)

  global stars
  stars = Stars(width, height)

  imagesPreload()

  
def draw():
  # Sets black background
  background(0)

  spaceship.update()
  spaceship.render()
  stars.update()

  for laser in lasers:
    laser.update();
    laser.render();

    hit = laser.hits(enemies);
    if hit:
      del enemies[hit - 1]
      del lasers[lasers.index(laser)]
    elif laser.offScreen():  
      del lasers[lasers.index(laser)]

  for enemy in enemies:
    enemy.update()
    enemy.render()

    if spaceship.hits(enemy) or enemy.offScreen():
      global gameOver
      gameOver = True

  game()


def key_pressed():
  global start

  if key == ' ':
    lasers.append(Laser(spaceship.posX, spaceship.posY - spaceship.size/2))
  elif (key == 's' or key == 'S') and not gameOver:
    start = True
    loop()
  elif key == 'p' or key == 'P':
    start = False
    no_loop()

def game():
  if not start:
    no_loop()
    image(spaceInvImg, (width/2, height/3))
    image(startImg, (width/2, height/2))
  elif gameOver:
    no_loop()
    image(gameOverImg, (width/2, height/2))
  elif randint(1, 100) <= 3:
    enemies.append(Enemy(width, height))

if __name__ == '__main__':
    run()