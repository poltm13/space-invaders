function Ship() {
    
    this.size = 50;
    
    this.posX = width/2;
    this.posY = 5*height/6;
    
    this.vel = 6;
    
    
    this.update = function () {
        if (keyIsDown(68) || keyIsDown(RIGHT_ARROW))    {
            
            this.posX = (this.posX + this.vel + this.size/2 < width) ? this.posX + this.vel : this.posX;
        }
        if (keyIsDown(65) || keyIsDown(LEFT_ARROW)) {
            
            this.posX = (this.posX - this.vel - this.size/2 > 0) ? this.posX - this.vel : this.posX;
        }
    };
    
    this.render = function () {
        imageMode(CENTER);
        image(shipImg, this.posX, this.posY, this.size, this.size);
    };
    
}