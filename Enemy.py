from p5 import *
from random import randint

class Enemy:

    def __init__(self, width, height):
        self.window_width = width
        self.window_height = height
        
        self.enemyImg = load_image('./assets/Enemy' + str(randint(0, 3)) + '.png')

        self.posX = randint(20, width-20);
        self.posY = 0;
        self.size = 40;

        self.velocity = randint(3, 8);

    def update(self):
        self.posY += self.velocity

    def render(self):
        image_mode(CENTER)
        image(self.enemyImg, self.posX, self.posY, self.size, self.size)

    def offScreen(self):
        return self.posY > self.window_height

