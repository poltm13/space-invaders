function Penguin() {
    this.posX = random(20, width-20);
    this.posY = 0;
    this.size = 40;
    
    this.vel = 1.5;
    
    this.update = function () {
        this.posY += this.vel;
    };
    
    this.render = function () {
        imageMode(CENTER);
        image(penguinImg, this.posX, this.posY, this.size, this.size);
    };
}