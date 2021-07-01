from p5 import *
from random import randint

class Stars: 
    def __init__(self, width, height):
        self.number = 10
        self.stars = []

        # Init stars
        for i in range(self.number):
           self.stars.append(Star(width, height))
   
    def update(self):
        # Update each star
        for star in self.stars:
            star.update()
            star.render()

# ---------------------------------------------------------------------

class Star:

    def __init__(self, width, height):
        # Store init values
        self.window_height = height
        self.size = randint(1, 4)
        self.posX = randint(0, width)
        self.posY = randint(0, height)
        self.vel = randint(3, 20)
    
    def update(self):
        # Update star pos if it's inside the window
        self.posY = self.posY + self.vel if (self.posY < self.window_height) else  0
        
    def render(self):
        # Render white point of weight size 
        stroke(255)
        stroke_weight(self.size)
        point(self.posX, self.posY)
    
