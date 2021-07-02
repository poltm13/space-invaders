from p5 import *
from Spaceship import Spaceship
from Stars import Stars
from Enemy import Enemy
from Laser import Laser
from random import randint

height = 800
width = 600
start = False
gameOver = False
lasers = []
enemies = []
spaceship = None
stars = None
frame = 0
time = 0

shipImg = None
startImg = None
spaceInvImg = None
gameOverImg = None
explosionImages = []

def imagesPreload():
  global startImg
  startImg = load_image('./assets/start-text.png')

  global spaceInvImg
  spaceInvImg = load_image('./assets/Title.png')

  global gameOverImg
  gameOverImg = load_image('./assets/GameOver.png')

  global explosionImg
  for i in range(12):
    explosionImages.append(load_image('./assets/explosion/' + str(i) + '.png'))

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
  global gameOver
  # Sets black background
  background(0)

  if not gameOver:
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
      gameOver = True


  game()


def key_pressed():
  global start

  if key == ' ':
    if not gameOver:
      lasers.append(Laser(spaceship.posX, spaceship.posY - spaceship.size/2, height))
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
    image(gameOverImg, (width/2, height/2))

    global frame
    frame = (frame + 1) % 12
    image(
      explosionImages[frame],
      (
        spaceship.posX + randint(-spaceship.size/2, spaceship.size/2),
        spaceship.posY + randint(-spaceship.size/2, spaceship.size/2)
      )
    )

  elif randint(1, 100) <= 3:
    enemies.append(Enemy(width, height))

if __name__ == '__main__':
    run()