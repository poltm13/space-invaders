function Stars() {
    
    this.number = 30;
    
    this.stars = [];
    
    for (let i = 0; i<this.number; i++) {
        this.stars.push(new Star());
    }
    
    this.update = function () {
        for (let i = 0; i<this.stars.length; i++)   {
            this.stars[i].update();
            this.stars[i].render();
        }
    }
}

function Star() {
    
    this.size = random(1, 4);
    
    this.posX = random(0, width);
    
    this.posY = random(-height, height);
    
    this.vel = random(3, 20);
    
    this.update = function () {
    
        this.posY = (this.posY + this.vel < height) ? this.posY + this.vel : -height;
        
    };
    
    this.render = function () {
        push();
        stroke(255);
        strokeWeight(this.size);
        point(this.posX, this.posY);
        pop();
    }
}