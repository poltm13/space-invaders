from p5 import *

class Enemy:

    def __init__(self, width, height):
        self.enemyImg = load_image('./assets/Enemy2.png')
        self.posX = random(20, width-20);
        self.posY = 0;
        self.size = 40;

        self.velocity = 1.5;

    def update(self):
        self.posY += self.velocity

    def render(self):
        image_mode(CENTER)
        image(enemyImg, self.posX, self.posY, self.size, self.size)


