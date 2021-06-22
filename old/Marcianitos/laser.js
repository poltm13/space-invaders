function Laser(x0, y0) {
    this.posX = x0;
    this.posY = y0;
    this.vel = -20;
    this.size = 20;

    this.update = function () {
        this.posY += this.vel;
    };

    this.render = function () {
        ///*imageMode(CENTER);
        image(heartImg, this.posX, this.posY, this.size, this.size);
        //*/
        /*
        push();
        strokeWeight(this.size/3);
        stroke('red');
        point(this.posX, this.posY);
        pop();
        */
    };

    this.hits = function (penguins) {
    
        for (let i=0; i<penguins.length; i++)   {
            let d = dist(this.posX, this.posY, penguins[i].posX, penguins[i].posY);
            if (d < penguins[i].size/2 + this.size/2)   {
                return i + 1;
            }
        }
        return 0;
    };

    this.offScreen = function () {
        return (this.posY > height || this.posY < 0);
    };
}
