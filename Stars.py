from p5 import *

class Stars: 
    def __init__(self):
        self.number = 30
        self.stars = []

        #for i in self.number:
           # MIRAR
           # self.stars.push(new Star())
   
    def update(self):
        for i in len(self.stars):
            self.stars[i].update()
            self.stars[i].render()

# ---------------------------------------------------------------------
class Star:

    def __init__(self, width, height):
        self.size = random(1, 4)
        self.posX = random(0, width)
        self.posY = random(-height, height)
        self.vel = random(3, 20)
    
    #def update(self):
        # esta no sé como cambiar lo del ?
        # self.posY = (self.posY + self.vel < height) ? self.posY + self.vel : -height
    
    def render(self): 
        push()
        stroke(255)
        strokeWeight(self.size)
        point(self.posX, self.posY)
        pop()
    
